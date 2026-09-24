from typing import List, Optional, Any
from pydantic import BaseModel
from datetime import datetime

# Common
class ResponseMessage(BaseModel):
    message: str
    success: bool = True

# User / Admin
class UserSchema(BaseModel):
    id: int
    full_name: str
    email: str
    role: str
    avatar_url: Optional[str] = None
    is_active: bool

    class Config:
        from_attributes = True

# Seat Tier & Packages
class SeatTierSchema(BaseModel):
    id: int
    name: str
    tier_type: str
    price: float
    capacity: int
    booked_count: int
    benefits: Optional[List[str]] = None

    class Config:
        from_attributes = True

class PackageSchema(BaseModel):
    id: int
    name: str
    type_label: str
    price: float
    description: Optional[str] = None
    features: Optional[List[str]] = None

    class Config:
        from_attributes = True

class MerchandiseSchema(BaseModel):
    id: int
    name: str
    price: float
    image_url: Optional[str] = None
    stock_quantity: int

    class Config:
        from_attributes = True

# Event
class EventBase(BaseModel):
    title: str
    slug: str
    category: str
    status: str
    banner_image_url: Optional[str] = None
    start_datetime: datetime
    end_datetime: Optional[datetime] = None
    venue_name: str
    venue_address: Optional[str] = None
    geo_lat: Optional[float] = None
    geo_lng: Optional[float] = None
    transit_info: Optional[dict] = None
    about_text: Optional[str] = None
    terms_and_conditions: Optional[str] = None
    total_capacity: int
    tickets_sold: int
    min_price: float

class EventDetailSchema(EventBase):
    id: int
    seat_tiers: List[SeatTierSchema] = []
    packages: List[PackageSchema] = []
    merchandise: List[MerchandiseSchema] = []

    class Config:
        from_attributes = True

class EventListSchema(BaseModel):
    id: int
    title: str
    slug: str
    category: str
    status: str
    banner_image_url: Optional[str] = None
    start_datetime: datetime
    venue_name: str
    venue_address: Optional[str] = None
    total_capacity: int
    tickets_sold: int
    min_price: float
    percentage_sold: int = 0
    tickets_left: int = 0

    class Config:
        from_attributes = True

# Booking
class BookingSchema(BaseModel):
    id: int
    invoice_id_str: str
    customer_name: str
    customer_email: Optional[str] = None
    customer_phone: Optional[str] = None
    event_title: Optional[str] = None
    event_category: Optional[str] = None
    ticket_category: str
    price: float
    quantity: int
    total_amount: float
    status: str
    e_voucher_code: Optional[str] = None
    seat_number: Optional[str] = None
    gate_number: Optional[str] = None
    booking_date: datetime

    class Config:
        from_attributes = True

# Invoice
class InvoiceItemSchema(BaseModel):
    id: int
    ticket_category: str
    unit_price: float
    quantity: int
    amount: float

    class Config:
        from_attributes = True

class InvoiceDetailSchema(BaseModel):
    id: int
    invoice_number: str
    bill_from_name: str
    bill_from_address: str
    bill_from_email: str
    bill_from_phone: str
    bill_to_name: str
    bill_to_address: str
    bill_to_email: str
    bill_to_phone: str
    issued_date: datetime
    due_date: Optional[datetime] = None
    status: str
    subtotal: float
    tax_rate: float
    tax_amount: float
    fee_amount: float
    total_amount: float
    notes: Optional[str] = None
    items: List[InvoiceItemSchema] = []

    class Config:
        from_attributes = True

# Message
class MessageSchema(BaseModel):
    id: int
    sender_name: str
    sender_email: str
    sender_avatar: Optional[str] = None
    sender_initials: str
    label: str
    folder: str
    subject: str
    snippet: Optional[str] = None
    body_text: str
    is_starred: bool
    is_read: bool
    timestamp: datetime

    class Config:
        from_attributes = True

class MessageReplyRequest(BaseModel):
    message_id: int
    reply_body: str

# Agenda / Calendar
class AgendaSchema(BaseModel):
    id: int
    event_id: Optional[int] = None
    title: str
    category: str
    start_datetime: datetime
    end_datetime: Optional[datetime] = None
    pic_name: str
    pic_role: str
    pic_phone: str
    pic_email: str
    assigned_team: Optional[List[dict]] = None
    notes: Optional[str] = None

    class Config:
        from_attributes = True

class AgendaCreateSchema(BaseModel):
    title: str
    category: str
    start_datetime: datetime
    end_datetime: Optional[datetime] = None
    pic_name: str
    pic_role: str
    pic_phone: str
    pic_email: str
    notes: Optional[str] = None

# Transaction
class TransactionSchema(BaseModel):
    id: int
    date: datetime
    event_name: Optional[str] = None
    type: str
    category: str
    amount: float
    note: Optional[str] = None
    status: str

    class Config:
        from_attributes = True

# Feedback
class FeedbackSchema(BaseModel):
    id: int
    customer_name: str
    customer_avatar: Optional[str] = None
    rating: float
    event_title: Optional[str] = None
    event_category: Optional[str] = None
    comment: str
    created_at: datetime

    class Config:
        from_attributes = True

# Activity Log
class ActivityLogSchema(BaseModel):
    id: int
    actor_name: str
    action_type: str
    description: str
    timestamp: datetime

    class Config:
        from_attributes = True

# Gallery
class GalleryAlbumSchema(BaseModel):
    id: int
    title: str
    category: str
    event_date: Optional[str] = None
    cover_image_url: str
    photo_count: int

    class Config:
        from_attributes = True
