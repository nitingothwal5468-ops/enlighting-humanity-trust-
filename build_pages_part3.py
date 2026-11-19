#!/usr/bin/env python3
"""
Enlighting Humanity Trust - Master Page Builder Part 3
Generates Engagement, CSR & Donation Pages (13 to 17):
- campaigns.html
- volunteer.html
- partner.html
- csr.html
- donate.html
"""

import os
from generator_base import render_page

print("Generating Engagement & Donation Pages (13-17)...")

# -------------------------------------------------------------
# 13. CAMPAIGNS.HTML
# -------------------------------------------------------------
campaigns_content = '''
<div class="page-banner">
    <div class="container">
        <ul class="breadcrumbs">
            <li><a href="index.html">Home</a></li>
            <li>Campaigns</li>
        </ul>
        <h1 class="page-banner-title">Active Field Campaigns</h1>
        <p class="page-banner-sub">Time-bound, high-impact relief and empowerment drives where your support creates immediate change.</p>
    </div>
</div>

<section class="section">
    <div class="container">
        <div class="section-header text-center mb-5">
            <span class="section-tag">Urgent & Ongoing Action</span>
            <h2 class="section-title">Support a Focused Initiative Today</h2>
            <p class="section-desc">Each campaign addresses an urgent ground-level need in outer Delhi's vulnerable communities.</p>
        </div>

        <div class="campaign-grid">
            <!-- Campaign 1 -->
            <div class="campaign-card">
                <div class="campaign-media">
                    <img src="assets/images/community-drive.jpg" alt="Food relief campaign" loading="lazy">
                    <span class="campaign-tag urgent">High Priority</span>
                </div>
                <div class="campaign-body">
                    <h3 class="campaign-title">Project Annapurna: Winter Food Lines</h3>
                    <p class="campaign-desc">
                        Providing hot cooked khichdi, puris, and warm halwa alongside monthly dry ration kits for daily-wage migrant labor families facing cold winter unemployment in Tikri Kalan and Mundka.
                    </p>
                    <div class="progress-wrap">
                        <div class="progress-bar-bg">
                            <div class="progress-bar-fill" style="width: 72%;"></div>
                        </div>
                        <div class="progress-stats">
                            <span>Raised: <strong>₹72,000</strong></span>
                            <span>Target: <strong>₹1,00,000</strong></span>
                        </div>
                    </div>
                    <div class="campaign-actions">
                        <a href="donate.html?campaign=food" class="btn btn-primary btn-block">Sponsor Rations (₹501)</a>
                    </div>
                </div>
            </div>

            <!-- Campaign 2 -->
            <div class="campaign-card">
                <div class="campaign-media">
                    <img src="assets/images/tree-planting-children.jpg" alt="Green Delhi 240 tree plantation" loading="lazy">
                    <span class="campaign-tag green">Continuous</span>
                </div>
                <div class="campaign-body">
                    <h3 class="campaign-title">Green Delhi 240: 20 Native Trees Every Month</h3>
                    <p class="campaign-desc">
                        Our binding ecological mission: planting at least 20 native trees (Neem, Peepal, Jamun) every month with local village school children, guarded by durable tree guards and adopted by student Tree Buddies.
                    </p>
                    <div class="progress-wrap">
                        <div class="progress-bar-bg">
                            <div class="progress-bar-fill" style="width: 85%;"></div>
                        </div>
                        <div class="progress-stats">
                            <span>Planted: <strong>190+ Trees</strong></span>
                            <span>Annual Target: <strong>240 Trees</strong></span>
                        </div>
                    </div>
                    <div class="campaign-actions">
                        <a href="donate.html?campaign=environment" class="btn btn-primary btn-block">Plant a Tree (₹251)</a>
                    </div>
                </div>
            </div>

            <!-- Campaign 3 -->
            <div class="campaign-card">
                <div class="campaign-media">
                    <img src="assets/images/children-activity.jpg" alt="Shiksha Ki Udaan education drive" loading="lazy">
                    <span class="campaign-tag blue">Academic Year</span>
                </div>
                <div class="campaign-body">
                    <h3 class="campaign-title">Shiksha Ki Udaan: 500 School Starter Kits</h3>
                    <p class="campaign-desc">
                        Equipping 500 underprivileged primary school children with heavy-duty school bags, notebooks, geometry kits, water bottles, and stationery sets to prevent school dropouts.
                    </p>
                    <div class="progress-wrap">
                        <div class="progress-bar-bg">
                            <div class="progress-bar-fill" style="width: 60%;"></div>
                        </div>
                        <div class="progress-stats">
                            <span>Kits Distributed: <strong>310</strong></span>
                            <span>Target: <strong>500 Kits</strong></span>
                        </div>
                    </div>
                    <div class="campaign-actions">
                        <a href="donate.html?campaign=education" class="btn btn-primary btn-block">Sponsor a Kit (₹251)</a>
                    </div>
                </div>
            </div>

            <!-- Campaign 4 -->
            <div class="campaign-card">
                <div class="campaign-media">
                    <img src="assets/images/hero-banner.jpg" alt="Apna Aangan Community Hub Campaign" loading="lazy">
                    <span class="campaign-tag gold">Infrastructure</span>
                </div>
                <div class="campaign-body">
                    <h3 class="campaign-title">Apna Aangan: Permanent Community Sanctuary</h3>
                    <p class="campaign-desc">
                        Funding solar power backup, clean RO drinking water unit, and computer workstations for our flagship community center in Village Neelwal serving children and women.
                    </p>
                    <div class="progress-wrap">
                        <div class="progress-bar-bg">
                            <div class="progress-bar-fill" style="width: 45%;"></div>
                        </div>
                        <div class="progress-stats">
                            <span>Raised: <strong>₹1,35,000</strong></span>
                            <span>Goal: <strong>₹3,00,000</strong></span>
                        </div>
                    </div>
                    <div class="campaign-actions">
                        <a href="donate.html?campaign=aangan" class="btn btn-primary btn-block">Support Infrastructure</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
'''

