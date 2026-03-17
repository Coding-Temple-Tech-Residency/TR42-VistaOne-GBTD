# Key Performance Indicators (KPIs) Documentation
## VistaOne Vendor Web Application

---

## Overview

This document defines and proposes Key Performance Indicators (KPIs) for the VistaOne Vendor Web Application. These KPIs are designed to measure business performance, user engagement, system reliability, and overall success of the platform.

---

## 1. Daily Active Users (DAU)

**Definition:** Number of unique users who log in and perform at least one meaningful action within a 24-hour period.

**Calculation:**
`DAU = COUNT(DISTINCT user_id) WHERE login_date = current_date AND action_count > 0`

**Target:** 500+ DAU by end of Q1; 1,000+ DAU by end of Q2.

**Data Sources:**
- `users` table (user_id, name)
- `sessions` table (user_id, login_timestamp, activity_timestamp)
- `authentication_events` table (user_id, event_timestamp, event_type)

**Dashboard:** Line chart showing DAU trend over last 30 days.

**Alerting:** Alert if DAU drops below 200 for 3 consecutive days.

---

## 2. Weekly Active Users (WAU) / Monthly Active Users (MAU)

**Definition:** Number of unique users who engage with the platform at least once within a 7-day (WAU) or 30-day (MAU) period.

**Calculation:**
`WAU = COUNT(DISTINCT user_id) WHERE login_timestamp >= (current_date - 7 days)`
`MAU = COUNT(DISTINCT user_id) WHERE login_timestamp >= (current_date - 30 days)`

**Target:** WAU: 2,000+; MAU: 5,000+ by end of Q2.

**Data Sources:**
- `users` table (user_id, name, signup_date)
- `sessions` table (user_id, login_timestamp, session_duration)
- `authentication_events` table (user_id, event_timestamp)

**Dashboard:** Bar chart comparing WAU vs MAU over time; stickiness ratio (WAU/MAU).

**Alerting:** Alert if WAU/MAU ratio drops below 0.30.

---

## 3. User Retention Rate (Weekly/Monthly Cohort Analysis)

**Definition:** Percentage of users who continue to use the platform after their initial signup, measured by cohort (signup week/month).

**Calculation:**
`Retention Rate = (Users active in period N / Users who signed up in period 0) * 100`

**Target:** 40% Week 1 retention; 25% Month 1 retention; 15% Month 3 retention.

**Data Sources:**
- `users` table (user_id, signup_date, account_status)
- `sessions` table (user_id, login_timestamp)
- `authentication_events` table (user_id, event_timestamp)

**Dashboard:** Cohort heatmap showing retention by signup period over time.

**Alerting:** Alert if retention drops more than 10% week-over-week.

---

## 4. Signup Conversion Rate

**Definition:** Percentage of visitors who complete the signup process out of total visitors who initiate the signup flow.

**Calculation:**
`Conversion Rate = (Completed signups / Signup page views) * 100`

**Target:** 25% overall conversion rate; 35% conversion for referred users.

**Data Sources:**
- `users` table (user_id, signup_date, signup_source)
- `sessions` table (page_views, referrer_url)
- `authentication_events` table (event_type: signup_started, signup_completed)

**Dashboard:** Funnel chart showing visitor -> signup page -> completed signup.

**Alerting:** Alert if conversion rate drops below 15% for 2 consecutive days.

---

## 5. Average Transaction Value (ATV)

**Definition:** Average monetary value per transaction completed on the platform.

**Calculation:**
`ATV = SUM(transaction_amount) / COUNT(transactions)`

**Target:** $50+ ATV; $75+ ATV by end of Q2.

**Data Sources:**
- `orders` table (order_id, user_id, total_amount, created_at)
- `order_items` table (item_id, order_id, quantity, price_per_unit)
- `users` table (user_id, account_type)

**Dashboard:** Bar chart showing ATV by category/vendor; trend line over time.

**Alerting:** Alert if ATV drops below $30 for 3 consecutive days.

---

## 6. Authentication Success/Failure Rates

**Definition:** Percentage of login attempts that succeed vs. fail, broken down by failure reason.

**Calculation:**
`Success Rate = (Successful logins / Total login attempts) * 100`
`Failure Rate = (Failed logins / Total login attempts) * 100`

