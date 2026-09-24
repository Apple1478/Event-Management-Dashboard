import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { DashboardDataService } from './services/dashboard-data.service';
import { 
  NavView, EventItem, BookingItem, InvoiceItem, 
  MessageItem, MessageReply, AgendaItem, AgendaTimelineSlot, ReviewItem, GalleryAlbum,
  FinancialTransaction, FinancialSummary 
} from './models/dashboard.models';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  currentView: NavView = 'dashboard';
  globalSearch: string = '';

  // Data collections
  events: EventItem[] = [];
  bookings: BookingItem[] = [];
  invoices: InvoiceItem[] = [];
  messages: MessageItem[] = [];
  agendas: AgendaItem[] = [];
  reviews: ReviewItem[] = [];
  albums: GalleryAlbum[] = [];
  transactions: FinancialTransaction[] = [];
  financialSummary: FinancialSummary | null = null;

  // Mobile navigation
  mobileMenuOpen: boolean = false;

  // Active selections
  selectedEventId: number = 1;
  selectedBookingId: number = 1;
  selectedInvoiceNumber: string = 'INV10012';
  selectedMessageId: number = 1;
  selectedAgenda: AgendaItem | null = null;
  activeCalendarDay: number = 23;
  lightboxAlbum: GalleryAlbum | null = null;

  // View state & filters
  bookingsTab: string = 'All';
  bookingsSearch: string = '';
  bookingsCategory: string = 'All Category';
  bookingsCurrentPage: number = 1;

  invoicesSearch: string = '';
  activeInboxFolder: string = 'inbox';
  activeInboxLabel: string | null = null;
  inboxSearch: string = '';
  isReplying: boolean = false;
  replyText: string = '';

  eventsTab: string = 'Active';
  eventsViewMode: 'list' | 'grid' = 'list';
  eventsSearch: string = '';

  financialsTab: string = 'All';
  financialsCategory: string = 'All Category';
  financialsSearch: string = '';

  termsExpanded: boolean = true;
  calendarDrawerOpen: boolean = true;
  calendarMonthName: string = 'May 2029';
  calendarViewMode: 'month' | 'schedule' = 'month';
  feedbackFilterRating: number = 0; // 0 = all

  // Modals & Panels
  showNotifications: boolean = false;
  showSettingsModal: boolean = false;
  showVersionModal: boolean = false;
  showLocationModal: boolean = false;
  showCreateEventModal: boolean = false;
  showAddInvoiceModal: boolean = false;
  showNewAgendaModal: boolean = false;
  showCreateFolderModal: boolean = false;
  showComposeModal: boolean = false;
  showAddTransactionModal: boolean = false;
  toastMessage: string | null = null;

  // Form Models
  newEventTitle = '';
  newEventCategory = 'Music';
  newEventVenue = '';
  newEventPrice = 50;

  newInvoiceNumber = '';
  newInvoiceCustomer = '';
  newInvoiceAmount = 150;

  newAgendaTitle = '';
  newAgendaCategory = 'Event';
  newAgendaTime = '10:00 AM';

  composeTo = '';
  composeSubject = '';
  composeLabel = 'Customer';
  composeBody = '';

  newFolderName = '';
  newFolderCategory = 'Music';

  newTxEventName = '';
  newTxType = 'Income';
  newTxCategory = 'Ticket Sales';
  newTxAmount = 2500;
  newTxMethod = 'Stripe Gateway';
  newTxNote = '';

  // Cart counter for merch
  cartCount: number = 0;

  constructor(private dataService: DashboardDataService) {}

  async ngOnInit() {
    this.events = await this.dataService.getEvents();
    this.bookings = await this.dataService.getBookings();
    this.invoices = await this.dataService.getInvoices();
    this.messages = await this.dataService.getMessages();
    this.agendas = await this.dataService.getAgendas();
    this.reviews = await this.dataService.getReviews();
    this.albums = await this.dataService.getAlbums();
    this.transactions = await this.dataService.getFinancialTransactions();
    this.financialSummary = await this.dataService.getFinancialSummary();

    if (this.agendas.length > 0) {
      this.selectedAgenda = this.agendas[0];
    }
  }

  // Toast feedback helper
  showToast(msg: string) {
    this.toastMessage = msg;
    setTimeout(() => {
      this.toastMessage = null;
    }, 3200);
  }

  // Navigation
  setView(view: NavView | string) {
    this.currentView = view as NavView;
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  getPageTitle(): string {
    switch (this.currentView) {
      case 'dashboard': return 'Dashboard';
      case 'bookings': return 'Bookings';
      case 'invoices': return 'Invoices';
      case 'inbox': return 'Inbox';
      case 'calendar': return 'Calendar';
      case 'events': return 'Events';
      case 'event-detail': return 'Event Details';
      case 'financials': return 'Financials';
      case 'feedback': return 'Feedback';
      case 'voucher': return 'E-Voucher';
      case 'gallery': return 'Gallery';
      default: return 'Dashboard';
    }
  }

  // Event Details
  selectEvent(id: number) {
    this.selectedEventId = id;
    this.setView('event-detail');
  }

  getSelectedEvent(): EventItem {
    return this.events.find(e => e.id === this.selectedEventId) || this.events[0];
  }

  // Bookings & Voucher
  openVoucher(bookingId: number) {
    this.selectedBookingId = bookingId;
    this.setView('voucher');
  }

  getSelectedBooking(): BookingItem {
    return this.bookings.find(b => b.id === this.selectedBookingId) || this.bookings[0];
  }

  getFilteredBookings(): BookingItem[] {
    return this.bookings.filter(b => {
      const matchTab = this.bookingsTab === 'All' || b.status === this.bookingsTab;
      const matchSearch = !this.bookingsSearch || 
        b.customer_name.toLowerCase().includes(this.bookingsSearch.toLowerCase()) ||
        b.invoice_id.toLowerCase().includes(this.bookingsSearch.toLowerCase()) ||
        b.event_title.toLowerCase().includes(this.bookingsSearch.toLowerCase());
      const matchCategory = this.bookingsCategory === 'All Category' || b.event_category === this.bookingsCategory;
      return matchTab && matchSearch && matchCategory;
    });
  }

  // Invoices
  selectInvoice(num: string) {
    this.selectedInvoiceNumber = num;
  }

  getSelectedInvoice(): InvoiceItem {
    return this.invoices.find(inv => inv.invoice_number === this.selectedInvoiceNumber) || this.invoices[0];
  }

  getFilteredInvoices(): InvoiceItem[] {
    return this.invoices.filter(inv => {
      return !this.invoicesSearch || 
        inv.invoice_number.toLowerCase().includes(this.invoicesSearch.toLowerCase()) ||
        inv.customer_name.toLowerCase().includes(this.invoicesSearch.toLowerCase());
    });
  }

  sendInvoice(invoiceNum: string) {
    this.showToast(`Invoice ${invoiceNum} sent to customer's email!`);
  }

  holdInvoice(invoiceNum: string) {
    const inv = this.invoices.find(i => i.invoice_number === invoiceNum);
    if (inv) {
      inv.status = inv.status === 'Overdue' ? 'Unpaid' : 'Overdue';
      this.showToast(`Invoice ${invoiceNum} marked as ${inv.status}!`);
    }
  }

  downloadInvoicePdf(invoiceNum: string) {
    this.showToast(`Generating and downloading PDF for ${invoiceNum}...`);
    setTimeout(() => {
      window.print();
    }, 600);
  }

  addInvoice() {
    if (!this.newInvoiceNumber) return;
    const newInv: InvoiceItem = {
      id: Date.now(),
      invoice_number: this.newInvoiceNumber,
      customer_name: this.newInvoiceCustomer || 'Guest Client',
      amount: this.newInvoiceAmount,
      date: 'Today, ' + new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      status: 'Unpaid',
      subtotal: this.newInvoiceAmount,
      tax: Math.round(this.newInvoiceAmount * 0.1),
      fee: 5,
      total: Math.round(this.newInvoiceAmount * 1.1 + 5),
      items: [{ ticket_category: 'Standard Entry', price: this.newInvoiceAmount, quantity: 1, amount: this.newInvoiceAmount }]
    };
    this.invoices.unshift(newInv);
    this.selectedInvoiceNumber = newInv.invoice_number;
    this.showAddInvoiceModal = false;
    this.newInvoiceNumber = '';
    this.newInvoiceCustomer = '';
    this.showToast(`Invoice ${newInv.invoice_number} created successfully!`);
  }

  // Inbox
  getFilteredMessages(): MessageItem[] {
    return this.messages.filter(m => {
      const matchFolder = this.activeInboxFolder === 'all' || 
        (this.activeInboxFolder === 'starred' ? m.is_starred : m.folder === this.activeInboxFolder);
      const matchLabel = !this.activeInboxLabel || m.label === this.activeInboxLabel;
      const matchSearch = !this.inboxSearch || 
        m.subject.toLowerCase().includes(this.inboxSearch.toLowerCase()) ||
        m.sender_name.toLowerCase().includes(this.inboxSearch.toLowerCase()) ||
        (m.body_text && m.body_text.toLowerCase().includes(this.inboxSearch.toLowerCase()));
      return matchFolder && matchLabel && matchSearch;
    });
  }

  setInboxFolder(folder: string) {
    this.activeInboxFolder = folder;
    this.activeInboxLabel = null;
    const filtered = this.getFilteredMessages();
    if (filtered.length > 0) {
      this.selectedMessageId = filtered[0].id;
    }
  }

  getFolderCount(folder: string): number {
    if (folder === 'starred') return this.messages.filter(m => m.is_starred).length;
    return this.messages.filter(m => m.folder === folder).length;
  }

  getSelectedMessage(): MessageItem {
    const found = this.messages.find(m => m.id === this.selectedMessageId);
    if (found) return found;
    const filtered = this.getFilteredMessages();
    return filtered.length > 0 ? filtered[0] : this.messages[0];
  }

  selectMessage(msg: MessageItem) {
    this.selectedMessageId = msg.id;
    msg.is_read = true;
    this.isReplying = false;
  }

  toggleStar(message: MessageItem, event?: MouseEvent) {
    if (event) event.stopPropagation();
    message.is_starred = !message.is_starred;
    this.showToast(message.is_starred ? `Starred "${message.subject}"` : `Unstarred "${message.subject}"`);
  }

  openComposeModal() {
    this.composeTo = '';
    this.composeSubject = '';
    this.composeLabel = 'Customer';
    this.composeBody = '';
    this.showComposeModal = true;
  }

  sendComposeMessage() {
    if (!this.composeTo.trim() || !this.composeSubject.trim() || !this.composeBody.trim()) {
      this.showToast('Please fill in recipient, subject, and message.');
      return;
    }
    const newMsg: MessageItem = {
      id: Date.now(),
      sender_name: 'Ventixe Organizer',
      sender_email: 'admin@ventixe.com',
      sender_initials: 'VO',
      label: this.composeLabel,
      folder: 'sent',
      subject: this.composeSubject,
      snippet: this.composeBody.substring(0, 75) + '...',
      body_text: this.composeBody,
      is_starred: false,
      is_read: true,
      time_str: 'Just now',
      replies: []
    };
    this.messages.unshift(newMsg);
    this.showComposeModal = false;
    this.setInboxFolder('sent');
    this.selectedMessageId = newMsg.id;
    this.showToast(`Message sent to ${this.composeTo}!`);
  }

  sendReply() {
    if (!this.replyText.trim()) return;
    const currentMsg = this.getSelectedMessage();
    if (!currentMsg) return;

    const replyItem: MessageReply = {
      id: Date.now(),
      sender_name: 'Ventixe Organizer',
      sender_email: 'admin@ventixe.com',
      body_text: this.replyText,
      time_str: 'Just now'
    };

    if (!currentMsg.replies) {
      currentMsg.replies = [];
    }
    currentMsg.replies.push(replyItem);

    // Also record in Sent folder so the user sees it in their "Sent" box!
    const sentMsg: MessageItem = {
      id: Date.now() + 1,
      sender_name: 'Ventixe Organizer',
      sender_email: 'admin@ventixe.com',
      sender_initials: 'VO',
      label: currentMsg.label,
      folder: 'sent',
      subject: `Re: ${currentMsg.subject}`,
      snippet: this.replyText.substring(0, 75) + '...',
      body_text: this.replyText,
      is_starred: false,
      is_read: true,
      time_str: 'Just now',
      replies: []
    };
    this.messages.unshift(sentMsg);

    this.showToast(`Reply sent to ${currentMsg.sender_name}!`);
    this.replyText = '';
    this.isReplying = false;
  }

  forwardMessage(message: MessageItem) {
    this.composeTo = '';
    this.composeSubject = `Fwd: ${message.subject}`;
    this.composeLabel = message.label;
    this.composeBody = `\n\n--- Forwarded Message ---\nFrom: ${message.sender_name} <${message.sender_email}>\nDate: ${message.time_str}\nSubject: ${message.subject}\n\n${message.body_text}`;
    this.showComposeModal = true;
  }

  deleteMessage(messageId: number) {
    const msg = this.messages.find(m => m.id === messageId);
    if (!msg) return;

    if (msg.folder === 'trash') {
      this.messages = this.messages.filter(m => m.id !== messageId);
      this.showToast('Message permanently deleted.');
    } else {
      msg.folder = 'trash';
      this.showToast('Message moved to Trash.');
    }

    const remaining = this.getFilteredMessages();
    if (remaining.length > 0) {
      this.selectedMessageId = remaining[0].id;
    }
  }

  restoreMessage(messageId: number) {
    const msg = this.messages.find(m => m.id === messageId);
    if (msg) {
      msg.folder = 'inbox';
      this.showToast('Message restored to Inbox.');
    }
  }

  // Calendar & Agendas
  getAgendasForDay(day: number): AgendaItem[] {
    return this.agendas.filter(a => a.day === day);
  }

  selectCalendarDay(day: number) {
    this.activeCalendarDay = day;
    const existing = this.agendas.find(a => a.day === day);
    if (existing) {
      this.selectedAgenda = existing;
    } else {
      this.selectedAgenda = {
        id: day * 100,
        day: day,
        month_year: this.calendarMonthName,
        title: `Operations Briefing for May ${day}`,
        category: 'Operations',
        datetime: `May ${day}, 2029 — 09:00 AM to 05:00 PM`,
        location: 'Sunset Park, Los Angeles, CA',
        pic_name: 'Michael Taylor',
        pic_role: 'Event Coordinator',
        pic_phone: '+1-800-555-7890',
        pic_email: 'michael.taylor@eventmgmt.com',
        notes: [
          'Daily coordination meeting and stage acoustic evaluation.',
          'Review attendee crowd flow and gate security protocols.'
        ],
        slots: [
          { time: '09:00 AM - 10:30 AM', title: 'Daily Logistics Briefing', stage: 'Control Room A', speaker: 'Michael Taylor', status: 'Completed' },
          { time: '11:00 AM - 01:00 PM', title: 'Venue Walkthrough & Facilities Inspection', stage: 'Arena East', speaker: 'Safety Inspector', status: 'In Progress' },
          { time: '02:00 PM - 04:30 PM', title: 'Team Shift Handover & Vendor Coordination', stage: 'Operations Hub', speaker: 'Shift Lead', status: 'Upcoming' }
        ]
      };
    }
    this.calendarDrawerOpen = true;
  }

  addAgenda() {
    if (!this.newAgendaTitle.trim()) {
      this.showToast('Please enter an agenda title.');
      return;
    }
    const newAg: AgendaItem = {
      id: Date.now(),
      day: this.activeCalendarDay,
      month_year: this.calendarMonthName,
      title: this.newAgendaTitle,
      category: this.newAgendaCategory,
      datetime: `May ${this.activeCalendarDay}, 2029 — ${this.newAgendaTime}`,
      location: 'Sunset Park, Los Angeles, CA',
      pic_name: 'Michael Taylor',
      pic_role: 'Event Coordinator',
      pic_phone: '+1-800-555-7890',
      pic_email: 'michael.taylor@eventmgmt.com',
      notes: ['Newly scheduled session. Sound, video, and safety leads alerted.'],
      slots: [
        { time: this.newAgendaTime, title: this.newAgendaTitle, stage: 'Main Stage', speaker: 'Host / Coordinator', status: 'Upcoming' },
        { time: '02:00 PM - 03:30 PM', title: 'Interactive Workshop & Attendee Q&A', stage: 'Auditorium Hall', speaker: 'Guest Panelists', status: 'Upcoming' }
      ]
    };
    this.agendas.unshift(newAg);
    this.selectedAgenda = newAg;
    this.showNewAgendaModal = false;
    this.newAgendaTitle = '';
    this.showToast(`Schedule added for May ${this.activeCalendarDay}!`);
  }

  deleteAgenda(agendaId: number) {
    this.agendas = this.agendas.filter(a => a.id !== agendaId);
    if (this.selectedAgenda && this.selectedAgenda.id === agendaId) {
      this.selectedAgenda = this.agendas.length > 0 ? this.agendas[0] : null;
    }
    this.showToast('Agenda item removed.');
  }

  prevMonth() {
    this.showToast('Viewing April 2029 schedule archive');
  }

  nextMonth() {
    this.showToast('Viewing June 2029 upcoming schedule');
  }

  // Events
  getFilteredEvents(): EventItem[] {
    return this.events.filter(e => {
      const matchTab = this.eventsTab === 'Active' || e.status === this.eventsTab;
      const matchSearch = !this.eventsSearch || 
        e.title.toLowerCase().includes(this.eventsSearch.toLowerCase()) ||
        e.venue_name.toLowerCase().includes(this.eventsSearch.toLowerCase());
      return matchTab && matchSearch;
    });
  }

  createEvent() {
    if (!this.newEventTitle) return;
    const newEv: EventItem = {
      id: Date.now(),
      title: this.newEventTitle,
      slug: this.newEventTitle.toLowerCase().replace(/\s+/g, '-'),
      category: this.newEventCategory,
      status: 'Active',
      banner_image_url: 'https://images.unsplash.com/photo-1470225620780-dba8ba36b745?auto=format&fit=crop&w=800&q=80',
      start_datetime: 'July 15, 2029 — 6:00 PM',
      venue_name: this.newEventVenue || 'Sunset Park, Los Angeles, CA',
      total_capacity: 5000,
      tickets_sold: 500,
      min_price: this.newEventPrice,
      percentage_sold: 10,
      tickets_left: 4500,
      about_text: 'Exciting newly launched event bringing community and entertainment together.'
    };
    this.events.unshift(newEv);
    this.showCreateEventModal = false;
    this.newEventTitle = '';
    this.newEventVenue = '';
    this.showToast(`Event "${newEv.title}" published!`);
  }

  // Feedback reviews filter
  getFilteredReviews(): ReviewItem[] {
    if (this.feedbackFilterRating === 0) return this.reviews;
    return this.reviews.filter(r => Math.floor(r.rating) === this.feedbackFilterRating);
  }

  // Merchandise Add to Cart
  addToCart(item: any) {
    this.cartCount++;
    this.showToast(`Added ${item.name} to cart ($${item.price})! Total in cart: ${this.cartCount}`);
  }

  // Gallery
  openLightbox(album: GalleryAlbum) {
    this.lightboxAlbum = album;
  }

  closeLightbox() {
    this.lightboxAlbum = null;
  }

  createFolder() {
    if (!this.newFolderName) return;
    const newAlb: GalleryAlbum = {
      id: Date.now(),
      title: this.newFolderName,
      category: this.newFolderCategory,
      event_date: 'July 2029',
      cover_image_url: 'https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=600&q=80',
      photo_count: 12
    };
    this.albums.unshift(newAlb);
    this.showCreateFolderModal = false;
    this.newFolderName = '';
    this.showToast(`Media album folder "${newAlb.title}" created!`);
  }

  printVoucher() {
    window.print();
  }

  // Mobile Navigation
  toggleMobileMenu() {
    this.mobileMenuOpen = !this.mobileMenuOpen;
  }

  // Financials
  getFilteredTransactions(): FinancialTransaction[] {
    return this.transactions.filter(t => {
      const matchTab = this.financialsTab === 'All' || t.type.toLowerCase() === this.financialsTab.toLowerCase();
      const matchCat = this.financialsCategory === 'All Category' || t.category === this.financialsCategory;
      const matchSearch = !this.financialsSearch || 
        t.event_name.toLowerCase().includes(this.financialsSearch.toLowerCase()) ||
        t.transaction_code.toLowerCase().includes(this.financialsSearch.toLowerCase()) ||
        (t.note && t.note.toLowerCase().includes(this.financialsSearch.toLowerCase())) ||
        t.category.toLowerCase().includes(this.financialsSearch.toLowerCase());
      return matchTab && matchCat && matchSearch;
    });
  }

  getTotalBalance(): number {
    return this.transactions.reduce((acc, t) => acc + t.amount, 0);
  }

  getTotalIncome(): number {
    return this.transactions
      .filter(t => t.type === 'Income')
      .reduce((acc, t) => acc + Math.abs(t.amount), 0);
  }

  getTotalExpense(): number {
    return this.transactions
      .filter(t => t.type === 'Expense')
      .reduce((acc, t) => acc + Math.abs(t.amount), 0);
  }

  addTransaction() {
    if (!this.newTxEventName.trim() || !this.newTxAmount) {
      this.showToast('Please provide event/description and amount.');
      return;
    }
    const finalAmount = this.newTxType === 'Expense' ? -Math.abs(this.newTxAmount) : Math.abs(this.newTxAmount);
    const newTx: FinancialTransaction = {
      id: Date.now(),
      transaction_code: 'TRX-' + Math.floor(1000 + Math.random() * 9000),
      date: 'May 20, 2029 — 04:00 PM',
      event_name: this.newTxEventName,
      type: this.newTxType,
      category: this.newTxCategory,
      amount: finalAmount,
      payment_method: this.newTxMethod,
      note: this.newTxNote || 'Direct entry from accounting console',
      status: 'Completed'
    };

    this.transactions.unshift(newTx);
    this.showAddTransactionModal = false;
    this.newTxEventName = '';
    this.newTxAmount = 2500;
    this.newTxNote = '';
    this.showToast(`Transaction ${newTx.transaction_code} recorded successfully!`);
  }

  exportFinancialsCsv() {
    const headers = ['Transaction ID', 'Event Description', 'Category', 'Date', 'Type', 'Amount', 'Method', 'Status'];
    const rows = this.transactions.map(t => [
      t.transaction_code,
      `"${t.event_name}"`,
      t.category,
      `"${t.date}"`,
      t.type,
      t.amount,
      t.payment_method,
      t.status
    ]);
    const csvContent = 'data:text/csv;charset=utf-8,' + [headers.join(','), ...rows.map(e => e.join(','))].join('\n');
    const encodedUri = encodeURI(csvContent);
    const link = document.createElement('a');
    link.setAttribute('href', encodedUri);
    link.setAttribute('download', 'ventixe_financial_report_2029.csv');
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    this.showToast('Financial statement CSV exported successfully!');
  }
}
