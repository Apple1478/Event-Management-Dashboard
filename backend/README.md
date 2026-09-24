# Ventixe Event Management Backend (FastAPI + SQLAlchemy)

Production-ready RESTful backend engine powering the **Ventixe Event Management Dashboard**, engineered with **FastAPI**, **SQLAlchemy ORM**, **Pydantic v2**, and **SQLite / PostgreSQL**.

---

## 📋 Table of Contents
- [Tech Stack & Architecture](#tech-stack--architecture)
- [Directory Structure](#directory-structure)
- [Prerequisites & Installation](#prerequisites--installation)
- [Database Setup & Seeding](#database-setup--seeding)
- [Running the Server](#running-the-server)
- [API Documentation & Endpoints](#api-documentation--endpoints)
  - [Dashboard & Analytics](#1-dashboard--analytics)
  - [Events Management](#2-events-management)
  - [Bookings & Vouchers](#3-bookings--vouchers)
  - [Invoices & Billing](#4-invoices--billing)
  - [Inbox & Messages](#5-inbox--messages)
  - [Calendar & Schedule](#6-calendar--schedule)
  - [Financials & Ledger](#7-financials--ledger)
  - [Gallery Albums](#8-gallery-albums)
  - [Customer Reviews](#9-customer-reviews)
- [Database Schema & Models](#database-schema--models)
- [Troubleshooting & FAQs](#troubleshooting--faqs)

---

## 🛠️ Tech Stack & Architecture

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/) (Python 3.10 - 3.13)
- **ASGI Server**: [Uvicorn](https://www.uvicorn.org/) with Hot Module Reloading
- **ORM**: [SQLAlchemy 2.0](https://www.sqlalchemy.org/)
- **Validation**: [Pydantic v2](https://docs.pydantic.dev/)
- **Database**: SQLite (default `ventixe.db` for instant zero-config setup; drop-in compatible with PostgreSQL)
- **CORS**: Configured for local development (`http://localhost:4200`, `http://localhost:5173`, `http://127.0.0.1:4200`)

---

## 📂 Directory Structure

```plaintext
backend/
├── database.py       # SQLAlchemy engine, session maker, Base declarative model
├── models.py         # 11 core database models with foreign keys & relationships
├── schemas.py        # Pydantic v2 request/response validation schemas
├── seeds.py          # Realistic seed script populating all 13 Figma screens
├── main.py           # FastAPI app instance, CORS middleware, REST routers
├── ventixe.db        # SQLite database file (generated automatically upon seed/start)
└── README.md         # Comprehensive backend documentation
```

---

## 🚀 Prerequisites & Installation

### 1. Python Environment
Ensure Python 3.10, 3.11, 3.12, or 3.13 is installed:
```powershell
python --version
```

### 2. Install Required Dependencies
Run the following in your terminal:
```powershell
pip install fastapi uvicorn sqlalchemy pydantic python-multipart
```

---

## 💾 Database Setup & Seeding

The backend includes a pre-configured database seeding utility (`seeds.py`) that populates realistic mock data matching every Figma design view (VIP ticket packages, conference agendas, revenue metrics, customer reviews, gallery albums, and invoices).

To initialize and seed the database:
```powershell
cd D:\proj\EventManagementDashboard\backend
python seeds.py
```

*Output:*
```plaintext
Database tables initialized successfully.
Database seeded successfully with Figma-aligned mockup dataset!
```

---

## ⚡ Running the Server

### Option A: From inside `backend/` directory
```powershell
cd D:\proj\EventManagementDashboard\backend
python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

### Option B: From the project root
```powershell
cd D:\proj\EventManagementDashboard
python -m uvicorn backend.main:app --host 127.0.0.1 --port 8000 --reload
```

### 🌐 Access Points
- **REST API Base URL**: `http://127.0.0.1:8000`
- **Interactive OpenAPI Docs (Swagger UI)**: `http://127.0.0.1:8000/docs`
- **Alternative API Docs (ReDoc)**: `http://127.0.0.1:8000/redoc`

---

## 📡 API Documentation & Endpoints

### 1. Dashboard & Analytics
- `GET /api/dashboard/stats`: Returns aggregated key performance indicators:
  ```json
  {
    "total_revenue": 128450.00,
    "revenue_change_pct": 12.5,
    "total_bookings": 1420,
    "bookings_change_pct": 8.2,
    "active_events": 24,
    "total_customers": 3890,
    "customers_change_pct": 14.1
  }
  ```
- `GET /api/dashboard/chart?timeframe=weekly`: Timeframe breakdown (`weekly`, `monthly`, `yearly`).

### 2. Events Management
- `GET /api/events`: List all events. Supports query filters: `?category=Music&status=Active&search=Gala`.
- `GET /api/events/{id}`: Detailed event payload including:
  - Seat tiers (`VIP`, `Gold`, `Early Bird`)
  - Packages & Addons
  - Official Merchandise items with pricing and stock levels
  - Terms and Conditions
- `POST /api/events`: Create a new event.
- `PUT /api/events/{id}`: Update existing event details.
- `DELETE /api/events/{id}`: Soft/Hard delete an event.

### 3. Bookings & Vouchers
- `GET /api/bookings`: Retrieve paginated booking list.
  - Query parameters: `status` (`All`, `Confirmed`, `Pending`, `Cancelled`), `search`, `page`, `page_size`.
- `GET /api/bookings/{id}`: Booking details.
- `GET /api/bookings/{id}/voucher`: Generates complete E-Voucher payload (Ticket code, Barcode data, QR token, Seat assignment, Venue gate, Terms).
- `POST /api/bookings`: Book tickets for an event.
- `PATCH /api/bookings/{id}/status`: Update status (e.g. `Cancelled` or `Confirmed`).

### 4. Invoices & Billing
- `GET /api/invoices`: Returns the master billing ledger.
- `GET /api/invoices/{invoice_number}`: Retrieves complete line items, tax breakdown, subtotal, and customer info for the paper invoice preview.
- `POST /api/invoices`: Issue a new invoice.
- `PATCH /api/invoices/{invoice_number}/status`: Toggle status (`Paid`, `Unpaid`, `Overdue`).
- `POST /api/invoices/{invoice_number}/send`: Dispatches mock invoice notification email to client.

### 5. Inbox & Messages
- `GET /api/messages`: List inbox threads. Filters: `?folder=inbox|starred|sent|drafts|trash` and `?label=VIP|Urgent|Inquiry`.
- `GET /api/messages/{id}`: Retrieve message conversation thread.
- `PATCH /api/messages/{id}/star`: Toggle starred state.
- `POST /api/messages/{id}/reply`: Send response to a thread.
- `DELETE /api/messages/{id}`: Move to trash or permanently remove.

### 6. Calendar & Schedule
- `GET /api/calendar/agendas`: Retrieve scheduled agenda items. Supports `?day=23` or `?date=2029-02-23`.
- `POST /api/calendar/agendas`: Schedule a new stage session or agenda event.
- `DELETE /api/calendar/agendas/{id}`: Remove an agenda item.

### 7. Financials & Ledger
- `GET /api/financials/summary`: Income, operational expenses, net profit, and pending payouts.
- `GET /api/financials/transactions`: Full accounting transactions ledger with category tags and payment methods.

### 8. Gallery Albums
- `GET /api/gallery`: List all photo albums with photo counts, cover thumbnails, and categories.
- `POST /api/gallery`: Create a new photo album.

### 9. Customer Reviews
- `GET /api/reviews`: List reviews with star rating breakdown. Supports `?rating=5`.
- `POST /api/reviews/{id}/respond`: Post organizer reply to a customer review.

---

## 🗄️ Database Schema & Models

### Core Entities & Relationships
1. **`User`**: Admin and organizer accounts (`id`, `name`, `email`, `role`, `avatar`).
2. **`Event`**: Main event entity (`id`, `title`, `category`, `venue`, `date`, `start_time`, `status`, `banner_url`, `description`).
   - `has_many`: `EventSeatTier`, `EventPackage`, `EventMerchandise`, `AgendaItem`, `Booking`.
3. **`EventSeatTier`**: Tiered seating configurations (`name`, `price`, `capacity`, `available_seats`).
4. **`EventPackage`**: VIP and bundle packages (`title`, `price`, `perks`).
5. **`EventMerchandise`**: Official apparel and merchandise (`item_name`, `price`, `stock_qty`, `image_url`).
6. **`Booking`**: Customer reservations (`invoice_id`, `customer_name`, `customer_email`, `status`, `total_price`, `seat_tier`).
7. **`Invoice` & `InvoiceItem`**: Accounting invoices with itemized ticket/merchandise line items, taxes, fees, and dates.
8. **`Message`**: Direct messages and support tickets with star states, tags, and threads.
9. **`AgendaItem`**: Schedule items linked to dates, venues, and speakers.
10. **`FinancialTransaction`**: Audit log of credits and debits.
11. **`FeedbackReview`**: Star ratings (1-5) and customer feedback comments.
12. **`GalleryAlbum`**: Albums containing event photography portfolios.

---

## ❓ Troubleshooting & FAQs

### Error: `[WinError 10013] An attempt was made to access a socket in a way forbidden by its access permissions`
- **Cause**: Port `8000` is already in use by a background process or reserved by Windows NAT/Hyper-V.
- **Solution**: Run on an alternate port:
  ```powershell
  python -m uvicorn main:app --host 127.0.0.1 --port 8001 --reload
  ```
  *(Remember to update the API base URL in `frontend-angular/src/app/services/dashboard-data.service.ts` if changing ports).*

### SQLite Database Locked
- Ensure only one instance of the backend is writing to `ventixe.db`.
