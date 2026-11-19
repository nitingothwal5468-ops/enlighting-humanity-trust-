#!/usr/bin/env python3
"""
Enlighting Humanity Trust - Master Page Builder Part 4
Generates Media, Governance, Contact & Legal Pages (18 to 24):
- gallery.html
- stories.html
- transparency.html
- contact.html
- privacy-policy.html
- terms.html
- refund-policy.html
"""

import os
from generator_base import render_page

print("Generating Media, Governance, Contact & Legal Pages (18-24)...")

# -------------------------------------------------------------
# 18. GALLERY.HTML
# -------------------------------------------------------------
gallery_content = '''
<div class="page-banner">
    <div class="container">
        <ul class="breadcrumbs">
            <li><a href="index.html">Home</a></li>
            <li><a href="stories.html">Impact</a></li>
            <li>Photo & Media Gallery</li>
        </ul>
        <h1 class="page-banner-title">Field Impact Gallery</h1>
        <p class="page-banner-sub">Authentic, un-staged photographs of our ground-level work in Village Neelwal, Tikri Kalan, and surrounding communities.</p>
    </div>
</div>

<section class="section">
    <div class="container">
        <!-- Filter Tabs -->
        <div class="gallery-filter-tabs text-center mb-5">
            <button class="filter-btn active" data-filter="all">All Photos</button>
            <button class="filter-btn" data-filter="environment">Tree Plantation (20/Mo)</button>
            <button class="filter-btn" data-filter="education">Child Education</button>
            <button class="filter-btn" data-filter="community">Community & Women</button>
            <button class="filter-btn" data-filter="food">Food Alleviation</button>
        </div>

        <!-- Gallery Grid -->
        <div class="gallery-masonry-grid" id="galleryContainer">
            <!-- Item 1: Tree planting -->
            <div class="gallery-item" data-category="environment">
                <div class="gallery-img-box">
                    <img src="assets/images/tree-planting-children.jpg" alt="School children planting native trees" loading="lazy">
                    <div class="gallery-overlay">
                        <h4>Monthly Tree Plantation</h4>
                        <p>Village school children planting native saplings in Village Neelwal.</p>
                        <span class="gallery-date">Active Monthly Commitment</span>
                    </div>
                </div>
            </div>

            <!-- Item 2: Children activity -->
            <div class="gallery-item" data-category="education">
                <div class="gallery-img-box">
                    <img src="assets/images/children-activity.jpg" alt="Children engaged in remedial learning" loading="lazy">
                    <div class="gallery-overlay">
                        <h4>Remedial Learning Pod</h4>
                        <p>Foundational literacy and group learning sessions for first-generation students.</p>
                        <span class="gallery-date">Tikri Kalan Study Center</span>
                    </div>
                </div>
            </div>

            <!-- Item 3: Community meeting -->
            <div class="gallery-item" data-category="community">
                <div class="gallery-img-box">
                    <img src="assets/images/community-drive.jpg" alt="Community members gathered for local welfare meeting" loading="lazy">
                    <div class="gallery-overlay">
                        <h4>Community Mobilization</h4>
                        <p>Dialogue with village elders, mothers, and local youth in Village Neelwal.</p>
                        <span class="gallery-date">Neelwal Gram Chaupal</span>
                    </div>
                </div>
            </div>

            <!-- Item 4: Hero banner team -->
            <div class="gallery-item" data-category="community">
                <div class="gallery-img-box">
                    <img src="assets/images/hero-banner.jpg" alt="Trust volunteers and community coordinators" loading="lazy">
                    <div class="gallery-overlay">
                        <h4>Field Coordinators & Volunteers</h4>
                        <p>The grassroots leadership team spearheading relief across West Delhi.</p>
                        <span class="gallery-date">Enlighting Humanity Trust Team</span>
                    </div>
                </div>
            </div>

            <!-- Item 5: Tree plantation care -->
            <div class="gallery-item" data-category="environment">
                <div class="gallery-img-box">
                    <img src="assets/images/tree-planting-children.jpg" alt="Tree guard installation" loading="lazy">
                    <div class="gallery-overlay">
                        <h4>Tree Guards & Care</h4>
                        <p>Protecting every planted sapling with sturdy guards to ensure high survival rates.</p>
                        <span class="gallery-date">Tikri Kalan Green Drive</span>
                    </div>
                </div>
            </div>

            <!-- Item 6: Educational empowerment -->
            <div class="gallery-item" data-category="education">
                <div class="gallery-img-box">
                    <img src="assets/images/children-activity.jpg" alt="Educational materials distribution" loading="lazy">
                    <div class="gallery-overlay">
                        <h4>Stationery Distribution</h4>
                        <p>Handing over school bags and notebooks to prevent dropouts.</p>
                        <span class="gallery-date">Shiksha Ki Udaan Drive</span>
                    </div>
                </div>
            </div>
        </div>

        <div class="text-center mt-5">
            <p class="text-muted">Want to participate in our next monthly tree planting or community drive?</p>
            <a href="volunteer.html" class="btn btn-primary">Join as a Volunteer</a>
            <a href="donate.html" class="btn btn-outline ml-2">Support These Drives</a>
        </div>
    </div>
</section>
'''

