#!/usr/bin/env python3
"""
Enlighting Humanity Trust - Master Page Builder
Generates all 24 production-ready pages with authentic text, rich layout,
and full functional hooks.
"""

import os
from generator_base import render_page

print("Starting full generation of 24 pages...")

# -------------------------------------------------------------
# 1. INDEX.HTML (Home)
# -------------------------------------------------------------
home_content = '''
<!-- Hero Section -->
<section class="hero-section" style="background-image: linear-gradient(rgba(16, 55, 41, 0.88), rgba(22, 75, 54, 0.82)), url('assets/images/hero-banner.jpg');">
    <div class="container hero-inner">
        <div class="hero-content">
            <span class="hero-badge">Empowering Underprivileged Communities in New Delhi</span>
            <h1 class="hero-title">Empowering Lives, Enriching Humanity.</h1>
            <p class="hero-subtitle">
                A registered grassroots public trust dedicated to eradicating hunger, providing quality education, fostering women self-reliance, youth skills, and environmental conservation in Delhi-NCR since 2017.
            </p>
            <div class="hero-actions">
                <a href="donate.html" class="btn btn-primary btn-lg">Donate Online (UPI)</a>
                <a href="our-work.html" class="btn btn-outline btn-lg">Explore Our Programs</a>
                <a href="volunteer.html" class="btn btn-secondary btn-lg">Join As Volunteer</a>
            </div>
            <div class="hero-highlights">
                <span>✓ 80G Tax Exemption</span>
                <span>✓ Direct UPI: 9654518368@paytm</span>
                <span>✓ 100% Grassroots Focused</span>
            </div>
        </div>
    </div>
</section>

<!-- Impact Stats Ribbon -->
<section class="stats-ribbon">
    <div class="container">
        <div class="stats-grid">
            <div class="stat-card">
                <span class="stat-number">9+</span>
                <span class="stat-label">Years of Grassroots Action</span>
                <span class="stat-sub">Active since 2017</span>
            </div>
            <div class="stat-card">
                <span class="stat-number">20+</span>
                <span class="stat-label">Trees Planted Every Month</span>
                <span class="stat-sub">Hands-on with local children</span>
            </div>
            <div class="stat-card">
                <span class="stat-number">6</span>
                <span class="stat-label">Core Lifeline Programs</span>
                <span class="stat-sub">Holistic community support</span>
            </div>
            <div class="stat-card">
                <span class="stat-number">100%</span>
                <span class="stat-label">Programmatic Direct Allocation</span>
                <span class="stat-sub">Zero administrative waste</span>
            </div>
        </div>
    </div>
</section>

<!-- Founder Message & About Spotlight -->
<section class="section about-spotlight">
    <div class="container">
        <div class="grid-2-col align-center">
            <div class="about-img-wrap">
                <img src="assets/images/community-drive.jpg" alt="Enlighting Humanity Trust community drive in Neelwal" class="rounded-img shadow-lg" loading="lazy">
                <div class="img-badge">
                    <span class="badge-num">2017</span>
                    <span class="badge-text">Founded in Tikri Kalan, Delhi</span>
                </div>
            </div>
            <div class="about-text-content">
                <span class="section-tag">About Our Foundation</span>
                <h2 class="section-title">Rooted in Grassroots Empathy, Driven by Measurable Change</h2>
                <p class="lead-text">
                    "True empowerment does not come from charity from afar, but from standing shoulder to shoulder with the most marginalized families in our villages and resettlement clusters."
                </p>
                <p>
                    Established under the Indian Trusts Act in West Delhi, <strong>Enlighting Humanity Trust</strong> works directly at ground level in Village Neelwal, Post Office Tikri Kalan, and surrounding semi-urban clusters. Founded by <strong>Nitin Gothwal</strong>, our organization is committed to transparent social service where every rupee, hour, and resource directly reaches those who need it most.
                </p>
                <div class="feature-bullets">
                    <div class="feature-item">
                        <span class="bullet-icon">🌾</span>
                        <div>
                            <strong>Daily & Weekly Nutrition</strong>
                            <p>Ensuring no child or migrant worker goes to sleep hungry through Project Annapurna.</p>
                        </div>
                    </div>
                    <div class="feature-item">
                        <span class="bullet-icon">📚</span>
                        <div>
                            <strong>Grassroots Learning Pods</strong>
                            <p>Remedial after-school classes, stationery kits, and school re-enrollment drives.</p>
                        </div>
                    </div>
                    <div class="feature-item">
                        <span class="bullet-icon">🌱</span>
                        <div>
                            <strong>Environmental Pledge</strong>
                            <p>Engaging school children to plant and nurture at least 20 native trees every single month.</p>
                        </div>
                    </div>
                </div>
                <div class="mt-4">
                    <a href="about.html" class="btn btn-outline">Read Our Full Story &rarr;</a>
                    <a href="transparency.html" class="btn btn-secondary ml-2">Trust Governance</a>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Core Programs Grid -->
<section class="section bg-light" id="programs">
    <div class="container">
        <div class="section-header text-center">
            <span class="section-tag">What We Do</span>
            <h2 class="section-title">Our Six Pillars of Community Transformation</h2>
            <p class="section-desc">
                From emergency food relief to long-term vocational independence, our initiatives address the multi-dimensional challenges of underprivileged communities.
            </p>
        </div>

        <div class="cards-grid">
            <!-- Program 1 -->
            <div class="program-card">
                <div class="card-icon">🍲</div>
                <h3 class="card-title">Food for Hunger</h3>
                <p class="card-text">
                    Daily hot meals and monthly dry ration kits (wheat flour, pulses, cooking oil, rice) for daily-wage migrant families and vulnerable elderly citizens.
                </p>
                <ul class="card-list">
                    <li>✓ Weekly cooked meal drives</li>
                    <li>✓ Dry ration kits for migrant families</li>
                    <li>✓ Child nutrition supplement packs</li>
                </ul>
                <div class="card-footer">
                    <a href="food-for-hunger.html" class="card-link">Learn More &rarr;</a>
                    <a href="donate.html?campaign=food" class="btn-text-donate">Sponsor a Meal</a>
                </div>
            </div>

            <!-- Program 2 -->
            <div class="program-card">
                <div class="card-icon">📖</div>
                <h3 class="card-title">Child Education & Welfare</h3>
                <p class="card-text">
                    Remedial tutoring, foundational literacy, and distribution of school bags, notebooks, and learning materials to keep underprivileged children in school.
                </p>
                <ul class="card-list">
                    <li>✓ Remedial after-school coaching</li>
                    <li>✓ School dropout re-enrollment</li>
                    <li>✓ Annual stationery distribution kits</li>
                </ul>
                <div class="card-footer">
                    <a href="education.html" class="card-link">Learn More &rarr;</a>
                    <a href="donate.html?campaign=education" class="btn-text-donate">Support a Student</a>
                </div>
            </div>

            <!-- Program 3 -->
            <div class="program-card">
                <div class="card-icon">🧵</div>
                <h3 class="card-title">Women Empowerment</h3>
                <p class="card-text">
                    Vocational stitching and tailoring workshops, financial literacy circles, and free menstrual hygiene product distribution drives for village women.
                </p>
                <ul class="card-list">
                    <li>✓ Certified tailoring & stitching batches</li>
                    <li>✓ Self-Help Group (SHG) micro-finance</li>
                    <li>✓ Menstrual health & sanitary pad drives</li>
                </ul>
                <div class="card-footer">
                    <a href="women-empowerment.html" class="card-link">Learn More &rarr;</a>
                    <a href="donate.html?campaign=women" class="btn-text-donate">Empower a Woman</a>
                </div>
            </div>

            <!-- Program 4 -->
            <div class="program-card">
                <div class="card-icon">💻</div>
                <h3 class="card-title">Youth Skill Development</h3>
                <p class="card-text">
                    Basic computer applications, digital literacy, spoken English, and customer service readiness for unemployed youths to secure stable livelihoods.
                </p>
                <ul class="card-list">
                    <li>✓ Digital computer workstations</li>
                    <li>✓ Spoken English & interview prep</li>
                    <li>✓ Resume building and placement support</li>
                </ul>
                <div class="card-footer">
                    <a href="skill-development.html" class="card-link">Learn More &rarr;</a>
                    <a href="donate.html?campaign=skills" class="btn-text-donate">Sponsor Training</a>
                </div>
            </div>

            <!-- Program 5 -->
            <div class="program-card">
                <div class="card-icon">🌳</div>
                <h3 class="card-title">Environment (20 Trees/Mo)</h3>
                <p class="card-text">
                    Our verifiable ecological commitment: planting a minimum of 20 native trees every single month with local school children, complete with tree guards and care.
                </p>
                <ul class="card-list">
                    <li>✓ Native shade & fruit saplings (Peepal, Neem)</li>
                    <li>✓ Hands-on student tree guardianship</li>
                    <li>✓ Cleanliness & anti-plastic campaigns</li>
                </ul>
                <div class="card-footer">
                    <a href="environment.html" class="card-link">Learn More &rarr;</a>
                    <a href="donate.html?campaign=environment" class="btn-text-donate">Plant a Tree (₹251)</a>
                </div>
            </div>

            <!-- Program 6 -->
            <div class="program-card highlighted-card">
                <div class="card-icon">🏡</div>
                <h3 class="card-title">Apna Aangan Community Hub</h3>
                <p class="card-text">
                    Our signature grassroots sanctuary in West Delhi — a multi-purpose safe haven providing a children's library, women's training room, and wellness checkup space.
                </p>
                <ul class="card-list">
                    <li>✓ Community library & study desk</li>
                    <li>✓ Safe space for women's workshops</li>
                    <li>✓ Free medical checkup camps</li>
                </ul>
                <div class="card-footer">
                    <a href="apna-aangan.html" class="card-link">Discover The Center &rarr;</a>
                    <a href="donate.html?campaign=aangan" class="btn-text-donate">Build Apna Aangan</a>
                </div>
            </div>
        </div>

        <div class="text-center mt-4">
            <a href="our-work.html" class="btn btn-primary">View Comprehensive Programs Overview</a>
        </div>
    </div>
</section>

<!-- Hands-on Tree Plantation Spotlight -->
<section class="section tree-feature-section">
    <div class="container">
        <div class="grid-2-col align-center">
            <div class="feature-content">
                <span class="section-tag">Signature Environmental Pledge</span>
                <h2 class="section-title">20 Native Trees Every Month, Planted with Local Children</h2>
                <p>
                    Rather than ceremonial one-day plantation stunts, Enlighting Humanity Trust runs a continuous, disciplined ecological drive. Every month, rain or shine, we gather village children, teachers, and volunteers to plant at least 20 native trees (Neem, Peepal, Jamun, Shisham) across Village Neelwal, Tikri Kalan, and rural schools.
                </p>
                <div class="stat-highlight-box">
                    <div class="highlight-val">240+</div>
                    <div class="highlight-text">
                        <strong>Native trees planted each year</strong>
                        <p>Protected with durable tree guards and adopted by student "Tree Buddies" for 100% survival rate.</p>
                    </div>
                </div>
                <ul class="custom-check-list">
                    <li>Native drought-resistant species suited to Delhi's soil.</li>
                    <li>Geotagged monitoring and regular watering schedules.</li>
                    <li>Instilling lifetime environmental empathy in next-generation leaders.</li>
                </ul>
                <div class="mt-3">
                    <a href="environment.html" class="btn btn-primary">Learn About The Green Mission</a>
                    <a href="donate.html?campaign=environment" class="btn btn-secondary ml-2">Sponsor Saplings (₹251/tree)</a>
                </div>
            </div>
            <div class="feature-media">
                <img src="assets/images/tree-planting-children.jpg" alt="Children planting native trees in Village Neelwal with Enlighting Humanity Trust" class="rounded-img shadow-lg">
                <p class="img-caption">Authentic Field Photo: School children planting saplings during our monthly green drive in Tikri Kalan.</p>
            </div>
        </div>
    </div>
</section>

<!-- Quick Dynamic Donation Box Section -->
<section class="section bg-light" id="donate-box">
    <div class="container">
        <div class="donation-card-wrapper">
            <div class="donation-card-header text-center">
                <span class="section-tag">Direct Grassroots Support</span>
                <h2 class="section-title">Support Our Grassroots Missions Directly</h2>
                <p>100% of your contribution directly funds grassroots programs. Instant tax exemption under Section 80G.</p>
            </div>

            <div class="donation-engine-box">
                <div class="donation-left">
                    <div class="form-group mb-3">
                        <label class="form-label">Select Impact Program:</label>
                        <select id="campaignSelect" class="form-control">
                            <option value="General Donation">General Donation (Where needed most)</option>
                            <option value="Food for Hunger">Food for Hunger (Project Annapurna)</option>
                            <option value="Child Education">Child Education & Remedial Pods</option>
                            <option value="Women Empowerment">Women Empowerment & Self-Reliance</option>
                            <option value="Youth Skill Development">Youth Skill & Computer Center</option>
                            <option value="Environment Tree Plantation">Tree Plantation Drive (20 Trees/Month)</option>
                            <option value="Apna Aangan Hub">Apna Aangan Community Center</option>
                        </select>
                    </div>

                    <div class="form-group mb-3">
                        <label class="form-label">Choose Contribution Amount (INR):</label>
                        <div class="amount-pills-wrap">
                            <button type="button" class="amount-pill" data-amount="101">₹101</button>
                            <button type="button" class="amount-pill" data-amount="251">₹251</button>
                            <button type="button" class="amount-pill active" data-amount="501">₹501</button>
                            <button type="button" class="amount-pill" data-amount="1001">₹1,001</button>
                            <button type="button" class="amount-pill" data-amount="2501">₹2,501</button>
                            <button type="button" class="amount-pill" data-amount="custom">Custom</button>
                        </div>
                        <input type="number" id="customAmountInput" class="form-control mt-2" placeholder="Enter custom amount in ₹" style="display:none;" min="50" step="50">
                    </div>

                    <div class="impact-hint">
                        <strong>Your Impact:</strong> <span class="current-amount-display">₹501</span> provides a month of nutritious food packets or educational study kits for a child.
                    </div>

                    <div class="trust-donor-info mt-3">
                        <p class="small text-muted">
                            🔒 <strong>Official Trust Account:</strong> Enlighting Humanity Trust<br>
                            Direct UPI ID: <strong id="displayUpiId">9654518368@paytm</strong> 
                            <button type="button" class="btn-inline-copy" onclick="copyUpiId()">Copy UPI ID</button>
                            <span id="copyFeedback" class="copy-alert" style="display:none;">Copied!</span>
                        </p>
                    </div>
                </div>

                <div class="donation-right text-center">
                    <div class="qr-panel">
                        <h4 class="qr-title">Scan to Pay via Any UPI App</h4>
                        <div id="qrcodeCanvas" class="qr-canvas-holder"></div>
                        <div class="upi-apps-icons">
                            <span>Paytm</span> • <span>PhonePe</span> • <span>Google Pay</span> • <span>BHIM</span>
                        </div>
                        <a id="directUpiBtn" href="upi://pay?pa=9654518368@paytm&pn=Enlighting%20Humanity%20Trust&am=501.00&cu=INR&tn=Donation" class="btn btn-primary btn-block mt-2">Pay via UPI App (Mobile)</a>
                        <small class="disclaimer-note">
                            Please save your 12-digit UTR number or WhatsApp the screenshot to <strong>+91 9654518368</strong> to receive your 80G tax receipt.
                        </small>
                    </div>
                </div>
            </div>
            
            <div class="text-center mt-3">
                <a href="donate.html" class="link-styled">Looking for Bank NEFT/RTGS details or Cheque options? Visit our Master Donation Page &rarr;</a>
            </div>
        </div>
    </div>
</section>

<!-- Authentic Image Gallery Preview -->
<section class="section">
    <div class="container">
        <div class="section-header text-center">
            <span class="section-tag">Ground Realities</span>
            <h2 class="section-title">Moments of Hope and Collective Action</h2>
            <p class="section-desc">Snapshots of genuine field drives in Village Neelwal, Tikri Kalan, and community centers.</p>
        </div>

        <div class="gallery-preview-grid">
            <div class="gallery-card">
                <img src="assets/images/tree-planting-children.jpg" alt="School children planting native trees" loading="lazy">
                <div class="gallery-info">
                    <h4>Green Delhi Drive</h4>
                    <p>Monthly tree plantation with local village children</p>
                </div>
            </div>
            <div class="gallery-card">
                <img src="assets/images/children-activity.jpg" alt="Children engaged in remedial learning" loading="lazy">
                <div class="gallery-info">
                    <h4>Remedial Education</h4>
                    <p>Foundational literacy and joyful learning sessions</p>
                </div>
            </div>
            <div class="gallery-card">
                <img src="assets/images/community-drive.jpg" alt="Community members gathered for local welfare meeting" loading="lazy">
                <div class="gallery-info">
                    <h4>Community Mobilization</h4>
                    <p>Grassroots dialogue with village elders and parents</p>
                </div>
            </div>
        </div>
        <div class="text-center mt-4">
            <a href="gallery.html" class="btn btn-outline">Explore Full Photo Gallery (40+ Field Moments) &rarr;</a>
        </div>
    </div>
</section>

<!-- Call to Action Banner -->
<section class="cta-banner">
    <div class="container">
        <div class="cta-inner text-center">
            <h2 class="cta-heading">Be The Light in Someone's Journey</h2>
            <p class="cta-sub">
                Whether you volunteer your time, sponsor a child's study kit, or partner with us for corporate CSR, your presence strengthens grassroots India.
            </p>
            <div class="cta-buttons">
                <a href="donate.html" class="btn btn-primary btn-lg">Make a Contribution</a>
                <a href="volunteer.html" class="btn btn-secondary btn-lg">Volunteer With Us</a>
                <a href="csr.html" class="btn btn-outline btn-lg">Corporate CSR Partnerships</a>
            </div>
        </div>
    </div>
</section>
'''

