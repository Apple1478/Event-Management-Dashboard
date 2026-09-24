import { Injectable } from '@angular/core';
import { 
  EventItem, BookingItem, InvoiceItem, MessageItem, 
  AgendaItem, ReviewItem, GalleryAlbum, 
  FinancialTransaction, FinancialSummary 
} from '../models/dashboard.models';

@Injectable({
  providedIn: 'root'
})
export class DashboardDataService {
  private apiBase = 'http://127.0.0.1:8000/api/v1';

  async getEvents(): Promise<EventItem[]> {
    try {
      const res = await fetch(`${this.apiBase}/events`);
      if (res.ok) {
        const data = await res.json();
        if (data.events && data.events.length) return data.events;
      }
    } catch (e) {
      console.warn('API fallback for events');
    }

    return [
      {
        id: 1,
        title: 'Echo Beats Festival',
        slug: 'echo-beats-festival',
        category: 'Music',
        status: 'Active',
        banner_image_url: 'https://images.unsplash.com/photo-1470225620780-dba8ba36b745?auto=format&fit=crop&w=800&q=80',
        start_datetime: 'May 20, 2029 — 6:00 PM',
        venue_name: 'Sunset Park, Los Angeles, CA',
        venue_address: '625 S Lafayette Park Pl, Los Angeles, CA 90057',
        total_capacity: 30000,
        tickets_sold: 21000,
        min_price: 60,
        percentage_sold: 70,
        tickets_left: 55,
        about_text: 'The Echo Beats Festival brings together a stellar lineup of artists across EDM, pop, and hip-hop genres. Prepare to experience a night of electrifying music, vibrant light shows, and unforgettable performances under the stars.',
        terms_and_conditions: 'All attendees must possess a valid ticket for entry. Tickets are non-refundable and non-transferable unless specified by the event organizer. Prohibited items include weapons, drugs, alcohol, fireworks, and other hazardous materials.',
        transit_info: {
          by_car: 'Accessible via Wilshire Blvd; limited parking available.',
          by_metro: 'Wilshire/Vermont Station (15-minute walk).',
          by_bus: 'Bus lines 16, 18, and 603 stop near the park.'
        },
        seat_tiers: [
          { id: 1, name: 'Diamond', price: 120 },
          { id: 2, name: 'Platinum', price: 100 },
          { id: 3, name: 'Gold', price: 85 },
          { id: 4, name: 'Silver', price: 70 },
          { id: 5, name: 'Bronze', price: 60 },
          { id: 6, name: 'VIP Lounge', price: 150 }
        ],
        packages: [
          { id: 1, name: 'General Admission Package', price: 50, features: ['Standing', 'Access to Festival Grounds'] },
          { id: 2, name: 'Silver Package', price: 70, features: ['Seating', 'Mid-tier View'] },
          { id: 3, name: 'Gold Package', price: 85, features: ['Seating', 'Prime View'] },
          { id: 4, name: 'Platinum Package', price: 100, features: ['Seating', 'Near Stage'] },
          { id: 5, name: 'VIP Lounge Package', price: 150, features: ['Seating', 'Complimentary Drinks', 'Fast-Track Entry'] },
          { id: 6, name: 'Backstage Access Package', price: 200, features: ['Standing', 'Artist Meet-and-Greet', 'Exclusive Merch'] }
        ],
        merchandise: [
          { id: 1, name: 'Echo Beats Cap', price: 20, image_url: 'https://images.unsplash.com/photo-1588850561407-ed78c282e89b?auto=format&fit=crop&w=300&q=80' },
          { id: 2, name: 'Festival T-Shirt', price: 25, image_url: 'https://images.unsplash.com/photo-1521572267360-ee0c2909d518?auto=format&fit=crop&w=300&q=80' },
          { id: 3, name: 'Light-Up Wristband', price: 15, image_url: 'https://images.unsplash.com/photo-1611591475850-8451bdf858ff?auto=format&fit=crop&w=300&q=80' }
        ]
      },
      {
        id: 2,
        title: 'Adventure Gear Show',
        slug: 'adventure-gear-show',
        category: 'Outdoor & Adventure',
        status: 'Active',
        banner_image_url: 'https://images.unsplash.com/photo-1551632811-561732d1e306?auto=format&fit=crop&w=600&q=80',
        start_datetime: 'June 5, 2029 — 3:00 PM',
        venue_name: 'Rocky Ridge Hall, Denver, CO',
        total_capacity: 1000,
        tickets_sold: 650,
        min_price: 40,
        percentage_sold: 65,
        tickets_left: 115,
        about_text: 'Top outdoor brands showcase the latest gear. Discounts, demos, and expert consultations.'
      },
      {
        id: 3,
        title: 'Culinary Delights Festival',
        slug: 'culinary-delights-festival',
        category: 'Food & Culinary',
        status: 'Active',
        banner_image_url: 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?auto=format&fit=crop&w=600&q=80',
        start_datetime: 'May 25, 2029 — 11:00 AM',
        venue_name: 'The Plaza, San Francisco, CA',
        total_capacity: 1000,
        tickets_sold: 600,
        min_price: 45,
        percentage_sold: 60,
        tickets_left: 120,
        about_text: 'Embark on a culinary adventure! Sample delicious dishes, watch chef demos, and savor diverse cuisine.'
      },
      {
        id: 4,
        title: 'Runway Revolution 2029',
        slug: 'runway-revolution-2029',
        category: 'Fashion',
        status: 'Active',
        banner_image_url: 'https://images.unsplash.com/photo-1509631179647-0177331693ae?auto=format&fit=crop&w=600&q=80',
        start_datetime: 'May 1, 2029 — 8:00 PM',
        venue_name: 'Vogue Hall, New York, NY',
        total_capacity: 1000,
        tickets_sold: 1000,
        min_price: 30,
        percentage_sold: 100,
        tickets_left: 0,
        about_text: 'Celebrate emerging talent at Runway Revolution 2029. Discover the next generation of fashion icons.'
      },
      {
        id: 5,
        title: 'Artistry Unveiled Expo',
        slug: 'artistry-unveiled-expo',
        category: 'Art & Design',
        status: 'Active',
        banner_image_url: 'https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?auto=format&fit=crop&w=600&q=80',
        start_datetime: 'May 15, 2029 — 10:00 AM',
        venue_name: 'Modern Art Gallery, Chicago, IL',
        total_capacity: 1000,
        tickets_sold: 850,
        min_price: 20,
        percentage_sold: 85,
        tickets_left: 20,
        about_text: 'Explore diverse art and design forms. Connect with global artists and discover creative inspiration.'
      },
      {
        id: 6,
        title: 'Tech Future Expo',
        slug: 'tech-future-expo',
        category: 'Technology',
        status: 'Active',
        banner_image_url: 'https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=600&q=80',
        start_datetime: 'June 1, 2029 — 10:00 AM',
        venue_name: 'Silicon Valley, San Jose, CA',
        total_capacity: 1000,
        tickets_sold: 550,
        min_price: 80,
        percentage_sold: 55,
        tickets_left: 85,
        about_text: 'Explore the latest tech innovations here. Discover trends and solutions shaping tomorrow.'
      }
    ];
  }

