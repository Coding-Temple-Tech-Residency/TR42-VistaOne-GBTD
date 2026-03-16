# Entity Relationship Diagram (ERD) - VistaOne Vendor Web Application

## Overview

This document describes the database structure for the VistaOne vendor web platform. The ERD visualizes how data entities relate to each other and provides a reference for building consistent data collection systems.

## Core Entities

### 1. users
Stores user account information for customers, vendors, and admins.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| user_id | int | PK, AUTO INCREMENT | Primary key |
| username | varchar(50) | UNIQUE, NOT NULL | Unique username |
| email | varchar(100) | UNIQUE, NOT NULL | Unique email address |
| password_hash | varchar(255) | NOT NULL | Hashed password |
| first_name | varchar(50) | - | User's first name |
| last_name | varchar(50) | - | User's last name |
| phone | varchar(20) | - | Contact phone number |
| user_type | varchar(20) | NOT NULL, CHECK | Role: customer, vendor, or admin |
| is_active | boolean | DEFAULT TRUE | Account active status |
| created_at | timestamp | DEFAULT CURRENT_TIMESTAMP | Record creation time |
| updated_at | timestamp | DEFAULT CURRENT_TIMESTAMP | Last update time |

### 2. vendors
Stores vendor business profile and verification details.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| vendor_id | int | PK, AUTO INCREMENT | Primary key |
| user_id | int | FK → users.user_id | Links to user account |
| business_name | varchar(100) | NOT NULL | Vendor business name |
| business_description | text | - | Business description |
| business_address | varchar(255) | - | Business street address |
| city | varchar(50) | - | City |
| state | varchar(50) | - | State/Province |
| zip_code | varchar(10) | - | Postal code |
| country | varchar(50) | - | Country |
| business_phone | varchar(20) | - | Business phone |
| business_email | varchar(100) | - | Business email |
| tax_id | varchar(50) | - | Tax identification number |
| is_verified | boolean | DEFAULT FALSE | Vendor verification status |
| rating | decimal(3,2) | DEFAULT 0.00 | Average vendor rating |
| created_at | timestamp | DEFAULT CURRENT_TIMESTAMP | Record creation time |
| updated_at | timestamp | DEFAULT CURRENT_TIMESTAMP | Last update time |

### 3. categories
Product/Service categories with hierarchical (parent/child) structure.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| category_id | int | PK, AUTO INCREMENT | Primary key |
| category_name | varchar(100) | NOT NULL | Category name |
| description | text | - | Category description |
| parent_category_id | int | FK → categories.category_id | Self-reference for hierarchy |
| created_at | timestamp | DEFAULT CURRENT_TIMESTAMP | Record creation time |

### 4. products
Product catalog with pricing and inventory.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| product_id | int | PK, AUTO INCREMENT | Primary key |
| vendor_id | int | FK → vendors.vendor_id | Links to vendor |
| category_id | int | FK → categories.category_id | Product category |
| product_name | varchar(200) | NOT NULL | Product name |
| description | text | - | Product description |
| price | decimal(10,2) | NOT NULL | Product price |
| quantity_available | int | DEFAULT 0 | Inventory count |
| sku | varchar(50) | UNIQUE | Stock Keeping Unit |
| is_active | boolean | DEFAULT TRUE | Product active status |
| created_at | timestamp | DEFAULT CURRENT_TIMESTAMP | Record creation time |
| updated_at | timestamp | DEFAULT CURRENT_TIMESTAMP | Last update time |

### 5. orders
Customer orders with shipping information.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| order_id | int | PK, AUTO INCREMENT | Primary key |
| customer_id | int | FK → users.user_id | Links to customer user |
| order_status | varchar(20) | NOT NULL, CHECK | Status: pending, processing, shipped, delivered, cancelled |
| total_amount | decimal(10,2) | NOT NULL | Order total |
| shipping_address | varchar(255) | - | Shipping address |
| city | varchar(50) | - | City |
| state | varchar(50) | - | State |
| zip_code | varchar(10) | - | Postal code |
| country | varchar(50) | - | Country |
| created_at | timestamp | DEFAULT CURRENT_TIMESTAMP | Order creation time |
| updated_at | timestamp | DEFAULT CURRENT_TIMESTAMP | Last update time |

### 6. order_items
Line items for each order (join table between orders and products).

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| order_item_id | int | PK, AUTO INCREMENT | Primary key |
| order_id | int | FK → orders.order_id | Links to order |
| product_id | int | FK → products.product_id | Links to product |
| quantity | int | NOT NULL | Quantity ordered |
| unit_price | decimal(10,2) | NOT NULL | Price per unit |
| subtotal | decimal(10,2) | NOT NULL | Line total (qty × unit_price) |
| created_at | timestamp | DEFAULT CURRENT_TIMESTAMP | Record creation time |

### 7. reviews
Customer reviews and ratings for products.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| review_id | int | PK, AUTO INCREMENT | Primary key |
| product_id | int | FK → products.product_id | Links to product |
| customer_id | int | FK → users.user_id | Links to customer user |
| rating | int | NOT NULL, CHECK (1-5) | Star rating |
| review_text | text | - | Review content |
| is_verified_purchase | boolean | DEFAULT FALSE | Verified purchase flag |
| created_at | timestamp | DEFAULT CURRENT_TIMESTAMP | Review creation time |
| updated_at | timestamp | DEFAULT CURRENT_TIMESTAMP | Last update time |

## Entity Relationships

### Cardinality Overview

| Relationship | Type | Cardinality | Business Logic |
|-------------|------|-------------|----------------|
| vendors → users | FK | 1:1 | Each vendor has exactly one user account |
| products → vendors | FK | N:1 | Many products belong to one vendor |
| products → categories | FK | N:1 | Many products belong to one category |
| categories → categories | Self-Ref | N:1 | Categories can have parent categories (hierarchy) |
| orders → users | FK | N:1 | Many orders belong to one customer |
| order_items → orders | FK | N:1 | Many items belong to one order |
| order_items → products | FK | N:1 | Many order items reference one product |
| reviews → products | FK | N:1 | Many reviews belong to one product |
| reviews → users | FK | N:1 | Many reviews come from one customer |

### Relationship Diagram

```
users (1) ←─── (1) vendors (1) ───→ (N) products (N) ───→ (1) categories
  │                                        │
  │ (1)                                    │ (1)
  ↓                                        ↓
(N) orders (1) ───→ (N) order_items        (N) reviews (N)
```

## Data Flow

1. **User Registration** → Creates a `users` record with customer, vendor, or admin role
2. **Vendor Onboarding** → Links a `users` record to a new `vendors` profile
3. **Product Listing** → Vendor creates `products` linked to their `vendor_id` and a `category_id`
4. **Customer Order** → Customer places an `orders` record, which creates multiple `order_items`
5. **Review System** → Customers submit `reviews` linked to both the `product` and their user account

## Visual ERD

The interactive ERD is available at: **https://dbdiagram.io/d/69b893d9fb2db18e3b9568ac**

---
*Last Updated: 2026-03-16*