render_page(
    filename="index.html",
    active_nav="home",
    title="Home | Empowering Underprivileged Lives",
    meta_desc="Enlighting Humanity Trust is a registered public charitable trust in New Delhi (Tikri Kalan/Neelwal) focused on hunger relief, education, women empowerment, and planting 20 native trees monthly.",
    content_html=home_content
)

# -------------------------------------------------------------
# 2. ABOUT.HTML
# -------------------------------------------------------------
about_content = '''
<div class="page-banner">
    <div class="container">
        <ul class="breadcrumbs">
            <li><a href="index.html">Home</a></li>
            <li>About Us</li>
        </ul>
        <h1 class="page-banner-title">About Enlighting Humanity Trust</h1>
        <p class="page-banner-sub">A 9+ year grassroots journey founded on radical transparency, human dignity, and ground-level action.</p>
    </div>
</div>

<section class="section">
    <div class="container">
        <div class="grid-2-col align-center mb-5">
            <div>
                <span class="section-tag">Our Founding Story</span>
                <h2 class="section-title">Born in Village Neelwal, Built on Unshakeable Empathy</h2>
                <p class="lead-text">
                    Enlighting Humanity Trust was founded in 2017 by <strong>Nitin Gothwal</strong> in Village Neelwal, Post Office Tikri Kalan, West Delhi. 
                </p>
                <p>
                    Having witnessed first-hand the acute challenges faced by daily-wage migrant laborers, out-of-school children, and neglected green spaces in outer Delhi's urban-rural boundary, our founders resolved to create an organization free of administrative bloat. The philosophy was simple: direct action where the problem exists, not from high-rise offices.
                </p>
                <p>
                    Over nine years, that localized effort has grown into a vibrant grassroots ecosystem touching thousands of lives through sustained hunger alleviation, remedial tutoring, women's self-help groups, youth computer literacy, and an unwavering commitment to plant at least 20 native trees every single month with village school children.
                </p>
            </div>
            <div>
                <img src="assets/images/community-drive.jpg" alt="Trust community meeting" class="rounded-img shadow-lg">
            </div>
        </div>

        <div class="content-box bg-light mb-5">
            <h3 class="mb-3">Organizational Identity & Meaning</h3>
            <p>
                The name <strong>Enlighting Humanity</strong> embodies our fundamental belief: every human soul possesses boundless potential that only requires the right spark of opportunity, nourishment, and dignity to flourish. We do not view underprivileged communities as passive recipients of charity, but as active co-creators of their own liberation.
            </p>
        </div>

        <div class="leadership-section mb-5">
            <div class="section-header text-center">
                <span class="section-tag">Leadership & Governance</span>
                <h2 class="section-title">Stewarded by People of the Soil</h2>
                <p class="section-desc">Our leadership remains directly accessible, accountable, and deeply involved in every field initiative.</p>
            </div>

            <div class="grid-3-col">
                <div class="team-card">
                    <div class="team-avatar">👨‍💼</div>
                    <h3 class="team-name">Nitin Gothwal</h3>
                    <span class="team-role">Founder & Managing Trustee</span>
                    <p class="team-bio">
                        Social visionary and grassroots organizer who established Enlighting Humanity Trust in 2017. He coordinates field operations, donor accountability, and youth mentorship across Tikri Kalan and Neelwal.
                    </p>
                    <p class="team-contact">Direct: <a href="tel:+919654518368">+91 9654518368</a></p>
                </div>

                <div class="team-card">
                    <div class="team-avatar">👩‍🏫</div>
                    <h3 class="team-name">Board of Trustees</h3>
                    <span class="team-role">Strategic Governance & Compliance</span>
                    <p class="team-bio">
                        Comprising community educators, social advocates, and legal advisors ensuring complete statutory adherence under the Indian Trusts Act and Income Tax department guidelines.
                    </p>
                    <p class="team-contact">Email: <a href="mailto:enlightinghumanitytrust@gmail.com">trustees@enlightinghumanity</a></p>
                </div>

                <div class="team-card">
                    <div class="team-avatar">🤝</div>
                    <h3 class="team-name">Grassroots Volunteer Council</h3>
                    <span class="team-role">Field Program Leads</span>
                    <p class="team-bio">
                        Dedicated local youth, college volunteers, and village coordinators who lead the weekly food distributions, study pods, and monthly tree plantation drives.
                    </p>
                    <p class="team-contact"><a href="volunteer.html">Join This Council &rarr;</a></p>
                </div>
            </div>
        </div>

        <div class="accreditation-bar p-4 bg-light rounded shadow-sm text-center">
            <h4 class="mb-2">Statutory Registrations & Legal Standing</h4>
            <p class="text-muted mb-3">Operating strictly under Indian Charitable Laws with complete statutory transparency.</p>
            <div class="badges-row">
                <span class="pill-badge">Indian Trusts Act, 1882 Reg.</span>
                <span class="pill-badge">NITI Aayog NGO Darpan Verified</span>
                <span class="pill-badge">Section 12A Certified</span>
                <span class="pill-badge">Section 80G Tax Exemption</span>
                <span class="pill-badge">PAN & Bank Verified</span>
            </div>
            <div class="mt-3">
                <a href="transparency.html" class="btn btn-outline btn-sm">Inspect Complete Legal & Financial Details &rarr;</a>
            </div>
        </div>
    </div>
</section>
'''