  async getBookings(): Promise<BookingItem[]> {
    try {
      const res = await fetch(`${this.apiBase}/bookings`);
      if (res.ok) {
        const data = await res.json();
        if (data.bookings && data.bookings.length) return data.bookings;
      }
    } catch (e) {
      console.warn('API fallback for bookings');
    }

    return [
      { id: 1, invoice_id: 'INV10011', date: '2029/02/15 10:30 AM', customer_name: 'Jackson Moore', event_title: 'Symphony Under the Stars', event_category: 'Music', ticket_category: 'Diamond', price: 50, quantity: 2, total_amount: 100, status: 'Confirmed', e_voucher_code: '123456-MUSIC' },
      { id: 2, invoice_id: 'INV10012', date: '2029/02/16 03:45 PM', customer_name: 'Alicia Smithson', event_title: 'Runway Revolution 2024', event_category: 'Fashion', ticket_category: 'Platinum', price: 120, quantity: 1, total_amount: 120, status: 'Pending', e_voucher_code: '-' },
      { id: 3, invoice_id: 'INV10013', date: '2029/02/17 01:15 PM', customer_name: 'Natalie Johnson', event_title: 'Global Wellness Summit', event_category: 'Beauty & Wellness', ticket_category: 'CAT 1', price: 80, quantity: 3, total_amount: 240, status: 'Confirmed', e_voucher_code: '789101-WELLNESS' },
      { id: 4, invoice_id: 'INV10014', date: '2029/02/18 09:00 AM', customer_name: 'Patrick Cooper', event_title: 'Champions League Screening Night', event_category: 'Sport', ticket_category: 'CAT 3', price: 30, quantity: 4, total_amount: 120, status: 'Cancelled', e_voucher_code: '-' },
      { id: 5, invoice_id: 'INV10015', date: '2029/02/18 05:30 PM', customer_name: 'Gilda Ramos', event_title: 'Artistry Unveiled: Modern Art Expo', event_category: 'Art & Design', ticket_category: 'Silver', price: 25, quantity: 2, total_amount: 50, status: 'Confirmed', e_voucher_code: '202324-ART' },
      { id: 6, invoice_id: 'INV10016', date: '2029/02/19 12:00 PM', customer_name: 'Clara Simmons', event_title: 'Tech Future Expo', event_category: 'Technology', ticket_category: 'CAT 2', price: 75, quantity: 2, total_amount: 150, status: 'Confirmed', e_voucher_code: '564738-TECH' },
      { id: 7, invoice_id: 'INV10017', date: '2029/02/20 02:30 PM', customer_name: 'Daniel White', event_title: 'Culinary Delights Festival', event_category: 'Food & Culinary', ticket_category: 'Gold', price: 60, quantity: 1, total_amount: 60, status: 'Cancelled', e_voucher_code: '928374-CULINARY' },
      { id: 8, invoice_id: 'INV10018', date: '2029/02/21 06:00 PM', customer_name: 'Natalie Johnson', event_title: 'Echo Beats Festival', event_category: 'Music', ticket_category: 'Platinum', price: 70, quantity: 3, total_amount: 210, status: 'Pending', e_voucher_code: '-' },
    ];
  }

