# E-Commerce Order Management System

A complete **E-Commerce Order Management Backend API** built using **FastAPI, Python, MySQL, SQLAlchemy, Alembic, JWT Authentication, and SMTP**.

The system manages products, categories, customers, shopping carts, addresses, orders, payments, returns, refunds, reviews, email notifications, and admin reports.

It also implements real-world business rules such as stock management, order status transitions, payment validation, return eligibility, refund processing, role-based authorization, database transactions, and background email notifications.

---

## Features

### Authentication & Authorization

* Customer registration
* Customer login
* JWT-based authentication
* 30-minute JWT token expiration
* Password hashing using bcrypt
* Role-based access control
* Admin and Customer roles
* Protected APIs
* `401 Unauthorized` for invalid/expired tokens
* `403 Forbidden` for insufficient permissions

### Category Management

* Create category
* View categories
* Update category
* Delete category
* Unique category names
* Prevent deletion when active products exist

### Product Management

* Create products
* View products
* View product by ID
* Update products
* Soft delete products
* Unique SKU
* Product price validation
* Stock validation
* Category relationship
* Active/inactive product handling

### Product Search & Filtering

Products can be searched and filtered using:

* Partial product name
* Category
* Minimum price
* Maximum price
* Stock availability
* Price sorting
* Created date sorting
* Ascending/descending order
* Pagination using `skip` and `limit`

Example:

```text
GET /products?name=phone&min_price=10000&max_price=30000&sort_by=price&order=asc&skip=0&limit=10
```

### Shopping Cart

* One cart per customer
* Add product to cart
* Update quantity
* Remove cart item
* Clear cart
* Automatic quantity increase for duplicate products
* Stock validation
* Cart subtotal calculation
* Item price and line total calculation

### Address Management

* Add address
* View addresses
* Update address
* Delete address
* Set default address
* Multiple addresses per customer
* Only one default address
* 10-digit phone validation
* 6-digit pincode validation

### Order Management

* Place order from cart
* View customer orders
* Admin can view all orders
* View order details
* Cancel order
* Admin order status management
* Automatic order number generation
* GST calculation
* Delivery charge calculation
* Stock deduction
* Cart clearing after order placement

### Payments

Mock payment system supporting:

* UPI
* Card
* Net Banking
* COD

Features:

* Payment amount validation
* Unique transaction ID
* Successful payment
* Failed payment
* Payment retry
* Payment history
* Prevent duplicate payment
* Cancelled orders cannot be paid

### Returns & Refunds

* Request return
* View returns
* Admin approval
* Admin rejection
* Refund processing
* Stock restoration
* Refund amount calculation
* Rejection reason
* Seven-day return window

### Product Reviews

* Add review
* View product reviews
* Update own review
* Delete own review
* Rating from 1 to 5
* One review per customer/product
* Delivered-order eligibility
* Average rating
* Total review count

### Email Notifications

Email notifications are handled using:

* FastAPI `BackgroundTasks`
* Python `smtplib`
* SMTP
* Gmail App Password or Mailtrap

Emails are sent for:

* Registration
* Order placed
* Payment successful
* Order shipped
* Order delivered
* Order cancelled
* Return approved
* Refund processed
* Return rejected

Email failures are logged and do not cause the main API operation to fail.

### Admin Reports

Admin-only reports include:

* Sales report
* Orders by status
* Top five products
* Low-stock products

---

# Technology Stack

| Technology              | Purpose                     |
| ----------------------- | --------------------------- |
| Python 3.9+             | Programming language        |
| FastAPI                 | Backend REST API            |
| Pydantic                | Data validation             |
| SQLAlchemy              | ORM                         |
| MySQL                   | Relational database         |
| Alembic                 | Database migrations         |
| JWT                     | Authentication              |
| bcrypt                  | Password hashing            |
| FastAPI BackgroundTasks | Background email processing |
| smtplib                 | SMTP email sending          |
| Uvicorn                 | ASGI server                 |
| Pytest                  | Testing                     |

---

# Project Architecture