render_page(
    filename="gallery.html",
    active_nav="impact",
    title="Photo Gallery | Authentic Ground Action",
    meta_desc="Browse genuine field photos of tree plantation drives, remedial education pods, and community meetings organized by Enlighting Humanity Trust.",
    content_html=gallery_content
)

# -------------------------------------------------------------
# 19. STORIES.HTML
# -------------------------------------------------------------
stories_content = '''
<div class="page-banner">
    <div class="container">
        <ul class="breadcrumbs">
            <li><a href="index.html">Home</a></li>
            <li><a href="stories.html">Impact</a></li>
            <li>Stories of Change</li>
        </ul>
        <h1 class="page-banner-title">Stories of Real Change</h1>
        <p class="page-banner-sub">Authentic journeys of resilience, dignity, and empowerment from the villages and resettlement colonies of West Delhi.</p>
    </div>
</div>

<section class="section">
    <div class="container">
        <div class="stories-feed">
            <!-- Story 1 -->
            <article class="story-card mb-5">
                <div class="grid-2-col align-center">
                    <div class="story-media">
                        <img src="assets/images/community-drive.jpg" alt="Sunita Devi learning tailoring" class="rounded-img shadow">
                    </div>
                    <div class="story-content">
                        <span class="story-tag">Women Empowerment</span>
                        <h2 class="story-title">From Household Uncertainty to Financial Self-Reliance: Sunita's Story</h2>
                        <span class="story-meta">📍 Village Neelwal, West Delhi</span>
                        <p>
                            Sunita Devi, 34, is a mother of three whose husband works as a temporary construction laborer with irregular earnings. Months with no construction work often meant borrowing money from local moneylenders at exorbitant interest rates simply to feed her children.
                        </p>
                        <p>
                            When Enlighting Humanity Trust opened its free vocational tailoring center in Village Neelwal, Sunita enrolled in the 6-month stitching and garment finishing course. Today, Sunita runs a home-based alterations and tailoring shop, earning between ₹5,000 to ₹7,000 every month.
                        </p>
                        <blockquote class="story-quote">
                            "For the first time in my life, I don't have to plead with anyone for my children's school fees. I earn it with my own hands."
                        </blockquote>
                    </div>
                </div>
            </article>

            <!-- Story 2 -->
            <article class="story-card mb-5">
                <div class="grid-2-col align-center reverse">
                    <div class="story-media">
                        <img src="assets/images/tree-planting-children.jpg" alt="Children tending to native trees" class="rounded-img shadow">
                    </div>
                    <div class="story-content">
                        <span class="story-tag green">Environmental Stewardship</span>
                        <h2 class="story-title">The Green Guardians: How 20 Trees a Month Transformed a School Ground</h2>
                        <span class="story-meta">📍 Tikri Kalan Government Primary School</span>
                        <p>
                            Surrounded by dusty transit corridors and vehicle emissions, the government primary school near Tikri Kalan lacked shade, leaving its playground scorched during Delhi summers.
                        </p>
                        <p>
                            Enlighting Humanity Trust instituted its "Tree Buddy" initiative, planting 20 native Neem and Peepal saplings on the school perimeter. Grade 5 student Rohit and his classmates each took ownership of one tree, watering them daily and inspecting their tree guards. Two years later, those saplings have grown into dense, cooling green canopies.
                        </p>
                        <blockquote class="story-quote">
                            "Our Peepal tree is now taller than me! Birds have started nesting in it, and we sit under its shade to read during recess."
                        </blockquote>
                    </div>
                </div>
            </article>

            <!-- Story 3 -->
            <article class="story-card mb-5">
                <div class="grid-2-col align-center">
                    <div class="story-media">
                        <img src="assets/images/children-activity.jpg" alt="Aayan studying with books" class="rounded-img shadow">
                    </div>
                    <div class="story-content">
                        <span class="story-tag blue">Child Education</span>
                        <h2 class="story-title">Overcoming the Dropout Cycle: Aayan's Leap Back into School</h2>
                        <span class="story-meta">📍 Resettlement Cluster, Mundka</span>
                        <p>
                            Aayan, 11, dropped out of school when his family relocated from Bihar to outer Delhi for factory labor. Unable to read Hindi or do basic multiplication, he spent his days collecting scrap plastic until our volunteer survey team met his parents.
                        </p>
                        <p>
                            Through our remedial bridge pod, Aayan received 4 months of intensive foundational literacy support, a sturdy school kit, and formal enrollment assistance into grade 4 at the local municipal school. Today, Aayan consistently ranks in the top five of his class.
                        </p>
                        <blockquote class="story-quote">
                            "I want to become a computer engineer so I can build learning software for children who cannot afford school."
                        </blockquote>
                    </div>
                </div>
            </article>
        </div>

        <div class="p-5 bg-light rounded text-center mt-5">
            <h3>You Can Be Part of the Next Story of Change</h3>
            <p class="text-muted mb-4">Every contribution, whether a single tree sapling (₹251) or a monthly child study kit (₹501), rewrites a life's trajectory.</p>
            <a href="donate.html" class="btn btn-primary btn-lg">Make an Impact Today</a>
            <a href="volunteer.html" class="btn btn-outline btn-lg ml-2">Volunteer With Us</a>
        </div>
    </div>
</section>
'''