render_page(
    filename="about.html",
    active_nav="about",
    title="About Us | Grassroots Journey Since 2017",
    meta_desc="Learn about the history, leadership, and founding philosophy of Enlighting Humanity Trust, a registered public trust in West Delhi founded by Nitin Gothwal.",
    content_html=about_content
)

# -------------------------------------------------------------
# 3. MISSION.HTML
# -------------------------------------------------------------
mission_content = '''
<div class="page-banner">
    <div class="container">
        <ul class="breadcrumbs">
            <li><a href="index.html">Home</a></li>
            <li><a href="about.html">About Us</a></li>
            <li>Our Mission</li>
        </ul>
        <h1 class="page-banner-title">Our Mission</h1>
        <p class="page-banner-sub">Clear, unwavering commitments that guide every program, rupee, and volunteer hour.</p>
    </div>
</div>

<section class="section">
    <div class="container">
        <div class="mission-manifesto mb-5 text-center">
            <span class="section-tag">The Enlighting Humanity Manifesto</span>
            <h2 class="section-title">Our Core Mission Statement</h2>
            <blockquote class="mission-quote">
                "To catalyze sustainable grassroots transformation by providing reliable nutritional security to the vulnerable, remedial quality education to out-of-school children, self-reliance pathways to marginalized women, career skills for youth, and environmental restoration through consistent monthly tree plantation drives."
            </blockquote>
        </div>

        <div class="grid-2-col mb-5">
            <div class="feature-card">
                <h3>1. Zero Hunger & Nutritional Dignity</h3>
                <p>
                    We believe that hunger is the most immediate barrier to human potential. Our mission is to maintain daily and weekly cooked food lines and provide essential dry ration hampers so that no child or laborer in our target clusters experiences sleep-depriving malnutrition.
                </p>
            </div>
            <div class="feature-card">
                <h3>2. Universal Remedial Learning</h3>
                <p>
                    Every child deserves the basic foundation of literacy, numeracy, and critical thinking. We bridge the educational gap for first-generation learners from migrant families who otherwise drop out due to lack of after-school academic support.
                </p>
            </div>
            <div class="feature-card">
                <h3>3. Economic Autonomy for Women</h3>
                <p>
                    Empowering women is the most effective antidote to systemic household poverty. Our mission provides certified tailoring, stitching, and financial literacy to give rural women their own independent source of income and dignity.
                </p>
            </div>
            <div class="feature-card">
                <h3>4. Youth Employability & Digital Skills</h3>
                <p>
                    We train underprivileged youths in practical computer skills, spoken English, and job-readiness to transition them from precarious informal labor into dignified, organized employment.
                </p>
            </div>
            <div class="feature-card">
                <h3>5. Continuous Ecological Stewardship</h3>
                <p>
                    We take climate action directly to the soil. Planting a minimum of 20 native trees every single month with village school children nurtures green cover and instills generational ecological consciousness.
                </p>
            </div>
            <div class="feature-card">
                <h3>6. Apna Aangan Community Sanctuary</h3>
                <p>
                    Establishing multi-purpose community resource centers where children study in peace, women conduct livelihood workshops, and health awareness camps are held free of charge.
                </p>
            </div>
        </div>

        <div class="strategic-roadmap bg-light p-4 rounded">
            <h3 class="mb-3 text-center">Strategic Goals (2024 – 2027)</h3>
            <div class="roadmap-grid">
                <div class="roadmap-item">
                    <span class="roadmap-year">Goal 1</span>
                    <h4>500+ Children Enrolled</h4>
                    <p>Integrate 500 out-of-school migrant children into mainstream formal schools through remedial bridge centers.</p>
                </div>
                <div class="roadmap-item">
                    <span class="roadmap-year">Goal 2</span>
                    <h4>1,000 Native Trees Planted</h4>
                    <p>Sustain our 20+ trees/month pace to establish resilient green micro-belts across 10 rural schools in Delhi-NCR.</p>
                </div>
                <div class="roadmap-item">
                    <span class="roadmap-year">Goal 3</span>
                    <h4>300 Women Self-Reliant</h4>
                    <p>Graduate 300 village women from vocational sewing and craft programs into independent micro-enterprises.</p>
                </div>
                <div class="roadmap-item">
                    <span class="roadmap-year">Goal 4</span>
                    <h4>Apna Aangan Flagship</h4>
                    <p>Establish a fully-equipped, solar-powered permanent community learning center in Tikri Kalan / Neelwal.</p>
                </div>
            </div>
        </div>
    </div>
</section>
'''

