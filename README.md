# Ventixe Event Management Dashboard

A full-stack, enterprise-grade Event Management Admin Dashboard crafted with **FastAPI (Python 3.13)** on the backend and **Angular 19 (Standalone Components)** on the frontend, accurately mirroring the Figma design system (`images.pdf`).

---

## 📚 Documentation Index

- 📘 [**Backend Documentation (`backend/README.md`)**](file:///d:/proj/EventManagementDashboard/backend/README.md)
  - Python environment setup, SQLAlchemy ORM models, Pydantic schemas, database seeding (`seeds.py`), and complete REST API endpoint specifications with payload examples.
- 🎨 [**Frontend Documentation (`frontend-angular/README.md`)**](file:///d:/proj/EventManagementDashboard/frontend-angular/README.md)
  - Angular 19 architecture, design tokens, Plus Jakarta Sans typography, directory structure, dev server instructions, and detailed view breakdown.
- 🧩 [**Component Documentation (`component_documentation.md`)**](file:///d:/proj/EventManagementDashboard/component_documentation.md)
  - Comprehensive reference for all UI components, state properties, event handlers, interactive click behaviors, modal controls, and accessibility (WCAG AA/AAA) standards.

---

## ⚡ Quick Start: Running the Full Stack

### 1. Start the FastAPI Backend
Open a terminal:
```powershell
cd D:\proj\EventManagementDashboard\backend
python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```
- **API URL**: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **Interactive Swagger Docs**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc Documentation**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### 2. Start the Angular 19 Frontend
Open a second terminal:
```powershell
cd D:\proj\EventManagementDashboard\frontend-angular
npm start
```
- **Web Application URL**: [http://localhost:4200](http://localhost:4200)
- Hot Module Reloading (HMR) and live compilation are enabled.

---

## 🖥️ Overview of Dashboard Views

| # | Screen / View | Highlights & Interactivity |
| :-: | :--- | :--- |
| **1** | **Dashboard Overview** | Revenue analytics, Weekly/Monthly/Yearly toggles, quick creation shortcuts, and recent activity. |
| **2** | **Bookings Management** | Status tabs (*All*, *Confirmed*, *Pending*, *Cancelled*), keyword search, category filter, and voucher launch. |
| **3** | **Invoices & Billing** | Split master-detail view; select any invoice to load its printable sheet; actions to send email, hold/release, download PDF, or add new invoice. |
| **4** | **Inbox & Messaging** | Star messages, filter by folder/label, view full email conversations, reply inline, and delete threads. |
| **5** | **Calendar & Agendas** | Interactive date grid and collapsible slide-out agenda schedule drawer with speaker breakdown. |
| **6** | **Events Catalog** | Grid vs List view toggle, status filters (*Active*, *Draft*, *Past*), ticket sales progress bars. |
| **7** | **Event Details** | Hero imagery, ticket tier breakdown (VIP, Gold, Early Bird), merchandise store with interactive cart counter, and expandable terms accordion. |
| **8** | **Financials & Ledger** | Real-time balance calculations, Income/Expense filter tabs, category dropdown, search, "+ Record Transaction" modal, and dynamic CSV export. |
| **9** | **Media Gallery** | Photo albums with interactive full-screen Lightbox and thumbnail navigation strip. |
| **10** | **Customer Feedback** | Star rating distribution (1★ to 5★), filter by rating, and organizer response modal. |
| **11** | **Printable E-Voucher** | Authentic event pass with QR code, barcode, seat tier, date, and native browser print trigger (`window.print()`). |

---

## 🏗️ Project Structure

```plaintext
EventManagementDashboard/
├── backend/
│   ├── database.py                 # SQLAlchemy engine and session configuration
│   ├── models.py                   # 11 Database entities with relationships
│   ├── schemas.py                  # Pydantic v2 validation models
│   ├── seeds.py                    # Mock data seeder matching Figma specifications
│   ├── main.py                     # FastAPI app, CORS middleware, REST endpoints
│   ├── ventixe.db                  # SQLite database
│   └── README.md                   # Comprehensive backend documentation
├── frontend-angular/
│   ├── src/
│   │   ├── app/
│   │   │   ├── models/             # Domain TypeScript interfaces
│   │   │   ├── services/           # HTTP API client with resilient fallbacks
│   │   │   ├── app.component.ts    # Main state controller and action handlers
│   │   │   ├── app.component.html  # Templates for all 11 views and modals
│   │   │   └── app.component.css   # Component styling and micro-animations
│   │   ├── index.html              # Typography fonts and meta tags
│   │   └── styles.css              # Global design tokens and utilities
│   ├── package.json                # Angular 19 dependencies and scripts
│   └── README.md                   # Comprehensive frontend documentation
├── component_documentation.md      # Full component specifications & a11y standards
└── README.md                       # Project landing overview
```