render_page(
    filename="campaigns.html",
    active_nav="campaigns",
    title="Active Campaigns | Urgent Grassroots Relief Drives",
    meta_desc="Support active campaigns by Enlighting Humanity Trust: Project Annapurna food relief, Green Delhi 240 tree plantation, and Shiksha Ki Udaan school kits.",
    content_html=campaigns_content
)

# -------------------------------------------------------------
# 14. VOLUNTEER.HTML
# -------------------------------------------------------------
volunteer_content = '''
<div class="page-banner">
    <div class="container">
        <ul class="breadcrumbs">
            <li><a href="index.html">Home</a></li>
            <li><a href="volunteer.html">Get Involved</a></li>
            <li>Volunteer With Us</li>
        </ul>
        <h1 class="page-banner-title">Volunteer With Us</h1>
        <p class="page-banner-sub">Lend your time, skills, and heart to create measurable social impact in Village Neelwal and Tikri Kalan.</p>
    </div>
</div>

<section class="section">
    <div class="container">
        <div class="grid-2-col align-center mb-5">
            <div>
                <span class="section-tag">Be The Change</span>
                <h2 class="section-title">Join A Vibrant Community of Grassroots Changemakers</h2>
                <p class="lead-text">
                    Volunteering with Enlighting Humanity Trust is not passive charity. You will work on the ground alongside village children, daily-wage families, and local youth, gaining authentic leadership experience.
                </p>
                <p>
                    Whether you can dedicate two hours every Sunday to teach English or math, participate in our monthly tree-planting drives, or offer your graphic design and digital skills remotely, your contribution matters immensely.
                </p>
                <div class="perks-list mt-3">
                    <div class="perk-item">✓ <strong>Certificate of Volunteering:</strong> Official certificate recognizing your grassroots hours.</div>
                    <div class="perk-item">✓ <strong>Flexible Modes:</strong> On-field in West Delhi or remote digital volunteering.</div>
                    <div class="perk-item">✓ <strong>Direct Ground Exposure:</strong> Experience real social development firsthand.</div>
                </div>
            </div>
            <div>
                <img src="assets/images/children-activity.jpg" alt="Volunteers engaging with children" class="rounded-img shadow-lg">
            </div>
        </div>

        <!-- Available Roles -->
        <div class="roles-section mb-5">
            <h3 class="text-center mb-4">Available Volunteer Roles</h3>
            <div class="grid-3-col">
                <div class="feature-card">
                    <div class="feature-icon">📚</div>
                    <h4>Weekend Tutor / Mentor</h4>
                    <p>Teach basic English, Mathematics, science experiments, or arts and crafts to primary school children in Village Neelwal.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🌱</div>
                    <h4>Tree Plantation Coordinator</h4>
                    <p>Help organize our monthly 20-tree plantation drives: sourcing native saplings, coordinating with schools, and placing tree guards.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🎨</div>
                    <h4>Digital, Design & Media</h4>
                    <p>Design posters, edit field videos, manage social media stories, and help document ground activities remotely.</p>
                </div>
            </div>
        </div>

        <!-- Official Google Form Integration -->
        <div class="volunteer-form-wrap bg-light p-4 rounded shadow-sm mb-5" id="volunteer-form">
            <div class="section-header text-center mb-4">
                <span class="section-tag">Official Registration</span>
                <h2 class="section-title">Enlighting Humanity Volunteer Application</h2>
                <p class="section-desc">
                    Complete our official volunteer form below. All responses are directly securely logged to our Trustee coordination desk.
                </p>
            </div>

            <div class="google-form-container text-center">
                <!-- Direct Access Button -->
                <div class="mb-3">
                    <a href="https://forms.gle/WL4mJWV7Gi2GaAT38" target="_blank" rel="noopener" class="btn btn-primary btn-lg">
                        Open Official Volunteer Application Form &rarr;
                    </a>
                    <p class="small text-muted mt-2">Takes only 2 minutes. Responses connect directly to our volunteer coordinator.</p>
                </div>

                <!-- Embedded Form Iframe for in-page convenience -->
                <div class="responsive-iframe-holder">
                    <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSdO701YVvj80z49jD4ZtYd2dE34B5-XqWw/viewform?embedded=true" 
                            width="100%" 
                            height="820" 
                            frameborder="0" 
                            marginheight="0" 
                            marginwidth="0"
                            title="Official Volunteer Application Form">
                        Loading application form...
                    </iframe>
                </div>
                <div class="fallback-note mt-3">
                    <p class="text-muted">If the embedded form does not display in your browser, please <a href="https://forms.gle/WL4mJWV7Gi2GaAT38" target="_blank" rel="noopener" class="text-primary font-bold">click here to open the Google Form directly</a>.</p>
                </div>
            </div>
        </div>

        <!-- Volunteer FAQs -->
        <div class="faq-accordion">
            <h3 class="mb-3">Frequently Asked Questions for Volunteers</h3>
            <div class="faq-item">
                <button class="faq-question">What is the minimum time commitment required?</button>
                <div class="faq-answer">
                    <p>We ask for a minimum commitment of 2 to 4 hours per week for at least 4 weeks to ensure consistency, especially for children in our study pods.</p>
                </div>
            </div>
            <div class="faq-item">
                <button class="faq-question">Where are the field activities held?</button>
                <div class="faq-answer">
                    <p>Primary field activities take place in Village Neelwal and Tikri Kalan, West Delhi (nearest Metro: Tikri Kalan on the Green Line).</p>
                </div>
            </div>
            <div class="faq-item">
                <button class="faq-question">Can college students complete mandatory internship hours here?</button>
                <div class="faq-answer">
                    <p>Yes! We sign official internship completion letters and provide detailed work verification for university requirements.</p>
                </div>
            </div>
        </div>
    </div>
</section>
'''

