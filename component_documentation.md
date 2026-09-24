# Ventixe Event Management Dashboard — Component Documentation

Comprehensive component specification and design system reference for the **Ventixe Event Management Dashboard** built with **Angular 19 (Standalone Components)**.

---

## 📋 Table of Contents
1. [Design Tokens & Theme System](#1-design-tokens--theme-system)
2. [Component Hierarchy & Overview](#2-component-hierarchy--overview)
3. [Component Specifications](#3-component-specifications)
   - [3.1 AppShellComponent (Sidebar & Top Navigation)](#31-appshellcomponent-sidebar--top-navigation)
   - [3.2 DashboardOverviewComponent](#32-dashboardoverviewcomponent)
   - [3.3 BookingsListComponent](#33-bookingslistcomponent)
   - [3.4 InvoicesMasterDetailComponent](#34-invoicesmasterdetailcomponent)
   - [3.5 InboxMessengerComponent](#35-inboxmessengercomponent)
   - [3.6 CalendarAgendaDrawerComponent](#36-calendaragendadrawercomponent)
   - [3.7 EventsCatalogComponent & EventDetailComponent](#37-eventscatalogcomponent--eventdetailcomponent)
   - [3.8 FinancialsLedgerComponent](#38-financialsledgercomponent)
   - [3.9 GalleryLightboxComponent](#39-gallerylightboxcomponent)
   - [3.10 FeedbackReviewsComponent](#310-feedbackreviewscomponent)
   - [3.11 EVoucherTicketComponent](#311-evoucherticketcomponent)
   - [3.12 Shared UI Atoms & Modals](#312-shared-ui-atoms--modals)
4. [Accessibility (a11y) & Interactive Standards](#4-accessibility-a11y--interactive-standards)
5. [State Management & Data Flow Architecture](#5-state-management--data-flow-architecture)

---

## 1. Design Tokens & Theme System

The design system implements the exact tokens extracted from the 13-page Figma export (`images.pdf`).

### Color Palette
```css
:root {
  /* Brand Primary */
  --color-primary: #F02D8B;              /* Vibrant Magenta Brand Pink */
  --color-primary-hover: #D82279;        /* Hover State */
  --color-primary-light: #FDF2F7;        /* 8% Opacity Tint for Selected Nav / Badges */

  /* Secondary Accents */
  --color-secondary: #8B5CF6;            /* Electric Violet / Accent */
  --color-secondary-light: #F5F3FF;      /* Light Violet Background */

  /* Neutral Surface & Backgrounds */
  --color-bg-main: #F8F9FD;              /* Application Canvas Background */
  --color-card-bg: #FFFFFF;              /* Content Cards & Modals */
  --color-border: #EDF0F7;               /* Subtle Outlines & Table Dividers */

  /* Typography Colors */
  --color-text-main: #0F172A;            /* Slate-900 (High Contrast Headings & Body) */
  --color-text-muted: #64748B;           /* Slate-500 (Captions, Subtitles, Meta) */
  --color-text-placeholder: #94A3B8;     /* Slate-400 (Inputs & Inactive Icons) */

  /* Semantic Status Tokens */
  --color-success: #059669;              /* Emerald-600 (Confirmed / Paid / Active) */
  --color-success-bg: #ECFDF5;
  --color-warning: #D97706;              /* Amber-600 (Pending / Unpaid) */
  --color-warning-bg: #FFFBEB;
  --color-danger: #DC2626;               /* Rose-600 (Cancelled / Overdue / Delete) */
  --color-danger-bg: #FEF2F2;
}
```

### Typography Scale
- **Font Family**: `'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`
- **Page Titles (`H1`)**: `24px` / Weight: `800` / Line Height: `1.2`
- **Section Headers (`H2`)**: `18px` / Weight: `700` / Line Height: `1.3`
- **Card Titles (`H3`)**: `15px` / Weight: `700` / Line Height: `1.4`
- **Body Regular**: `13px` / Weight: `400` / Line Height: `1.5`
- **Body Semibold**: `13px` / Weight: `600` / Line Height: `1.5`
- **Badges & Captions**: `11px` / Weight: `700` / Text Transform: `uppercase`

### Elevation & Border Radii
- **Card Border Radius**: `16px` (Outer containers), `12px` (Internal sub-cards/inputs), `8px` (Buttons & Badges), `9999px` (Pills).
- **Subtle Elevation**: `box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.05), 0 1px 2px -1px rgba(0, 0, 0, 0.05);`
- **Overlay Elevation**: `box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);`

---

## 2. Component Hierarchy & Overview

```plaintext
<AppComponent>
├── <SidebarNav>              (Brand logo, navigation links, upgrade promo banner)
├── <HeaderBar>               (Global search, + Create Event action, notifications bell, user avatar)
└── <MainContentView>         (Conditional view rendering based on currentView signal)
    ├── [currentView == 'dashboard']     -> <DashboardOverview>
    ├── [currentView == 'bookings']      -> <BookingsList>
    ├── [currentView == 'invoices']      -> <InvoicesMasterDetail>
    ├── [currentView == 'inbox']         -> <InboxMessenger>
    ├── [currentView == 'calendar']      -> <CalendarAgendaDrawer>
    ├── [currentView == 'events']        -> <EventsCatalog>
    ├── [currentView == 'event-detail']  -> <EventDetailView>
    ├── [currentView == 'financials']    -> <FinancialsLedger>
    ├── [currentView == 'gallery']       -> <GalleryLightbox>
    ├── [currentView == 'feedback']      -> <FeedbackReviews>
    └── [currentView == 'voucher']       -> <EVoucherTicket>
```

---

## 3. Component Specifications

### 3.1 AppShellComponent (Sidebar & Top Navigation)

#### Purpose & Scope
Provides continuous application framing, quick view switching, global contextual search, quick creation triggers, and notification center access across all 11 screens.

#### Inputs & Bound Properties
- `currentView: NavView` — Active view identifier (`'dashboard' | 'bookings' | 'invoices' | 'inbox' | 'calendar' | 'events' | 'financials' | 'gallery' | 'feedback' | 'voucher' | 'event-detail'`).
- `globalSearch: string` — Two-way bound string for cross-view querying.
- `showNotifications: boolean` — Toggles the header notifications popover.
- `cartCount: number` — Tracks merchandise items added from the Event Detail page.

#### Interactive Events & Handlers
- `setView(view: NavView | string)`: Changes view, resets scroll position smoothly to top.
- `toggleNotifications()`: Opens/closes notification dropdown.
- `openCreateEventModal()`: Opens the event creation modal.

---

### 3.2 DashboardOverviewComponent

#### Purpose & Scope
Corresponds to Figma Page 1 ("Overview / Analytics"). Summarizes total revenue, sales velocity, recent bookings, and upcoming event tickets.

#### Visual Elements & Interactivity
- **Metric Cards (4)**:
  - *Total Revenue*: `$128,450.00` (+12.5% vs last month).
  - *Total Bookings*: `1,420` (+8.2% vs last month).
  - *Active Events*: `24` events live.
  - *Total Customers*: `3,890` (+14.1% vs last month).
- **Timeframe Selector**: Toggles between `Weekly`, `Monthly`, and `Yearly` calculations.
- **Upcoming Events List**:
  - Interactive event rows displaying thumbnail, date pill, venue, and sold percentage progress bar.
  - Clicking any card navigates to `event-detail` for that specific event.
- **Recent Bookings Table**: Displays customer name, event title, amount, status badge, and an action button to jump directly to the customer's E-Voucher.

---

### 3.3 BookingsListComponent

#### Purpose & Scope
Corresponds to Figma Page 2 ("Bookings Management"). Full-featured booking ledger with real-time status filtering, text search, category filtering, and voucher retrieval.

#### State & Filters
- `bookingsTab: string` — `'All' | 'Confirmed' | 'Pending' | 'Cancelled'`.
- `bookingsSearch: string` — Real-time query matching customer name, invoice ID, or event title.
- `bookingsCategory: string` — Filter dropdown (`'All Category' | 'Music' | 'Technology' | 'Cultural'`).
- `bookingsCurrentPage: number` — Pagination state.

#### Interactive Handlers
- `openVoucher(bookingId: number)`: Sets selected booking and navigates to the printable voucher view.
- `toggleBookingStatus(booking: BookingItem)`: Cancels or re-confirms a reservation.
- Tab click triggers dynamic filtered list recalculation (`getFilteredBookings()`).

---

### 3.4 InvoicesMasterDetailComponent

#### Purpose & Scope
Corresponds to Figma Page 3 ("Billing & Invoices"). Implements a split master-detail view where selecting any invoice on the left ledger renders the complete, printable paper invoice on the right.

#### Left Panel (Ledger Table)
- Search filter by invoice code (`INV10012`) or customer name.
- Status badges: `Paid` (Emerald), `Unpaid` (Amber), `Overdue` (Red).
- Row click handler: `selectInvoice(num: string)` updates the right-hand paper sheet.

#### Right Panel (Rendered Paper Invoice)
- Realistic invoice layout with company branding, invoice number, issue date, and due date.
- Bill From (`Event Management Co.`) and Bill To (`Customer Name`).
- Itemized ticket breakdown table with Ticket Category, Unit Price, Qty, and Subtotal.
- Tax (10%), Processing Fee ($5), and Final Balance Due.
- **Action Buttons**:
  - `Send to Customer`: Triggers a toast notification simulating email dispatch.
  - `Hold / Release`: Toggles invoice status between Overdue and Unpaid.
  - `Download PDF`: Triggers PDF download feedback.

---

### 3.5 InboxMessengerComponent

#### Purpose & Scope
Corresponds to Figma Page 4 ("Inbox / Communication"). Enables organizers to handle customer inquiries, ticket support, partner communications, and draft replies across multiple dedicated folders.

#### Features & Interactivity
- **Folder Navigation**: Tabs for `Inbox`, `Starred`, `Sent`, `Drafts`, and `Trash` with dynamic unread and item counters.
- **Compose Modal (`showComposeModal`)**:
  - "+ Compose Message" action button launches modal with inputs for Recipient (`composeTo`), Subject (`composeSubject`), Category Tag (`composeLabel`), and Body (`composeBody`).
  - Dispatches message with `folder: 'sent'`, auto-selects newly created message, and shows toast notification.
- **Label Filters**: Filter by `Customer` (blue), `Sponsor` (purple), and `Partner` (green), with a reset action.
- **Star Toggle**: `toggleStar(message, $event)` toggles star flag on individual list items or within the reading pane header without triggering row click.
- **Thread Viewer**: Displays full customer inquiry text, sender metadata, email, and timestamp.
- **Thread Conversation History (`replies[]`)**: Renders all previous replies in chronological order with sender name, timestamp, and message bubble.
- **Inline Reply Composer**: Interactive textarea with `sendReply()` that appends the response to the current thread AND automatically registers an entry in the `sent` folder.
- **Forward Action (`forwardMessage`)**: Pre-fills the Compose Modal with `Fwd: ${subject}` and formatted quote text.
- **Trash & Restore Lifecycle**:
  - Clicking delete moves messages from `inbox`/`sent`/`drafts` to `folder: 'trash'`.
  - In `trash`, messages can be restored back to `inbox` with `restoreMessage(id)` or deleted permanently.

---

### 3.6 CalendarAgendaDrawerComponent

#### Purpose & Scope
Corresponds to Figma Page 5 ("Calendar & Agendas"). Interactive monthly calendar grid linked with a collapsible slide-out agenda schedule drawer and a full Schedule Timeline view.

#### Interactivity & Schedule Controls
- **Month Navigation Controls**: Previous (`◀`) and Next (`▶`) controls with active month indicator (`May 2029`).
- **View Mode Switcher**:
  - `Month Grid`: 7-column calendar grid for 31 days with dynamic agenda badges rendered inside each day cell (`getAgendasForDay(d)`).
  - `Schedule Timeline`: Master chronological list of all sessions and conference tracks across the month.
- **Dynamic Day Badging**: Day cells display colored pill badges corresponding to event categories (Event = Magenta, Meeting = Blue, Setup = Purple, Finance = Green). Newly created agendas immediately appear in their target day cell.
- **Date Selection**: `selectCalendarDay(day: number)` highlights the active day and retrieves or creates schedule items.
- **Slide-out Agenda Details Drawer**:
  - Event cover imagery, venue location, and timestamp.
  - **Timeline Session Breakdown (`slots[]`)**: Displays structured time blocks (e.g. `09:00 AM - 10:30 AM`), session title, stage/hall (e.g. `Main Stage`), speaker name, and status pills (`Completed`, `In Progress`, `Upcoming`).
  - PIC Lead Coordinator profile with direct phone and email contact lines.
  - Important operational notes list.
  - Action buttons to add sessions or delete agenda items (`deleteAgenda(id)`).
  - Drawer collapse/expand toggle button for flexible workspace viewing.
- **Schedule Modal (`showNewAgendaModal`)**: Select day in month, session title, time, and category to schedule new programming.

---

### 3.7 EventsCatalogComponent & EventDetailComponent

#### Purpose & Scope
Corresponds to Figma Pages 6 & 7 ("Events Catalog" & "Event Details").

#### Events Catalog
- **View Modes**: Toggle between **Grid View** (cards with hero images) and **List View** (compact rows).
- **Status Tabs**: `Active`, `Draft`, `Past`.
- Event cards with progress bars indicating ticket sales velocity.

#### Event Detail View
- **Hero Banner**: High-resolution photography, event date badge, location tag, and organizer bio.
- **Ticket Tiers**: Cards for `VIP Pass ($150)`, `Gold Seating ($85)`, and `Early Bird ($45)`.
- **Official Merchandise**: Apparel cards with pricing, stock status, and an interactive **Add to Cart** button that updates the global cart badge.
- **Terms & Conditions Accordion**: Clickable header to collapse or expand policy details.

---

### 3.8 FinancialsLedgerComponent

#### Purpose & Scope
Corresponds to Figma Page 8 ("Financial Analytics"). Comprehensive financial ledger, real-time KPI metrics, categorized transaction ledger, and transaction recording system.

#### Key Features & Interactivity
- **KPI Summary Cards**:
  - `Total Balance`: Calculated dynamically via `getTotalBalance()` reflecting current operating liquidity with percentage trends.
  - `Total Income`: Real-time sum of all income transactions via `getTotalIncome()` (ticket sales, brand sponsorships, merchandise).
  - `Total Expenses`: Real-time sum of all outgoing transactions via `getTotalExpense()` (artist booking, venue leasing, security, marketing).
  - `Operating Margin`: Net operating profit margin percentage.
- **Filter Tabs**:
  - `All Transactions`: Full chronological transaction records.
  - `Income (+)`: Filters for inflow revenue.
  - `Expenses (-)`: Filters for operational outflow.
- **Category Filter Dropdown**:
  - Dynamically filters ledger entries by `Ticket Sales`, `Sponsorship`, `Vendor Payout`, `Operations`, `Merchandise`, and `Marketing`.
- **Search Filter**:
  - Real-time instant query matching transaction description, internal note, payment channel, or transaction reference ID.
- **Record Transaction Modal (`showAddTransactionModal`)**:
  - Full modal dialog with input validation: Event/Description, Type (Income / Expense), Amount ($), Category, Payment Channel (Stripe, Square, Corporate Visa, Wire Transfer, Direct Deposit), and internal audit memo.
  - On record submission, assigns a unique transaction ID (`TRX-XXXX`), updates global balance, and injects the transaction into the reactive ledger.
- **CSV Data Export (`exportFinancialsCsv`)**:
  - Generates and triggers automatic browser download of formatted `ventixe_financial_report_2029.csv` with complete audit trails.

---

### 3.9 GalleryLightboxComponent

#### Purpose & Scope
Corresponds to Figma Page 9 ("Event Photo Gallery"). Categorized photo collections with full-screen lightbox preview.

#### Interactivity
- Category filter pills (`All`, `Music`, `Conferences`, `Parties`).
- Album cards with photo count badges.
- **Full-Screen Lightbox**:
  - Clicking any album opens high-resolution preview modal.
  - Thumbnail navigation strip to jump between photos.
  - Prev, Next, and Close controls with keyboard ESC support.

---

### 3.10 FeedbackReviewsComponent

#### Purpose & Scope
Corresponds to Figma Page 10 ("Customer Feedback"). Star rating distribution and attendee reviews.

#### Interactivity
- Star breakdown bars (5-star down to 1-star percentage fill).
- Star rating filter (click `5 Stars` to isolate top ratings).
- Customer review cards with verified attendee badges.
- `Respond to Review`: Interactive modal to compose and publish an organizer response.

---

### 3.11 EVoucherTicketComponent

#### Purpose & Scope
Corresponds to Figma Page 11 ("E-Voucher Pass"). Realistic boarding pass / event ticket layout.

#### Interactivity
- Displayed data: Event Title, Attendee Name, Seat Tier, Gate/Entrance, Date & Time, QR Code graphic, and Barcode scan line.
- `Print E-Voucher`: Triggers native `window.print()` formatted for print media.
- `Download Pass`: Simulates ticket pass download.
- `Back to Bookings`: Seamless navigation back to the bookings ledger.

---

### 3.12 Shared UI Atoms & Modals

- **Toast Notification**: Auto-dismissing status banner (`showToast(msg)`).
- **Create Event Modal**: Form fields for Title, Category, Date, Price, and Venue.
- **Add Invoice Modal**: Form fields for Invoice ID, Customer, and Total Amount.
- **Add Agenda Modal**: Form fields for Session Title, Category, and Time.
- **Create Album Modal**: Form fields for Album Name and Category.

---

## 4. Accessibility (a11y) & Interactive Standards

- **Semantic HTML5**: Native `<header>`, `<nav>`, `<main>`, `<section>`, `<table>`, and `<button>` elements.
- **Buttons vs Links**: All interactive triggers are native `<button>` elements with `cursor: pointer` and clear focus rings.
- **Color Contrast**: Main body text (`#0F172A`) against background (`#F8F9FD`) exceeds WCAG AAA (contrast ratio > 12:1). Primary brand magenta (`#F02D8B`) meets WCAG AA standards.
- **Keyboard Navigation**: Modals can be closed with the Escape key or interactive close buttons.

---

## 5. State Management & Data Flow Architecture

```plaintext
[Backend API: FastAPI / SQLite]
           │ HTTP (GET/POST/PATCH)
           ▼
[DashboardDataService (Angular Service)]
  ├── In-Memory Fallback Cache
  └── Asynchronous Promises / Observables
           │
           ▼
[AppComponent (Root Controller)]
  ├── State: currentView, events, bookings, invoices, messages, agendas, financials
  ├── Computed Filters: getFilteredBookings(), getFilteredInvoices(), getFilteredTransactions(), etc.
  └── Action Handlers: setView(), showToast(), addTransaction(), toggleMobileMenu(), etc.
           │ Two-Way Data Binding ([(ngModel)]) & Event Bindings ((click))
           ▼
[HTML Template Views & Modals]
```

---

## 6. Responsive Design & Mobile Phone Compatibility

The dashboard has been engineered for seamless compatibility from wide desktop displays down to small mobile phone viewports:

### Breakpoints & Adaptive Layouts
- **Desktop (`>= 1200px`)**:
  - Full fixed-width 250px left navigation sidebar.
  - Multi-column grids: 4-column card matrices, 3-column overview grids, 3-panel split messenger layout (`240px 360px 1fr`).
- **Small Laptops / Large Tablets (`1024px – 1200px`)**:
  - Grid columns compress automatically (`.stats-grid-4` adapts to 2-columns, `.four-col-grid` adapts to 3-columns).
  - Messenger layout adapts to `210px 300px 1fr`.
- **Tablets (`768px – 1024px`)**:
  - Navigation sidebar converts to a slide-over off-canvas drawer (`transform: translateX(-100%)`).
  - Hamburger menu trigger button (`☰`) dynamically reveals in the top navigation header.
  - Full backdrop overlay (`.mobile-backdrop`) with tap-to-dismiss behavior.
  - 2-column layouts (`.dashboard-layout`, `.invoices-layout`, `.calendar-layout`, `.event-detail-layout`) collapse into clean single vertical column flows.
  - Inbox collapses from 3 horizontal columns into stacked functional cards.
- **Mobile Phones (`< 768px`)**:
  - Compact 64px header with touch-optimized action targets.
  - `.stats-grid-4`, `.three-col-grid`, and `.four-col-grid` gracefully stack to 1 column.
  - Modal sheets scale to 95vw with optimized padding.
  - Filter tabs feature horizontal touch panning (`-webkit-overflow-scrolling: touch`).
  - Complex data tables wrapped in `.data-table-wrapper` with smooth horizontal scrolling to prevent content clipping.
- **Extra Small Phones (`< 480px`)**:
  - Global search collapses into an icon to preserve space for title and profile controls.
  - Compact typography and padding for high density viewports.

