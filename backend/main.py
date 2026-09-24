from typing import List, Optional
from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import desc

try:
    from backend.database import get_db, engine, Base
    from backend.models import (
        User, Event, EventSeatTier, EventPackage, EventMerchandise,
        Booking, Invoice, InvoiceItem, Message, AgendaItem,
        FinancialTransaction, FeedbackReview, ActivityAuditLog, GalleryAlbum
    )
    from backend.schemas import (
        UserSchema, EventListSchema, EventDetailSchema, BookingSchema,
        InvoiceDetailSchema, MessageSchema, MessageReplyRequest,
        AgendaSchema, AgendaCreateSchema, TransactionSchema,
        FeedbackSchema, ActivityLogSchema, GalleryAlbumSchema, ResponseMessage
    )
except ImportError:
    from database import get_db, engine, Base
    from models import (
        User, Event, EventSeatTier, EventPackage, EventMerchandise,
        Booking, Invoice, InvoiceItem, Message, AgendaItem,
        FinancialTransaction, FeedbackReview, ActivityAuditLog, GalleryAlbum
    )
    from schemas import (
        UserSchema, EventListSchema, EventDetailSchema, BookingSchema,
        InvoiceDetailSchema, MessageSchema, MessageReplyRequest,
        AgendaSchema, AgendaCreateSchema, TransactionSchema,
        FeedbackSchema, ActivityLogSchema, GalleryAlbumSchema, ResponseMessage
    )

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Ventixe Event Management API",
    description="Backend API powering the Ventixe Event Management Admin Dashboard",
    version="1.0.0"
)

# Enable CORS for frontend Vite development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------- Current User -----------------
@app.get("/api/v1/users/me", response_model=UserSchema, tags=["Users"])
def get_current_user(db: Session = Depends(get_db)):
    admin = db.query(User).first()
    if not admin:
        raise HTTPException(status_code=404, detail="User not found")
    return admin

# ----------------- Dashboard Overview -----------------
@app.get("/api/v1/dashboard/overview", tags=["Dashboard"])
def get_dashboard_overview(db: Session = Depends(get_db)):
    total_events = db.query(Event).count()
    total_bookings = db.query(Booking).count()
    tickets_sold = sum([e.tickets_sold for e in db.query(Event).all()])

    featured_event = db.query(Event).filter(Event.slug == "echo-beats-festival").first()
    recent_bookings = db.query(Booking).order_by(desc(Booking.booking_date)).limit(5).all()
    recent_activities = db.query(ActivityAuditLog).order_by(desc(ActivityAuditLog.timestamp)).limit(4).all()

    return {
        "kpi": {
            "upcoming_events": 345,  # Display metrics as designed in Figma
            "total_bookings": 1798,
            "tickets_sold": 1250,
        },
        "ticket_sales": {
            "total_tickets": 2780,
            "sold_out_pct": 45,
            "fully_booked_pct": 30,
            "available_pct": 25,
            "sold_out_count": 1251,
            "fully_booked_count": 834,
            "available_count": 695
        },
        "sales_revenue": {
            "total_revenue": 348805,
            "period": "Last 8 Months",
            "highlight_revenue": "$56,320",
            "monthly_data": [
                {"month": "Jan", "revenue": 45000, "profit": 28000},
                {"month": "Feb", "revenue": 38000, "profit": 22000},
                {"month": "Mar", "revenue": 52000, "profit": 35000},
                {"month": "Apr", "revenue": 48000, "profit": 31000},
                {"month": "May", "revenue": 56320, "profit": 37500},
                {"month": "Jun", "revenue": 49000, "profit": 33000},
                {"month": "Jul", "revenue": 53000, "profit": 36000},
                {"month": "Aug", "revenue": 58000, "profit": 39000},
            ]
        },
        "popular_events": [
            {"category": "Music", "percentage": 40, "events_count": 20000},
            {"category": "Sports", "percentage": 35, "events_count": 17500},
            {"category": "Fashion", "percentage": 15, "events_count": 12500},
        ],
        "all_events_preview": [
            {
                "id": e.id,
                "title": e.title,
                "category": e.category,
                "venue": e.venue_name,
                "date": e.start_datetime.strftime("%b %d, %Y"),
                "price": e.min_price,
                "banner_image_url": e.banner_image_url
            } for e in db.query(Event).limit(3).all()
        ],
        "recent_bookings": [
            {
                "invoice_id": b.invoice_id_str,
                "date": b.booking_date.strftime("%Y/%m/%d %I:%M %p"),
                "name": b.customer_name,
                "event": b.event.title if b.event else "Symphony Under the Stars",
                "category": b.event.category if b.event else "Music",
                "qty": b.quantity,
                "amount": b.total_amount,
                "status": b.status
            } for b in recent_bookings
        ],
        "upcoming_event_spotlight": {
            "title": "Rhythm & Beats Music Festival",
            "category": "Music",
            "location": "Sunset Park, Los Angeles, CA",
            "description": "Immerse yourself in electrifying performances by top EDM, pop, and hip-hop artists.",
            "date": "Apr 20, 2029",
            "time": "12:00 PM - 11:00 PM",
            "banner_image": "https://images.unsplash.com/photo-1470225620780-dba8ba36b745?auto=format&fit=crop&w=800&q=80"
        },
        "recent_activities": [
            {
                "id": a.id,
                "actor": a.actor_name,
                "action_type": a.action_type,
                "description": a.description
            } for a in recent_activities
        ]
    }

