export type NavView = 
  | 'dashboard'
  | 'bookings'
  | 'invoices'
  | 'inbox'
  | 'calendar'
  | 'events'
  | 'event-detail'
  | 'financials'
  | 'feedback'
  | 'voucher'
  | 'gallery';

export interface EventItem {
  id: number;
  title: string;
  slug: string;
  category: string;
  status: string;
  banner_image_url: string;
  start_datetime: string;
  venue_name: string;
  venue_address?: string;
  total_capacity: number;
  tickets_sold: number;
  min_price: number;
  percentage_sold: number;
  tickets_left: number;
  about_text: string;
  transit_info?: {
    by_car?: string;
    by_metro?: string;
    by_bus?: string;
  };
  terms_and_conditions?: string;
  seat_tiers?: Array<{ id: number; name: string; price: number }>;
  packages?: Array<{ id: number; name: string; price: number; features: string[] }>;
  merchandise?: Array<{ id: number; name: string; price: number; image_url: string }>;
}

export interface BookingItem {
  id: number;
  invoice_id: string;
  date: string;
  customer_name: string;
  customer_email?: string;
  event_title: string;
  event_category: string;
  ticket_category: string;
  price: number;
  quantity: number;
  total_amount: number;
  status: 'Confirmed' | 'Pending' | 'Cancelled';
  e_voucher_code?: string;
}

export interface InvoiceItem {
  id: number;
  invoice_number: string;
  date: string;
  customer_name: string;
  customer_email?: string;
  amount: number;
  status: 'Paid' | 'Unpaid' | 'Overdue';
  items?: Array<{ ticket_category: string; price: number; quantity: number; amount: number }>;
  subtotal?: number;
  tax?: number;
  fee?: number;
  total?: number;
  notes?: string;
}

export interface MessageReply {
  id: number;
  sender_name: string;
  sender_email: string;
  body_text: string;
  time_str: string;
}

export interface MessageItem {
  id: number;
  sender_name: string;
  sender_email: string;
  sender_initials: string;
  label: 'Customer' | 'Sponsor' | 'Partner' | string;
  folder: string;
  subject: string;
  snippet: string;
  body_text: string;
  is_starred: boolean;
  is_read: boolean;
  time_str: string;
  replies?: MessageReply[];
}

export interface AgendaTimelineSlot {
  time: string;
  title: string;
  stage: string;
  speaker?: string;
  status?: 'Completed' | 'In Progress' | 'Upcoming';
}

export interface AgendaItem {
  id: number;
  day: number;
  month_year?: string;
  title: string;
  category: string;
  datetime: string;
  location: string;
  pic_name: string;
  pic_role: string;
  pic_phone: string;
  pic_email: string;
  notes: string[];
  slots?: AgendaTimelineSlot[];
}

export interface ReviewItem {
  id: number;
  customer_name: string;
  customer_avatar: string;
  rating: number;
  event_title: string;
  event_category: string;
  comment: string;
  date: string;
}

export interface GalleryAlbum {
  id: number;
  title: string;
  category: string;
  event_date: string;
  cover_image_url: string;
  photo_count: number;
}

export interface FinancialTransaction {
  id: number;
  transaction_code: string;
  date: string;
  event_name: string;
  type: 'Income' | 'Expense' | string;
  category: string;
  amount: number;
  payment_method: string;
  note?: string;
  status: 'Completed' | 'Pending' | 'Processing' | string;
}

export interface FinancialSummary {
  total_balance: number;
  total_income: number;
  total_expense: number;
  operating_margin: number;
  balance_change_pct: number;
  income_change_pct: number;
  expense_change_pct: number;
}
