# LEAD_GENERATION — Design Document (PROPOSED)

Status: Design only. Do not implement until separate approval.

## Goal
Distinguish 3 result types:
1. For-sale listing (شقة للبيع) — NOT a lead
2. Purchase request (مطلوب/أبحث عن) — IS a lead
3. Broker / agency — source, not a lead

## Acceptance rule
A source is a lead ONLY if it contains purchase-intent text.

## Keywords (PROPOSED)
- Purchase intent (AR): "مطلوب شقة", "أبحث عن شقة", "أرغب في شراء", "مشتري", "طلب شراء"
- Purchase intent (EN): "looking for apartment", "want to buy", "buyer", "purchase request"
- Exclude (sale): "شقة للبيع", "for sale", "وحدة للبيع"
- Broker: "وسيط", "شركة عقارية", "مطور", "broker", "agency"

## Flow
1. route_intent detects purchase term -> LEAD_GENERATION
2. _collect_research uses "مطلوب" and "أبحث عن" in queries
3. filter adds _has_purchase_intent(source)
4. If none: return kind="no_lead_evidence", message="لم يُثبت وجود عميل محتمل"

## Test cases (Arabic)
| # | Question | Route | Expected |
|---|----------|-------|----------|
| 1 | أبحث عن عميل يريد شراء شقة بالعاصمة | LEAD_GENERATION | purchase intent sources |
| 2 | مطلوب شقة 3 غرف بالعاصمة | LEAD_GENERATION | purchase requests |
| 3 | شقق للبيع في العاصمة | WEB_SIMPLE | sale listings |
| 4 | مطلوب شقة للبيع | CLARIFY | clarification requested |
| 5 | وسيط عقاري بالعاصمة | WEB_SIMPLE | brokers listed |

## Constraints
- Do not implement in this PR.
- Requires separate design session with Claude/Grok.
- Do not merge to main before tests.