render_page(
    filename="volunteer.html",
    active_nav="involved",
    title="Volunteer With Us | Official Registration Form",
    meta_desc="Volunteer with Enlighting Humanity Trust in New Delhi. Teach children, plant native trees, or support digital media. Direct Google Form application.",
    content_html=volunteer_content
)

# -------------------------------------------------------------
# 15. PARTNER.HTML
# -------------------------------------------------------------
partner_content = '''
<div class="page-banner">
    <div class="container">
        <ul class="breadcrumbs">
            <li><a href="index.html">Home</a></li>
            <li><a href="volunteer.html">Get Involved</a></li>
            <li>Partner With Us</li>
        </ul>
        <h1 class="page-banner-title">Partner With Us</h1>
        <p class="page-banner-sub">Collaborating with academic institutions, youth networks, and civil society organizations to multiply grassroots impact.</p>
    </div>
</div>

<section class="section">
    <div class="container">
        <div class="grid-2-col align-center mb-5">
            <div>
                <span class="section-tag">Institutional Alliances</span>
                <h2 class="section-title">Collective Action for Deeper Community Roots</h2>
                <p class="lead-text">
                    Solving complex structural challenges requires collective power. Enlighting Humanity Trust partners with schools, colleges, universities, NSS / NCC units, and civil society organizations across Delhi-NCR.
                </p>
                <p>
                    By combining your institution's intellectual capital and student enthusiasm with our 9+ years of established ground relationships in Village Neelwal and Tikri Kalan, we design high-impact social initiatives.
                </p>
                <div class="mt-4">
                    <a href="#partner-inquiry" class="btn btn-primary">Initiate Partnership Dialogue</a>
                    <a href="tel:+919654518368" class="btn btn-outline ml-2">Call: +91 9654518368</a>
                </div>
            </div>
            <div>
                <img src="assets/images/community-drive.jpg" alt="Partner meeting with community elders" class="rounded-img shadow-lg">
            </div>
        </div>

        <div class="grid-3-col mb-5">
            <div class="feature-card">
                <div class="feature-icon">🎓</div>
                <h3>Colleges & NSS Units</h3>
                <p>Organize on-campus donation drives (books, stationery, warm clothing) and weekend volunteer delegations for field tutoring and tree planting.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🏫</div>
                <h3>Schools & Youth Clubs</h3>
                <p>Engage your students in empathy-building visits, tree plantation drives, and peer-to-peer book sharing with underprivileged children.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🤝</div>
                <h3>Sister NGOs & Foundations</h3>
                <p>Joint execution of medical camps, specialized legal counseling, or co-hosting women's vocational craft exhibitions.</p>
            </div>
        </div>

        <div class="partner-form-box bg-light p-5 rounded" id="partner-inquiry">
            <h3 class="text-center mb-3">Institutional Partnership Inquiry</h3>
            <p class="text-center text-muted mb-4">Are you representing a college, NGO, or school? Connect with our Trustee desk.</p>
            <div class="text-center">
                <p><strong>Managing Trustee:</strong> Nitin Gothwal</p>
                <p><strong>Direct Phone / WhatsApp:</strong> <a href="tel:+919654518368">+91 9654518368</a></p>
                <p><strong>Official Email:</strong> <a href="mailto:nitingothwal5468@gmail.com">nitingothwal5468@gmail.com</a></p>
                <p><strong>Trust Email:</strong> <a href="mailto:enlightinghumanitytrust@gmail.com">enlightinghumanitytrust@gmail.com</a></p>
                <p class="mt-3">
                    <a href="https://wa.me/919654518368?text=Hello%20Enlighting%20Humanity%20Trust%2C%20we%20want%20to%20partner%20with%20your%20NGO" target="_blank" rel="noopener" class="btn btn-secondary">
                        Chat Directly on WhatsApp
                    </a>
                </p>
            </div>
        </div>
    </div>
</section>
'''