**Target:** 95%+ success rate; <5% failure rate.

**Data Sources:**
- `authentication_events` table (user_id, event_type, event_timestamp, device_info, ip_address)
- `users` table (user_id, email, account_status)

**Dashboard:** Pie chart of login outcomes; line chart of failure rate over time.

**Alerting:** Alert if failure rate exceeds 10% or spike in failed logins from single IP.

---

## 7. User Engagement Metrics (Session Duration, Frequency)

**Definition:** Measures of how long and how often users interact with the platform.

**Calculation:**
`Avg Session Duration = SUM(session_duration) / COUNT(sessions)`
`Avg Sessions Per User = COUNT(sessions) / COUNT(DISTINCT user_id)`
`Pages Per Session = SUM(page_views) / COUNT(sessions)`

**Target:** 5+ min avg session duration; 3+ sessions per user per week; 8+ pages per session.

**Data Sources:**
- `sessions` table (session_id, user_id, login_timestamp, logout_timestamp, session_duration, page_views)
- `users` table (user_id, account_type)

**Dashboard:** Trend lines for session duration, frequency, and pages per session.

**Alerting:** Alert if avg session duration drops below 2 minutes.

---

## 8. Error Rates and System Reliability Metrics

**Definition:** Measures of system health including error rates, uptime, and response times.

**Calculation:**
`Error Rate = (Error responses / Total requests) * 100`
`Uptime = (Uptime seconds / Total seconds in period) * 100`
`Avg Response Time = SUM(response_time_ms) / COUNT(requests)`

**Target:** <1% error rate; 99.9% uptime; <500ms avg response time.

**Data Sources:**
- `sessions` table (request_count, error_count)
- `authentication_events` table (event_type: login_error, system_error)
- Application logs (request_timestamp, response_time_ms, status_code)

**Dashboard:** Gauge charts for uptime and error rate; line chart for response times.

**Alerting:** Alert if error rate >2%, uptime <99%, or response time >1000ms.

---

## KPI Dashboard Template

### Executive Summary Dashboard
- DAU/MAU trend with comparison to previous period
- Retention rate heatmap
- Top 5 KPIs with current values vs targets

### User Engagement Dashboard
- Session duration trends
- Signup conversion funnel
- User retention by cohort

### Transaction Dashboard
- ATV trends by category
- Transaction volume over time
- Revenue by vendor

### System Health Dashboard
- Error rate over time
- Uptime status
- Response time trends

---

## Monitoring and Alerting Strategy

### Alert Tiers
1. **Critical:** Error rate >5%, system downtime, security breach indicators
2. **High:** DAU drop >20%, conversion rate <10%, ATV drop >15%
3. **Medium:** Retention drop >10%, session duration <2 min, authentication failure >10%
4. **Low:** Any KPI deviating from target by 10%

### Notification Channels
- Critical: PagerDuty/SMS + Email + Slack
- High: Slack + Email
- Medium/Low: Slack + Dashboard notification

### Review Cadence
- Daily: Automated dashboard review
- Weekly: KPI review meeting with stakeholders
- Monthly: KPI target reassessment and adjustment

---

## KPI Framework Alignment with Business Goals

| Business Goal | Supporting KPIs |
|---|---|
| Grow user base | DAU, WAU, MAU, Signup Conversion Rate |
| Increase user engagement | Session Duration, Pages Per Session, Retention Rate |
| Maximize revenue | ATV, Transaction Volume, Revenue by Vendor |
| Ensure platform reliability | Error Rate, Uptime, Response Time |
| Improve user security | Authentication Success Rate, Failed Login Attempts |

---

## Implementation Notes

### Backend Implementation
- Add event logging for all user actions
- Implement session tracking with duration calculation
- Create database views for KPI calculations
- Set up scheduled jobs for daily/weekly/monthly aggregation

### Frontend Implementation
- Implement analytics SDK integration
- Track page views, button clicks, and user flows
- Add session start/end events
- Implement user identification and tracking

### Data Pipeline
- ETL jobs to aggregate raw data into KPI metrics
- Data warehouse tables for historical KPI storage
- API endpoints for dashboard data consumption
