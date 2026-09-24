# Ventixe Event Management Dashboard (Angular 19 Frontend)

A high-fidelity, production-grade Event Management Admin Dashboard crafted with **Angular 19 (Standalone Components)**, TypeScript, and Vanilla CSS design tokens. Strictly modeled after the 13-page Figma design specifications (`images.pdf`).

---

## 📋 Table of Contents
- [Design System & Aesthetics](#design-system--aesthetics)
- [Architecture & Tech Stack](#architecture--tech-stack)
- [Directory Structure](#directory-structure)
- [Getting Started & Installation](#getting-started--installation)
- [Running Locally & Dev Server](#running-locally--dev-server)
- [Production Build](#production-build)
- [Component Architecture & Views](#component-architecture--views)
  - [1. App Shell (Sidebar & Header)](#1-app-shell-sidebar--header)
  - [2. Dashboard Overview](#2-dashboard-overview)
  - [3. Bookings Management](#3-bookings-management)
  - [4. Invoices & Billing (Split View)](#4-invoices--billing-split-view)
  - [5. Inbox & Messaging Center](#5-inbox--messaging-center)
  - [6. Calendar & Agenda Drawer](#6-calendar--agenda-drawer)
  - [7. Events Catalog & Event Details](#7-events-catalog--event-details)
  - [8. Financials & Accounting](#8-financials--accounting)
  - [9. Media Gallery & Fullscreen Lightbox](#9-media-gallery--fullscreen-lightbox)
  - [10. Customer Feedback & Reviews](#10-customer-feedback--reviews)
  - [11. Printable E-Voucher Pass](#11-printable-e-voucher-pass)
- [State Management & Data Services](#state-management--data-services)
- [Troubleshooting & FAQs](#troubleshooting--faqs)

---

## 🎨 Design System & Aesthetics

The application adheres to the Figma design tokens defined in [`src/styles.css`](file:///d:/proj/EventManagementDashboard/frontend-angular/src/styles.css):

### Color Palette
- **Primary Brand**: `#F02D8B` (Vibrant Magenta / Pink)
- **Primary Hover**: `#D82279`
- **Primary Subdued / Light**: `#FDF2F7`
- **Secondary Accent**: `#8B5CF6` (Electric Violet)
- **Background Main**: `#F8F9FD` (Soft off-white / light slate)
- **Card & Surface Background**: `#FFFFFF`
- **Borders & Dividers**: `#EDF0F7`
- **Text Primary**: `#0F172A` (Deep Slate)
- **Text Secondary / Muted**: `#64748B`

### Status Badges
- **Confirmed / Paid / Active**: Soft Emerald (`background: #ECFDF5; color: #059669;`)
- **Pending / Unpaid**: Warm Amber (`background: #FFFBEB; color: #D97706;`)
- **Cancelled / Overdue**: Soft Coral (`background: #FEF2F2; color: #DC2626;`)

### Typography & Elevation
- **Font Family**: `'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif`
- **Shadows**:
  - Cards: `0 1px 3px 0 rgba(0, 0, 0, 0.05), 0 1px 2px -1px rgba(0, 0, 0, 0.05)`
  - Modals & Drawers: `0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1)`

---

## 🛠️ Architecture & Tech Stack

- **Angular Version**: 19.2.x (Modern Standalone Components without NgModules)
- **Language**: TypeScript 5.7+
- **Reactivity**: RxJS 7.8, Angular Signals, and Two-Way Template Bindings (`[(ngModel)]`)
- **Icons**: [Lucide Angular](https://lucide.dev/) + Semantic Unicode Icons
- **HTTP Client**: Native `fetch` with seamless fallback mock data in [`DashboardDataService`](file:///d:/proj/EventManagementDashboard/frontend-angular/src/app/services/dashboard-data.service.ts)

---

## 📂 Directory Structure

```plaintext
frontend-angular/
├── src/
│   ├── app/
│   │   ├── models/
│   │   │   └── dashboard.models.ts       # TypeScript interfaces for all 11 domains
│   │   ├── services/
│   │   │   └── dashboard-data.service.ts # API client with resilient fallback dataset
│   │   ├── app.component.ts              # Root controller with state & action handlers
│   │   ├── app.component.html            # Complete template for all 11 Figma views
│   │   ├── app.component.css             # Component-scoped animations and transitions
│   │   └── app.config.ts                 # Angular application providers configuration
│   ├── index.html                        # Google Fonts (Plus Jakarta Sans) & title
│   ├── main.ts                           # Angular standalone bootstrapper
│   └── styles.css                        # Global CSS variables, reset, and utilities
├── angular.json                          # Angular workspace build configurations
├── package.json                          # Scripts and dependencies
└── tsconfig.json                         # Strict TypeScript configuration
```

---

## 🚀 Getting Started & Installation

### 1. Prerequisites
- **Node.js**: 18.x, 20.x, or 22.x
- **npm**: 9.x or higher

### 2. Install Node Dependencies
From the `frontend-angular` directory, run:
```powershell
cd D:\proj\EventManagementDashboard\frontend-angular
npm install
```

---

## ⚡ Running Locally & Dev Server

Start the Angular development server with Hot Module Reloading (HMR):
```powershell
npm start
```
*Or using the Angular CLI directly:*
```powershell
npx ng serve --port 4200
```

- Navigate to: **`http://localhost:4200/`**
- The application will automatically recompile and reload whenever files are modified.

---

## 📦 Production Build

To generate optimized production bundle artifacts:
```powershell
npm run build
```
The compiled output is saved to `dist/frontend-angular/browser/`.

---

## 🖥️ Component Architecture & Views

Every component in the application is fully interactive and clickable:

### 1. App Shell (Sidebar & Header)
- **Sidebar**:
  - Brand header with the Ventixe logo.
  - 8 Main Nav Buttons: **Dashboard**, **Bookings**, **Invoices**, **Inbox**, **Calendar**, **Events**, **Financials**, **Gallery**, **Feedback**.
  - Dynamic active route styling (`--color-primary-light` background and bold pink font).
  - "Get Pro $49" upgrade banner with interactive toast notification.
- **Top Header**:
  - Real-time Global Search bar (`[(ngModel)]="globalSearch"`).
  - Quick "+ Create Event" action button that opens the Creation Modal.
  - Notification Bell icon with active badge counter; toggles the Notification Center popover.
  - Organizer avatar and profile summary.

### 2. Dashboard Overview
- 4 Stat Metric Cards (Total Revenue, Total Bookings, Active Events, Total Customers) with mini trend sparklines and percentage delta tags.
- Timeframe filter tabs (**Weekly**, **Monthly**, **Yearly**) updating visual metrics.
- Upcoming Event Cards with direct click-through to the Event Details page.
- Recent Bookings summary table with status badges and "Voucher" action button.
- Quick Actions shortcut ribbon to launch common creation workflows.

### 3. Bookings Management
- **Status Filter Tabs**: *All*, *Confirmed*, *Pending*, *Cancelled* with real-time counters.
- **Dynamic Search**: Filters rows instantly by customer name, invoice ID, or event title.
- **Category Filter**: Filter events by category (e.g. *Music*, *Technology*, *Cultural*).
- **Interactive Action Buttons**:
  - `View Voucher`: Launches the printable E-Voucher pass modal.
  - `Cancel Booking`: Toggles booking cancellation status.
- **Pagination**: Interactive page numbers with "Prev" and "Next" controls.

### 4. Invoices & Billing (Split View)
- **Master-Detail Layout**: Left-hand billing records list; Right-hand live rendered printable paper invoice.
- **Row Selection**: Clicking any row in the ledger immediately binds its itemized breakdown, taxes, and customer details into the paper view.
- **Interactive Actions**:
  - `Send to Customer`: Dispatches mock email delivery confirmation toast.
  - `Hold / Release`: Toggles invoice status between *Paid*, *Unpaid*, and *Overdue*.
  - `Download PDF`: Simulates browser PDF receipt download.
  - `+ Add Invoice`: Opens invoice generation modal.

### 5. Inbox & Messaging Center
- **Folder Navigation**: Filter messages by *Inbox*, *Starred*, *Sent*, *Drafts*, and *Trash* with dynamic item counts.
- **Compose Modal**: Dedicated "+ Compose Message" modal with recipient, subject, category tag (Customer, Sponsor, Partner), and body textarea.
- **Sent Folder**: Automatically stores sent messages and replies with full timestamps and sender details.
- **Thread Conversation View**: Selecting any thread displays the full inquiry text and nested replies history (`replies[]`).
- **Inline Reply Composer**: Type replies and click "Send Reply"; immediately appends the response to the conversation thread and archives it in the *Sent* folder.
- **Forward Action**: Pre-fills the compose modal with formatted quotation text.
- **Star Toggle**: Click the star icon on any message to star/unstar it with toast feedback.
- **Trash & Restore**: Delete moves messages to Trash; from Trash, messages can be restored to Inbox or permanently deleted.

### 6. Calendar & Agenda Drawer
- **Interactive Calendar Grid**: 31-day month view for May 2029 with previous (`◀`) and next (`▶`) month navigation.
- **View Modes**: Switch between **Month Grid** and **Schedule Timeline** views.
- **Dynamic Day Badging**: Day cells display colored category badges (Event, Meeting, Setup, Finance, Operations) for any agenda scheduled on that day.
- **Slide-out Agenda Details Drawer**:
  - Event cover photo, location, and date/time.
  - **Structured Session Timeline (`slots[]`)**: Displays time ranges, session title, stage/hall, speaker/lead, and status pills (*Completed*, *In Progress*, *Upcoming*).
  - PIC Lead Coordinator profile with direct phone and email contact details.
  - Important operational notes list.
  - Action buttons to add agenda items or delete sessions.
  - Expand/collapse drawer toggle button.
- **Schedule Modal**: Modal to schedule new conference or stage items on any selected day.

### 7. Events Catalog & Event Details
- **View Switcher**: Toggle between **Grid View** (cards) and **List View** (compact rows).
- **Status Tabs**: Filter by *Active*, *Draft*, or *Past* events.
- **Event Detail Page**:
  - High-resolution hero banner with event metadata (dates, location, organizer).
  - Ticket tier breakdown (**VIP Access**, **Gold Seating**, **Early Bird**).
  - Official Merchandise section with live **Add to Cart** counter.
  - Expandable **Terms & Conditions** accordion.

### 8. Financials & Accounting
- **Real-Time Financial KPI Summary**:
  - `Total Balance`: Reactive liquidity balance reflecting all income minus expenses (`getTotalBalance()`).
  - `Total Income`: Dynamic summation of ticket sales, sponsorships, and merchandise revenue (`getTotalIncome()`).
  - `Total Expenses`: Dynamic summation of artist payouts, venue leases, stage operations, and marketing (`getTotalExpense()`).
  - `Operating Margin`: Calculated operating efficiency percentage (58.6%).
- **Interactive Transaction Tabs**: Filter by *All Transactions*, *Income (+)*, and *Expenses (-)*.
- **Category Filter Dropdown**: Filter transactions by *Ticket Sales*, *Sponsorship*, *Vendor Payout*, *Operations*, *Merchandise*, or *Marketing*.
- **Real-Time Transaction Search**: Instant keyword filtering across event descriptions, audit memos, transaction IDs, and payment methods.
- **"+ Record Transaction" Modal**:
  - Full interactive dialog to log new transactions.
  - Inputs for description, Income/Expense type, amount ($), category, payment channel (Stripe, Square POS, Corporate Visa, Wire Transfer, Direct Deposit), and internal audit notes.
  - Generates unique transaction codes (`TRX-XXXX`), updates the KPI balances immediately, and prepend-inserts into the ledger table.
- **CSV Accounting Report Export**: `exportFinancialsCsv()` dynamically builds and downloads `ventixe_financial_report_2029.csv` directly in the browser.

### 9. Media Gallery & Fullscreen Lightbox
- Category filter pills (*All*, *Music*, *Conferences*, *Festivals*).
- Album cards displaying photo count badges and cover photos.
- Clicking any album launches the **Full-Screen Lightbox** with thumbnail navigation strip and close controls.
- `+ Create Album`: Modal to create photo collections.

### 10. Customer Feedback & Reviews
- Star rating distribution analytics (5★ down to 1★).
- Interactive star filter to view ratings by grade.
- Detailed review cards with customer comments.
- `Respond`: Modal to post official organizer responses.

### 11. Printable E-Voucher Pass
- Designed to replicate physical event tickets with high-fidelity QR code, barcode, gate number, and seat tier.
- Clickable **Print E-Voucher** button (triggers browser `window.print()`).
- **Download Pass** button.

---

## 🔄 State Management & Data Services

[`DashboardDataService`](file:///d:/proj/EventManagementDashboard/frontend-angular/src/app/services/dashboard-data.service.ts) provides a resilient data architecture:
1. **Live API First**: Makes HTTP requests to the FastAPI backend (`http://127.0.0.1:8000/api/...`).
2. **Graceful Fallback**: If the backend is offline or unreachable, it falls back to a realistic local mock dataset matching the Figma prototype.
3. **Reactive UI State**: Managed via Angular two-way binding (`[(ngModel)]`), computed template getters, and event handlers.

---

## 📱 Mobile Responsiveness & Phone Compatibility

The dashboard features complete cross-device responsiveness with dedicated breakpoint optimizations:
- **Mobile Hamburger Drawer (`☰`)**: On devices under 1024px width, the left sidebar automatically transitions into a sliding drawer navigation. Tap the hamburger icon to open, or tap outside on the darkened backdrop (`.mobile-backdrop`) or on any navigation link to close.
- **Adaptive Grid Breakpoints**:
  - `@media (max-width: 1200px)`: Small laptops collapse 4-column metric grids to 2-columns.
  - `@media (max-width: 1024px)`: Tablets collapse dual-column split views (Dashboard, Invoices, Calendar drawer, Event Details) into single stacked columns.
  - `@media (max-width: 768px)`: Mobile phones collapse metrics and card lists to full-width stacked views. Modals expand to `95vw` with touch-friendly spacing.
  - `@media (max-width: 480px)`: Compact phones prioritize view titles and actions with optimized search and profile controls.
- **Horizontal Scrolling Protection**: All data tables (Bookings, Invoices, Financial Ledger) and filter tab bars are wrapped with smooth horizontal touch scrolling (`-webkit-overflow-scrolling: touch`) so tables never break mobile viewport boundaries.

---

## ❓ Troubleshooting & FAQs

### Port 4200 is in use
If another process is using port 4200, specify a different port:
```powershell
npx ng serve --port 4300
```

### Backend connection issues
Ensure the FastAPI backend is running on `http://127.0.0.1:8000`. You can check the backend health by visiting `http://127.0.0.1:8000/docs` in your browser.