  async getInvoices(): Promise<InvoiceItem[]> {
    try {
      const res = await fetch(`${this.apiBase}/invoices`);
      if (res.ok) {
        const data = await res.json();
        if (data.invoices && data.invoices.length) return data.invoices;
      }
    } catch (e) {
      console.warn('API fallback for invoices');
    }

    return [
      { id: 1, invoice_number: 'INV10011', date: 'Feb 15, 2029 10:30 AM', customer_name: 'Jackson Moore', amount: 100, status: 'Paid', subtotal: 90, tax: 9, fee: 1, total: 100 },
      { id: 2, invoice_number: 'INV10012', date: 'Feb 16, 2029 03:45 PM', customer_name: 'Alicia Smithson', customer_email: 'alicia.smithson@email.com', amount: 220, status: 'Unpaid', subtotal: 220, tax: 22, fee: 5, total: 247, items: [{ ticket_category: 'Platinum', price: 120, quantity: 1, amount: 120 }, { ticket_category: 'Silver', price: 50, quantity: 2, amount: 100 }] },
      { id: 3, invoice_number: 'INV10013', date: 'Feb 17, 2029 01:15 PM', customer_name: 'Natalie Johnson', amount: 240, status: 'Paid', subtotal: 215, tax: 21.5, fee: 3.5, total: 240 },
      { id: 4, invoice_number: 'INV10015', date: 'Feb 18, 2029 05:30 PM', customer_name: 'Gilda Ramos', amount: 50, status: 'Paid', subtotal: 45, tax: 4.5, fee: 0.5, total: 50 },
      { id: 5, invoice_number: 'INV10016', date: 'Feb 19, 2029 12:00 PM', customer_name: 'Clara Simmons', amount: 150, status: 'Paid', subtotal: 135, tax: 13.5, fee: 1.5, total: 150 },
      { id: 6, invoice_number: 'INV10017', date: 'Feb 20, 2029 02:30 PM', customer_name: 'Daniel White', amount: 60, status: 'Unpaid', subtotal: 55, tax: 5, fee: 0, total: 60 },
      { id: 7, invoice_number: 'INV10018', date: 'Feb 21, 2029 06:00 PM', customer_name: 'Natalie Johnson', amount: 210, status: 'Paid', subtotal: 190, tax: 19, fee: 1, total: 210 },
    ];
  }