render_page(
    filename="stories.html",
    active_nav="impact",
    title="Stories of Change | Real Field Impact Case Studies",
    meta_desc="Read authentic stories of transformation in women empowerment, child education, and environmental restoration by Enlighting Humanity Trust in New Delhi.",
    content_html=stories_content
)

# -------------------------------------------------------------
# 20. TRANSPARENCY.HTML
# -------------------------------------------------------------
transparency_content = '''
<div class="page-banner">
    <div class="container">
        <ul class="breadcrumbs">
            <li><a href="index.html">Home</a></li>
            <li><a href="about.html">About Us</a></li>
            <li>Transparency & Governance</li>
        </ul>
        <h1 class="page-banner-title">Transparency & Governance</h1>
        <p class="page-banner-sub">Complete statutory disclosures, legal registrations, financial accountability, and our donor bill of rights.</p>
    </div>
</div>

<section class="section">
    <div class="container">
        <div class="lead-box text-center mb-5">
            <span class="section-tag">Radical Accountability</span>
            <h2 class="section-title">Open Books, Pure Intent, Zero Compromise</h2>
            <p class="lead-text max-800 mx-auto">
                Trust is the foundation of public social service. Enlighting Humanity Trust is committed to complete disclosure of our legal standing, board governance, and programmatic fund allocation.
            </p>
        </div>

        <!-- Statutory Details Grid -->
        <div class="grid-2-col mb-5">
            <div class="p-4 bg-light rounded shadow-sm">
                <h3 class="mb-3">Legal & Registration Particulars</h3>
                <table class="table-info">
                    <tr>
                        <td><strong>Entity Name:</strong></td>
                        <td>Enlighting Humanity Trust</td>
                    </tr>
                    <tr>
                        <td><strong>Governing Law:</strong></td>
                        <td>Indian Trusts Act, 1882</td>
                    </tr>
                    <tr>
                        <td><strong>Registered Office:</strong></td>
                        <td>Village Neelwal, Post Office Tikri Kalan, New Delhi – 110041, India</td>
                    </tr>
                    <tr>
                        <td><strong>Founding Year:</strong></td>
                        <td>2017 (9+ Years Active Public Service)</td>
                    </tr>
                    <tr>
                        <td><strong>Founder & Managing Trustee:</strong></td>
                        <td>Nitin Gothwal</td>
                    </tr>
                    <tr>
                        <td><strong>Official Contact:</strong></td>
                        <td>+91 9654518368 | nitingothwal5468@gmail.com</td>
                    </tr>
                </table>
            </div>

            <div class="p-4 bg-light rounded shadow-sm">
                <h3 class="mb-3">Tax & Accreditation Status</h3>
                <table class="table-info">
                    <tr>
                        <td><strong>Section 12A Status:</strong></td>
                        <td>Registered Public Charitable Trust (Income Tax Dept.)</td>
                    </tr>
                    <tr>
                        <td><strong>Section 80G Status:</strong></td>
                        <td>Donations 50% Tax Exempt for Indian Donors & Companies</td>
                    </tr>
                    <tr>
                        <td><strong>NITI Aayog NGO Darpan:</strong></td>
                        <td>Registered & Verified</td>
                    </tr>
                    <tr>
                        <td><strong>Official UPI ID:</strong></td>
                        <td><code>9654518368@paytm</code> (Payee: Enlighting Humanity Trust)</td>
                    </tr>
                    <tr>
                        <td><strong>Statutory Auditor:</strong></td>
                        <td>Independent Chartered Accountants, New Delhi</td>
                    </tr>
                </table>
            </div>
        </div>

        <!-- Financial Allocation Principles -->
        <div class="mb-5 p-4 border rounded">
            <h3 class="mb-3">Financial Allocation Principles</h3>
            <div class="grid-3-col text-center">
                <div class="p-3">
                    <span class="huge-percent text-primary">85%+</span>
                    <h4>Direct Programmatic Relief</h4>
                    <p class="small text-muted">Directly allocated to cooked meals, dry grains, school supplies, tree saplings, and vocational tools.</p>
                </div>
                <div class="p-3">
                    <span class="huge-percent text-secondary">10%</span>
                    <h4>Field Monitoring & Quality</h4>
                    <p class="small text-muted">Logistics, teacher honorariums, tree guard maintenance, and community survey coordination.</p>
                </div>
                <div class="p-3">
                    <span class="huge-percent text-muted">5%</span>
                    <h4>Statutory & Administrative</h4>
                    <p class="small text-muted">Audit fees, banking compliance, website server maintenance, and legal filings.</p>
                </div>
            </div>
        </div>

        <!-- Donor Bill of Rights -->
        <div class="donor-rights bg-light p-4 rounded mb-5">
            <h3 class="mb-3">Donor Bill of Rights</h3>
            <p class="mb-3">As a valued supporter of Enlighting Humanity Trust, you have the right to:</p>
            <ul class="custom-check-list">
                <li>Be informed of the Trust’s mission, the way your donated funds are utilized, and the capacity of the Trust to use donations effectively for their intended purposes.</li>
                <li>Receive prompt and truthful answers to any questions regarding our programs, field operations, and tax exemption certificates.</li>
                <li>Receive an official signed 80G tax receipt for every eligible monetary donation upon sharing transaction verification.</li>
                <li>Be assured that your contact information and donation records are kept completely confidential and never sold, rented, or exchanged.</li>
            </ul>
        </div>

        <!-- Grievance & RTI Desk -->
        <div class="text-center p-4 border rounded">
            <h4>Grievance Redressal & Public Information Officer</h4>
            <p class="text-muted">For any financial query, receipt verification, or audit report request, contact our Managing Trustee directly:</p>
            <p><strong>Nitin Gothwal</strong> | Managing Trustee<br>
            Phone: <a href="tel:+919654518368">+91 9654518368</a> | Email: <a href="mailto:nitingothwal5468@gmail.com">nitingothwal5468@gmail.com</a></p>
        </div>
    </div>
</section>
'''

