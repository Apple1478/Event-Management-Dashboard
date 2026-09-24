import datetime
from sqlalchemy import (
    Column, Integer, String, Float, Boolean, DateTime,
    ForeignKey, Text, Numeric, JSON
)
from sqlalchemy.orm import relationship
try:
    from backend.database import Base
except ImportError:
    from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(150), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    role = Column(String(50), default="Admin")  # Admin, Coordinator, Staff
    avatar_url = Column(String(500), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    slug = Column(String(255), unique=True, index=True)
    category = Column(String(100), nullable=False)  # Music, Sport, Fashion, Art & Design, Food & Culinary, Technology, Health & Wellness, Outdoor & Adventure
    status = Column(String(50), default="Active")  # Active, Draft, Past
    banner_image_url = Column(String(500), nullable=True)
    start_datetime = Column(DateTime, nullable=False)
    end_datetime = Column(DateTime, nullable=True)
    venue_name = Column(String(255), nullable=False)
    venue_address = Column(String(255), nullable=True)
    geo_lat = Column(Float, nullable=True)
    geo_lng = Column(Float, nullable=True)
    transit_info = Column(JSON, nullable=True)  # by car, by metro, by bus
    about_text = Column(Text, nullable=True)
    terms_and_conditions = Column(Text, nullable=True)
    total_capacity = Column(Integer, default=1000)
    tickets_sold = Column(Integer, default=0)
    min_price = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    # Relationships
    seat_tiers = relationship("EventSeatTier", back_populates="event", cascade="all, delete-orphan")
    packages = relationship("EventPackage", back_populates="event", cascade="all, delete-orphan")
    merchandise = relationship("EventMerchandise", back_populates="event", cascade="all, delete-orphan")
    bookings = relationship("Booking", back_populates="event")
    agendas = relationship("AgendaItem", back_populates="event")
    reviews = relationship("FeedbackReview", back_populates="event")

class EventSeatTier(Base):
    __tablename__ = "event_seat_tiers"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)
    name = Column(String(100), nullable=False)  # Diamond, Platinum, Gold, Silver, Bronze, General Admission, VIP Lounge, Backstage Access
    tier_type = Column(String(50), default="Seated")  # Seated, Standing
    price = Column(Float, nullable=False)
    capacity = Column(Integer, default=100)
    booked_count = Column(Integer, default=0)
    benefits = Column(JSON, nullable=True)  # List of string perks

    event = relationship("Event", back_populates="seat_tiers")

class EventPackage(Base):
    __tablename__ = "event_packages"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)
    name = Column(String(150), nullable=False)
    type_label = Column(String(50), default="Standing")  # Standing, Seating
    price = Column(Float, nullable=False)
    description = Column(String(255), nullable=True)
    features = Column(JSON, nullable=True)

    event = relationship("Event", back_populates="packages")

class EventMerchandise(Base):
    __tablename__ = "event_merchandise"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)
    name = Column(String(150), nullable=False)
    price = Column(Float, nullable=False)
    image_url = Column(String(500), nullable=True)
    stock_quantity = Column(Integer, default=100)

    event = relationship("Event", back_populates="merchandise")

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    invoice_id_str = Column(String(50), unique=True, index=True, nullable=False)  # e.g., INV10011
    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)
    customer_name = Column(String(150), nullable=False)
    customer_email = Column(String(150), nullable=True)
    customer_phone = Column(String(50), nullable=True)
    customer_address = Column(String(255), nullable=True)
    ticket_category = Column(String(100), default="General Admission")
    price = Column(Float, nullable=False)
    quantity = Column(Integer, default=1)
    total_amount = Column(Float, nullable=False)
    status = Column(String(50), default="Confirmed")  # Confirmed, Pending, Cancelled
    e_voucher_code = Column(String(50), nullable=True)  # 123456-MUSIC
    seat_number = Column(String(50), default="B12")
    gate_number = Column(String(50), default="3")
    booking_date = Column(DateTime, default=datetime.datetime.utcnow)

    event = relationship("Event", back_populates="bookings")
    invoice = relationship("Invoice", back_populates="booking", uselist=False)