render_page(
    filename="mission.html",
    active_nav="about",
    title="Our Mission | Grassroots Strategic Pillars",
    meta_desc="Explore the strategic mission and 2024-2027 roadmap of Enlighting Humanity Trust, dedicated to nutrition, education, women empowerment, and green restoration.",
    content_html=mission_content
)

# -------------------------------------------------------------
# 4. VISION.HTML
# -------------------------------------------------------------
vision_content = '''
<div class="page-banner">
    <div class="container">
        <ul class="breadcrumbs">
            <li><a href="index.html">Home</a></li>
            <li><a href="about.html">About Us</a></li>
            <li>Our Vision</li>
        </ul>
        <h1 class="page-banner-title">Our Vision for 2030</h1>
        <p class="page-banner-sub">Envisioning a just, inclusive, and climate-resilient society where human dignity is universal.</p>
    </div>
</div>

<section class="section">
    <div class="container">
        <div class="vision-lead text-center mb-5">
            <span class="section-tag">The Horizon We Build Towards</span>
            <h2 class="section-title">A World Where No Potential Remains In The Dark</h2>
            <blockquote class="vision-quote">
                "We envision an India where no child is deprived of schooling due to poverty, no family suffers the anguish of empty cooking pots, every woman leads an economically self-determined life, and every community lives surrounded by healthy native trees that clean the air for future generations."
            </blockquote>
        </div>

        <div class="grid-3-col mb-5">
            <div class="vision-pillar-card">
                <div class="pillar-icon">🌅</div>
                <h3>Dignity Over Dependency</h3>
                <p>
                    Charity provides momentary relief, but empowerment creates lasting freedom. Our vision moves beneficiaries from needing assistance to becoming self-sufficient leaders and donors themselves.
                </p>
            </div>
            <div class="vision-pillar-card">
                <div class="pillar-icon">🌳</div>
                <h3>Ecological Harmony</h3>
                <p>
                    Outer Delhi's semi-rural fringe faces severe air pollution and concretization. We envision lush, child-tended green corridors in every village school, counteracting urban sprawl with native biodiversity.
                </p>
            </div>
            <div class="vision-pillar-card">
                <div class="pillar-icon">🏡</div>
                <h3>The "Apna Aangan" Model</h3>
                <p>
                    A decentralized network of community courtyards across resettlement colonies where learning, healthcare, and female solidarity take root permanently.
                </p>
            </div>
        </div>

        <div class="quote-card p-5 text-center bg-light rounded">
            <h3>"When you enlighten a single child, you brighten an entire generation."</h3>
            <p class="text-muted mt-2">— Nitin Gothwal, Founder, Enlighting Humanity Trust</p>
            <div class="mt-3">
                <a href="donate.html" class="btn btn-primary">Support Our Vision Today</a>
                <a href="volunteer.html" class="btn btn-outline ml-2">Volunteer Your Talents</a>
            </div>
        </div>
    </div>
</section>
'''

