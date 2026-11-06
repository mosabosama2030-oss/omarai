"""Tenant-scoped product profile persistence tests."""
from __future__ import annotations

import pytest

from agents.omarai import LeadStore
from agents.sales_domain import MarketProfile, ProductProfile


def _tenant(store: LeadStore, name: str) -> str:
    tenant_id = store.create_tenant(name, name.casefold().replace(" ", "-"))
    user_id = store.create_user(
        name.casefold().replace(" ", "") + "@example.test",
        name + " User",
    )
    store.add_membership(tenant_id, user_id, "owner")
    return tenant_id


def test_product_profiles_persist_update_and_remain_tenant_scoped(tmp_path):
    store = LeadStore(tmp_path / "profiles.sqlite3")
    tenant_a = _tenant(store, "Company A")
    tenant_b = _tenant(store, "Company B")
    profile = ProductProfile(
        name="نظام إنذار حريق",
        aliases=("Fire alarm system", "إنذار حريق"),
        category_path=("أنظمة السلامة", "إنذار الحريق"),
        use_cases=("المباني التجارية",),
        problems_solved=("الكشف المبكر عن الحريق",),
    )
    market = MarketProfile(
        locations=("القاهرة", "الجيزة"),
        industries=("المقاولات",),
        customer_types=("شركات إدارة المباني",),
        decision_roles=("مدير المشتريات",),
        exclusions=("الأفراد",),
    )

    saved = store.save_product_profile(profile, market, tenant_id=tenant_a)

    assert saved["profile"]["name"] == "نظام إنذار حريق"
    assert saved["profile"]["aliases"] == ["Fire alarm system", "إنذار حريق"]
    assert saved["market"]["locations"] == ["القاهرة", "الجيزة"]
    assert store.get_product_profile(saved["id"], tenant_id=tenant_b) is None
    assert store.list_product_profiles(tenant_id=tenant_b) == []

    updated = store.save_product_profile(
        ProductProfile(name="نظام إنذار حريق متقدم"),
        MarketProfile(locations=("الإسكندرية",)),
        tenant_id=tenant_a,
        profile_id=saved["id"],
    )
    assert updated["id"] == saved["id"]
    assert updated["profile"]["name"] == "نظام إنذار حريق متقدم"
    assert updated["market"]["locations"] == ["الإسكندرية"]
    assert len(store.list_product_profiles(tenant_id=tenant_a)) == 1


def test_product_profile_requires_an_active_tenant(tmp_path):
    store = LeadStore(tmp_path / "profiles.sqlite3")
    with pytest.raises(ValueError, match="active tenant"):
        store.save_product_profile(
            ProductProfile(name="Product"),
            MarketProfile(),
            tenant_id="tenant_missing",
        )