  async getMessages(): Promise<MessageItem[]> {
    try {
      const res = await fetch(`${this.apiBase}/inbox/messages`);
      if (res.ok) {
        const data = await res.json();
        if (data.messages && data.messages.length) return data.messages;
      }
    } catch (e) {
      console.warn('API fallback for messages');
    }

    return [
      {
        id: 1,
        sender_name: 'Harmony Audio',
        sender_email: 'support@harmonyaudio.com',
        sender_initials: 'HA',
        label: 'Sponsor',
        folder: 'inbox',
        subject: 'Sound System Confirmation',
        snippet: "We'd like to confirm the delivery schedule for the sound system setup.",
        body_text: "Dear Event Management Team,\n\nWe hope this message finds you well. As the official sound partner for the Rhythm & Beats Music Festival, we are reaching out to confirm the delivery schedule for the sound system setup.\n\nKey discussion items:\n1. Delivery Timing: Preferred delivery date/time at Sunset Park.\n2. Access Requirements: Loading dock passes.\n3. Rehearsals: Soundcheck timeline with the headline artist.\n\nWarm regards,\nHarmony Audio Team",
        is_starred: true,
        is_read: true,
        time_str: '02:30 PM',
        replies: [
          {
            id: 11,
            sender_name: 'Ventixe Organizer',
            sender_email: 'admin@ventixe.com',
            body_text: 'Thank you for reaching out. Loading dock access is confirmed for May 23 at 08:00 AM. Gate passes have been authorized for your fleet.',
            time_str: '03:15 PM'
          }
        ]
      },
      {
        id: 2,
        sender_name: 'Patrick Cooper',
        sender_email: 'patrick@example.com',
        sender_initials: 'PC',
        label: 'Customer',
        folder: 'inbox',
        subject: 'Feedback on Champions League Event',
        snippet: 'The event was great, but the seating arrangements could be improved.',
        body_text: 'Hi Event Team,\n\nThe screening event had fantastic energy. Just wanted to share some feedback regarding the tiered seating on the east wing.\n\nBest,\nPatrick',
        is_starred: false,
        is_read: true,
        time_str: '01:45 PM',
        replies: []
      },
      {
        id: 3,
        sender_name: 'Marcus Rawless',
        sender_email: 'marcus@example.com',
        sender_initials: 'MR',
        label: 'Customer',
        folder: 'inbox',
        subject: 'Request for Invoice Update',
        snippet: 'Could you please update the billing address on my invoice?',
        body_text: 'Hello team,\n\nI need an updated invoice INV10013 reflecting our new registered business address in downtown LA.\n\nThanks,\nMarcus',
        is_starred: false,
        is_read: true,
        time_str: '11:30 AM',
        replies: []
      },
      {
        id: 4,
        sender_name: 'Alicia Smithson',
        sender_email: 'alicia.smithson@email.com',
        sender_initials: 'AS',
        label: 'Customer',
        folder: 'inbox',
        subject: 'Query Regarding Ticket Availability',
        snippet: 'Hi, I would like to confirm if additional Platinum tickets are available.',
        body_text: 'Good morning,\n\nAre any extra Platinum or VIP passes becoming available for Runway Revolution 2029?\n\nWarmly,\nAlicia',
        is_starred: true,
        is_read: true,
        time_str: '10:15 AM',
        replies: []
      },
      {
        id: 5,
        sender_name: 'FreshFlavors Catering',
        sender_email: 'orders@freshflavors.com',
        sender_initials: 'FC',
        label: 'Partner',
        folder: 'inbox',
        subject: 'Final Menu Selection for VIP Lounge',
        snippet: 'Please confirm the final menu selections for the event.',
        body_text: 'Hi Organizers,\n\nAttached is our suggested catering list for the VIP tent. Please confirm your selections by tomorrow so we can finalize supplier orders.\n\nBest,\nFreshFlavors Team',
        is_starred: false,
        is_read: false,
        time_str: 'Yesterday',
        replies: []
      },
      // --- SENT FOLDER ITEMS ---
      {
        id: 101,
        sender_name: 'Ventixe Organizer',
        sender_email: 'admin@ventixe.com',
        sender_initials: 'VO',
        label: 'Partner',
        folder: 'sent',
        subject: 'Confirmed: Loading Dock Schedule for Echo Beats',
        snippet: 'Hi Team, Loading dock access has been officially confirmed for May 23...',
        body_text: 'Dear Harmony Audio and Stage Production Leads,\n\nThis confirms that loading dock gates at Sunset Park will open at 07:00 AM on May 23, 2029. Security passes have been synchronized with your vehicle registration IDs.\n\nBest regards,\nVentixe Operations Team',
        is_starred: false,
        is_read: true,
        time_str: '03:15 PM',
        replies: []
      },
      {
        id: 102,
        sender_name: 'Ventixe Organizer',
        sender_email: 'admin@ventixe.com',
        sender_initials: 'VO',
        label: 'Customer',
        folder: 'sent',
        subject: 'VIP Ticket Upgrade Process & Gate Entry Details',
        snippet: 'Hi Alicia, We have released 5 additional VIP Platinum passes...',
        body_text: 'Dear Alicia,\n\nWe have successfully unlocked 5 additional Platinum Tier passes for the Runway Revolution 2029 gala. You can claim and process payment directly through your account dashboard.\n\nWarm regards,\nVentixe Ticketing Desk',
        is_starred: true,
        is_read: true,
        time_str: 'May 18',
        replies: []
      },
      {
        id: 103,
        sender_name: 'Ventixe Organizer',
        sender_email: 'admin@ventixe.com',
        sender_initials: 'VO',
        label: 'Sponsor',
        folder: 'sent',
        subject: 'Partnership Agreement Countersigned - Red Bull Live',
        snippet: 'Enclosed is the signed sponsorship agreement for the summer festival season...',
        body_text: 'Hi Brand Partnerships Team,\n\nAttached is our signed copy of the 2029 Mainstage Sponsorship Agreement. We look forward to executing a memorable festival activation.\n\nWarmly,\nExecutive Director',
        is_starred: false,
        is_read: true,
        time_str: 'May 14',
        replies: []
      },
      // --- DRAFTS FOLDER ITEMS ---
      {
        id: 201,
        sender_name: 'Draft (You)',
        sender_email: 'admin@ventixe.com',
        sender_initials: 'DR',
        label: 'Partner',
        folder: 'drafts',
        subject: '[Draft] Press Release: International Headliners Lineup',
        snippet: 'Draft announcement regarding the international EDM and Jazz artists lineup...',
        body_text: 'Official Press Release - For Immediate Release\n\nVentixe Entertainment is thrilled to announce the global artist roster for the upcoming 2029 season...\n\n[Pending Final Legal Review]',
        is_starred: false,
        is_read: true,
        time_str: 'Draft',
        replies: []
      },
      {
        id: 202,
        sender_name: 'Draft (You)',
        sender_email: 'admin@ventixe.com',
        sender_initials: 'DR',
        label: 'Sponsor',
        folder: 'drafts',
        subject: '[Draft] Q3 VIP Lounge Beverage Sponsorship Proposal',
        snippet: 'Proposal deck draft for premium mixology beverage partners...',
        body_text: 'Hi Sponsors,\n\nWe would love to invite your brand as the title lounge sponsor for our high-profile executive networking summit.\n\n[Attach deck before sending]',
        is_starred: false,
        is_read: true,
        time_str: 'Draft',
        replies: []
      },
      // --- TRASH FOLDER ITEMS ---
      {
        id: 301,
        sender_name: 'Event Tech Weekly',
        sender_email: 'no-reply@eventnews.io',
        sender_initials: 'ET',
        label: 'Partner',
        folder: 'trash',
        subject: 'Weekly Audio/Visual Rigging Trends for 2029',
        snippet: 'Discover the latest wireless lighting and laser rigging protocols...',
        body_text: 'Check out the new trends in stage lighting, digital audio mixers, and sustainable power generators for large outdoor arenas.',
        is_starred: false,
        is_read: true,
        time_str: 'May 04',
        replies: []
      }
    ];
  }