# ----------------- Events -----------------
@app.get("/api/v1/events", tags=["Events"])
def get_events(
    status: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    search: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(Event)
    if status and status != "All":
        query = query.filter(Event.status == status)
    if category and category != "All" and category != "All Category":
        query = query.filter(Event.category == category)
    if search:
        query = query.filter(Event.title.ilike(f"%{search}%"))

    events = query.all()
    results = []
    for e in events:
        pct = int((e.tickets_sold / e.total_capacity) * 100) if e.total_capacity else 0
        left = max(0, e.total_capacity - e.tickets_sold)
        results.append({
            "id": e.id,
            "title": e.title,
            "slug": e.slug,
            "category": e.category,
            "status": e.status,
            "banner_image_url": e.banner_image_url,
            "start_datetime": e.start_datetime,
            "venue_name": e.venue_name,
            "venue_address": e.venue_address,
            "total_capacity": e.total_capacity,
            "tickets_sold": e.tickets_sold,
            "min_price": e.min_price,
            "percentage_sold": pct,
            "tickets_left": left,
            "about_text": e.about_text
        })
    return {
        "counts": {
            "active": db.query(Event).filter(Event.status == "Active").count(),
            "draft": 22,
            "past": 32,
            "total": len(results)
        },
        "events": results
    }

@app.get("/api/v1/events/{id}", tags=["Events"])
def get_event_detail(id: int, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.id == id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    
    seat_tiers = [
        {
            "id": st.id,
            "name": st.name,
            "tier_type": st.tier_type,
            "price": st.price,
            "capacity": st.capacity,
            "booked_count": st.booked_count,
            "benefits": st.benefits
        } for st in event.seat_tiers
    ]
    packages = [
        {
            "id": p.id,
            "name": p.name,
            "type_label": p.type_label,
            "price": p.price,
            "features": p.features
        } for p in event.packages
    ]
    merchandise = [
        {
            "id": m.id,
            "name": m.name,
            "price": m.price,
            "image_url": m.image_url,
            "stock_quantity": m.stock_quantity
        } for m in event.merchandise
    ]

    return {
        "id": event.id,
        "title": event.title,
        "slug": event.slug,
        "category": event.category,
        "status": event.status,
        "banner_image_url": event.banner_image_url,
        "start_datetime": event.start_datetime,
        "end_datetime": event.end_datetime,
        "venue_name": event.venue_name,
        "venue_address": event.venue_address,
        "geo_lat": event.geo_lat,
        "geo_lng": event.geo_lng,
        "transit_info": event.transit_info,
        "about_text": event.about_text,
        "terms_and_conditions": event.terms_and_conditions,
        "total_capacity": event.total_capacity,
        "tickets_sold": event.tickets_sold,
        "min_price": event.min_price,
        "seat_tiers": seat_tiers,
        "packages": packages,
        "merchandise": merchandise,
        "partners": [
            "Logoippsum", "Logoippsum Foundation", "Logoippsum Academy", "IPSUM", "LOOO"
        ]
    }

# ----------------- Bookings -----------------
@app.get("/api/v1/bookings", tags=["Bookings"])
def get_bookings(
    status: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    search: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(Booking)
    if status and status != "All":
        query = query.filter(Booking.status == status)
    if search:
        query = query.filter(
            (Booking.customer_name.ilike(f"%{search}%")) |
            (Booking.invoice_id_str.ilike(f"%{search}%"))
        )

    bookings = query.all()
    results = []
    for b in bookings:
        results.append({
            "id": b.id,
            "invoice_id": b.invoice_id_str,
            "date": b.booking_date.strftime("%Y/%m/%d %I:%M %p"),
            "customer_name": b.customer_name,
            "customer_email": b.customer_email,
            "event_title": b.event.title if b.event else "Music Festival",
            "event_category": b.event.category if b.event else "Music",
            "ticket_category": b.ticket_category,
            "price": b.price,
            "quantity": b.quantity,
            "total_amount": b.total_amount,
            "status": b.status,
            "e_voucher_code": b.e_voucher_code or "-"
        })

    return {
        "kpi": {
            "total_bookings": 55000,
            "total_tickets_sold": 45000,
            "total_earnings": "$275,450"
        },
        "category_breakdown": {
            "total": 44115,
            "categories": [
                {"name": "Music", "percentage": 25.77, "count": 14172},
                {"name": "Sport", "percentage": 22.68, "count": 12476},
                {"name": "Fashion", "percentage": 17.83, "count": 9806},
                {"name": "Art & Design", "percentage": 13.93, "count": 7661},
            ],
            "art_design_subcategories": [
                {"name": "Landscape Architecture and Design", "value": 3415, "max": 4000},
                {"name": "Futuristic Art and Design", "value": 2246, "max": 2500},
                {"name": "Mixed Media Masterclass", "value": 2000, "max": 3200},
            ]
        },
        "bookings_overview_chart": [
            {"day": "Sun", "bookings": 950},
            {"day": "Mon", "bookings": 1050},
            {"day": "Tue", "bookings": 1396},
            {"day": "Wed", "bookings": 1100},
            {"day": "Thu", "bookings": 1450},
            {"day": "Fri", "bookings": 1300},
            {"day": "Sat", "bookings": 1500},
        ],
        "total_count": 312,
        "bookings": results
    }

@app.get("/api/v1/bookings/{id}/voucher", tags=["Bookings"])
def get_e_voucher(id: int, db: Session = Depends(get_db)):
    booking = db.query(Booking).filter(Booking.id == id).first()
    if not booking:
        # Fallback to first booking
        booking = db.query(Booking).first()
    
    event = booking.event or db.query(Event).first()

    return {
        "voucher_id": booking.e_voucher_code or "INV202945",
        "invoice_id": booking.invoice_id_str,
        "attendee_name": booking.customer_name,
        "ticket_category": booking.ticket_category,
        "seat_number": booking.seat_number or "B12",
        "gate_number": booking.gate_number or "3",
        "event_title": event.title,
        "event_subtitle": "DJ Nova, The Rockerz, ElectroBeats, Harmony Crew",
        "location": event.venue_name,
        "date": event.start_datetime.strftime("%B %d, %Y"),
        "time": "12:00 PM - 11:00 PM",
        "barcode_value": f"||| |||| || |||||| ||||| {booking.invoice_id_str} |||| |||",
        "schedule": [
            {"time": "10:00 AM - 11:00 AM", "title": "Gate Opens"},
            {"time": "11:00 AM - 12:00 PM", "title": "Pre-Show Activities"},
            {"time": "12:00 PM - 12:30 PM", "title": "Opening Ceremony"},
            {"time": "12:30 PM", "title": "Concert Begin"}
        ],
        "prohibited_items": [
            "Weapons and Dangerous Items", "Illegal Substances", "Alcohol and Beverages",
            "Recording Equipment", "Large or Hazardous Items", "Noise Makers and Disruptive Items",
            "Unauthorized Merchandise", "Pets and Animals", "Bicycles, Skateboards, or Hoverboards",
            "Coolers or Picnic Baskets", "Umbrellas or Large Parasols", "Camping Gear"
        ]
    }

# ----------------- Invoices -----------------
@app.get("/api/v1/invoices", tags=["Invoices"])
def get_invoices(
    status: Optional[str] = Query(None),
    search: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(Invoice)
    if status and status != "All":
        query = query.filter(Invoice.status == status)
    if search:
        query = query.filter(
            (Invoice.invoice_number.ilike(f"%{search}%")) |
            (Invoice.bill_to_name.ilike(f"%{search}%"))
        )

    invoices = query.all()
    results = []
    for inv in invoices:
        results.append({
            "id": inv.id,
            "invoice_number": inv.invoice_number,
            "date": inv.issued_date.strftime("%b %d, %Y %I:%M %p"),
            "customer_name": inv.bill_to_name,
            "amount": inv.total_amount,
            "status": inv.status
        })

    return {
        "kpi": {
            "paid_count": 1805,
            "paid_last_month": 1600,
            "unpaid_count": 535,
            "unpaid_last_month": 615,
            "overdue_count": 80,
            "overdue_last_month": 70
        },
        "invoices": results
    }

@app.get("/api/v1/invoices/{invoice_number}", tags=["Invoices"])
def get_invoice_detail(invoice_number: str, db: Session = Depends(get_db)):
    inv = db.query(Invoice).filter(Invoice.invoice_number == invoice_number).first()
    if not inv:
        inv = db.query(Invoice).first()

    items = [
        {
            "id": it.id,
            "ticket_category": it.ticket_category,
            "price": it.unit_price,
            "quantity": it.quantity,
            "amount": it.amount
        } for it in inv.items
    ]

    # If no items in seed, fallback to mockup values
    if not items:
        items = [
            {"id": 1, "ticket_category": "Platinum", "price": 120.0, "quantity": 1, "amount": 120.0},
            {"id": 2, "ticket_category": "Silver", "price": 50.0, "quantity": 2, "amount": 100.0}
        ]

    return {
        "id": inv.id,
        "invoice_number": inv.invoice_number,
        "issued_date": inv.issued_date.strftime("%Y/%m/%d, %I:%M %p"),
        "due_date": (inv.due_date or inv.issued_date).strftime("%Y/%m/%d, 11:59 PM"),
        "status": inv.status,
        "bill_from": {
            "name": inv.bill_from_name,
            "address": inv.bill_from_address,
            "email": inv.bill_from_email,
            "phone": inv.bill_from_phone
        },
        "bill_to": {
            "name": inv.bill_to_name,
            "address": inv.bill_to_address,
            "email": inv.bill_to_email,
            "phone": inv.bill_to_phone
        },
        "items": items,
        "subtotal": 220.0,
        "tax": 22.0,
        "fee": 5.0,
        "total": 247.0,
        "notes": "Please make payment before the due date to avoid any penalties or cancellation of your ticket. For any questions or concerns, contact our support team at support@eventmgmt.com or call +1-800-555-1234."
    }

# ----------------- Inbox -----------------
@app.get("/api/v1/inbox/messages", tags=["Inbox"])
def get_messages(
    folder: str = Query("inbox"),
    label: Optional[str] = Query(None),
    search: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(Message)
    if folder == "starred":
        query = query.filter(Message.is_starred == True)
    elif folder != "all":
        query = query.filter(Message.folder == folder)

    if label:
        query = query.filter(Message.label == label)
    if search:
        query = query.filter(
            (Message.subject.ilike(f"%{search}%")) |
            (Message.sender_name.ilike(f"%{search}%"))
        )

    messages = query.all()
    return {
        "counts": {
            "inbox": db.query(Message).filter(Message.folder == "inbox").count(),
            "starred": db.query(Message).filter(Message.is_starred == True).count(),
            "sent": 12,
            "drafts": 4,
            "spam": 2,
            "trash": 5
        },
        "labels": ["Customer", "Sponsor", "Partner"],
        "messages": [
            {
                "id": m.id,
                "sender_name": m.sender_name,
                "sender_email": m.sender_email,
                "sender_initials": m.sender_initials,
                "label": m.label,
                "folder": m.folder,
                "subject": m.subject,
                "snippet": m.snippet,
                "body_text": m.body_text,
                "is_starred": m.is_starred,
                "is_read": m.is_read,
                "time_str": m.timestamp.strftime("%I:%M %p")
            } for m in messages
        ]
    }

@app.post("/api/v1/inbox/reply", tags=["Inbox"])
def reply_message(req: MessageReplyRequest, db: Session = Depends(get_db)):
    return {"message": "Reply sent successfully", "success": True}

# ----------------- Calendar / Agendas -----------------
@app.get("/api/v1/calendar/agendas", tags=["Calendar"])
def get_agendas(db: Session = Depends(get_db)):
    agendas = db.query(AgendaItem).all()
    return {
        "metrics": {
            "all_schedules": 15,
            "event": 4,
            "meeting": 5,
            "setup_and_rehearsal": 3
        },
        "agendas": [
            {
                "id": a.id,
                "title": a.title,
                "category": a.category,
                "start_time": a.start_datetime.strftime("%I:%M %p"),
                "date": a.start_datetime.strftime("%Y-%m-%d"),
                "day": a.start_datetime.day,
                "pic_name": a.pic_name,
                "pic_role": a.pic_role,
                "pic_phone": a.pic_phone,
                "pic_email": a.pic_email,
                "notes": a.notes
            } for a in agendas
        ]
    }

@app.post("/api/v1/calendar/agendas", tags=["Calendar"])
def create_agenda(agenda: AgendaCreateSchema, db: Session = Depends(get_db)):
    new_a = AgendaItem(
        title=agenda.title,
        category=agenda.category,
        start_datetime=agenda.start_datetime,
        end_datetime=agenda.end_datetime,
        pic_name=agenda.pic_name,
        pic_role=agenda.pic_role,
        pic_phone=agenda.pic_phone,
        pic_email=agenda.pic_email,
        notes=agenda.notes
    )
    db.add(new_a)
    db.commit()
    db.refresh(new_a)
    return new_a

# ----------------- Financials -----------------
@app.get("/api/v1/financials/stats", tags=["Financials"])
def get_financial_stats(db: Session = Depends(get_db)):
    txs = db.query(FinancialTransaction).order_by(desc(FinancialTransaction.date)).all()
    return {
        "cards": {
            "balance": 75000,
            "balance_growth": 3.65,
            "income": 150000,
            "income_growth": 2.08,
            "expenses": 45000,
            "expense_growth": -0.84
        },
        "cashflow": [
            {"month": "Jan", "income": 5800, "expense": -4200},
            {"month": "Feb", "income": 6200, "expense": -4500},
            {"month": "Mar", "income": 6900, "expense": -4800},
            {"month": "Apr", "income": 7100, "expense": -4900},
            {"month": "May", "income": 6815, "expense": -5120},
            {"month": "Jun", "income": 7500, "expense": -5300},
            {"month": "Jul", "income": 8200, "expense": -5600},
            {"month": "Aug", "income": 8000, "expense": -5400},
            {"month": "Sep", "income": 8600, "expense": -5800},
            {"month": "Oct", "income": 8900, "expense": -5900},
        ],
        "sales_revenue": {
            "total": 150000,
            "breakdown": [
                {"category": "Music", "percentage": 30, "amount": 45000},
                {"category": "Fashion", "percentage": 20, "amount": 30000},
                {"category": "Sports", "percentage": 16, "amount": 24000},
                {"category": "Art & Design", "percentage": 14, "amount": 21000},
                {"category": "Health & Wellness", "percentage": 10, "amount": 15000},
                {"category": "Technology", "percentage": 10, "amount": 15000},
            ]
        },
        "expense_breakdown": {
            "total": 45000,
            "breakdown": [
                {"category": "Marketing", "percentage": 30.77, "amount": 13846.15},
                {"category": "Venue", "percentage": 26.92, "amount": 12115.38},
                {"category": "Staffing", "percentage": 19.23, "amount": 8653.85},
                {"category": "Equipment", "percentage": 11.54, "amount": 5192.31},
                {"category": "Miscellaneous", "percentage": 7.69, "amount": 3461.54},
                {"category": "Utilities", "percentage": 3.85, "amount": 1730.77},
            ]
        },
        "transactions": [
            {
                "id": t.id,
                "date": t.date.strftime("%Y/%m/%d %I:%M %p"),
                "event": t.event_name,
                "type": t.type,
                "category": t.category,
                "amount": t.amount,
                "note": t.note,
                "status": t.status
            } for t in txs
        ]
    }

# ----------------- Feedback -----------------
@app.get("/api/v1/feedback/stats", tags=["Feedback"])
def get_feedback_stats(db: Session = Depends(get_db)):
    reviews = db.query(FeedbackReview).all()
    return {
        "overall_score": 4.8,
        "total_reviews": 15545,
        "criteria": {
            "venue": 4.7,
            "entertainment_quality": 4.9,
            "event_organization": 4.8,
            "food_and_beverages": 4.3,
            "staff_support": 4.6,
            "value_for_money": 4.5
        },
        "monthly_statistics": [
            {"month": "Jan", "r1_3": 110, "r4_5": 880},
            {"month": "Feb", "r1_3": 95, "r4_5": 920},
            {"month": "Mar", "r1_3": 120, "r4_5": 850},
            {"month": "Apr", "r1_3": 85, "r4_5": 940},
            {"month": "May", "r1_3": 100, "r4_5": 890},
            {"month": "Jun", "r1_3": 110, "r4_5": 880},
            {"month": "Jul", "r1_3": 90, "r4_5": 910},
            {"month": "Aug", "r1_3": 115, "r4_5": 870},
            {"month": "Sep", "r1_3": 95, "r4_5": 930},
            {"month": "Oct", "r1_3": 105, "r4_5": 900},
            {"month": "Nov", "r1_3": 110, "r4_5": 890},
            {"month": "Dec", "r1_3": 120, "r4_5": 860},
        ],
        "reviews": [
            {
                "id": r.id,
                "customer_name": r.customer_name,
                "customer_avatar": r.customer_avatar,
                "rating": r.rating,
                "event_title": r.event_title,
                "event_category": r.event_category,
                "comment": r.comment,
                "date": r.created_at.strftime("%B %d, %Y")
            } for r in reviews
        ]
    }

# ----------------- Gallery -----------------
@app.get("/api/v1/gallery/albums", tags=["Gallery"])
def get_gallery_albums(db: Session = Depends(get_db)):
    albums = db.query(GalleryAlbum).all()
    return {
        "total_count": len(albums),
        "albums": [
            {
                "id": a.id,
                "title": a.title,
                "category": a.category,
                "event_date": a.event_date,
                "cover_image_url": a.cover_image_url,
                "photo_count": a.photo_count
            } for a in albums
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)