```text
E-Commerce-Order-Management/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── config.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── category.py
│   │   ├── product.py
│   │   ├── cart.py
│   │   ├── cart_item.py
│   │   ├── address.py
│   │   ├── order.py
│   │   ├── order_item.py
│   │   ├── payment.py
│   │   ├── return_model.py
│   │   └── review.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── category.py
│   │   ├── product.py
│   │   ├── cart.py
│   │   ├── address.py
│   │   ├── order.py
│   │   ├── payment.py
│   │   ├── return_schema.py
│   │   └── review.py
│   │
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── categories.py
│   │   ├── products.py
│   │   ├── cart.py
│   │   ├── addresses.py
│   │   ├── orders.py
│   │   ├── payments.py
│   │   ├── returns.py
│   │   ├── reviews.py
│   │   └── reports.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   ├── category_service.py
│   │   ├── product_service.py
│   │   ├── cart_service.py
│   │   ├── address_service.py
│   │   ├── order_service.py
│   │   ├── payment_service.py
│   │   ├── return_service.py
│   │   ├── review_service.py
│   │   └── report_service.py
│   │
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── jwt.py
│   │   └── dependencies.py
│   │
│   └── utils/
│       ├── __init__.py
│       └── email.py
│
├── alembic/
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
│
├── alembic.ini
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

# Database Relationships

The application uses the following relationships:

```text
Category
   │
   └── 1 : Many
          │
       Products
```

```text
Customer
   │
   ├── 1 : 1 ── Cart
   │             │
   │             └── 1 : Many ── CartItems
   │
   ├── 1 : Many ── Addresses
   │
   ├── 1 : Many ── Orders
   │                    │
   │                    └── 1 : Many ── OrderItems
   │
   └── 1 : Many ── Reviews
```

```text
Order
   │
   ├── 1 : Many ── Payments
   │
   └── 1 : 1 ── ReturnRequest
```

```text
Product
   │
   └── 1 : Many ── Reviews
```

---

# Requirements

Before running the project, install:

* Python 3.9 or higher
* MySQL Server
* MySQL Workbench
* Visual Studio Code
* Git

Verify Python:

```bash
python --version
```

Verify pip:

```bash
pip --version
```

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/E-Commerce-Order-Management.git
```

Move into the project:

```bash
cd E-Commerce-Order-Management
```

---

# 2. Create Virtual Environment

Windows:

```powershell
python -m venv venv
```

Activate it:

```powershell
venv\Scripts\activate
```

After activation, the terminal should show:

```text
(venv)
```

---

# 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

---

# 4. Create MySQL Database

Open MySQL Workbench or MySQL command line.

Create the database:

```sql
CREATE DATABASE ecommerce_order_db;
```

Verify:

```sql
SHOW DATABASES;
```

---

# 5. Configure Environment Variables

Create a `.env` file in the project root.

Example:

```env
DATABASE_URL=mysql+mysqlconnector://root:YOUR_PASSWORD@localhost:3306/ecommerce_order_db

JWT_SECRET_KEY=your-super-secret-jwt-key
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=30

SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=your-gmail-app-password
SMTP_FROM=your-email@gmail.com
```

Never commit the real `.env` file to GitHub.

Use `.env.example` for sharing configuration structure.

Example:

```env
DATABASE_URL=mysql+mysqlconnector://root:YOUR_PASSWORD@localhost:3306/ecommerce_order_db

JWT_SECRET_KEY=CHANGE_THIS_SECRET_KEY
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=30

SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=
SMTP_PASSWORD=
SMTP_FROM=
```

---

# 6. Database URL Special Characters

If the MySQL password contains URL-special characters such as:

```text
@
#
/
:
?
%
```

the password may need URL encoding when used inside `DATABASE_URL`.

For example, a password containing `@` must not be placed directly into a URL without encoding.

---

# 7. Run Alembic Migrations

The project uses Alembic for database schema management.

Check the current migration:

```powershell
alembic current
```

Check migration history:

```powershell
alembic history
```

Apply all migrations:

```powershell
alembic upgrade head
```

Verify the database tables in MySQL:

```sql
USE ecommerce_order_db;

SHOW TABLES;
```

Important:

The application does **not** use:

```python
Base.metadata.create_all()
```

All database schema changes are handled through Alembic.

---

# 8. Run the FastAPI Application

Start Uvicorn:

```powershell
uvicorn app.main:app --reload
```

The server will start at:

```text
http://127.0.0.1:8000
```

---

# 9. Open Swagger Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

FastAPI provides interactive Swagger API documentation.

Alternative ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

# Authentication Flow

The authentication process is:

```text
Register
   ↓
Login
   ↓
Receive JWT Access Token
   ↓
Authorize in Swagger
   ↓
Access Protected APIs
```

## Register

```http
POST /auth/register
```

Example:

```json
{
    "name": "Pavan",
    "email": "pavan@example.com",
    "password": "Password123"
}
```