  async getAgendas(): Promise<AgendaItem[]> {
    return [
      {
        id: 1,
        day: 23,
        month_year: 'May 2029',
        title: 'Echo Beats Festival Main Performance',
        category: 'Event',
        datetime: 'May 23, 2029 — 09:00 AM to 08:30 PM',
        location: 'Sunset Park, Los Angeles, CA',
        pic_name: 'Michael Taylor',
        pic_role: 'Event Coordinator',
        pic_phone: '+1-800-555-7890',
        pic_email: 'michael.taylor@eventmgmt.com',
        notes: [
          'Headline performance of the Echo Beats Festival featuring international guest artists.',
          'Technical team ready for sound/lighting checks by 01:30 PM.',
          'VIP seating and catering arrangements finalized by 03:00 PM.'
        ],
        slots: [
          { time: '09:00 AM - 10:30 AM', title: 'Gates Open & Attendee Registration', stage: 'Entrance Gate A & B', speaker: 'Logistics Desk', status: 'Completed' },
          { time: '10:30 AM - 12:00 PM', title: 'Opening Acts & Indie Electronic Showcase', stage: 'Acoustic Dome', speaker: 'DJ Solar & Friends', status: 'Completed' },
          { time: '12:00 PM - 01:30 PM', title: 'Networking Lunch & VIP Chef Experience', stage: 'VIP Pavilion', speaker: 'Executive Chef Marco', status: 'Completed' },
          { time: '01:30 PM - 03:30 PM', title: 'Echo Beats Headline Soundcheck & Rehearsal', stage: 'Main Stage', speaker: 'Sound Engineer Alex', status: 'In Progress' },
          { time: '04:00 PM - 06:30 PM', title: 'Live Performance — Echo Beats Extravaganza', stage: 'Main Stage', speaker: 'Echo Beats Collective', status: 'Upcoming' },
          { time: '07:00 PM - 08:30 PM', title: 'Afterparty, Artist Meet & Press Briefing', stage: 'Lounge West', speaker: 'Festival Directors', status: 'Upcoming' }
        ]
      },
      {
        id: 2,
        day: 1,
        month_year: 'May 2029',
        title: 'Team Brainstorming & Festival Kickoff',
        category: 'Meeting',
        datetime: 'May 1, 2029 — 09:00 AM to 04:00 PM',
        location: 'HQ Boardroom A / Hybrid Zoom',
        pic_name: 'Sarah Connor',
        pic_role: 'Lead Planner',
        pic_phone: '+1-800-555-4321',
        pic_email: 'sarah.c@eventmgmt.com',
        notes: [
          'Review Q2 multi-channel marketing campaigns and ticket milestone targets.',
          'Coordinate artist transportation protocols and hotel hospitality suites.'
        ],
        slots: [
          { time: '09:00 AM - 10:30 AM', title: 'Campaign Analytics & Sales Review', stage: 'Boardroom A', speaker: 'Marketing Team', status: 'Completed' },
          { time: '11:00 AM - 12:30 PM', title: 'Artist Hospitality & Rider Approvals', stage: 'Boardroom A', speaker: 'Talent Lead', status: 'Completed' },
          { time: '02:00 PM - 04:00 PM', title: 'Security & Medical Emergency Plan Signoff', stage: 'Conference Hall', speaker: 'City Services Liaison', status: 'Completed' }
        ]
      },
      {
        id: 3,
        day: 15,
        month_year: 'May 2029',
        title: 'Symphony Under the Stars Stage Setup',
        category: 'Setup & Rehearsal',
        datetime: 'May 15, 2029 — 08:00 AM to 05:00 PM',
        location: 'Sunset Park Amphitheater',
        pic_name: 'David Vance',
        pic_role: 'Technical Director',
        pic_phone: '+1-800-555-9876',
        pic_email: 'david.v@eventmgmt.com',
        notes: [
          'Acoustic riser installation, LED screen rigging, and orchestra pit checks.',
          'Live broadcast microwave links test with national streaming partner.'
        ],
        slots: [
          { time: '08:00 AM - 11:00 AM', title: 'Stage Construction & Riser Assembly', stage: 'Amphitheater Pit', speaker: 'Rigging Crew Lead', status: 'Completed' },
          { time: '11:30 AM - 02:00 PM', title: 'Audio System Tuning & Acoustic Profiling', stage: 'Main Rake', speaker: 'Sound Master', status: 'Completed' },
          { time: '02:30 PM - 05:00 PM', title: 'Full Orchestra Lighting & Camera Rehearsal', stage: 'Main Stage', speaker: 'Conductor & Video Dir', status: 'Upcoming' }
        ]
      },
      {
        id: 4,
        day: 28,
        month_year: 'May 2029',
        title: 'Post-Festival Wrap-up & Vendor Settlement',
        category: 'Finance',
        datetime: 'May 28, 2029 — 10:00 AM to 03:00 PM',
        location: 'Operations Center',
        pic_name: 'Michael Taylor',
        pic_role: 'Event Coordinator',
        pic_phone: '+1-800-555-7890',
        pic_email: 'michael.taylor@eventmgmt.com',
        notes: [
          'Inventory reconciliation of ticket merchandise and bar concessions.',
          'Vendor security deposit releases and feedback gathering.'
        ],
        slots: [
          { time: '10:00 AM - 11:30 AM', title: 'Merchandise Inventory Audit', stage: 'Warehouse B', speaker: 'Merch Manager', status: 'Upcoming' },
          { time: '12:00 PM - 01:30 PM', title: 'Vendor Settlement Meetings', stage: 'Finance Room', speaker: 'CFO / Accounting', status: 'Upcoming' },
          { time: '02:00 PM - 03:00 PM', title: 'Executive Retrospective & Debrief', stage: 'Boardroom A', speaker: 'All Department Heads', status: 'Upcoming' }
        ]
      }
    ];
  }