render_page(
    filename="transparency.html",
    active_nav="about",
    title="Transparency & Governance | Statutory Details & 80G",
    meta_desc="Inspect Enlighting Humanity Trust's legal registrations, Indian Trusts Act status, 12A/80G certifications, financial stewardship, and donor bill of rights.",
    content_html=transparency_content
)

# -------------------------------------------------------------
# 21. CONTACT.HTML
# -------------------------------------------------------------
contact_content = '''
<div class="page-banner">
    <div class="container">
        <ul class="breadcrumbs">
            <li><a href="index.html">Home</a></li>
            <li>Contact Us</li>
        </ul>
        <h1 class="page-banner-title">Contact Enlighting Humanity Trust</h1>
        <p class="page-banner-sub">Get in touch with our team, visit our registered office in West Delhi, or collaborate on community relief.</p>
    </div>
</div>

<section class="section">
    <div class="container">
        <div class="grid-2-col mb-5">
            <!-- Left: Contact Details -->
            <div class="contact-details-col">
                <span class="section-tag">Reach Us Directly</span>
                <h2 class="section-title">We Are Always Open to Dialogue and Collaboration</h2>
                <p class="lead-text mb-4">
                    Whether you want to inquire about donations, volunteer in field drives, propose a CSR alliance, or visit our community center, we welcome you with open arms.
                </p>

                <div class="contact-card-list">
                    <div class="contact-card-item">
                        <div class="contact-icon">📍</div>
                        <div>
                            <h4>Registered Office Address</h4>
                            <p>
                                <strong>Enlighting Humanity Trust</strong><br>
                                Village Neelwal, Post Office Tikri Kalan,<br>
                                West Delhi, New Delhi – 110041, India.
                            </p>
                        </div>
                    </div>

                    <div class="contact-card-item">
                        <div class="contact-icon">📞</div>
                        <div>
                            <h4>Founder & Trustee Contact</h4>
                            <p>
                                <strong>Nitin Gothwal</strong> (Managing Trustee)<br>
                                Direct Call: <a href="tel:+919654518368">+91 9654518368</a><br>
                                WhatsApp: <a href="https://wa.me/919654518368?text=Hello%20Enlighting%20Humanity%20Trust" target="_blank" rel="noopener">+91 9654518368</a>
                            </p>
                        </div>
                    </div>

                    <div class="contact-card-item">
                        <div class="contact-icon">✉️</div>
                        <div>
                            <h4>Official Email Addresses</h4>
                            <p>
                                Primary: <a href="mailto:nitingothwal5468@gmail.com">nitingothwal5468@gmail.com</a><br>
                                Trust Desk: <a href="mailto:enlightinghumanitytrust@gmail.com">enlightinghumanitytrust@gmail.com</a>
                            </p>
                        </div>
                    </div>

                    <div class="contact-card-item">
                        <div class="contact-icon">🕒</div>
                        <div>
                            <h4>Office & Visiting Hours</h4>
                            <p>
                                Monday – Saturday: 9:00 AM – 6:00 PM IST<br>
                                Sunday: Field Activities & Community Drives Only
                            </p>
                        </div>
                    </div>

                    <div class="contact-card-item">
                        <div class="contact-icon">🚇</div>
                        <div>
                            <h4>Transit & Metro Directions</h4>
                            <p>
                                <strong>Nearest Metro Station:</strong> Tikri Kalan Metro Station (Green Line, Delhi Metro). E-rickshaws and autos are readily available directly to Village Neelwal (approx. 7–10 minutes).
                            </p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Right: Interactive Contact Form -->
            <div class="contact-form-col">
                <div class="p-4 bg-light rounded shadow-sm">
                    <h3 class="mb-3">Send Us a Direct Message</h3>
                    <p class="small text-muted mb-4">Fill in the form below and our team will get back to you promptly.</p>

                    <form id="generalContactForm">
                        <div class="form-group mb-3">
                            <label for="contactName" class="form-label">Full Name *</label>
                            <input type="text" id="contactName" class="form-control" placeholder="Your name" required>
                        </div>

                        <div class="form-row">
                            <div class="form-group mb-3">
                                <label for="contactEmail" class="form-label">Email Address *</label>
                                <input type="email" id="contactEmail" class="form-control" placeholder="your@email.com" required>
                            </div>
                            <div class="form-group mb-3">
                                <label for="contactPhone" class="form-label">Phone / WhatsApp</label>
                                <input type="tel" id="contactPhone" class="form-control" placeholder="+91 98765 43210">
                            </div>
                        </div>

                        <div class="form-group mb-3">
                            <label for="contactSubject" class="form-label">Subject</label>
                            <select id="contactSubject" class="form-control">
                                <option value="General Inquiry">General Inquiry</option>
                                <option value="Donation & 80G Receipt">Donation & 80G Receipt</option>
                                <option value="Volunteering Inquiries">Volunteering Inquiries</option>
                                <option value="CSR Collaboration">CSR Collaboration</option>
                                <option value="Visit to Village Neelwal">Visit to Village Neelwal</option>
                            </select>
                        </div>

                        <div class="form-group mb-3">
                            <label for="contactMessage" class="form-label">Your Message *</label>
                            <textarea id="contactMessage" rows="5" class="form-control" placeholder="Share your message or inquiry..." required></textarea>
                        </div>

                        <button type="submit" id="contactSubmitBtn" class="btn btn-primary btn-block">Send Message</button>
                        <div id="contactStatusMessage" class="mt-3" style="display:none;"></div>
                    </form>
                </div>
            </div>
        </div>

        <!-- Google Map / Location Showcase -->
        <div class="map-card-box p-4 bg-white border rounded text-center">
            <h3 class="mb-2">Location Map & Directions</h3>
            <p class="text-muted mb-3">Village Neelwal, Post Office Tikri Kalan, West Delhi – 110041 (Near Tikri Kalan Metro Station, Green Line)</p>
            <div class="map-action-btns">
                <a href="https://maps.google.com/?q=Village+Neelwal+Tikri+Kalan+Delhi+110041" target="_blank" rel="noopener" class="btn btn-outline">
                    🗺️ Open in Google Maps Navigation &rarr;
                </a>
                <a href="https://wa.me/919654518368?text=Hello%20Enlighting%20Humanity%20Trust%2C%20I%20need%20directions%20to%20your%20office" target="_blank" rel="noopener" class="btn btn-secondary ml-2">
                    Request Live WhatsApp Location
                </a>
            </div>
        </div>
    </div>
</section>
'''