render_page(
    filename="vision.html",
    active_nav="about",
    title="Our Vision | Inspiring Sustainable Human Dignity",
    meta_desc="Read the 2030 vision of Enlighting Humanity Trust: breaking generational poverty, establishing community learning hubs, and restoring Delhi's green cover.",
    content_html=vision_content
)

# -------------------------------------------------------------
# 5. VALUES.HTML
# -------------------------------------------------------------
values_content = '''
<div class="page-banner">
    <div class="container">
        <ul class="breadcrumbs">
            <li><a href="index.html">Home</a></li>
            <li><a href="about.html">About Us</a></li>
            <li>Core Values</li>
        </ul>
        <h1 class="page-banner-title">Our Core Organizational Values</h1>
        <p class="page-banner-sub">The non-negotiable moral and operational principles that govern all trust activities.</p>
    </div>
</div>

<section class="section">
    <div class="container">
        <div class="section-header text-center mb-5">
            <span class="section-tag">Guiding Light</span>
            <h2 class="section-title">The Six Pillars of Trust & Integrity</h2>
            <p class="section-desc">These principles guide our interactions with beneficiaries, donors, volunteers, and the natural world.</p>
        </div>

        <div class="values-grid">
            <div class="value-item">
                <span class="val-num">01</span>
                <h3>Radical Transparency (Satya)</h3>
                <p>
                    Every rupee entrusted to us is accounted for. We publish open financial records, share genuine photo proofs of field projects, and maintain open communication with all supporters.
                </p>
            </div>

            <div class="value-item">
                <span class="val-num">02</span>
                <h3>Grassroots Compassion (Karuna)</h3>
                <p>
                    We operate with profound empathy, treating every community member with respect and honor. We never display beneficiaries in humiliating postures for fundraising.
                </p>
            </div>

            <div class="value-item">
                <span class="val-num">03</span>
                <h3>Environmental Reverence (Prakriti)</h3>
                <p>
                    Human progress must never come at the expense of our living ecosystem. Our ongoing monthly 20-tree plantation is a testament to our sacred bond with Mother Nature.
                </p>
            </div>

            <div class="value-item">
                <span class="val-num">04</span>
                <h3>Community Co-Ownership</h3>
                <p>
                    We do not impose external solutions. All initiatives are planned in close consultation with village elders, mothers, and local youth to ensure deep grassroots roots.
                </p>
            </div>

            <div class="value-item">
                <span class="val-num">05</span>
                <h3>Zero Administrative Waste</h3>
                <p>
                    We maintain lean operations. Volunteerism and localized direct action ensure maximum donor funds directly translate into food, books, seeds, and sewing machines.
                </p>
            </div>

            <div class="value-item">
                <span class="val-num">06</span>
                <h3>Unyielding Inclusivity</h3>
                <p>
                    We serve all human beings regardless of caste, creed, religion, gender, or regional background. Poverty recognizes no boundaries, and neither does our solidarity.
                </p>
            </div>
        </div>

        <div class="ethical-charter mt-5 p-4 bg-light rounded">
            <h3 class="mb-2">Our Field Code of Ethics</h3>
            <ul class="custom-check-list">
                <li>Strict child protection protocol: All volunteer interactions are supervised and adhere to POSH and POCSO ethical norms.</li>
                <li>Financial integrity: Direct UPI transfers go exclusively to the verified Trust account (9654518368@paytm).</li>
                <li>Honest reporting: We never fabricate beneficiary counts, awards, or operational scale.</li>
            </ul>
        </div>
    </div>
</section>
'''

