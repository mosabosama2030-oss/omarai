"""Provider-independent domain contracts for Omarai sales intelligence.

These models describe evidence and assessments; they do not discover buyers,
infer identity, calculate purchase probability, or execute external actions.
Storage and API integration are deliberately kept separate from this module.
"""
from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from datetime import date, datetime
from enum import Enum
from typing import Iterable
from urllib.parse import urlsplit


MAX_NAME_LENGTH = 240
MAX_TEXT_LENGTH = 2_000
MAX_TERM_COUNT = 64
_MAX_CATEGORY_DEPTH = 8

_ARABIC_MARKS = re.compile(r"[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED]")
_PUNCTUATION = re.compile(r"[\s\t\r\n.,،؛;:!?؟()\[\]{}<>\"'«»]+")
_SPACE = re.compile(r"\s+")


class FactOrigin(str, Enum):
    USER_PROVIDED = "user_provided"
    SOURCE_VERIFIED = "source_verified"
    INFERRED = "inferred"
    UNKNOWN = "unknown"


class DemandSignalType(str, Enum):
    DIRECT_PURCHASE_REQUEST = "direct_purchase_request"
    REQUEST_FOR_QUOTATION = "request_for_quotation"
    TENDER_OR_PROCUREMENT = "tender_or_procurement"
    STATED_NEED = "stated_need"
    INDIRECT_INDICATOR = "indirect_indicator"
    ICP_MATCH_ONLY = "icp_match_only"
    NEGATED = "negated"
    CANCELLED = "cancelled"
    EXPIRED = "expired"
    CONFLICTING = "conflicting"
    UNKNOWN = "unknown"


class ProductFit(str, Enum):
    FIT = "fit"
    NO_FIT = "no_fit"
    UNASSESSED = "unassessed"


class EvidenceBasis(str, Enum):
    PAGE_TEXT = "page_text"
    TITLE = "title"
    SEARCH_SNIPPET = "search_snippet"
    OFFICIAL_DOCUMENT = "official_document"
    USER_PROVIDED = "user_provided"


class IdentityStatus(str, Enum):
    VERIFIED = "verified"
    UNVERIFIED = "unverified"
    UNKNOWN = "unknown"


class SourceQuality(str, Enum):
    PRIMARY_SOURCE = "primary_source"
    SECONDARY_SOURCE = "secondary_source"
    SNIPPET_ONLY = "snippet_only"
    PAGE_UNREAD = "page_unread"
    UNKNOWN = "unknown"


class FreshnessStatus(str, Enum):
    CURRENT = "current"
    STALE = "stale"
    UNKNOWN = "unknown"


class ContactabilityStatus(str, Enum):
    PUBLIC_CHANNEL_AVAILABLE = "public_channel_available"
    NOT_FOUND = "not_found"
    NOT_ASSESSED = "not_assessed"


def normalize_text(value: str) -> str:
    """Normalize Arabic/Latin text for deterministic matching, not for display."""
    if not isinstance(value, str):
        return ""
    text = unicodedata.normalize("NFKC", value).casefold()
    text = _ARABIC_MARKS.sub("", text)
    text = text.replace("ـ", "").translate(
        str.maketrans(
            {
                "أ": "ا",
                "إ": "ا",
                "آ": "ا",
                "ٱ": "ا",
                "ى": "ي",
                "ة": "ه",
            }
        )
    )
    text = _PUNCTUATION.sub(" ", text)
    return _SPACE.sub(" ", text).strip()


def _clean_text(value: str, *, field_name: str, maximum: int = MAX_TEXT_LENGTH) -> str:
    if not isinstance(value, str):
        raise TypeError(f"{field_name} must be a string")
    cleaned = value.strip()
    if not cleaned:
        raise ValueError(f"{field_name} is required")
    if len(cleaned) > maximum:
        raise ValueError(f"{field_name} exceeds {maximum} characters")
    return cleaned


def _clean_terms(
    values: Iterable[str],
    *,
    field_name: str,
    maximum_count: int = MAX_TERM_COUNT,
) -> tuple[str, ...]:
    if isinstance(values, (str, bytes)):
        raise TypeError(f"{field_name} must be an iterable of strings, not a string")
    cleaned: list[str] = []
    seen: set[str] = set()
    for value in values:
        term = _clean_text(value, field_name=field_name, maximum=MAX_NAME_LENGTH)
        key = normalize_text(term)
        if key and key not in seen:
            cleaned.append(term)
            seen.add(key)
        if len(cleaned) > maximum_count:
            raise ValueError(f"{field_name} exceeds {maximum_count} items")
    return tuple(cleaned)