  async getReviews(): Promise<ReviewItem[]> {
    return [
      {
        id: 1,
        customer_name: 'Jackson Moore',
        customer_avatar: 'https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?auto=format&fit=crop&w=150&q=80',
        rating: 5,
        date: 'April 22, 2029',
        event_title: 'Echo Beats Festival',
        event_category: 'Music',
        comment: 'An absolutely amazing festival! The lineup of artists was incredible, and the sound quality was impeccable. The energy from the crowd made it a night to remember.'
      },
      {
        id: 2,
        customer_name: 'Alicia Smithson',
        customer_avatar: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=150&q=80',
        rating: 4,
        date: 'May 2, 2029',
        event_title: 'Runway Revolution 2029',
        event_category: 'Fashion',
        comment: 'Beautiful designs and a well-organized event overall. The models and lighting were captivating, but seating arrangements could be planned better for the audience.'
      },
      {
        id: 3,
        customer_name: 'Patrick Cooper',
        customer_avatar: 'https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?auto=format&fit=crop&w=150&q=80',
        rating: 5,
        date: 'April 20, 2029',
        event_title: 'Symphony Under the Stars',
        event_category: 'Music',
        comment: 'The music under the open sky was breathtaking. The orchestra was phenomenal, and the ambiance made it feel like a dream. Everything was organized beautifully.'
      },
      {
        id: 4,
        customer_name: 'Clara Simmons',
        customer_avatar: 'https://images.unsplash.com/photo-1580489944761-15a19d654956?auto=format&fit=crop&w=150&q=80',
        rating: 4.5,
        date: 'May 25, 2029',
        event_title: 'Culinary Delights Festival',
        event_category: 'Food & Culinary',
        comment: 'The variety of cuisines and food stalls was fantastic! The flavors were outstanding, though some popular stalls ran out of food early in the event.'
      },
      {
        id: 5,
        customer_name: 'Natalie Johnson',
        customer_avatar: 'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?auto=format&fit=crop&w=150&q=80',
        rating: 5,
        date: 'May 15, 2029',
        event_title: 'Artistry Unveiled Expo',
        event_category: 'Art & Design',
        comment: 'The expo was a treat for art lovers! The installations were awe-inspiring, and meeting the artists was a highlight for me.'
      },
      {
        id: 6,
        customer_name: 'Henry Carter',
        customer_avatar: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=150&q=80',
        rating: 4.2,
        date: 'June 1, 2029',
        event_title: 'Tech Future Expo',
        event_category: 'Technology',
        comment: 'A fantastic platform for tech enthusiasts to explore the latest innovations. More hands-on workshops would have made the event even better.'
      }
    ];
  }