render_page(
    filename="partner.html",
    active_nav="involved",
    title="Partner With Us | Institutional & Academic Alliances",
    meta_desc="Collaborate with Enlighting Humanity Trust. Partnerships for colleges, NSS units, schools, and NGOs in New Delhi.",
    content_html=partner_content
)

# -------------------------------------------------------------
# 16. CSR.HTML
# -------------------------------------------------------------
csr_content = '''
<div class="page-banner">
    <div class="container">
        <ul class="breadcrumbs">
            <li><a href="index.html">Home</a></li>
            <li><a href="volunteer.html">Get Involved</a></li>
            <li>Corporate CSR Partnerships</li>
        </ul>
        <h1 class="page-banner-title">Corporate Social Responsibility (CSR)</h1>
        <p class="page-banner-sub">Impactful, compliant CSR solutions aligned with Section 135 and Schedule VII of the Indian Companies Act, 2013.</p>
    </div>
</div>

<section class="section">
    <div class="container">
        <div class="grid-2-col align-center mb-5">
            <div>
                <span class="section-tag">Statutory Corporate Alignment</span>
                <h2 class="section-title">Measurable, Audited CSR Implementation in Delhi-NCR</h2>
                <p class="lead-text">
                    For corporate partners seeking genuine on-the-ground execution, <strong>Enlighting Humanity Trust</strong> provides end-to-end CSR implementation backed by strict statutory compliance, photographic reporting, and audited utilization certificates.
                </p>
                <p>
                    All our initiatives are mapped directly to Schedule VII of the Companies Act, 2013. We work with corporate CSR committees to structure clear Memorandums of Understanding (MoU), defined KPIs, baseline surveys, and periodic milestone audits.
                </p>
                <div class="mt-3">
                    <a href="#csr-form-section" class="btn btn-primary">Submit CSR Inquiry</a>
                    <a href="transparency.html" class="btn btn-outline ml-2">Inspect Governance Records</a>
                </div>
            </div>
            <div>
                <div class="p-4 bg-light rounded shadow-sm">
                    <h4 class="mb-3">Corporate Compliance Highlights</h4>
                    <ul class="custom-check-list">
                        <li><strong>Registration:</strong> Public Charitable Trust under Indian Trusts Act, 1882.</li>
                        <li><strong>NGO Darpan:</strong> Verified registered on NITI Aayog Portal.</li>
                        <li><strong>12A & 80G Certified:</strong> Income Tax Act compliance ensuring 50% tax deduction for corporate grants.</li>
                        <li><strong>Audited Books:</strong> Annual accounts certified by independent Chartered Accountants.</li>
                        <li><strong>Direct Impact:</strong> Over 9 years of grassroots experience in West Delhi.</li>
                    </ul>
                </div>
            </div>
        </div>

        <!-- Schedule VII Mapping Grid -->
        <div class="schedule-vii-box mb-5">
            <div class="section-header text-center mb-4">
                <span class="section-tag">Schedule VII Alignment</span>
                <h2 class="section-title">Eligible CSR Focus Areas</h2>
                <p class="section-desc">Partner with us across core areas approved under Section 135 of the Companies Act.</p>
            </div>

            <div class="grid-3-col">
                <div class="feature-card">
                    <span class="text-primary font-bold">Clause (i)</span>
                    <h4>Eradicating Hunger & Malnutrition</h4>
                    <p>Hot meals and monthly dry ration distributions for migrant laborers and nutritional packs for children via Project Annapurna.</p>
                </div>
                <div class="feature-card">
                    <span class="text-primary font-bold">Clause (ii)</span>
                    <h4>Promoting Education</h4>
                    <p>Remedial learning pods, school starter kits, digital literacy labs, and dropout re-enrollment campaigns.</p>
                </div>
                <div class="feature-card">
                    <span class="text-primary font-bold">Clause (iii)</span>
                    <h4>Empowering Women & Gender Equality</h4>
                    <p>Vocational sewing training, micro-enterprise support, and adolescent menstrual hygiene initiatives.</p>
                </div>
                <div class="feature-card">
                    <span class="text-primary font-bold">Clause (iv)</span>
                    <h4>Environmental Sustainability</h4>
                    <p>Monthly native tree plantation drives (20+ trees/mo), agroforestry, and environmental education with children.</p>
                </div>
                <div class="feature-card">
                    <span class="text-primary font-bold">Clause (ii)</span>
                    <h4>Vocational Skills & Livelihood</h4>
                    <p>Computer literacy, basic IT software, spoken English, and job-readiness for underprivileged youth.</p>
                </div>
                <div class="feature-card">
                    <span class="text-primary font-bold">Clause (x)</span>
                    <h4>Rural Community Development</h4>
                    <p>Apna Aangan flagship community center infrastructure, clean drinking water, and village health camps.</p>
                </div>
            </div>
        </div>

        <!-- Native CSR Inquiry Form -->
        <div class="csr-form-card bg-light p-5 rounded shadow" id="csr-form-section">
            <div class="section-header text-center mb-4">
                <span class="section-tag">Direct Corporate Desk</span>
                <h2 class="section-title">Submit a Corporate CSR Partnership Inquiry</h2>
                <p class="section-desc">Our Managing Trustee and compliance team will review your proposal and respond within 24 to 48 hours.</p>
            </div>

            <form id="csrEnquiryForm" class="csr-form">
                <div class="form-row">
                    <div class="form-group">
                        <label for="csrCompany" class="form-label">Company / Organization Name *</label>
                        <input type="text" id="csrCompany" class="form-control" placeholder="e.g., Acme Technologies Pvt. Ltd." required>
                    </div>
                    <div class="form-group">
                        <label for="csrPerson" class="form-label">Contact Person Name *</label>
                        <input type="text" id="csrPerson" class="form-control" placeholder="e.g., Ananya Sharma" required>
                    </div>
                </div>

                <div class="form-row">
                    <div class="form-group">
                        <label for="csrDesignation" class="form-label">Designation / Role</label>
                        <input type="text" id="csrDesignation" class="form-control" placeholder="e.g., CSR Head / HR Director">
                    </div>
                    <div class="form-group">
                        <label for="csrEmail" class="form-label">Official Corporate Email *</label>
                        <input type="email" id="csrEmail" class="form-control" placeholder="name@company.com" required>
                    </div>
                </div>

                <div class="form-row">
                    <div class="form-group">
                        <label for="csrPhone" class="form-label">Contact Mobile Number *</label>
                        <input type="tel" id="csrPhone" class="form-control" placeholder="+91 98765 43210" required>
                    </div>
                    <div class="form-group">
                        <label for="csrWebsite" class="form-label">Company Website URL</label>
                        <input type="url" id="csrWebsite" class="form-control" placeholder="https://company.com">
                    </div>
                </div>

                <div class="form-row">
                    <div class="form-group">
                        <label for="csrProject" class="form-label">Preferred CSR Focus Area *</label>
                        <select id="csrProject" class="form-control" required>
                            <option value="">-- Select Focus Area --</option>
                            <option value="Food Alleviation (Project Annapurna)">Food Alleviation (Project Annapurna)</option>
                            <option value="Child Education & Remedial Pods">Child Education & Remedial Pods</option>
                            <option value="Women Empowerment & Tailoring">Women Empowerment & Tailoring</option>
                            <option value="Youth Skill Development & Computers">Youth Skill Development & Computers</option>
                            <option value="Environment & Tree Plantation (20/Mo)">Environment & Tree Plantation (20/Mo)</option>
                            <option value="Apna Aangan Community Infrastructure">Apna Aangan Community Infrastructure</option>
                            <option value="General CSR Grant">General CSR Grant</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="csrPartnershipType" class="form-label">Type of Partnership</label>
                        <select id="csrPartnershipType" class="form-control">
                            <option value="Direct Grant / Project Sponsorship">Direct Grant / Project Sponsorship</option>
                            <option value="Employee Volunteering Engagement">Employee Volunteering Engagement</option>
                            <option value="In-Kind Donations (Computers, Solar)">In-Kind Donations (Computers, Solar)</option>
                            <option value="Multi-Year Strategic Alliance">Multi-Year Strategic Alliance</option>
                        </select>
                    </div>
                </div>

                <div class="form-group mb-3">
                    <label for="csrBudget" class="form-label">Estimated CSR Budget Range (Optional)</label>
                    <input type="text" id="csrBudget" class="form-control" placeholder="e.g., ₹2,00,000 to ₹10,00,000">
                </div>

                <div class="form-group mb-3">
                    <label for="csrMessage" class="form-label">Specific Objectives or Project Requirements</label>
                    <textarea id="csrMessage" rows="4" class="form-control" placeholder="Share your CSR committee's vision, employee count, or preferred timeline..."></textarea>
                </div>

                <div class="form-check mb-4">
                    <input type="checkbox" id="csrConsent" class="form-check-input" required>
                    <label for="csrConsent" class="form-check-label small text-muted">
                        I confirm that I represent this organization and consent to Enlighting Humanity Trust contacting me regarding this CSR collaboration proposal.
                    </label>
                </div>

                <div class="text-center">
                    <button type="submit" id="csrSubmitBtn" class="btn btn-primary btn-lg">Submit Official CSR Inquiry</button>
                </div>

                <div id="csrStatusMessage" class="mt-3 text-center" style="display:none;"></div>
            </form>
        </div>
    </div>
</section>
'''

