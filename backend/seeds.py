import datetime
try:
    from backend.database import SessionLocal, engine, Base
    from backend.models import (
        User, Event, EventSeatTier, EventPackage, EventMerchandise,
        Booking, Invoice, InvoiceItem, Message, AgendaItem,
        FinancialTransaction, FeedbackReview, ActivityAuditLog, GalleryAlbum
    )
except ImportError:
    from database import SessionLocal, engine, Base
    from models import (
        User, Event, EventSeatTier, EventPackage, EventMerchandise,
        Booking, Invoice, InvoiceItem, Message, AgendaItem,
        FinancialTransaction, FeedbackReview, ActivityAuditLog, GalleryAlbum
    )

def run_seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    # Clear existing
    db.query(InvoiceItem).delete()
    db.query(Invoice).delete()
    db.query(Booking).delete()
    db.query(EventMerchandise).delete()
    db.query(EventPackage).delete()
    db.query(EventSeatTier).delete()
    db.query(AgendaItem).delete()
    db.query(FeedbackReview).delete()
    db.query(FinancialTransaction).delete()
    db.query(ActivityAuditLog).delete()
    db.query(GalleryAlbum).delete()
    db.query(Message).delete()
    db.query(Event).delete()
    db.query(User).delete()
    db.commit()

    # 1. Admin User
    admin = User(
        full_name="Orlando Laurentius",
        email="orlando.laurentius@ventixe.com",
        role="Admin",
        avatar_url="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=200&q=80",
        is_active=True
    )
    db.add(admin)
    db.commit()

    # 2. Events
    event1 = Event(
        title="Echo Beats Festival",
        slug="echo-beats-festival",
        category="Music",
        status="Active",
        banner_image_url="https://images.unsplash.com/photo-1470225620780-dba8ba36b745?auto=format&fit=crop&w=1200&q=80",
        start_datetime=datetime.datetime(2029, 5, 20, 18, 0),
        end_datetime=datetime.datetime(2029, 5, 20, 23, 0),
        venue_name="Sunset Park, Los Angeles, CA",
        venue_address="625 S Lafayette Park Pl, Los Angeles, CA 90057",
        geo_lat=34.0625,
        geo_lng=-118.2838,
        transit_info={
            "by_car": "Accessible via Wilshire Blvd; limited parking available.",
            "by_metro": "Wilshire/Vermont Station (15-minute walk).",
            "by_bus": "Bus lines 16, 18, and 603 stop near the park."
        },
        about_text="The Echo Beats Festival brings together a stellar lineup of artists across EDM, pop, and hip-hop genres. Prepare to experience a night of electrifying music, vibrant light shows, and unforgettable performances under the stars. Explore food trucks, art installations, and VIP lounges for an elevated experience.",
        terms_and_conditions="All attendees must possess a valid ticket for entry. Tickets are non-refundable and non-transferable unless specified by the event organizer. Prohibited items include weapons, drugs, alcohol, fireworks, and other hazardous materials. Any disruptive behavior will result in immediate removal from the event without refund.",
        total_capacity=30000,
        tickets_sold=21000,
        min_price=60.0
    )

    event2 = Event(
        title="Adventure Gear Show",
        slug="adventure-gear-show",
        category="Outdoor & Adventure",
        status="Active",
        banner_image_url="https://images.unsplash.com/photo-1551632811-561732d1e306?auto=format&fit=crop&w=1200&q=80",
        start_datetime=datetime.datetime(2029, 6, 5, 15, 0),
        end_datetime=datetime.datetime(2029, 6, 5, 20, 0),
        venue_name="Rocky Ridge Hall, Denver, CO",
        venue_address="1000 Chopper Cir, Denver, CO 80204",
        about_text="Top outdoor brands showcase the latest gear. Discounts, live demos, and expert consultations.",
        total_capacity=1000,
        tickets_sold=650,
        min_price=40.0
    )

    event3 = Event(
        title="Culinary Delights Festival",
        slug="culinary-delights-festival",
        category="Food & Culinary",
        status="Active",
        banner_image_url="https://images.unsplash.com/photo-1555939594-58d7cb561ad1?auto=format&fit=crop&w=1200&q=80",
        start_datetime=datetime.datetime(2029, 5, 25, 11, 0),
        venue_name="The Plaza, San Francisco, CA",
        about_text="Embark on a culinary adventure! Sample delicious dishes, watch chef demos, and savor diverse cuisine.",
        total_capacity=1000,
        tickets_sold=600,
        min_price=45.0
    )

    event4 = Event(
        title="Runway Revolution 2029",
        slug="runway-revolution-2029",
        category="Fashion",
        status="Active",
        banner_image_url="https://images.unsplash.com/photo-1509631179647-0177331693ae?auto=format&fit=crop&w=1200&q=80",
        start_datetime=datetime.datetime(2029, 5, 1, 20, 0),
        venue_name="Vogue Hall, New York, NY",
        about_text="Celebrate emerging talent at Runway Revolution 2029. Discover the next generation of fashion icons.",
        total_capacity=1000,
        tickets_sold=1000,
        min_price=30.0
    )

    event5 = Event(
        title="Artistry Unveiled Expo",
        slug="artistry-unveiled-expo",
        category="Art & Design",
        status="Active",
        banner_image_url="https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?auto=format&fit=crop&w=1200&q=80",
        start_datetime=datetime.datetime(2029, 5, 15, 10, 0),
        venue_name="Modern Art Gallery, Chicago, IL",
        about_text="Explore diverse art and design forms. Connect with global artists and discover creative inspiration.",
        total_capacity=1000,
        tickets_sold=850,
        min_price=20.0
    )

    event6 = Event(
        title="Tech Future Expo",
        slug="tech-future-expo",
        category="Technology",
        status="Active",
        banner_image_url="https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1200&q=80",
        start_datetime=datetime.datetime(2029, 6, 1, 10, 0),
        venue_name="Silicon Valley, San Jose, CA",
        about_text="Explore the latest tech innovations here. Discover trends and solutions shaping tomorrow.",
        total_capacity=1000,
        tickets_sold=550,
        min_price=80.0
    )

    event7 = Event(
        title="Symphony Under the Stars",
        slug="symphony-under-the-stars",
        category="Music",
        status="Active",
        banner_image_url="https://images.unsplash.com/photo-1465847899084-d164df4dedc6?auto=format&fit=crop&w=1200&q=80",
        start_datetime=datetime.datetime(2029, 4, 20, 19, 0),
        venue_name="Sunset Park, Los Angeles, CA",
        about_text="Experience an enchanting evening of classical masterpieces performed by the Los Angeles Philharmonic.",
        total_capacity=1500,
        tickets_sold=1125,
        min_price=50.0
    )

    event8 = Event(
        title="Global Wellness Summit",
        slug="global-wellness-summit",
        category="Health & Wellness",
        status="Active",
        banner_image_url="https://images.unsplash.com/photo-1545205597-3d9d02c29597?auto=format&fit=crop&w=1200&q=80",
        start_datetime=datetime.datetime(2029, 5, 5, 9, 0),
        venue_name="Wellness Arena, Miami, FL",
        about_text="Connect with thought leaders and pioneers in health, mindfulness, fitness, and holistic wellbeing.",
        total_capacity=2000,
        tickets_sold=800,
        min_price=75.0
    )

    db.add_all([event1, event2, event3, event4, event5, event6, event7, event8])
    db.commit()

    # Seat tiers for Echo Beats Festival
    tiers = [
        EventSeatTier(event_id=event1.id, name="Diamond", tier_type="Seated", price=120.0, capacity=2000, booked_count=1800, benefits=["Front-Row View", "Complimentary Lounge Access"]),
        EventSeatTier(event_id=event1.id, name="Platinum", tier_type="Seated", price=100.0, capacity=3500, booked_count=2900, benefits=["Near Stage", "Priority Entry"]),
        EventSeatTier(event_id=event1.id, name="Gold", tier_type="Seated", price=85.0, capacity=5000, booked_count=4200, benefits=["Prime View", "Fast-track Security"]),
        EventSeatTier(event_id=event1.id, name="Silver", tier_type="Seated", price=70.0, capacity=6000, booked_count=4800, benefits=["Mid-tier View"]),
        EventSeatTier(event_id=event1.id, name="Bronze", tier_type="Seated", price=60.0, capacity=6500, booked_count=4500, benefits=["Standard Seating"]),
        EventSeatTier(event_id=event1.id, name="General Admission", tier_type="Standing", price=50.0, capacity=5000, booked_count=3200, benefits=["Access to Festival Grounds"]),
        EventSeatTier(event_id=event1.id, name="Backstage Access", tier_type="Standing", price=200.0, capacity=500, booked_count=450, benefits=["Artist Meet-and-Greet", "Exclusive Merch"]),
        EventSeatTier(event_id=event1.id, name="VIP Lounge", tier_type="Seated", price=150.0, capacity=1500, booked_count=1300, benefits=["Premium Seating", "Complimentary Drinks", "Fast-track Entry"])
    ]
    db.add_all(tiers)

    # Packages for Echo Beats Festival
    packages = [
        EventPackage(event_id=event1.id, name="General Admission Package", type_label="Standing", price=50.0, features=["Standing", "Access to Festival Grounds"]),
        EventPackage(event_id=event1.id, name="Silver Package", type_label="Seating", price=70.0, features=["Seating", "Mid-tier View"]),
        EventPackage(event_id=event1.id, name="Gold Package", type_label="Seating", price=85.0, features=["Seating", "Prime View"]),
        EventPackage(event_id=event1.id, name="Platinum Package", type_label="Seating", price=100.0, features=["Seating", "Near Stage"]),
        EventPackage(event_id=event1.id, name="Diamond Package", type_label="Seating", price=120.0, features=["Seating", "Front-Row View"]),
        EventPackage(event_id=event1.id, name="VIP Lounge Package", type_label="Seating", price=150.0, features=["Seating", "Exclusive Lounge", "Free Drinks"]),
        EventPackage(event_id=event1.id, name="Artist Meet-and-Greet Package", type_label="Standing", price=180.0, features=["Standing", "Backstage Access", "Artist Photo"]),
        EventPackage(event_id=event1.id, name="Ultimate Access Package", type_label="Standing", price=200.0, features=["Standing", "All-Inclusive Benefits", "VIP Gift Bag"])
    ]
    db.add_all(packages)

    # Merchandise
    merch = [
        EventMerchandise(event_id=event1.id, name="Echo Beats Cap", price=20.0, image_url="https://images.unsplash.com/photo-1588850561407-ed78c282e89b?auto=format&fit=crop&w=400&q=80", stock_quantity=150),
        EventMerchandise(event_id=event1.id, name="Festival T-Shirt", price=25.0, image_url="https://images.unsplash.com/photo-1521572267360-ee0c2909d518?auto=format&fit=crop&w=400&q=80", stock_quantity=200),
        EventMerchandise(event_id=event1.id, name="Light-Up Wristband", price=15.0, image_url="https://images.unsplash.com/photo-1611591475850-8451bdf858ff?auto=format&fit=crop&w=400&q=80", stock_quantity=500)
    ]
    db.add_all(merch)
    db.commit()

    # 3. Bookings & Invoices
    booking_specs = [
        ("INV10011", event7.id, "Jackson Moore", "jackson@example.com", "Diamond", 50.0, 2, 100.0, "Confirmed", "123456-MUSIC", datetime.datetime(2029, 2, 15, 10, 30)),
        ("INV10012", event4.id, "Alicia Smithson", "alicia.smithson@email.com", "Platinum", 120.0, 1, 120.0, "Unpaid", None, datetime.datetime(2029, 2, 16, 15, 45)),
        ("INV10013", event8.id, "Natalie Johnson", "natalie@example.com", "CAT 1", 80.0, 3, 240.0, "Confirmed", "789101-WELLNESS", datetime.datetime(2029, 2, 17, 13, 15)),
        ("INV10014", event2.id, "Patrick Cooper", "patrick@example.com", "CAT 3", 30.0, 4, 120.0, "Cancelled", None, datetime.datetime(2029, 2, 18, 9, 0)),
        ("INV10015", event5.id, "Gilda Ramos", "gilda@example.com", "Silver", 25.0, 2, 50.0, "Confirmed", "202324-ART", datetime.datetime(2029, 2, 18, 17, 30)),
        ("INV10016", event6.id, "Clara Simmons", "clara@example.com", "CAT 2", 75.0, 2, 150.0, "Confirmed", "564738-TECH", datetime.datetime(2029, 2, 19, 12, 0)),
        ("INV10017", event3.id, "Daniel White", "daniel@example.com", "Gold", 60.0, 1, 60.0, "Unpaid", "928374-CULINARY", datetime.datetime(2029, 2, 20, 14, 30)),
        ("INV10018", event1.id, "Natalie Johnson", "natalie@example.com", "Platinum", 70.0, 3, 210.0, "Confirmed", None, datetime.datetime(2029, 2, 21, 18, 0)),
    ]

    for inv_num, ev_id, c_name, c_email, cat, price, qty, total, status, voucher, b_date in booking_specs:
        b = Booking(
            invoice_id_str=inv_num,
            event_id=ev_id,
            customer_name=c_name,
            customer_email=c_email,
            customer_phone="+1-310-555-6789",
            customer_address="789 Main Street, Beverly Hills, CA, 90210",
            ticket_category=cat,
            price=price,
            quantity=qty,
            total_amount=total,
            status="Confirmed" if status == "Paid" else status,
            e_voucher_code=voucher or f"VCH-{inv_num}",
            seat_number="B12",
            gate_number="3",
            booking_date=b_date
        )
        db.add(b)
        db.flush()

        inv = Invoice(
            invoice_number=inv_num,
            booking_id=b.id,
            bill_from_name="Event Management Co.",
            bill_from_address="123 Sunset Avenue, Los Angeles, CA, 90001",
            bill_from_email="billing@eventmgmt.com",
            bill_from_phone="+1-800-555-1234",
            bill_to_name=c_name,
            bill_to_address="789 Main Street, Beverly Hills, CA, 90210",
            bill_to_email=c_email,
            bill_to_phone="+1-310-555-6789",
            issued_date=b_date,
            due_date=b_date + datetime.timedelta(days=4),
            status="Unpaid" if inv_num in ["INV10012", "INV10017"] else "Paid",
            subtotal=total,
            tax_rate=0.10,
            tax_amount=round(total * 0.10, 2),
            fee_amount=5.0,
            total_amount=round(total + (total * 0.10) + 5.0, 2),
            notes="Please make payment before the due date to avoid cancellation. For questions, contact support@eventmgmt.com"
        )
        db.add(inv)
        db.flush()

        item = InvoiceItem(
            invoice_id=inv.id,
            ticket_category=cat,
            unit_price=price,
            quantity=qty,
            amount=total
        )
        db.add(item)

    db.commit()

    # 4. Messages (Inbox)
    msgs = [
        Message(
            sender_name="Harmony Audio",
            sender_email="support@harmonyaudio.com",
            sender_initials="HA",
            label="Sponsor",
            folder="inbox",
            subject="Sound System Confirmation",
            snippet="We'd like to confirm the delivery schedule for the sound system setup.",
            body_text="Dear Event Management Team,\n\nWe hope this message finds you well. As the official sound partner for the Rhythm & Beats Music Festival, we are reaching out to confirm the delivery schedule for the sound system setup.\n\nHere are a few key points we'd like to discuss:\n1. Delivery Timing: Please confirm preferred date and time for our team to deliver equipment to Sunset Park.\n2. Access Requirements: Loading dock availability and on-site contacts.\n3. Setup Specifications: Stage layout requirements.\n4. Testing and Rehearsal: Sound testing schedule.\n\nWarm regards,\nHarmony Audio Team",
            is_starred=True,
            is_read=False,
            timestamp=datetime.datetime(2029, 2, 20, 14, 30)
        ),
        Message(
            sender_name="Patrick Cooper",
            sender_email="patrick.cooper@example.com",
            sender_initials="PC",
            label="Customer",
            folder="inbox",
            subject="Feedback on Champions League Event",
            snippet="The event was great, but the seating arrangements could be improved.",
            body_text="Hi team,\n\nOverall the event atmosphere was electric. However, the seating near block C had somewhat obstructed views. Would appreciate if you could keep this in mind for future screenings.\n\nThanks,\nPatrick",
            is_starred=False,
            is_read=True,
            timestamp=datetime.datetime(2029, 2, 20, 13, 45)
        ),
        Message(
            sender_name="Marcus Rawless",
            sender_email="marcus@example.com",
            sender_initials="MR",
            label="Customer",
            folder="inbox",
            subject="Request for Invoice Update",
            snippet="Could you please update the billing address on my invoice?",
            body_text="Hello,\n\nI recently booked 3 tickets under Invoice INV10013 and need to update our corporate company address for tax filing purposes.\n\nBest,\nMarcus",
            is_starred=False,
            is_read=True,
            timestamp=datetime.datetime(2029, 2, 20, 11, 30)
        ),
        Message(
            sender_name="Alicia Smithson",
            sender_email="alicia.smithson@email.com",
            sender_initials="AS",
            label="Customer",
            folder="inbox",
            subject="Query Regarding Ticket Availability",
            snippet="Hi, I'd like to confirm if additional Platinum tickets are available for the event.",
            body_text="Good morning,\n\nAre there any additional Platinum passes opening up for Runway Revolution? A couple colleagues would love to join.\n\nCheers,\nAlicia",
            is_starred=True,
            is_read=True,
            timestamp=datetime.datetime(2029, 2, 20, 10, 15)
        ),
        Message(
            sender_name="FreshFlavors Catering",
            sender_email="orders@freshflavors.com",
            sender_initials="FC",
            label="Partner",
            folder="inbox",
            subject="Final Menu Selection",
            snippet="Please confirm the final menu selections for the event.",
            body_text="Dear Organizer,\n\nPlease find attached our proposed catering lineup for VIP Lounge guests at Echo Beats Festival. Let us know your preferred final menu by Friday.\n\nBest regards,\nFreshFlavors Team",
            is_starred=False,
            is_read=False,
            timestamp=datetime.datetime(2029, 2, 18, 9, 0)
        )
    ]
    db.add_all(msgs)

    # 5. Calendar Agendas
    agendas = [
        AgendaItem(
            event_id=event1.id,
            title="Echo Beats Festival Main Performance",
            category="Event",
            start_datetime=datetime.datetime(2029, 5, 24, 19, 0),
            end_datetime=datetime.datetime(2029, 5, 24, 23, 0),
            pic_name="Michael Taylor",
            pic_role="Event Coordinator",
            pic_phone="+1-800-555-7890",
            pic_email="michael.taylor@eventmgmt.com",
            assigned_team=[
                {"name": "Sarah Connor", "role": "Lighting"},
                {"name": "David Wu", "role": "Sound Engineer"},
                {"name": "Elena Rostova", "role": "Stage Manager"}
            ],
            notes="This is the headline performance of the Echo Beats Festival, featuring top artists. Ensure technical team is ready for sound and lighting checks by 5:00 PM. VIP seating finalized by 6:30 PM."
        ),
        AgendaItem(
            title="Team Brainstorming for Marketing",
            category="Meeting",
            start_datetime=datetime.datetime(2029, 5, 1, 15, 0),
            pic_name="Michael Taylor",
            notes="Review Q2 social media blitz and influencer engagements."
        ),
        AgendaItem(
            title="Stage Setup for Symphony Under the Stars",
            category="Setup and Rehearsal",
            start_datetime=datetime.datetime(2029, 5, 17, 7, 0),
            pic_name="Michael Taylor",
            notes="Acoustic shell assembly and orchestra riser placements."
        ),
        AgendaItem(
            title="Technical Rehearsal & Soundcheck",
            category="Setup and Rehearsal",
            start_datetime=datetime.datetime(2029, 5, 21, 17, 0),
            pic_name="Michael Taylor",
            notes="Complete frequency sweep and monitor check."
        )
    ]
    db.add_all(agendas)

    # 6. Financial Transactions
    txs = [
        FinancialTransaction(date=datetime.datetime(2029, 5, 1, 10, 0), event_name="Sunset Park Booking", type="Expense", category="Vendor", amount=-7000.0, note="Echo Beats Festival venue payment", status="Completed"),
        FinancialTransaction(date=datetime.datetime(2029, 5, 2, 14, 0), event_name="Ticket Sales", type="Income", category="Event", amount=15000.0, note="Echo Beats Festival ticket sales", status="Completed"),
        FinancialTransaction(date=datetime.datetime(2029, 5, 3, 9, 30), event_name="Echo Beats Festival Promotion", type="Expense", category="Marketing", amount=-8000.0, note="Social media promotions", status="Pending"),
        FinancialTransaction(date=datetime.datetime(2029, 5, 4, 15, 0), event_name="Harmony Audio Deposit", type="Income", category="Sponsorship", amount=10000.0, note="Official sponsor payment", status="Completed"),
        FinancialTransaction(date=datetime.datetime(2029, 5, 5, 11, 0), event_name="Sound & Lighting Rental", type="Expense", category="Equipment", amount=-3000.0, note="Equipment lease", status="Pending"),
        FinancialTransaction(date=datetime.datetime(2029, 5, 6, 12, 0), event_name="Merchandise Sales", type="Income", category="Event", amount=2500.0, note="Echo Beats Festival merch", status="Completed"),
        FinancialTransaction(date=datetime.datetime(2029, 5, 7, 9, 0), event_name="Catering Services Payment", type="Expense", category="Vendor", amount=-5500.0, note="VIP catering advance", status="Completed"),
        FinancialTransaction(date=datetime.datetime(2029, 5, 8, 16, 30), event_name="Volunteer Stipends", type="Expense", category="Staffing", amount=-2000.0, note="Crew per diem", status="Pending"),
    ]
    db.add_all(txs)

    # 7. Feedback Reviews
    reviews = [
        FeedbackReview(event_id=event1.id, customer_name="Jackson Moore", rating=5.0, event_title="Echo Beats Festival", event_category="Music", comment="An absolutely amazing festival! The lineup of artists was incredible, and the sound quality was impeccable. The energy from the crowd made it a night to remember.", customer_avatar="https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?auto=format&fit=crop&w=150&q=80"),
        FeedbackReview(event_id=event4.id, customer_name="Alicia Smithson", rating=4.0, event_title="Runway Revolution 2029", event_category="Fashion", comment="Beautiful designs and a well-organized event overall. The models and lighting were captivating, but the seating arrangements could have been planned better for the audience.", customer_avatar="https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=150&q=80"),
        FeedbackReview(event_id=event7.id, customer_name="Patrick Cooper", rating=5.0, event_title="Symphony Under the Stars", event_category="Music", comment="The music under the open sky was breathtaking. The orchestra was phenomenal, and the ambiance made it feel like a dream. Everything was organized beautifully.", customer_avatar="https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?auto=format&fit=crop&w=150&q=80"),
        FeedbackReview(event_id=event3.id, customer_name="Clara Simmons", rating=4.5, event_title="Culinary Delights Festival", event_category="Food & Culinary", comment="The variety of cuisines and food stalls was fantastic! The flavors were outstanding, though some popular stalls ran out of food too early in the evening.", customer_avatar="https://images.unsplash.com/photo-1580489944761-15a19d654956?auto=format&fit=crop&w=150&q=80"),
        FeedbackReview(event_id=event5.id, customer_name="Natalie Johnson", rating=5.0, event_title="Artistry Unveiled Expo", event_category="Art & Design", comment="The expo was a treat for art lovers! The installations were awe-inspiring, and the chance to meet artists was a highlight of the event for me.", customer_avatar="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?auto=format&fit=crop&w=150&q=80"),
        FeedbackReview(event_id=event6.id, customer_name="Henry Carter", rating=4.2, event_title="Tech Future Expo", event_category="Technology", comment="A fantastic platform for tech enthusiasts to explore the latest innovations. More hands-on workshops would have made the event even better, but it was still very informative.", customer_avatar="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=150&q=80")
    ]
    db.add_all(reviews)

    # 8. Activity Logs
    logs = [
        ActivityAuditLog(actor_name="Admin Stefanus Weber", action_type="REFUND_REVIEW", description="reviewed a refund request for Invoice ID: 'INV1004' (05:30 PM)", timestamp=datetime.datetime.utcnow() - datetime.timedelta(minutes=15)),
        ActivityAuditLog(actor_name="Wella McGrath", action_type="PRICE_UPDATE", description="updated ticket prices for event 'Runway Revolution 2024' under category 'Fashion' (02:00 PM)", timestamp=datetime.datetime.utcnow() - datetime.timedelta(hours=2)),
        ActivityAuditLog(actor_name="Patrick Cooper", action_type="BOOKING_CANCEL", description="canceled a booking with Invoice ID: 'INV10014' (11:15 AM)", timestamp=datetime.datetime.utcnow() - datetime.timedelta(hours=5)),
        ActivityAuditLog(actor_name="Andrew Shaw", action_type="EVENT_CREATE", description="created a new event: 'Symphony Under the Stars' under category 'Music' (09:30 AM)", timestamp=datetime.datetime.utcnow() - datetime.timedelta(hours=8))
    ]
    db.add_all(logs)

    # 9. Gallery Albums
    albums = [
        GalleryAlbum(title="Echo Beats Festival", category="Music", event_date="May 20, 2029", cover_image_url="https://images.unsplash.com/photo-1470225620780-dba8ba36b745?auto=format&fit=crop&w=600&q=80", photo_count=36),
        GalleryAlbum(title="Culinary Delights Festival", category="Food & Culinary", event_date="May 25, 2029", cover_image_url="https://images.unsplash.com/photo-1555939594-58d7cb561ad1?auto=format&fit=crop&w=600&q=80", photo_count=42),
        GalleryAlbum(title="Artistry Unveiled Expo", category="Art & Design", event_date="May 15, 2029", cover_image_url="https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?auto=format&fit=crop&w=600&q=80", photo_count=28),
        GalleryAlbum(title="Tech Future Expo", category="Technology", event_date="June 1, 2029", cover_image_url="https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=600&q=80", photo_count=50),
        GalleryAlbum(title="Runway Revolution 2029", category="Fashion", event_date="May 1, 2029", cover_image_url="https://images.unsplash.com/photo-1509631179647-0177331693ae?auto=format&fit=crop&w=600&q=80", photo_count=64),
        GalleryAlbum(title="Global Wellness Summit", category="Health & Wellness", event_date="May 5, 2029", cover_image_url="https://images.unsplash.com/photo-1545205597-3d9d02c29597?auto=format&fit=crop&w=600&q=80", photo_count=19),
        GalleryAlbum(title="Adventure Gear Show", category="Outdoor & Adventure", event_date="June 5, 2029", cover_image_url="https://images.unsplash.com/photo-1551632811-561732d1e306?auto=format&fit=crop&w=600&q=80", photo_count=31),
        GalleryAlbum(title="Symphony Under the Stars", category="Music", event_date="April 20, 2029", cover_image_url="https://images.unsplash.com/photo-1465847899084-d164df4dedc6?auto=format&fit=crop&w=600&q=80", photo_count=45),
        GalleryAlbum(title="Harmony Health Fair", category="Health & Wellness", event_date="June 15, 2029", cover_image_url="https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&w=600&q=80", photo_count=22),
        GalleryAlbum(title="Live Paint Battle", category="Art & Design", event_date="June 20, 2029", cover_image_url="https://images.unsplash.com/photo-1513364776144-60967b0f800f?auto=format&fit=crop&w=600&q=80", photo_count=38),
        GalleryAlbum(title="Spring Trends Runway", category="Fashion", event_date="June 10, 2029", cover_image_url="https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?auto=format&fit=crop&w=600&q=80", photo_count=52),
        GalleryAlbum(title="Champions League Final Viewing Party", category="Sports", event_date="May 10, 2029", cover_image_url="https://images.unsplash.com/photo-1508098682722-e99c43a406b2?auto=format&fit=crop&w=600&q=80", photo_count=60)
    ]
    db.add_all(albums)

    db.commit()
    db.close()
    print("Database successfully seeded with Ventixe Figma mockup data!")

if __name__ == "__main__":
    run_seed()
