docs/DATA_DICTIONARY.md# Data Dictionary - VistaOne

## USERS
| Field | Type | Nullable | Unique | Description |
|user_id|INT|NO|YES|Primary key, auto-increment|
|username|VARCHAR(50)|NO|YES|Unique login username|
|email|VARCHAR(100)|NO|YES|Email address|
|password_hash|VARCHAR(255)|NO|NO|Bcrypt hashed password|
|first_name|VARCHAR(50)|YES|NO|First name|
|last_name|VARCHAR(50)|YES|NO|Last name|
|phone|VARCHAR(20)|YES|NO|Phone number|
|user_type|VARCHAR(20)|NO|NO|customer/vendor/admin|
|is_active|BOOLEAN|NO|NO|Active status (default: true)|
|created_at|TIMESTAMP|NO|NO|Creation time|
|updated_at|TIMESTAMP|NO|NO|Update time|

## VENDORS
| Field | Type | Nullable | FK | Description |
|vendor_id|INT|NO|N/A|Primary key|
|user_id|INT|NO|users.user_id|Associated user|
|business_name|VARCHAR(100)|NO|N/A|Business name|
|business_description|TEXT|YES|N/A|Description|
|business_address|VARCHAR(255)|YES|N/A|Address|
|city|VARCHAR(50)|YES|N/A|City|
|state|VARCHAR(50)|YES|N/A|State|
|zip_code|VARCHAR(10)|YES|N/A|Zip code|
|country|VARCHAR(50)|YES|N/A|Country|
|business_phone|VARCHAR(20)|YES|N/A|Business phone|
|business_email|VARCHAR(100)|YES|N/A|Business email|
|tax_id|VARCHAR(50)|YES|N/A|Tax ID|
|is_verified|BOOLEAN|NO|N/A|Verified (default: false)|
|rating|DECIMAL(3,2)|NO|N/A|Rating 0-5 (default: 0.00)|
|created_at|TIMESTAMP|NO|N/A|Creation time|
|updated_at|TIMESTAMP|NO|N/A|Update time|

## PRODUCTS
| Field | Type | Nullable | FK | Description |
|product_id|INT|NO|N/A|Primary key|
|vendor_id|INT|NO|vendors.vendor_id|Vendor|
|category_id|INT|YES|categories.category_id|Category|
|product_name|VARCHAR(200)|NO|N/A|Product name|
|description|TEXT|YES|N/A|Description|
|price|DECIMAL(10,2)|NO|N/A|Price|
|quantity_available|INT|NO|N/A|Inventory (default: 0)|
|sku|VARCHAR(50)|YES|YES|Stock code|
|is_active|BOOLEAN|NO|N/A|Active (default: true)|
|created_at|TIMESTAMP|NO|N/A|Creation time|
|updated_at|TIMESTAMP|NO|N/A|Update time|

## ORDERS
| Field | Type | Nullable | FK | Description |
|order_id|INT|NO|N/A|Primary key|
|customer_id|INT|YES|users.user_id|Customer|
|order_status|VARCHAR(20)|NO|N/A|pending/processing/shipped/delivered/cancelled|
|total_amount|DECIMAL(10,2)|NO|N/A|Order total|
|shipping_address|VARCHAR(255)|YES|N/A|Delivery address|
|city|VARCHAR(50)|YES|N/A|City|
|state|VARCHAR(50)|YES|N/A|State|
|zip_code|VARCHAR(10)|YES|N/A|Zip code|
|country|VARCHAR(50)|YES|N/A|Country|
|created_at|TIMESTAMP|NO|N/A|Creation time|
|updated_at|TIMESTAMP|NO|N/A|Update time|

## ORDER_ITEMS
| Field | Type | Nullable | FK | Description |
|order_item_id|INT|NO|N/A|Primary key|
|order_id|INT|NO|orders.order_id|Order|
|product_id|INT|YES|products.product_id|Product|
|quantity|INT|NO|N/A|Quantity|
|unit_price|DECIMAL(10,2)|NO|N/A|Unit price|
|subtotal|DECIMAL(10,2)|NO|N/A|Line total|
|created_at|TIMESTAMP|NO|N/A|Creation time|

## REVIEWS
| Field | Type | Nullable | FK | Description |
|review_id|INT|NO|N/A|Primary key|
|product_id|INT|NO|products.product_id|Product|
|customer_id|INT|YES|users.user_id|Reviewer|
|rating|INT|NO|N/A|Rating 1-5|
|review_text|TEXT|YES|N/A|Review text|
|is_verified_purchase|BOOLEAN|NO|N/A|Verified (default: false)|
|created_at|TIMESTAMP|NO|N/A|Creation time|
|updated_at|TIMESTAMP|NO|N/A|Update time|

## CATEGORIES
| Field | Type | Nullable | FK | Description |
|category_id|INT|NO|N/A|Primary key|
|category_name|VARCHAR(100)|NO|N/A|Category name|
|description|TEXT|YES|N/A|Description|
|parent_category_id|INT|YES|categories.category_id|Parent category|
|created_at|TIMESTAMP|NO|N/A|Creation time|

---
*Last Updated: 2026-03-16*