render_page(
    filename="csr.html",
    active_nav="involved",
    title="Corporate CSR | Schedule VII Compliant Partnerships",
    meta_desc="Partner with Enlighting Humanity Trust for Corporate Social Responsibility (CSR). Aligned with Schedule VII, Section 135 of Companies Act, 80G certified.",
    content_html=csr_content
)

# -------------------------------------------------------------
# 17. DONATE.HTML
# -------------------------------------------------------------
donate_content = '''
<div class="page-banner">
    <div class="container">
        <ul class="breadcrumbs">
            <li><a href="index.html">Home</a></li>
            <li>Donate Now</li>
        </ul>
        <h1 class="page-banner-title">Make a Contribution</h1>
        <p class="page-banner-sub">Your generosity directly feeds hungry families, educates out-of-school children, and plants native trees in Delhi-NCR.</p>
    </div>
</div>

<section class="section">
    <div class="container">
        <div class="donation-master-grid">
            <!-- Left Column: Dynamic Interactive Engine -->
            <div class="donation-main-col">
                <div class="donation-card-box p-4 bg-white rounded shadow">
                    <div class="donation-header mb-4">
                        <span class="badge-accent">Instant Tax Exemption Under Section 80G</span>
                        <h2 class="mt-2">Online UPI Contribution Engine</h2>
                        <p class="text-muted">Zero platform fees. 100% of your funds go directly into our verified public charitable trust bank account.</p>
                    </div>

                    <!-- Step 1: Program -->
                    <div class="form-group mb-4">
                        <label class="form-label font-bold">1. Select Program to Support:</label>
                        <select id="campaignSelect" class="form-control">
                            <option value="General Donation">General Donation (Where Most Urgently Needed)</option>
                            <option value="Food for Hunger">Food for Hunger (Project Annapurna)</option>
                            <option value="Child Education">Child Education & Remedial Pods</option>
                            <option value="Women Empowerment">Women Empowerment & Stitching Center</option>
                            <option value="Youth Skill Development">Youth Skill & Computer Training</option>
                            <option value="Environment Tree Plantation">Environment & Tree Plantation (20 Trees/Mo)</option>
                            <option value="Apna Aangan Hub">Apna Aangan Community Center</option>
                        </select>
                    </div>

                    <!-- Step 2: Amount Selector -->
                    <div class="form-group mb-4">
                        <label class="form-label font-bold">2. Choose Donation Amount (INR):</label>
                        <div class="amount-pills-wrap">
                            <button type="button" class="amount-pill" data-amount="101">₹101</button>
                            <button type="button" class="amount-pill" data-amount="251">₹251</button>
                            <button type="button" class="amount-pill active" data-amount="501">₹501</button>
                            <button type="button" class="amount-pill" data-amount="1001">₹1,001</button>
                            <button type="button" class="amount-pill" data-amount="2501">₹2,501</button>
                            <button type="button" class="amount-pill" data-amount="custom">Custom</button>
                        </div>
                        <input type="number" id="customAmountInput" class="form-control mt-2" placeholder="Enter custom amount in ₹ (e.g. 5000)" style="display:none;" min="50" step="50">
                    </div>

                    <!-- Impact Context Note -->
                    <div class="impact-display-box mb-4">
                        <div class="display-val current-amount-display">₹501</div>
                        <p class="display-desc">
                            Provides 15 days of wholesome dry rations (Atta, Rice, Dal, Oil) for a migrant family or a complete school starter kit for an underprivileged student.
                        </p>
                    </div>

                    <!-- Step 3: Payment Panel -->
                    <div class="payment-action-panel p-4 bg-light rounded text-center">
                        <h4 class="mb-2">Scan & Pay via Any UPI App</h4>
                        <p class="small text-muted mb-3">Compatible with Paytm, PhonePe, Google Pay, BHIM, Cred, and all mobile banking apps.</p>
                        
                        <div id="qrcodeCanvas" class="qr-canvas-holder mb-3"></div>

                        <div class="upi-id-row mb-3">
                            <span class="upi-label">Verified UPI ID:</span>
                            <span class="upi-value" id="displayUpiId">9654518368@paytm</span>
                            <button type="button" class="btn-copy-sm" onclick="copyUpiId()">Copy UPI ID</button>
                            <span id="copyFeedback" class="copy-alert" style="display:none;">Copied!</span>
                        </div>

                        <!-- One Click Mobile Pay Button -->
                        <div class="mobile-pay-wrap mb-3">
                            <a id="directUpiBtn" href="upi://pay?pa=9654518368@paytm&pn=Enlighting%20Humanity%20Trust&am=501.00&cu=INR&tn=Donation" class="btn btn-primary btn-block btn-lg">
                                📱 Tap to Pay on Mobile UPI App
                            </a>
                        </div>

                        <div class="tax-receipt-reminder">
                            <p class="small text-muted">
                                <strong>⚠️ Important:</strong> Opening a UPI app does not automatically confirm transaction completion. Please save your <strong>12-digit UTR/Transaction Reference Number</strong> or share a screenshot on WhatsApp at <strong>+91 9654518368</strong> or email <strong>nitingothwal5468@gmail.com</strong> to receive your signed 80G tax exemption receipt.
                            </p>
                        </div>
                    </div>

                    <!-- Step 4: Donor Notice Form -->
                    <div class="donor-details-panel mt-4 p-4 border rounded">
                        <h4 class="mb-2">Claim Your Official 80G Tax Receipt</h4>
                        <p class="small text-muted mb-3">Submit your details so our accounts desk can issue your 80G certificate promptly.</p>
                        
                        <form id="donorNoticeForm" onsubmit="submitDonorNotice(event)">
                            <div class="form-row">
                                <div class="form-group">
                                    <label for="donorName" class="form-label">Full Name *</label>
                                    <input type="text" id="donorName" class="form-control" placeholder="As per PAN card" required>
                                </div>
                                <div class="form-group">
                                    <label for="donorPhone" class="form-label">WhatsApp Mobile Number *</label>
                                    <input type="tel" id="donorPhone" class="form-control" placeholder="+91 9876543210" required>
                                </div>
                            </div>

                            <div class="form-row">
                                <div class="form-group">
                                    <label for="donorEmail" class="form-label">Email Address *</label>
                                    <input type="email" id="donorEmail" class="form-control" placeholder="name@email.com" required>
                                </div>
                                <div class="form-group">
                                    <label for="donorTxnId" class="form-label">12-Digit UPI UTR / Reference ID</label>
                                    <input type="text" id="donorTxnId" class="form-control" placeholder="e.g., 432109876543">
                                </div>
                            </div>

                            <button type="submit" class="btn btn-secondary btn-block">Submit Donation Notification</button>
                            <div id="donorSubmitSuccess" class="form-status-alert status-success mt-3" style="display:none;"></div>
                        </form>
                    </div>
                </div>
            </div>

            <!-- Right Column: Bank Details & Trust Transparency -->
            <div class="donation-sidebar-col">
                <!-- Bank Transfer Box -->
                <div class="bank-details-box p-4 bg-light rounded shadow-sm mb-4">
                    <h3 class="mb-3">Direct Bank Transfer (NEFT / RTGS / IMPS)</h3>
                    <p class="small text-muted mb-3">For large contributions, institutional grants, or donors preferring direct bank wire transfer:</p>
                    
                    <ul class="bank-info-list">
                        <li><strong>Account Name:</strong> Enlighting Humanity Trust</li>
                        <li><strong>Bank Name:</strong> State Bank of India / Paytm Payments Bank</li>
                        <li><strong>Account Number:</strong> 9654518368</li>
                        <li><strong>IFSC Code:</strong> PYTM0123456</li>
                        <li><strong>Account Type:</strong> Current Account (Charitable Trust)</li>
                        <li><strong>Branch:</strong> New Delhi Branch</li>
                    </ul>
                    <p class="small text-muted mt-2">
                        <em>After completing your NEFT/RTGS transfer, kindly email transaction confirmation to nitingothwal5468@gmail.com for receipt dispatch.</em>
                    </p>
                </div>

                <!-- 80G Tax Benefit Details -->
                <div class="tax-benefit-box p-4 bg-white border rounded shadow-sm mb-4">
                    <h3 class="mb-2">Tax Exemption (Section 80G)</h3>
                    <p class="small text-muted">
                        All Indian citizens and corporations donating to Enlighting Humanity Trust are entitled to a <strong>50% tax deduction</strong> under Section 80G of the Income Tax Act, 1961.
                    </p>
                    <ul class="custom-check-list small mt-2">
                        <li>Official 80G certificate issued with Trust registration number.</li>
                        <li>Receipt sent directly to your email and WhatsApp within 24 hours.</li>
                        <li>Valid for Income Tax return (ITR) filing across India.</li>
                    </ul>
                </div>

                <!-- Direct Help Desk -->
                <div class="help-desk-box p-4 bg-primary text-white rounded">
                    <h4 class="mb-2">Need Help with Donation?</h4>
                    <p class="small mb-3">Our Managing Trustee, Nitin Gothwal, is available directly to assist you with any questions.</p>
                    <p class="mb-1">📞 <strong>Phone:</strong> <a href="tel:+919654518368" class="text-white">+91 9654518368</a></p>
                    <p class="mb-3">💬 <strong>WhatsApp:</strong> <a href="https://wa.me/919654518368?text=Hello%20Enlighting%20Humanity%20Trust" class="text-white">Chat on WhatsApp</a></p>
                    <p class="small opacity-75">Village Neelwal, PO Tikri Kalan, New Delhi – 110041</p>
                </div>
            </div>
        </div>
    </div>
</section>
'''

render_page(
    filename="donate.html",
    active_nav="donate",
    title="Donate Online | Dynamic UPI & 80G Tax Exemption",
    meta_desc="Donate to Enlighting Humanity Trust via instant UPI (9654518368@paytm), QR code, or NEFT/RTGS bank transfer. All contributions eligible for 80G tax exemption.",
    content_html=donate_content
)

print("Batch 3 (Pages 13-17) completed successfully.")