render_page(
    filename="contact.html",
    active_nav="contact",
    title="Contact Us | Registered Office & Helpline",
    meta_desc="Contact Enlighting Humanity Trust in Village Neelwal, PO Tikri Kalan, New Delhi - 110041. Phone: +91 9654518368, Email: nitingothwal5468@gmail.com.",
    content_html=contact_content
)

# -------------------------------------------------------------
# 22. PRIVACY-POLICY.HTML
# -------------------------------------------------------------
privacy_content = '''
<div class="page-banner">
    <div class="container">
        <ul class="breadcrumbs">
            <li><a href="index.html">Home</a></li>
            <li>Privacy Policy</li>
        </ul>
        <h1 class="page-banner-title">Privacy Policy</h1>
        <p class="page-banner-sub">How Enlighting Humanity Trust safeguards your personal information and respects your data rights.</p>
    </div>
</div>

<section class="section">
    <div class="container legal-content-wrapper">
        <p class="text-muted"><strong>Last Updated:</strong> January 2026</p>

        <h3>1. Commitment to Privacy</h3>
        <p>
            Enlighting Humanity Trust ("we," "our," or "the Trust") respects the privacy of all visitors, donors, volunteers, and partners who interact with our website and programs. This Privacy Policy details our practices in compliance with the Indian Information Technology Act, 2000, the Information Technology (Reasonable Security Practices and Procedures and Sensitive Personal Data or Information) Rules, 2011, and the Digital Personal Data Protection (DPDP) Act.
        </p>

        <h3>2. Information We Collect</h3>
        <p>We only collect personal information when voluntarily submitted by you:</p>
        <ul class="custom-check-list">
            <li><strong>Donor Information:</strong> Name, email address, phone/WhatsApp number, PAN (for 80G tax receipt issuance), transaction reference number (UTR), and postal address.</li>
            <li><strong>Volunteer & Partner Inquiries:</strong> Name, educational background, professional skills, contact numbers, and location.</li>
            <li><strong>Technical Information:</strong> Standard server logs, browser type, and anonymous aggregate visit counts. We do not use intrusive tracking cookies.</li>
        </ul>

        <h3>3. Purpose of Data Use</h3>
        <p>The information collected is strictly utilized to:</p>
        <ul>
            <li>Issue official 80G tax deduction receipts and donation confirmations.</li>
            <li>Communicate project progress reports and quarterly community impact updates.</li>
            <li>Coordinate volunteer activities, field visits, and emergency relief deployments.</li>
            <li>Comply with statutory reporting requirements under the Indian Trusts Act and Income Tax Department.</li>
        </ul>

        <h3>4. Absolute Non-Disclosure Policy</h3>
        <p>
            <strong>We never sell, rent, lease, or trade your personal or financial data to any commercial third party, marketing agency, or external entity.</strong> Your information is strictly retained within the administrative custody of Enlighting Humanity Trust.
        </p>

        <h3>5. Financial Data Security</h3>
        <p>
            Direct UPI payments and QR code transactions are processed directly through your respective banking or UPI application (e.g., Paytm, BHIM, Google Pay, PhonePe). Enlighting Humanity Trust never stores, sees, or accesses your bank passwords, debit card numbers, or UPI PINs.
        </p>

        <h3>6. Data Retention & Your Rights</h3>
        <p>
            You have the right to request access to the personal data we hold about you, request corrections to erroneous details, or request the removal of your email from our newsletter updates. For any privacy requests, please contact our Data Redressal Officer at:
        </p>
        <p>
            <strong>Nitin Gothwal</strong>, Managing Trustee<br>
            Email: <a href="mailto:nitingothwal5468@gmail.com">nitingothwal5468@gmail.com</a><br>
            Phone: <a href="tel:+919654518368">+91 9654518368</a><br>
            Address: Village Neelwal, Post Office Tikri Kalan, New Delhi – 110041, India.
        </p>
    </div>
</section>
'''