def _clean_path(values: Iterable[str], *, field_name: str) -> tuple[str, ...]:
    path = _clean_terms(values, field_name=field_name, maximum_count=_MAX_CATEGORY_DEPTH)
    if not path:
        raise ValueError(f"{field_name} must contain at least one segment")
    return path


def _enum_value(enum_type: type[Enum], value: Enum | str, *, field_name: str) -> Enum:
    try:
        return value if isinstance(value, enum_type) else enum_type(value)
    except (TypeError, ValueError) as exc:
        allowed = ", ".join(item.value for item in enum_type)
        raise ValueError(f"{field_name} must be one of: {allowed}") from exc


def _validate_optional_date(value: str | None, *, field_name: str) -> str | None:
    if value is None:
        return None
    cleaned = _clean_text(value, field_name=field_name, maximum=32)
    try:
        parsed = date.fromisoformat(cleaned)
    except ValueError as exc:
        raise ValueError(f"{field_name} must be an ISO date (YYYY-MM-DD)") from exc
    if parsed.isoformat() != cleaned:
        raise ValueError(f"{field_name} must use YYYY-MM-DD")
    return cleaned


def _validate_optional_datetime(value: str | None, *, field_name: str) -> str | None:
    if value is None:
        return None
    cleaned = _clean_text(value, field_name=field_name, maximum=64)
    try:
        parsed = datetime.fromisoformat(cleaned.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError(f"{field_name} must be an ISO-8601 datetime") from exc
    if parsed.tzinfo is None:
        raise ValueError(f"{field_name} must include a timezone offset")
    return cleaned


def _validate_http_url(value: str) -> str:
    cleaned = _clean_text(value, field_name="source_url", maximum=2_048)
    parsed = urlsplit(cleaned)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        raise ValueError("source_url must be an absolute HTTP(S) URL")
    if parsed.username or parsed.password:
        raise ValueError("source_url must not contain embedded credentials")
    return cleaned


def _contains_phrase(text: str, phrase: str) -> bool:
    normalized_text = normalize_text(text)
    normalized_phrase = normalize_text(phrase)
    if not normalized_text or not normalized_phrase:
        return False
    # Unicode-aware word boundaries prevent e.g. "car" matching "cart".
    return re.search(
        rf"(?<!\w){re.escape(normalized_phrase)}(?!\w)",
        normalized_text,
        flags=re.UNICODE,
    ) is not None


@dataclass(frozen=True, slots=True)
class ProductFact:
    """One product attribute with an explicit origin and optional evidence pointer."""

    field: str
    value: str
    origin: FactOrigin = FactOrigin.USER_PROVIDED
    evidence_id: str | None = None

    def __post_init__(self) -> None:
        object.__setattr__(self, "field", _clean_text(self.field, field_name="field", maximum=80))
        object.__setattr__(self, "value", _clean_text(self.value, field_name="value"))
        object.__setattr__(
            self,
            "origin",
            _enum_value(FactOrigin, self.origin, field_name="origin"),
        )
        if self.evidence_id is not None:
            object.__setattr__(
                self,
                "evidence_id",
                _clean_text(self.evidence_id, field_name="evidence_id", maximum=160),
            )
        if self.origin == FactOrigin.SOURCE_VERIFIED and not self.evidence_id:
            raise ValueError("source_verified product facts require evidence_id")

    def to_dict(self) -> dict[str, str | None]:
        return {
            "field": self.field,
            "value": self.value,
            "origin": self.origin.value,
            "evidence_id": self.evidence_id,
        }


@dataclass(frozen=True, slots=True)
class ProductProfile:
    """Explicit product/service facts supplied by a user or supported by sources."""

    name: str
    aliases: tuple[str, ...] = ()
    category_path: tuple[str, ...] = ()
    use_cases: tuple[str, ...] = ()
    problems_solved: tuple[str, ...] = ()
    facts: tuple[ProductFact, ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(self, "name", _clean_text(self.name, field_name="name", maximum=MAX_NAME_LENGTH))
        object.__setattr__(self, "aliases", _clean_terms(self.aliases, field_name="aliases"))
        object.__setattr__(self, "use_cases", _clean_terms(self.use_cases, field_name="use_cases"))
        object.__setattr__(
            self,
            "problems_solved",
            _clean_terms(self.problems_solved, field_name="problems_solved"),
        )
        if self.category_path:
            object.__setattr__(
                self,
                "category_path",
                _clean_path(self.category_path, field_name="category_path"),
            )
        if not all(isinstance(item, ProductFact) for item in self.facts):
            raise TypeError("facts must contain ProductFact instances")
        if len(self.facts) > MAX_TERM_COUNT:
            raise ValueError(f"facts exceeds {MAX_TERM_COUNT} items")

    def matching_terms(self, text: str) -> tuple[str, ...]:
        """Return explicitly configured product terms mentioned in text.

        A mention is not a demand signal and does not establish a buyer or product fit.
        """
        terms = (self.name, *self.aliases)
        return tuple(term for term in terms if _contains_phrase(text, term))

    def to_dict(self) -> dict[str, object]:
        return {
            "name": self.name,
            "aliases": list(self.aliases),
            "category_path": list(self.category_path),
            "use_cases": list(self.use_cases),
            "problems_solved": list(self.problems_solved),
            "facts": [item.to_dict() for item in self.facts],
        }


@dataclass(frozen=True, slots=True)
class MarketProfile:
    """Target-market constraints; matching an ICP is not evidence of purchase intent."""

    locations: tuple[str, ...] = ()
    industries: tuple[str, ...] = ()
    customer_types: tuple[str, ...] = ()
    decision_roles: tuple[str, ...] = ()
    exclusions: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        for name in ("locations", "industries", "customer_types", "decision_roles", "exclusions"):
            object.__setattr__(
                self,
                name,
                _clean_terms(getattr(self, name), field_name=name),
            )

    def to_dict(self) -> dict[str, list[str]]:
        return {
            name: list(getattr(self, name))
            for name in ("locations", "industries", "customer_types", "decision_roles", "exclusions")
        }


@dataclass(frozen=True, slots=True)
class TaxonomyCategory:
    """A caller-defined taxonomy node; no sector is hard-coded in the matcher."""

    path: tuple[str, ...]
    aliases: tuple[str, ...]

    def __post_init__(self) -> None:
        object.__setattr__(self, "path", _clean_path(self.path, field_name="path"))
        object.__setattr__(self, "aliases", _clean_terms(self.aliases, field_name="aliases"))
        if not self.aliases:
            raise ValueError("taxonomy category requires at least one alias")


@dataclass(frozen=True, slots=True)
class ProductTaxonomy:
    """Extensible taxonomy supplied by configuration or a verified product catalogue."""

    categories: tuple[TaxonomyCategory, ...] = ()

    def __post_init__(self) -> None:
        if not all(isinstance(item, TaxonomyCategory) for item in self.categories):
            raise TypeError("categories must contain TaxonomyCategory instances")
        paths = [tuple(normalize_text(part) for part in item.path) for item in self.categories]
        if len(paths) != len(set(paths)):
            raise ValueError("taxonomy category paths must be unique")

    def match_categories(self, text: str) -> tuple[tuple[str, ...], ...]:
        """Return all explicit taxonomy matches; never choose a winner by guessing."""
        matches = [
            category.path
            for category in self.categories
            if any(_contains_phrase(text, alias) for alias in category.aliases)
        ]
        return tuple(matches)

    def to_list(self) -> list[dict[str, list[str]]]:
        return [
            {"path": list(item.path), "aliases": list(item.aliases)}
            for item in self.categories
        ]


@dataclass(frozen=True, slots=True)
class DemandEvidence:
    """Source provenance for a demand signal; dates remain distinct and optional."""

    source_id: str
    source_url: str
    excerpt: str
    content_basis: EvidenceBasis
    publication_date: str | None = None
    event_date: str | None = None
    observed_at: str | None = None
    page_read: bool = False

    def __post_init__(self) -> None:
        object.__setattr__(
            self,
            "source_id",
            _clean_text(self.source_id, field_name="source_id", maximum=160),
        )
        object.__setattr__(self, "source_url", _validate_http_url(self.source_url))
        object.__setattr__(
            self,
            "excerpt",
            _clean_text(self.excerpt, field_name="excerpt", maximum=MAX_TEXT_LENGTH),
        )
        object.__setattr__(
            self,
            "content_basis",
            _enum_value(EvidenceBasis, self.content_basis, field_name="content_basis"),
        )
        object.__setattr__(
            self,
            "publication_date",
            _validate_optional_date(self.publication_date, field_name="publication_date"),
        )
        object.__setattr__(
            self,
            "event_date",
            _validate_optional_date(self.event_date, field_name="event_date"),
        )
        object.__setattr__(
            self,
            "observed_at",
            _validate_optional_datetime(self.observed_at, field_name="observed_at"),
        )
        if not isinstance(self.page_read, bool):
            raise TypeError("page_read must be a boolean")
        if self.content_basis == EvidenceBasis.SEARCH_SNIPPET and self.page_read:
            raise ValueError("a search snippet cannot be marked as a successfully read page")
        if self.content_basis == EvidenceBasis.PAGE_TEXT and not self.page_read:
            raise ValueError("page_text evidence requires page_read=True")

    def to_dict(self) -> dict[str, object]:
        return {
            "source_id": self.source_id,
            "source_url": self.source_url,
            "excerpt": self.excerpt,
            "content_basis": self.content_basis.value,
            "publication_date": self.publication_date,
            "event_date": self.event_date,
            "observed_at": self.observed_at,
            "page_read": self.page_read,
        }


@dataclass(frozen=True, slots=True)
class DemandSignal:
    """A classified demand signal, kept independent from product-fit assessment."""

    signal_id: str
    signal_type: DemandSignalType
    evidence: DemandEvidence
    product_fit: ProductFit = ProductFit.UNASSESSED
    identity_status: IdentityStatus = IdentityStatus.UNKNOWN
    classification_reason: str = ""
    product_fit_reason: str = ""

    def __post_init__(self) -> None:
        object.__setattr__(
            self,
            "signal_id",
            _clean_text(self.signal_id, field_name="signal_id", maximum=160),
        )
        object.__setattr__(
            self,
            "signal_type",
            _enum_value(DemandSignalType, self.signal_type, field_name="signal_type"),
        )
        object.__setattr__(
            self,
            "product_fit",
            _enum_value(ProductFit, self.product_fit, field_name="product_fit"),
        )
        object.__setattr__(
            self,
            "identity_status",
            _enum_value(IdentityStatus, self.identity_status, field_name="identity_status"),
        )
        if not isinstance(self.evidence, DemandEvidence):
            raise TypeError("evidence must be a DemandEvidence instance")
        for name in ("classification_reason", "product_fit_reason"):
            value = getattr(self, name)
            if not isinstance(value, str):
                raise TypeError(f"{name} must be a string")
            if len(value) > 500:
                raise ValueError(f"{name} exceeds 500 characters")
        if self.product_fit == ProductFit.UNASSESSED and self.product_fit_reason:
            raise ValueError("unassessed product fit must not have a fit rationale")
        if self.product_fit != ProductFit.UNASSESSED and not self.product_fit_reason.strip():
            raise ValueError("assessed product fit requires a rationale")

    def to_dict(self) -> dict[str, object]:
        return {
            "signal_id": self.signal_id,
            "signal_type": self.signal_type.value,
            "evidence": self.evidence.to_dict(),
            "product_fit": self.product_fit.value,
            "identity_status": self.identity_status.value,
            "classification_reason": self.classification_reason,
            "product_fit_reason": self.product_fit_reason,
        }


@dataclass(frozen=True, slots=True)
class LeadQualification:
    """Independent qualification dimensions; deliberately contains no purchase score."""

    signal_id: str
    product_fit: ProductFit = ProductFit.UNASSESSED
    source_quality: SourceQuality = SourceQuality.UNKNOWN
    freshness: FreshnessStatus = FreshnessStatus.UNKNOWN
    identity_status: IdentityStatus = IdentityStatus.UNKNOWN
    contactability: ContactabilityStatus = ContactabilityStatus.NOT_ASSESSED
    missing_information: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(
            self,
            "signal_id",
            _clean_text(self.signal_id, field_name="signal_id", maximum=160),
        )
        for name, enum_type in (
            ("product_fit", ProductFit),
            ("source_quality", SourceQuality),
            ("freshness", FreshnessStatus),
            ("identity_status", IdentityStatus),
            ("contactability", ContactabilityStatus),
        ):
            object.__setattr__(
                self,
                name,
                _enum_value(enum_type, getattr(self, name), field_name=name),
            )
        object.__setattr__(
            self,
            "missing_information",
            _clean_terms(self.missing_information, field_name="missing_information"),
        )

    def to_dict(self) -> dict[str, object]:
        return {
            "signal_id": self.signal_id,
            "product_fit": self.product_fit.value,
            "source_quality": self.source_quality.value,
            "freshness": self.freshness.value,
            "identity_status": self.identity_status.value,
            "contactability": self.contactability.value,
            "missing_information": list(self.missing_information),
        }


def to_json_dict(value: ProductProfile | MarketProfile | DemandEvidence | DemandSignal | LeadQualification) -> dict[str, object]:
    """Serialize a supported domain object without silently dropping evidence fields."""
    if not hasattr(value, "to_dict"):
        raise TypeError("unsupported sales domain object")
    return value.to_dict()