class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    invoice_number = Column(String(50), unique=True, index=True, nullable=False)  # INV10012
    booking_id = Column(Integer, ForeignKey("bookings.id"), nullable=True)
    bill_from_name = Column(String(150), default="Event Management Co.")
    bill_from_address = Column(String(255), default="123 Sunset Avenue, Los Angeles, CA, 90001")
    bill_from_email = Column(String(150), default="billing@eventmgmt.com")
    bill_from_phone = Column(String(50), default="+1-800-555-1234")
    bill_to_name = Column(String(150), nullable=False)
    bill_to_address = Column(String(255), default="789 Main Street, Beverly Hills, CA, 90210")
    bill_to_email = Column(String(150), default="customer@email.com")
    bill_to_phone = Column(String(50), default="+1-310-555-6789")
    issued_date = Column(DateTime, default=datetime.datetime.utcnow)
    due_date = Column(DateTime, nullable=True)
    status = Column(String(50), default="Paid")  # Paid, Unpaid, Overdue
    subtotal = Column(Float, default=0.0)
    tax_rate = Column(Float, default=0.10)  # 10%
    tax_amount = Column(Float, default=0.0)
    fee_amount = Column(Float, default=5.0)  # $5 processing fee
    total_amount = Column(Float, default=0.0)
    notes = Column(Text, nullable=True)

    booking = relationship("Booking", back_populates="invoice")
    items = relationship("InvoiceItem", back_populates="invoice", cascade="all, delete-orphan")

class InvoiceItem(Base):
    __tablename__ = "invoice_items"

    id = Column(Integer, primary_key=True, index=True)
    invoice_id = Column(Integer, ForeignKey("invoices.id"), nullable=False)
    ticket_category = Column(String(100), nullable=False)
    unit_price = Column(Float, nullable=False)
    quantity = Column(Integer, default=1)
    amount = Column(Float, nullable=False)

    invoice = relationship("Invoice", back_populates="items")

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    sender_name = Column(String(150), nullable=False)
    sender_email = Column(String(150), nullable=False)
    sender_avatar = Column(String(500), nullable=True)
    sender_initials = Column(String(10), default="HA")
    label = Column(String(50), default="Customer")  # Customer, Sponsor, Partner
    folder = Column(String(50), default="inbox")  # inbox, starred, sent, drafts, spam, trash
    subject = Column(String(255), nullable=False)
    snippet = Column(String(255), nullable=True)
    body_text = Column(Text, nullable=False)
    is_starred = Column(Boolean, default=False)
    is_read = Column(Boolean, default=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

class AgendaItem(Base):
    __tablename__ = "agenda_items"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=True)
    title = Column(String(255), nullable=False)
    category = Column(String(100), default="Meeting")  # All Schedules, Event, Meeting, Setup and Rehearsal, Task Deadlines
    start_datetime = Column(DateTime, nullable=False)
    end_datetime = Column(DateTime, nullable=True)
    pic_name = Column(String(150), default="Michael Taylor")
    pic_role = Column(String(100), default="Event Coordinator")
    pic_phone = Column(String(50), default="+1-800-555-7890")
    pic_email = Column(String(150), default="michael.taylor@eventmgmt.com")
    assigned_team = Column(JSON, nullable=True)  # [{name, avatar}]
    notes = Column(Text, nullable=True)

    event = relationship("Event", back_populates="agendas")

class FinancialTransaction(Base):
    __tablename__ = "financial_transactions"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    event_name = Column(String(150), nullable=True)
    type = Column(String(50), default="Income")  # Income, Expense
    category = Column(String(100), nullable=False)  # Vendor, Event, Marketing, Sponsorship, Equipment, Staffing
    amount = Column(Float, nullable=False)
    note = Column(String(255), nullable=True)
    status = Column(String(50), default="Completed")  # Completed, Pending

class FeedbackReview(Base):
    __tablename__ = "feedback_reviews"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=True)
    customer_name = Column(String(150), nullable=False)
    customer_avatar = Column(String(500), nullable=True)
    rating = Column(Float, default=5.0)
    event_title = Column(String(255), nullable=True)
    event_category = Column(String(100), nullable=True)
    comment = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    event = relationship("Event", back_populates="reviews")

class ActivityAuditLog(Base):
    __tablename__ = "activity_logs"

    id = Column(Integer, primary_key=True, index=True)
    actor_name = Column(String(150), nullable=False)
    action_type = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

class GalleryAlbum(Base):
    __tablename__ = "gallery_albums"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    category = Column(String(100), nullable=False)
    event_date = Column(String(100), nullable=True)
    cover_image_url = Column(String(500), nullable=False)
    photo_count = Column(Integer, default=24)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