render_page(
    filename="privacy-policy.html",
    active_nav="",
    title="Privacy Policy | Enlighting Humanity Trust",
    meta_desc="Official Privacy Policy of Enlighting Humanity Trust. Compliant with IT Act 2000 and DPDP Act. Zero commercial data sharing.",
    content_html=privacy_content
)

# -------------------------------------------------------------
# 23. TERMS.HTML
# -------------------------------------------------------------
terms_content = '''
<div class="page-banner">
    <div class="container">
        <ul class="breadcrumbs">
            <li><a href="index.html">Home</a></li>
            <li>Terms of Service</li>
        </ul>
        <h1 class="page-banner-title">Terms of Service</h1>
        <p class="page-banner-sub">Rules, rights, and conditions governing the use of the Enlighting Humanity Trust website.</p>
    </div>
</div>

<section class="section">
    <div class="container legal-content-wrapper">
        <p class="text-muted"><strong>Last Updated:</strong> January 2026</p>

        <h3>1. Acceptance of Terms</h3>
        <p>
            By accessing or using this website, you agree to be bound by these Terms of Service, all applicable laws and regulations of India, and agree that you are responsible for compliance with any applicable local laws. If you do not agree with any of these terms, you are prohibited from using or accessing this site.
        </p>

        <h3>2. Purpose of the Website</h3>
        <p>
            This website is maintained by Enlighting Humanity Trust, a registered public charitable trust under the Indian Trusts Act, 1882, to provide information about our non-profit programs, collect voluntary charitable contributions, recruit volunteers, and facilitate transparent communication with the public.
        </p>

        <h3>3. Intellectual Property Rights</h3>
        <p>
            All content on this site, including photographs taken during our field activities in Village Neelwal and Tikri Kalan, organizational logos, textual descriptions, and website design, is the exclusive intellectual property of Enlighting Humanity Trust, unless otherwise credited. Unauthorized reproduction, re-hosting, or commercial misuse without written consent from the Managing Trustee is strictly prohibited.
        </p>

        <h3>4. Voluntary Contributions</h3>
        <p>
            All donations made through UPI (9654518368@paytm) or direct bank transfer are voluntary charitable contributions. Donors are requested to verify payment details before confirming transactions. Tax exemption certificates under Section 80G will be issued in accordance with prevailing Indian Income Tax regulations.
        </p>

        <h3>5. Limitation of Liability</h3>
        <p>
            While Enlighting Humanity Trust strives to keep all information on this website accurate and updated, we do not warrant that all content is free of technical inaccuracies or typographical errors. The Trust shall not be held liable for any damages arising out of the use or inability to use the materials on this site.
        </p>

        <h3>6. Governing Law & Jurisdiction</h3>
        <p>
            These terms are governed by and construed in accordance with the laws of India. Any disputes arising out of or related to the use of this website shall be subject to the exclusive jurisdiction of the competent courts in New Delhi, India.
        </p>

        <h3>7. Contact for Legal Inquiries</h3>
        <p>
            For any clarifications or legal notices, please reach out to:<br>
            <strong>Enlighting Humanity Trust</strong><br>
            Village Neelwal, Post Office Tikri Kalan, New Delhi – 110041, India.<br>
            Email: <a href="mailto:enlightinghumanitytrust@gmail.com">enlightinghumanitytrust@gmail.com</a> | Phone: +91 9654518368
        </p>
    </div>
</section>
'''

