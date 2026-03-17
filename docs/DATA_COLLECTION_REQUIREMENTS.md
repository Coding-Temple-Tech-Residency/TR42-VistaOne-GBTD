# Data Collection Requirements - VistaOne Vendor Web Application

## Overview

This document defines all data points required for comprehensive analytics across the VistaOne platform. Data is organized by category with must-have vs nice-to-have classification.

---

## 1. User Data Requirements

### 1.1 Sign-up Data (MUST-HAVE)
| Data Point | Type | Source | Description |
|---|---|---|---|
| email | varchar(100) | users | User email at registration |
| phone | varchar(20) | users | User phone number |
| location | Derived | users.city/state/country | User geographic location |
| sign-up timestamp | timestamp | users.created_at | Account creation time |
| user_type | varchar(20) | users | Role: customer, vendor, or admin |
| username | varchar(50) | users | Unique username |

### 1.2 Profile Data (MUST-HAVE)
| Data Point | Type | Source | Description |
|---|---|---|---|
| name | Derived | users.first_name + last_name | Full user name |
| preferences | Extended | users (future) | Notification/theme preferences |
| account type | varchar(20) | users.user_type | customer/vendor/admin |
| status | boolean | users.is_active | Account active/inactive |
| vendor business info | Various | vendors table | Business profile details |

### 1.3 Login/Authentication Events (MUST-HAVE)
| Data Point | Type | Source | Description |
|---|---|---|---|
| timestamp | timestamp | auth_events | Event time |
| success/failure | boolean | auth_events | Login outcome |
| device info | varchar(255) | auth_events | Browser, OS, device type |
| ip_address | varchar(45) | auth_events | User IP address |
| session_id | varchar(100) | auth_events | Session identifier |
| auth_method | varchar(50) | auth_events | Password, OAuth, SSO |

---

## 2. Usage/Session Data Requirements

### 2.1 Session Data (MUST-HAVE)
| Data Point | Type | Source | Description |
|---|---|---|---|
| session_start | timestamp | sessions | Session start time |
| session_end | timestamp | sessions | Session end time |
| session_duration | Derived | sessions | Duration in seconds |
| idle_time | Derived | sessions | Time without activity |
| session_id | varchar(100) | sessions | Unique identifier |
| user_id | int | sessions | Associated user |

### 2.2 Navigation & Page Visits (MUST-HAVE)
| Data Point | Type | Source | Description |
|---|---|---|---|
| page_url | varchar(255) | page_views | Visited URL |
| page_title | varchar(200) | page_views | Page title |
| timestamp | timestamp | page_views | Visit time |
| referrer_url | varchar(255) | page_views | Traffic source |
| time_on_page | integer | page_views | Seconds on page |
| exit_page | boolean | page_views | Exit indicator |

### 2.3 Feature Interactions & Events (MUST-HAVE)
| Data Point | Type | Source | Description |
|---|---|---|---|
| event_type | varchar(100) | events | click, search, filter, add-to-cart, purchase, review |
| event_timestamp | timestamp | events | When event occurred |
| event_source | varchar(100) | events | Page/component |
| event_value | JSON | events | Additional data |
| product_id | int | events | Product involved |
| category_id | int | events | Category involved |

### 2.4 Nice-to-Have (FUTURE PHASE)
- Scroll depth tracking
- Mouse heatmaps
- Form abandonment
- Voice search queries
- A/B testing events

---

## 3. Transaction Data Requirements

### 3.1 Transaction Core Data (MUST-HAVE)
| Data Point | Type | Source | Description |
|---|---|---|---|
| amount | decimal(10,2) | orders.total_amount | Transaction value |
| currency | varchar(3) | orders | Currency code (USD) |
| transaction type | varchar(50) | Derived | purchase/refund/cancellation |
| order_id | int | orders | Associated order |
| customer_id | int | orders | Customer |
| vendor_id | int | Derived | Vendor |

### 3.2 Transaction Timing (MUST-HAVE)
| Data Point | Type | Source | Description |
|---|---|---|---|
| timestamp | timestamp | orders.created_at | Transaction time |
| duration | Derived | orders | Cart to purchase time |
| fulfillment_time | Derived | orders | Order to delivery |

### 3.3 Transaction Status (MUST-HAVE)
| Data Point | Type | Source | Description |
|---|---|---|---|
| success/failure | boolean | Derived | Transaction outcome |
| error_code | varchar(50) | Derived | Payment error code |
| payment_method | varchar(50) | payment_methods | Credit card, PayPal, etc. |
| order_status | varchar(20) | orders | pending/processing/shipped/delivered/cancelled |

---

## 4. Data Classification Summary

### Must-Have (Phase 1)
- All user registration and profile fields
- Authentication event logging
- Session tracking (start/end/duration)
- Page view tracking with URLs and timestamps
- Core event tracking (clicks, searches, purchases)
- All transaction/order data
- Product and category interaction data

### Nice-to-Have (Phase 2+)
- Advanced behavior tracking (scroll depth, heatmaps)
- Form abandonment analytics
- Voice search analytics
- A/B testing event tracking
- Customer lifetime value calculations
- Cohort analysis data points
- Real-time dashboard metrics

---

## 5. Assumptions & Constraints

### Assumptions
1. Users opt-in to analytics tracking (privacy-compliant)
2. Data stored in PostgreSQL (database_schema.sql)
3. Server-side sessions with cookie identifiers
4. Client-side event tracking with server verification
5. PII encrypted at rest
6. 2-year retention for analytics, 7-year for transactions

### Constraints
1. GDPR, CCPA, and privacy law compliance required
2. No PII to third-party analytics
3. Performance: <50ms tracking overhead per request
4. Storage: ~50GB/month estimated at scale
5. Real-time dashboards with <5 second latency

---

## 6. Review Checklist

- [ ] Backend team review (implementation feasibility)
- [ ] Frontend team review (client-side tracking)
- [ ] Product management review (business alignment)
- [ ] Data team review (analytics pipeline)

---
*Last Updated: 2026-03-16*
*Author: James Bustamante (Data)*