---

## Login

```http
POST /auth/login
```

Example:

```json
{
    "email": "pavan@example.com",
    "password": "Password123"
}
```

Response:

```json
{
    "access_token": "JWT_TOKEN",
    "token_type": "bearer"
}
```

---

## Current User

```http
GET /auth/me
```

Requires:

```text
Authorization: Bearer JWT_TOKEN
```

---

# Role-Based Access Control

The application supports two roles:

## Customer

Customers can:

* Browse products
* Manage their cart
* Manage their addresses
* Place orders
* Make payments
* Request returns
* Write reviews
* View their own orders

## Admin

Admins can:

* Manage categories
* Manage products
* View all orders
* Update order status
* Manage returns
* Process refunds
* View reports

Unauthorized access returns:

```text
403 Forbidden
```

---

# API Endpoints

## Authentication

| Method | Endpoint         | Access        |
| ------ | ---------------- | ------------- |
| POST   | `/auth/register` | Public        |
| POST   | `/auth/login`    | Public        |
| GET    | `/auth/me`       | Authenticated |

---

## Categories

| Method | Endpoint                    | Access        |
| ------ | --------------------------- | ------------- |
| POST   | `/categories`               | Admin         |
| GET    | `/categories`               | Authenticated |
| PUT    | `/categories/{category_id}` | Admin         |
| DELETE | `/categories/{category_id}` | Admin         |

---

## Products

| Method | Endpoint                 | Access        |
| ------ | ------------------------ | ------------- |
| POST   | `/products`              | Admin         |
| GET    | `/products`              | Authenticated |
| GET    | `/products/{product_id}` | Authenticated |
| PUT    | `/products/{product_id}` | Admin         |
| DELETE | `/products/{product_id}` | Admin         |

---

## Cart

| Method | Endpoint                | Access   |
| ------ | ----------------------- | -------- |
| GET    | `/cart`                 | Customer |
| POST   | `/cart/items`           | Customer |
| PUT    | `/cart/items/{item_id}` | Customer |
| DELETE | `/cart/items/{item_id}` | Customer |
| DELETE | `/cart`                 | Customer |

---

## Addresses

| Method | Endpoint                          | Access   |
| ------ | --------------------------------- | -------- |
| POST   | `/addresses`                      | Customer |
| GET    | `/addresses`                      | Customer |
| PUT    | `/addresses/{address_id}`         | Customer |
| DELETE | `/addresses/{address_id}`         | Customer |
| PUT    | `/addresses/{address_id}/default` | Customer |

---

## Orders

| Method | Endpoint                    | Access         |
| ------ | --------------------------- | -------------- |
| POST   | `/orders`                   | Customer       |
| GET    | `/orders`                   | Customer/Admin |
| GET    | `/orders/{order_id}`        | Customer/Admin |
| PUT    | `/orders/{order_id}/cancel` | Customer       |
| PUT    | `/orders/{order_id}/status` | Admin          |

---

## Payments

| Method | Endpoint                      | Access         |
| ------ | ----------------------------- | -------------- |
| POST   | `/orders/{order_id}/pay`      | Customer       |
| GET    | `/orders/{order_id}/payments` | Customer/Admin |

---

## Returns

| Method | Endpoint                       | Access         |
| ------ | ------------------------------ | -------------- |
| POST   | `/orders/{order_id}/returns`   | Customer       |
| GET    | `/returns`                     | Customer/Admin |
| PUT    | `/returns/{return_id}/approve` | Admin          |
| PUT    | `/returns/{return_id}/reject`  | Admin          |

---

## Reviews

| Method | Endpoint                         | Access        |
| ------ | -------------------------------- | ------------- |
| POST   | `/products/{product_id}/reviews` | Customer      |
| GET    | `/products/{product_id}/reviews` | Authenticated |
| PUT    | `/reviews/{review_id}`           | Owner         |
| DELETE | `/reviews/{review_id}`           | Owner         |

---

## Reports

| Method | Endpoint                    | Access |
| ------ | --------------------------- | ------ |
| GET    | `/reports/sales`            | Admin  |
| GET    | `/reports/orders-by-status` | Admin  |
| GET    | `/reports/top-products`     | Admin  |
| GET    | `/reports/low-stock`        | Admin  |

---

# Order Calculation

The order total follows the following formula:

```text
Subtotal = Sum of all Order Item Line Totals

GST = 18% of Subtotal

Delivery Charge =
    ₹50 if Subtotal <= ₹500
    ₹0  if Subtotal > ₹500

Grand Total =
    Subtotal + GST + Delivery Charge
```

Example:

```text
Product total = ₹1,000

GST = ₹180

Delivery = ₹0

Grand Total = ₹1,180
```

---

# Order Lifecycle

Normal order flow:

```text
Pending
   ↓
Confirmed
   ↓
Shipped
   ↓
Delivered
```

Cancellation:

```text
Pending ──────→ Cancelled
   │
   └──────────→ Confirmed ──────→ Cancelled
```

Orders that are already:

```text
Shipped
Delivered
```

cannot be cancelled by customers.

---

# Transactional Order Placement

Order creation is handled as a database transaction.

The process is:

```text
Validate Cart
      ↓
Validate Product
      ↓
Validate Stock
      ↓
Calculate Order Total
      ↓
Create Order
      ↓
Create Order Items
      ↓
Reduce Product Stock
      ↓
Clear Cart
      ↓
Commit Transaction
```

If any step fails:

```text
ROLLBACK
```

This prevents partial orders and incorrect stock quantities.

---

# Stock Management

When an order is placed:

```text
Available Stock - Ordered Quantity
```

When a qualifying cancellation or approved return occurs:

```text
Available Stock + Returned Quantity
```

Inactive products cannot be purchased.

Products with zero stock cannot be added to the cart.

---

# Payment Rules

Supported payment methods:

```text
UPI
Card
Net Banking
COD
```

Payment amount must exactly match the order grand total.

A successful payment:

```text
Payment Status = Success
Order Status = Confirmed
Order Payment Status = Paid
```

A failed payment:

```text
Order remains Pending
```

A cancelled order cannot receive a payment.

An already paid order cannot be paid again.

---

# Return & Refund Rules

Returns are allowed only when:

```text
Order Status = Delivered
```

and the return request is made within:

```text
7 days
```

Only one return request is allowed per order.

Approval flow:

```text
Requested
    ↓
Approved
    ↓
Refunded
```

When a return is approved:

```text
Restore Stock
      ↓
Refund Grand Total
      ↓
Set Return = Refunded
      ↓
Set Order Payment Status = Refunded
```

For rejected returns, an explanation is required.

---

# Product Review Rules

A customer can review a product only if:

1. The customer purchased the product.
2. The order containing the product was delivered.
3. The customer has not already reviewed the product.

Rating must be between:

```text
1 and 5
```

Customers can edit or delete only their own reviews.

Product details include:

```text
Average Rating
Total Review Count
```

---

# Email Notifications

The application uses FastAPI BackgroundTasks so email sending does not block the main API request.

Example flow:

```text
Customer places order
        ↓
Order saved successfully
        ↓
API returns response
        ↓
BackgroundTask
        ↓
SMTP Server
        ↓
Customer Email
```

Supported email events:

```text
Registration Successful
Order Placed
Payment Successful
Order Shipped
Order Delivered
Order Cancelled
Return Approved
Refund Processed
Return Rejected
```

If email delivery fails, the error is logged and the main transaction remains successful.

---

# Gmail SMTP Configuration

For Gmail, use a Gmail App Password instead of your normal Gmail password.

Example:

```env
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=YOUR_APP_PASSWORD
SMTP_FROM=your-email@gmail.com
```

Never commit real SMTP credentials to GitHub.

For development/testing, Mailtrap can also be used.

---

# Error Handling

The API uses appropriate HTTP status codes.

| Status | Meaning                               |
| ------ | ------------------------------------- |
| 200    | Successful request                    |
| 201    | Resource created                      |
| 400    | Invalid business operation            |
| 401    | Authentication required/invalid token |
| 403    | Insufficient permissions              |
| 404    | Resource not found                    |
| 409    | Duplicate/conflicting resource        |
| 422    | Validation error                      |

Examples:

```text
Duplicate email → 409
Duplicate SKU → 409
Invalid JWT → 401
Customer accessing admin API → 403
Product not found → 404
Invalid phone number → 422
```

---

# Database Migrations

Create a migration:

```powershell
alembic revision --autogenerate -m "your migration message"
```

Review the generated migration before applying it.

Apply migration:

```powershell
alembic upgrade head
```

Rollback one migration:

```powershell
alembic downgrade -1
```

Show migration history:

```powershell
alembic history
```

Show current version:

```powershell
alembic current
```

---

# Testing

Run the test suite using:

```powershell
pytest
```

Example tests should cover:

* Order placement
* Stock deduction
* Empty cart validation
* Insufficient stock
* Order cancellation
* Stock restoration
* Payment validation
* Return eligibility

---

# GitHub Setup

Before pushing the project to GitHub, make sure `.gitignore` contains:

```gitignore
venv/
__pycache__/
*.pyc
.env
.idea/
.vscode/
.pytest_cache/
```

The real `.env` file must never be committed.

The following file should be committed:

```text
.env.example
```

---

# Git Commands

Initialize Git if required:

```powershell
git init
```

Check files:

```powershell
git status
```

Add files:

```powershell
git add .
```

Commit:

```powershell
git commit -m "Initial E-Commerce Order Management System"
```

Add your GitHub repository:

```powershell
git remote add origin https://github.com/YOUR_USERNAME/E-Commerce-Order-Management.git
```

Rename the branch:

```powershell
git branch -M main
```

Push:

```powershell
git push -u origin main
```

---

# Important Security Notes

Never commit:

```text
.env
Database passwords
JWT secret keys
SMTP passwords
Gmail App Passwords
API keys
Production credentials
```

Use:

```text
.env
```

for local secrets and:

```text
.env.example
```

for the GitHub repository.

---

# API Documentation

After starting the application, Swagger documentation is available at:

```text
http://127.0.0.1:8000/docs
```

ReDoc documentation:

```text
http://127.0.0.1:8000/redoc
```

---

# Suggested Testing Flow

For a complete demonstration, follow this sequence:

```text
1. Register Customer
       ↓
2. Login
       ↓
3. Authorize JWT
       ↓
4. Create Category (Admin)
       ↓
5. Create Product (Admin)
       ↓
6. Browse Products
       ↓
7. Create Address
       ↓
8. Add Product to Cart
       ↓
9. View Cart
       ↓
10. Place Order
       ↓
11. Make Payment
       ↓
12. Admin confirms/ships order
       ↓
13. Admin marks order Delivered
       ↓
14. Customer submits Review
       ↓
15. Customer requests Return
       ↓
16. Admin approves Return
       ↓
17. Refund processed
       ↓
18. Email notification sent
```

---

# Main Screenshots for Project Documentation

Recommended screenshots for the project report:

1. Project folder structure
2. MySQL database and tables
3. Alembic migration
4. User registration
5. JWT login
6. Swagger authorization
7. Category management
8. Product management
9. Product search/filter/pagination
10. Cart management
11. Address management
12. Order placement
13. Payment
14. Return and refund
15. Product reviews
16. Admin reports
17. Order placed email
18. Order shipped email
19. Refund processed email

---

# Future Enhancements

Possible future improvements include:

* Wishlist
* Coupons
* Discount codes
* Product image upload
* Online payment gateway integration
* Razorpay/Stripe integration
* Redis caching
* Celery background workers
* Docker deployment
* Docker Compose
* CI/CD
* Automated API testing
* Advanced analytics
* Inventory management
* Product variants
* Order invoice generation
* Cloud deployment

---

# Bonus Features

The project can be extended with:

### Wishlist

```text
Add Wishlist Item
View Wishlist
Remove Wishlist Item
Move Wishlist Item to Cart
```

### Coupons

Support:

* Percentage discount
* Flat discount
* Minimum order value
* Expiry date
* Usage limit

### Automated Tests

Pytest tests for:

* Order creation
* Stock deduction
* Order cancellation
* Payment
* Returns
* Refunds

---

# Project Status

## Completed Core Modules

* [x] FastAPI project setup
* [x] MySQL database
* [x] SQLAlchemy models
* [x] Alembic migrations
* [x] JWT authentication
* [x] Role-based authorization
* [x] Category management
* [x] Product management
* [x] Product search/filtering
* [x] Pagination
* [x] Cart management
* [x] Address management
* [x] Order management
* [x] Transactional order placement
* [x] Payment management
* [x] Returns
* [x] Refund processing
* [x] Product reviews
* [x] Email notifications
* [x] Admin reports

## Optional Enhancements

* [ ] Wishlist
* [ ] Coupons
* [ ] Payment gateway
* [ ] Docker
* [ ] CI/CD
* [ ] Advanced automated tests

---
E-Commerce Order Management System
Built using Python, FastAPI, MySQL, SQLAlchemy, Alembic and JWT Authentication.

---

# License

This project is intended for learning, portfolio, and educational purposes.