render_page(
    filename="terms.html",
    active_nav="",
    title="Terms of Service | Enlighting Humanity Trust",
    meta_desc="Terms and conditions governing the use of Enlighting Humanity Trust's official website and voluntary contribution channels.",
    content_html=terms_content
)

# -------------------------------------------------------------
# 24. REFUND-POLICY.HTML
# -------------------------------------------------------------
refund_content = '''
<div class="page-banner">
    <div class="container">
        <ul class="breadcrumbs">
            <li><a href="index.html">Home</a></li>
            <li>Donation & Refund Policy</li>
        </ul>
        <h1 class="page-banner-title">Donation & Refund Policy</h1>
        <p class="page-banner-sub">Clear, ethical, and transparent guidelines regarding voluntary donations and cancellation requests.</p>
    </div>
</div>

<section class="section">
    <div class="container legal-content-wrapper">
        <p class="text-muted"><strong>Last Updated:</strong> January 2026</p>

        <h3>1. Nature of Contributions</h3>
        <p>
            Enlighting Humanity Trust is a registered public charitable trust. Contributions received through our website, dynamic UPI QR codes (<code>9654518368@paytm</code>), or bank transfers are treated as unconditional, voluntary charitable donations used to support our humanitarian programs (hunger alleviation, child education, women empowerment, youth skill development, and tree plantation drives).
        </p>

        <h3>2. Policy on Donation Refunds</h3>
        <p>
            As a standard non-profit practice, donations once made are generally non-refundable because funds are committed swiftly toward procurement of dry grains, stationery kits, or tree saplings. However, we acknowledge that genuine errors, accidental duplicate transactions, or banking technical glitches can occasionally occur.
        </p>

        <h3>3. Eligible Circumstances for Refund</h3>
        <p>Enlighting Humanity Trust will review and process refund requests under the following verifiable conditions:</p>
        <ul class="custom-check-list">
            <li><strong>Accidental Duplicate Deduction:</strong> If your bank or UPI app processed the transaction twice for the same amount.</li>
            <li><strong>Erroneous Amount:</strong> If you accidentally entered an incorrect sum (e.g., entered ₹5,000 instead of intended ₹500).</li>
            <li><strong>Unauthorized Payment:</strong> If an unauthorized transaction was made using your banking credentials without your consent.</li>
        </ul>

        <h3>4. Timeframe for Requesting a Refund</h3>
        <p>
            All refund requests must be submitted within <strong>seven (7) calendar days</strong> of the transaction date. Requests made after 7 days cannot be entertained as the funds may have already been disbursed into programmatic procurement.
        </p>

        <h3>5. How to Submit a Refund Request</h3>
        <p>To request a refund, please send an email to <a href="mailto:nitingothwal5468@gmail.com">nitingothwal5468@gmail.com</a> with the subject line <em>"Donation Refund Request - [Your Name]"</em> containing the following verifiable details:</p>
        <ul>
            <li>Full Name of the Donor</li>
            <li>Registered Mobile Number and Email Address</li>
            <li>Date and Time of Transaction</li>
            <li>Amount Transferred (in INR)</li>
            <li>12-Digit UPI Transaction Reference Number (UTR) / Bank Transaction ID</li>
            <li>Screenshot of the payment debit notification from your UPI or banking app</li>
            <li>A brief explanation of the reason for the refund request</li>
        </ul>

        <h3>6. Processing & Resolution Timeline</h3>
        <p>
            Upon receipt of your complete request, our accounts desk will cross-verify the transaction with our bank statements within <strong>2 to 3 business days</strong>. Once approved, the refund will be credited back exclusively to the original payment source (same bank account / UPI VPA) within <strong>5 to 7 business days</strong>.
        </p>
        <p class="small text-muted">
            <em>Note: If an official 80G tax exemption certificate has already been issued for the transaction, that certificate will be formally revoked and voided upon refund processing.</em>
        </p>

        <h3>7. Contact for Refund Inquiries</h3>
        <p>
            For any queries related to donations or refunds, you may speak directly with our Managing Trustee:<br>
            <strong>Nitin Gothwal</strong>, Managing Trustee<br>
            Phone / WhatsApp: <a href="tel:+919654518368">+91 9654518368</a><br>
            Email: <a href="mailto:nitingothwal5468@gmail.com">nitingothwal5468@gmail.com</a><br>
            Office: Village Neelwal, Post Office Tikri Kalan, New Delhi – 110041, India.
        </p>
    </div>
</section>
'''

render_page(
    filename="refund-policy.html",
    active_nav="",
    title="Donation & Refund Policy | Enlighting Humanity Trust",
    meta_desc="Clear guidelines on donation refunds, duplicate deduction reversals, and cancellation procedures for Enlighting Humanity Trust.",
    content_html=refund_content
)

print("Batch 4 (Pages 18-24) completed successfully.")
print("ALL 24 PAGES GENERATED SUCCESSFULLY!")