  async getAlbums(): Promise<GalleryAlbum[]> {
    return [
      { id: 1, title: 'Echo Beats Festival', category: 'Music', event_date: 'May 20, 2029', cover_image_url: 'https://images.unsplash.com/photo-1470225620780-dba8ba36b745?auto=format&fit=crop&w=600&q=80', photo_count: 36 },
      { id: 2, title: 'Culinary Delights Festival', category: 'Food & Culinary', event_date: 'May 25, 2029', cover_image_url: 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?auto=format&fit=crop&w=600&q=80', photo_count: 42 },
      { id: 3, title: 'Artistry Unveiled Expo', category: 'Art & Design', event_date: 'May 15, 2029', cover_image_url: 'https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?auto=format&fit=crop&w=600&q=80', photo_count: 28 },
      { id: 4, title: 'Tech Future Expo', category: 'Technology', event_date: 'June 1, 2029', cover_image_url: 'https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=600&q=80', photo_count: 50 },
      { id: 5, title: 'Runway Revolution 2029', category: 'Fashion', event_date: 'May 1, 2029', cover_image_url: 'https://images.unsplash.com/photo-1509631179647-0177331693ae?auto=format&fit=crop&w=600&q=80', photo_count: 64 },
      { id: 6, title: 'Global Wellness Summit', category: 'Health & Wellness', event_date: 'May 5, 2029', cover_image_url: 'https://images.unsplash.com/photo-1545205597-3d9d02c29597?auto=format&fit=crop&w=600&q=80', photo_count: 19 },
      { id: 7, title: 'Adventure Gear Show', category: 'Outdoor & Adventure', event_date: 'June 5, 2029', cover_image_url: 'https://images.unsplash.com/photo-1551632811-561732d1e306?auto=format&fit=crop&w=600&q=80', photo_count: 31 },
      { id: 8, title: 'Symphony Under the Stars', category: 'Music', event_date: 'April 20, 2029', cover_image_url: 'https://images.unsplash.com/photo-1465847899084-d164df4dedc6?auto=format&fit=crop&w=600&q=80', photo_count: 45 },
      { id: 9, title: 'Harmony Health Fair', category: 'Health & Wellness', event_date: 'June 15, 2029', cover_image_url: 'https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&w=600&q=80', photo_count: 22 },
      { id: 10, title: 'Live Paint Battle', category: 'Art & Design', event_date: 'June 20, 2029', cover_image_url: 'https://images.unsplash.com/photo-1513364776144-60967b0f800f?auto=format&fit=crop&w=600&q=80', photo_count: 38 },
      { id: 11, title: 'Spring Trends Runway', category: 'Fashion', event_date: 'June 10, 2029', cover_image_url: 'https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?auto=format&fit=crop&w=600&q=80', photo_count: 52 },
      { id: 12, title: 'Champions League Final Viewing Party', category: 'Sports', event_date: 'May 10, 2029', cover_image_url: 'https://images.unsplash.com/photo-1508098682722-e99c43a406b2?auto=format&fit=crop&w=600&q=80', photo_count: 60 }
    ];
  }

  async getFinancialSummary(): Promise<FinancialSummary> {
    return {
      total_balance: 104000.00,
      total_income: 177500.00,
      total_expense: 73500.00,
      operating_margin: 58.6,
      balance_change_pct: 3.65,
      income_change_pct: 2.08,
      expense_change_pct: -0.84
    };
  }

  async getFinancialTransactions(): Promise<FinancialTransaction[]> {
    return [
      {
        id: 1,
        transaction_code: 'TRX-9481',
        date: 'May 18, 2029 — 02:30 PM',
        event_name: 'Echo Beats Festival',
        type: 'Income',
        category: 'Ticket Sales',
        amount: 24500.00,
        payment_method: 'Stripe Gateway',
        note: 'Tier 1 & VIP ticket batch payout',
        status: 'Completed'
      },
      {
        id: 2,
        transaction_code: 'TRX-9480',
        date: 'May 17, 2029 — 11:15 AM',
        event_name: 'Sunset Park Stage Rigging',
        type: 'Expense',
        category: 'Vendor Payout',
        amount: -8200.00,
        payment_method: 'Wire Transfer',
        note: 'Amphitheater trussing & rigging load-in',
        status: 'Completed'
      },
      {
        id: 3,
        transaction_code: 'TRX-9479',
        date: 'May 16, 2029 — 04:45 PM',
        event_name: 'Harmony Audio Sponsorship',
        type: 'Income',
        category: 'Sponsorship',
        amount: 15000.00,
        payment_method: 'Direct Deposit',
        note: 'Headline sponsor tier activation',
        status: 'Completed'
      },
      {
        id: 4,
        transaction_code: 'TRX-9478',
        date: 'May 15, 2029 — 09:00 AM',
        event_name: 'City Park Permit & Security Bond',
        type: 'Expense',
        category: 'Operations',
        amount: -4500.00,
        payment_method: 'City ACH',
        note: 'Municipal park sound and staging permit',
        status: 'Completed'
      },
      {
        id: 5,
        transaction_code: 'TRX-9477',
        date: 'May 14, 2029 — 06:10 PM',
        event_name: 'Official Festival Merchandise',
        type: 'Income',
        category: 'Merchandise',
        amount: 6850.00,
        payment_method: 'Square POS',
        note: 'Early bird hoodie & cap pre-orders',
        status: 'Completed'
      },
      {
        id: 6,
        transaction_code: 'TRX-9476',
        date: 'May 13, 2029 — 01:20 PM',
        event_name: 'FreshFlavors Catering Deposit',
        type: 'Expense',
        category: 'Vendor Payout',
        amount: -5500.00,
        payment_method: 'Wire Transfer',
        note: 'VIP Lounge culinary catering retainer',
        status: 'Pending'
      },
      {
        id: 7,
        transaction_code: 'TRX-9475',
        date: 'May 12, 2029 — 10:30 AM',
        event_name: 'Social Media & Billboard Ad Spend',
        type: 'Expense',
        category: 'Marketing',
        amount: -3400.00,
        payment_method: 'Corporate Visa',
        note: 'Instagram & TikTok targeted geo campaign',
        status: 'Completed'
      },
      {
        id: 8,
        transaction_code: 'TRX-9474',
        date: 'May 10, 2029 — 03:00 PM',
        event_name: 'Runway Revolution Corporate Table',
        type: 'Income',
        category: 'Ticket Sales',
        amount: 18000.00,
        payment_method: 'Wire Transfer',
        note: 'Table booking x3 for Vogue Beverly Hills',
        status: 'Completed'
      }
    ];
  }
}