render_page(
    filename="values.html",
    active_nav="about",
    title="Core Values | Transparency, Empathy & Integrity",
    meta_desc="Discover the six foundational values of Enlighting Humanity Trust: radical transparency, grassroots compassion, environmental reverence, and zero waste.",
    content_html=values_content
)

# -------------------------------------------------------------
# 6. OUR-WORK.HTML
# -------------------------------------------------------------
our_work_content = '''
<div class="page-banner">
    <div class="container">
        <ul class="breadcrumbs">
            <li><a href="index.html">Home</a></li>
            <li>Our Programs</li>
        </ul>
        <h1 class="page-banner-title">Our Work & Grassroots Programs</h1>
        <p class="page-banner-sub">Six comprehensive initiatives tackling the root causes of urban and rural inequality in New Delhi.</p>
    </div>
</div>

<section class="section">
    <div class="container">
        <div class="section-header text-center mb-5">
            <span class="section-tag">Holistic Interventions</span>
            <h2 class="section-title">Transforming Communities From Within</h2>
            <p class="section-desc">Explore each dedicated wing of Enlighting Humanity Trust and discover how you can support.</p>
        </div>

        <!-- 6 Program Detailed Blocks -->
        <div class="programs-detailed-list">
            <!-- Block 1 -->
            <div class="program-detail-block">
                <div class="detail-text">
                    <span class="prog-tag">Nutritional Relief</span>
                    <h2>1. Food for Hunger (Project Annapurna)</h2>
                    <p>
                        Outer Delhi's industrial and construction belts in Tikri Kalan and Mundka house thousands of migrant daily-wagers. When work is irregular, meals are skipped. Our Food for Hunger initiative provides regular nutritious cooked food distribution and dry ration hampers (wheat flour, lentils, cooking oil, rice, salt) to ensure working families and elderly residents maintain food security with honor.
                    </p>
                    <ul class="custom-check-list">
                        <li>Over 9 years of emergency food response and regular drives.</li>
                        <li>Specially tailored child nutrition packs with iron and protein supplements.</li>
                        <li>Sponsor a family's full monthly dry rations for just ₹501.</li>
                    </ul>
                    <div class="mt-3">
                        <a href="food-for-hunger.html" class="btn btn-primary">Read Program Details</a>
                        <a href="donate.html?campaign=food" class="btn btn-outline ml-2">Sponsor Food Packets</a>
                    </div>
                </div>
                <div class="detail-media">
                    <img src="assets/images/community-drive.jpg" alt="Food and community distribution drive" class="rounded-img shadow">
                </div>
            </div>

            <!-- Block 2 -->
            <div class="program-detail-block reverse">
                <div class="detail-text">
                    <span class="prog-tag">Child Education</span>
                    <h2>2. Child Education & Remedial Support</h2>
                    <p>
                        Without strong academic support at home, children of illiterate migrant laborers often fall behind and drop out of government schools. Enlighting Humanity Trust operates localized study pods that provide homework assistance, foundational reading and arithmetic, digital literacy, and free educational starter kits (backpacks, notebooks, geometry boxes).
                    </p>
                    <ul class="custom-check-list">
                        <li>Remedial coaching bridging the COVID and generational learning gap.</li>
                        <li>School re-enrollment drives for dropouts and working children.</li>
                        <li>Student sponsorship for just ₹501 per month covers all study supplies.</li>
                    </ul>
                    <div class="mt-3">
                        <a href="education.html" class="btn btn-primary">Read Program Details</a>
                        <a href="donate.html?campaign=education" class="btn btn-outline ml-2">Support a Child's Studies</a>
                    </div>
                </div>
                <div class="detail-media">
                    <img src="assets/images/children-activity.jpg" alt="Children participating in learning activity" class="rounded-img shadow">
                </div>
            </div>

            <!-- Block 3 -->
            <div class="program-detail-block">
                <div class="detail-text">
                    <span class="prog-tag">Gender Equality</span>
                    <h2>3. Women Empowerment & Self-Reliance</h2>
                    <p>
                        True social transformation is impossible without elevating women. In Village Neelwal and Tikri Kalan, we conduct tailoring, embroidery, and handicraft courses that equip homemakers and young women with marketable livelihoods. Concurrently, we organize menstrual hygiene workshops, distributing free sanitary napkins to eradicate stigma.
                    </p>
                    <ul class="custom-check-list">
                        <li>Vocational sewing classes with certificate of completion.</li>
                        <li>Formation of Self-Help Groups (SHGs) for micro-savings.</li>
                        <li>Free sanitary pad distribution drives and health awareness.</li>
                    </ul>
                    <div class="mt-3">
                        <a href="women-empowerment.html" class="btn btn-primary">Read Program Details</a>
                        <a href="donate.html?campaign=women" class="btn btn-outline ml-2">Sponsor a Sewing Kit</a>
                    </div>
                </div>
                <div class="detail-media">
                    <img src="assets/images/community-drive.jpg" alt="Women self reliance meeting" class="rounded-img shadow">
                </div>
            </div>

            <!-- Block 4 -->
            <div class="program-detail-block reverse">
                <div class="detail-text">
                    <span class="prog-tag">Youth Livelihood</span>
                    <h2>4. Vocational Skill Development</h2>
                    <p>
                        First-generation high school graduates from underprivileged backgrounds frequently struggle to enter the formal job market. Our Vocational Skill Center offers practical, short-term modules in basic computer operations, data entry, English speaking, and interview preparedness.
                    </p>
                    <ul class="custom-check-list">
                        <li>Basic IT, MS Word, Excel, and Internet navigation training.</li>
                        <li>Confidence building, professional etiquette, and resume writing.</li>
                        <li>Connecting skilled trainees with local retail and office vacancies.</li>
                    </ul>
                    <div class="mt-3">
                        <a href="skill-development.html" class="btn btn-primary">Read Program Details</a>
                        <a href="donate.html?campaign=skills" class="btn btn-outline ml-2">Sponsor a Youth Trainee</a>
                    </div>
                </div>
                <div class="detail-media">
                    <img src="assets/images/hero-banner.jpg" alt="Youth training session" class="rounded-img shadow">
                </div>
            </div>

            <!-- Block 5 -->
            <div class="program-detail-block">
                <div class="detail-text">
                    <span class="prog-tag">Environmental Conservation</span>
                    <h2>5. Environment & Monthly Tree Plantation</h2>
                    <p>
                        Our signature green commitment: we plant and nurture at least 20 native trees every single month with village school children. By planting hardy species like Neem, Peepal, Jamun, and Banyan, we combat Delhi's hazardous air quality while teaching children environmental guardianship.
                    </p>
                    <ul class="custom-check-list">
                        <li>240+ trees planted annually with protective tree guards.</li>
                        <li>Child "Tree Buddy" system ensuring continuous watering and care.</li>
                        <li>Sponsor a native tree sapling with guard for ₹251.</li>
                    </ul>
                    <div class="mt-3">
                        <a href="environment.html" class="btn btn-primary">Read Program Details</a>
                        <a href="donate.html?campaign=environment" class="btn btn-outline ml-2">Plant Saplings (₹251)</a>
                    </div>
                </div>
                <div class="detail-media">
                    <img src="assets/images/tree-planting-children.jpg" alt="Children planting trees" class="rounded-img shadow">
                </div>
            </div>

            <!-- Block 6 -->
            <div class="program-detail-block reverse">
                <div class="detail-text">
                    <span class="prog-tag">Flagship Community Space</span>
                    <h2>6. Apna Aangan Community Hub</h2>
                    <p>
                        "Apna Aangan" (Our Courtyard) is our long-term vision of a multi-purpose sanctuary in West Delhi. It serves as a study library during the day, a vocational tailoring center in the afternoon, and a venue for community health checkups and elder care gatherings on weekends.
                    </p>
                    <ul class="custom-check-list">
                        <li>Solar-powered, clean water equipped community sanctuary.</li>
                        <li>Public study library equipped with textbooks and reference guides.</li>
                        <li>Venue for free doctor checkups, eye camps, and legal counseling.</li>
                    </ul>
                    <div class="mt-3">
                        <a href="apna-aangan.html" class="btn btn-primary">Discover Apna Aangan</a>
                        <a href="donate.html?campaign=aangan" class="btn btn-outline ml-2">Support Center Construction</a>
                    </div>
                </div>
                <div class="detail-media">
                    <img src="assets/images/community-drive.jpg" alt="Apna Aangan community gatherings" class="rounded-img shadow">
                </div>
            </div>
        </div>
    </div>
</section>
'''

render_page(
    filename="our-work.html",
    active_nav="work",
    title="Our Work | Six Pillars of Grassroots Impact",
    meta_desc="Comprehensive overview of Enlighting Humanity Trust's programs: food for hunger, child education, women empowerment, youth skills, environment, and Apna Aangan.",
    content_html=our_work_content
)

print("Batch 1 (Pages 1-6) completed successfully.")
