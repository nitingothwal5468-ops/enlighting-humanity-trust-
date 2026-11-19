#!/usr/bin/env python3
"""
Enlighting Humanity Trust - Master Page Builder Part 2
Generates detailed Program Pages (7 to 12):
- food-for-hunger.html
- education.html
- women-empowerment.html
- skill-development.html
- environment.html
- apna-aangan.html
"""

import os
from generator_base import render_page

print("Generating Program Pages (7-12)...")

# -------------------------------------------------------------
# 7. FOOD-FOR-HUNGER.HTML
# -------------------------------------------------------------
food_content = '''
<div class="page-banner" style="background-image: linear-gradient(rgba(16, 55, 41, 0.9), rgba(22, 75, 54, 0.85)), url('assets/images/community-drive.jpg');">
    <div class="container">
        <ul class="breadcrumbs">
            <li><a href="index.html">Home</a></li>
            <li><a href="our-work.html">Our Programs</a></li>
            <li>Food for Hunger</li>
        </ul>
        <h1 class="page-banner-title">Food for Hunger (Project Annapurna)</h1>
        <p class="page-banner-sub">Ensuring nutritional security and dignity for daily-wage migrant laborers, children, and elderly residents in outer Delhi.</p>
    </div>
</div>

<section class="section">
    <div class="container">
        <div class="grid-2-col align-center mb-5">
            <div>
                <span class="section-tag">Program Overview</span>
                <h2 class="section-title">Fighting Urban Hunger at the Grassroots Level</h2>
                <p class="lead-text">
                    In the industrial fringes and construction settlements of Tikri Kalan, Neelwal, and Mundka, hundreds of daily-wage laborers face intermittent work. When a day's wage is lost, the evening stove remains unlit.
                </p>
                <p>
                    Through <strong>Project Annapurna</strong>, Enlighting Humanity Trust steps in to provide continuous food relief. We organize freshly cooked, hygienic meal distribution drives and distribute monthly dry ration hampers containing staples like wheat flour (atta), pulses (dal), rice, cooking mustard oil, and iodized salt.
                </p>
                <p>
                    Our focus is not merely calories, but balanced nutrition. Malnutrition in early childhood causes irreversible cognitive and physical stunting. We supply special fruit, milk, and protein supplement kits directly to preschool and primary-age children.
                </p>
            </div>
            <div>
                <img src="assets/images/community-drive.jpg" alt="Food relief distribution drive in Tikri Kalan" class="rounded-img shadow-lg">
            </div>
        </div>

        <div class="program-pillars-grid mb-5">
            <div class="feature-card">
                <div class="feature-icon">🍲</div>
                <h3>Hot Nutritious Meals</h3>
                <p>Cooked with pure mustard oil and wholesome grains, served hot to migrant workers, cycle rickshaw pullers, and street dwellers.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">📦</div>
                <h3>Monthly Dry Ration Kits</h3>
                <p>Each family ration box contains 10kg Atta, 5kg Rice, 2kg Pulses, 1L Cooking Oil, Salt, and essential spices to support a family of 4 for a month.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🥛</div>
                <h3>Child Nutrition Supplement</h3>
                <p>Fortified milk powder, jaggery (gur), roasted chana, and seasonal fruits provided weekly to underprivileged children in our study pods.</p>
            </div>
        </div>

        <div class="sponsor-tier-card bg-light p-4 rounded mb-5">
            <h3 class="text-center mb-3">How Your Contribution Feeds Families</h3>
            <div class="grid-3-col text-center">
                <div class="p-3 bg-white rounded shadow-sm">
                    <h4 class="text-primary">₹251</h4>
                    <p class="small text-muted">Nutritional Fruit & Milk Pack</p>
                    <p>Provides fresh fruit, milk, and healthy snacks for 5 malnourished children for one week.</p>
                    <a href="donate.html?campaign=food" class="btn btn-primary btn-sm mt-2">Sponsor ₹251</a>
                </div>
                <div class="p-3 bg-white rounded shadow-sm">
                    <h4 class="text-primary">₹501</h4>
                    <p class="small text-muted">Family Monthly Dry Ration Kit</p>
                    <p>Supplies a complete 15-day dry ration hamper to a daily-wage worker's family facing unemployment.</p>
                    <a href="donate.html?campaign=food" class="btn btn-primary btn-sm mt-2">Sponsor ₹501</a>
                </div>
                <div class="p-3 bg-white rounded shadow-sm">
                    <h4 class="text-primary">₹2,501</h4>
                    <p class="small text-muted">Community Langar / Meal Drive</p>
                    <p>Funds a complete hot meal distribution feeding 100+ homeless individuals and labor families.</p>
                    <a href="donate.html?campaign=food" class="btn btn-primary btn-sm mt-2">Sponsor ₹2,501</a>
                </div>
            </div>
        </div>

        <div class="faq-accordion">
            <h3 class="mb-3">Frequently Asked Questions</h3>
            <div class="faq-item">
                <button class="faq-question">How does the Trust ensure food hygiene and safety?</button>
                <div class="faq-answer">
                    <p>All cooked meals are prepared under strict hygiene standards by local volunteer cooks using fresh ingredients, sealed stainless containers, and eco-friendly compostable plates (pattals).</p>
                </div>
            </div>
            <div class="faq-item">
                <button class="faq-question">Can I donate in kind (grains, pulses, cooking oil)?</button>
                <div class="faq-answer">
                    <p>Yes, absolutely! We welcome dry grain donations at our registered office in Village Neelwal, PO Tikri Kalan, New Delhi. Please call us at +91 9654518368 before dropping off supplies.</p>
                </div>
            </div>
        </div>
    </div>
</section>
'''

render_page(
    filename="food-for-hunger.html",
    active_nav="work",
    title="Food for Hunger | Project Annapurna Relief",
    meta_desc="Project Annapurna by Enlighting Humanity Trust provides hot cooked meals and monthly dry ration kits to daily-wage workers and children in West Delhi.",
    content_html=food_content
)

# -------------------------------------------------------------
# 8. EDUCATION.HTML
# -------------------------------------------------------------
edu_content = '''
<div class="page-banner" style="background-image: linear-gradient(rgba(16, 55, 41, 0.9), rgba(22, 75, 54, 0.85)), url('assets/images/children-activity.jpg');">
    <div class="container">
        <ul class="breadcrumbs">
            <li><a href="index.html">Home</a></li>
            <li><a href="our-work.html">Our Programs</a></li>
            <li>Education & Child Welfare</li>
        </ul>
        <h1 class="page-banner-title">Child Education & Welfare</h1>
        <p class="page-banner-sub">Bridging the educational divide through remedial study pods, school re-enrollment, and annual stationery distribution.</p>
    </div>
</div>

<section class="section">
    <div class="container">
        <div class="grid-2-col align-center mb-5">
            <div>
                <span class="section-tag">Educational Equity</span>
                <h2 class="section-title">Igniting Young Minds in Marginalized Neighborhoods</h2>
                <p class="lead-text">
                    For children born to illiterate migrant laborers, getting enrolled in school is only the first hurdle. Without academic help at home, many fall behind by grade 4, lose confidence, and eventually drop out to enter child labor.
                </p>
                <p>
                    <strong>Enlighting Humanity Trust</strong> runs grassroots remedial learning pods in Village Neelwal and Tikri Kalan. Our volunteer teachers offer daily after-school academic support in Hindi, English, and Mathematics, turning confusion into confidence.
                </p>
                <p>
                    We actively conduct door-to-door community surveys to identify out-of-school children, counsel their parents against child labor, and help navigate government school admission formalities under the Right to Education (RTE) Act.
                </p>
            </div>
            <div>
                <img src="assets/images/children-activity.jpg" alt="Children in active learning session" class="rounded-img shadow-lg">
            </div>
        </div>

        <div class="grid-3-col mb-5">
            <div class="feature-card">
                <div class="feature-icon">🎒</div>
                <h3>School Starter Kits</h3>
                <p>Every academic year, we provide sturdy backpacks, notebooks, pens, pencils, geometry kits, and coloring boxes to over 300 children.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">📐</div>
                <h3>Remedial Study Centers</h3>
                <p>Small batch tutoring (10–15 students) ensuring personalized attention for first-generation learners struggling with fundamental math and reading.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">💻</div>
                <h3>Digital Literacy Primer</h3>
                <p>Introducing children to basic computer hardware, digital educational apps, and interactive learning games to inspire curiosity.</p>
            </div>
        </div>

        <div class="sponsor-tier-card bg-light p-4 rounded mb-5">
            <h3 class="text-center mb-3">Sponsor a Child's Bright Future</h3>
            <div class="grid-3-col text-center">
                <div class="p-3 bg-white rounded shadow-sm">
                    <h4 class="text-primary">₹251</h4>
                    <p class="small text-muted">Stationery & Notebook Pack</p>
                    <p>Provides a child with complete notebooks, pens, geometry kit, and art supplies for an academic term.</p>
                    <a href="donate.html?campaign=education" class="btn btn-primary btn-sm mt-2">Sponsor ₹251</a>
                </div>
                <div class="p-3 bg-white rounded shadow-sm">
                    <h4 class="text-primary">₹501</h4>
                    <p class="small text-muted">Monthly Student Sponsorship</p>
                    <p>Covers one month of remedial tutoring, school supplies, and daily nutritional snacks for one student.</p>
                    <a href="donate.html?campaign=education" class="btn btn-primary btn-sm mt-2">Sponsor ₹501</a>
                </div>
                <div class="p-3 bg-white rounded shadow-sm">
                    <h4 class="text-primary">₹5,001</h4>
                    <p class="small text-muted">Annual Learning Pod Patron</p>
                    <p>Sponsors the complete annual learning materials, books, and exam preparations for an entire batch of 10 students.</p>
                    <a href="donate.html?campaign=education" class="btn btn-primary btn-sm mt-2">Sponsor ₹5,001</a>
                </div>
            </div>
        </div>

        <div class="faq-accordion">
            <h3 class="mb-3">Questions About Child Sponsorship</h3>
            <div class="faq-item">
                <button class="faq-question">Will I receive progress updates about the child I sponsor?</button>
                <div class="faq-answer">
                    <p>Yes! Regular donors receive periodic academic progress summaries, creative art samples made by the students, and verifiable photo documentation of study drives.</p>
                </div>
            </div>
            <div class="faq-item">
                <button class="faq-question">Can I volunteer to teach over weekends?</button>
                <div class="faq-answer">
                    <p>Yes, we welcome volunteer teachers for weekend English speaking, story-telling, science experiments, and basic mathematics! Visit our <a href="volunteer.html">Volunteer Page</a> to register.</p>
                </div>
            </div>
        </div>
    </div>
</section>
'''

render_page(
    filename="education.html",
    active_nav="work",
    title="Child Education & Welfare | Remedial Learning Pods",
    meta_desc="Support remedial tutoring, school starter kits, and dropout prevention for underprivileged children in New Delhi with Enlighting Humanity Trust.",
    content_html=edu_content
)

# -------------------------------------------------------------
# 9. WOMEN-EMPOWERMENT.HTML
# -------------------------------------------------------------
women_content = '''
<div class="page-banner" style="background-image: linear-gradient(rgba(16, 55, 41, 0.9), rgba(22, 75, 54, 0.85)), url('assets/images/community-drive.jpg');">
    <div class="container">
        <ul class="breadcrumbs">
            <li><a href="index.html">Home</a></li>
            <li><a href="our-work.html">Our Programs</a></li>
            <li>Women Empowerment</li>
        </ul>
        <h1 class="page-banner-title">Women Empowerment & Self-Reliance</h1>
        <p class="page-banner-sub">Fostering financial independence, vocational stitching skills, and menstrual hygiene awareness in rural Delhi.</p>
    </div>
</div>

<section class="section">
    <div class="container">
        <div class="grid-2-col align-center mb-5">
            <div>
                <span class="section-tag">Dignity & Livelihood</span>
                <h2 class="section-title">Unlocking Economic Independence for Rural Women</h2>
                <p class="lead-text">
                    In semi-rural communities like Village Neelwal and Tikri Kalan, many women spend their lives confined to unpaid domestic labor without any personal savings or financial decision-making power.
                </p>
                <p>
                    <strong>Enlighting Humanity Trust</strong> provides free tailoring, sewing, and embroidery classes equipped with durable sewing machines. Women learn cutting, garment assembly, and traditional needlework, enabling them to accept stitching orders from local families and markets.
                </p>
                <p>
                    Beyond livelihoods, we address the critical issue of menstrual health. Period poverty remains pervasive; we conduct regular health workshops and distribute free eco-friendly sanitary napkins to adolescent girls and mothers.
                </p>
            </div>
            <div>
                <img src="assets/images/community-drive.jpg" alt="Women gathering for self-reliance circle" class="rounded-img shadow-lg">
            </div>
        </div>

        <div class="grid-3-col mb-5">
            <div class="feature-card">
                <div class="feature-icon">🧵</div>
                <h3>Tailoring & Sewing Center</h3>
                <p>6-month structured training covering garment construction, alteration, hand embroidery, and machine maintenance.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🩸</div>
                <h3>Menstrual Dignity Drives</h3>
                <p>Educating adolescent girls on reproductive health, debunking myths, and distributing free sanitary pad packages.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">💰</div>
                <h3>Self-Help Group (SHG) Savings</h3>
                <p>Encouraging women to form pooled micro-saving circles, opening personal bank accounts, and building emergency funds.</p>
            </div>
        </div>

        <div class="sponsor-tier-card bg-light p-4 rounded mb-5">
            <h3 class="text-center mb-3">Support Women's Autonomy</h3>
            <div class="grid-3-col text-center">
                <div class="p-3 bg-white rounded shadow-sm">
                    <h4 class="text-primary">₹251</h4>
                    <p class="small text-muted">Menstrual Hygiene Pack</p>
                    <p>Provides 3 women with a 6-month supply of sanitary napkins and hygiene essentials.</p>
                    <a href="donate.html?campaign=women" class="btn btn-primary btn-sm mt-2">Sponsor ₹251</a>
                </div>
                <div class="p-3 bg-white rounded shadow-sm">
                    <h4 class="text-primary">₹1,001</h4>
                    <p class="small text-muted">Tailoring Course Sponsorship</p>
                    <p>Covers training fabrics, scissors, threads, and instructor mentorship for one woman for two months.</p>
                    <a href="donate.html?campaign=women" class="btn btn-primary btn-sm mt-2">Sponsor ₹1,001</a>
                </div>
                <div class="p-3 bg-white rounded shadow-sm">
                    <h4 class="text-primary">₹6,500</h4>
                    <p class="small text-muted">Gift a Sewing Machine</p>
                    <p>Provides a graduated woman with her own heavy-duty sewing machine so she can start earning from home immediately.</p>
                    <a href="donate.html?campaign=women" class="btn btn-primary btn-sm mt-2">Gift Machine</a>
                </div>
            </div>
        </div>
    </div>
</section>
'''

render_page(
    filename="women-empowerment.html",
    active_nav="work",
    title="Women Empowerment | Sewing, SHGs & Menstrual Dignity",
    meta_desc="Enlighting Humanity Trust empowers rural women in West Delhi with tailoring classes, SHG micro-savings, and menstrual hygiene drives.",
    content_html=women_content
)

# -------------------------------------------------------------
# 10. SKILL-DEVELOPMENT.HTML
# -------------------------------------------------------------
skill_content = '''
<div class="page-banner" style="background-image: linear-gradient(rgba(16, 55, 41, 0.9), rgba(22, 75, 54, 0.85)), url('assets/images/hero-banner.jpg');">
    <div class="container">
        <ul class="breadcrumbs">
            <li><a href="index.html">Home</a></li>
            <li><a href="our-work.html">Our Programs</a></li>
            <li>Skill Development</li>
        </ul>
        <h1 class="page-banner-title">Youth Vocational Skill Development</h1>
        <p class="page-banner-sub">Transforming unemployed youth into employable professionals with digital skills, communication, and career guidance.</p>
    </div>
</div>

<section class="section">
    <div class="container">
        <div class="grid-2-col align-center mb-5">
            <div>
                <span class="section-tag">Career Pathways</span>
                <h2 class="section-title">Equipping Underprivileged Youth for the Modern Economy</h2>
                <p class="lead-text">
                    In outer Delhi, many young men and women finish high school without the functional digital or communication skills required by modern employers. Without guidance, they fall into informal, insecure labor.
                </p>
                <p>
                    Our Skill Development Initiative bridges this exact employment bottleneck. We offer intensive 3-month courses in basic computer literacy, MS Office (Word, Excel, PowerPoint), email correspondence, typing speed, and spoken English communication.
                </p>
                <p>
                    Trainees participate in mock interviews, learn to craft professional resumes, and gain practical knowledge of workplace professional norms, preparing them for entry-level positions in retail, back-office administration, and customer service.
                </p>
            </div>
            <div>
                <img src="assets/images/hero-banner.jpg" alt="Youth training session" class="rounded-img shadow-lg">
            </div>
        </div>

        <div class="grid-3-col mb-5">
            <div class="feature-card">
                <div class="feature-icon">🖥️</div>
                <h3>Computer Applications</h3>
                <p>Hands-on training in operating systems, MS Office, spreadsheet data entry, web navigation, and secure online transactions.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🗣️</div>
                <h3>Spoken English & Communication</h3>
                <p>Interactive group discussions, vocabulary building, and conversational exercises to build workplace confidence.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">💼</div>
                <h3>Job Readiness & Placements</h3>
                <p>Resume crafting, interview simulation, professional grooming, and direct linkage to local job openings in West Delhi.</p>
            </div>
        </div>

        <div class="sponsor-tier-card bg-light p-4 rounded mb-5">
            <h3 class="text-center mb-3">Invest in Youth Employment</h3>
            <div class="grid-2-col text-center">
                <div class="p-4 bg-white rounded shadow-sm">
                    <h4 class="text-primary">₹1,001</h4>
                    <p class="small text-muted">Sponsor a Student's IT Course</p>
                    <p>Covers computer lab usage, study software licenses, and training guides for one youth trainee for 3 months.</p>
                    <a href="donate.html?campaign=skills" class="btn btn-primary btn-sm mt-2">Sponsor ₹1,001</a>
                </div>
                <div class="p-4 bg-white rounded shadow-sm">
                    <h4 class="text-primary">₹15,000</h4>
                    <p class="small text-muted">Donate a Computer Workstation</p>
                    <p>Funds a complete refurbished PC workstation with monitor, UPS, and keyboard for our community skill lab.</p>
                    <a href="donate.html?campaign=skills" class="btn btn-primary btn-sm mt-2">Donate Workstation</a>
                </div>
            </div>
        </div>
    </div>
</section>
'''

render_page(
    filename="skill-development.html",
    active_nav="work",
    title="Youth Skill Development | Computer Training & Career Prep",
    meta_desc="Empowering underprivileged youth in New Delhi with basic computer literacy, spoken English, and job-readiness skills through Enlighting Humanity Trust.",
    content_html=skill_content
)

# -------------------------------------------------------------
# 11. ENVIRONMENT.HTML
# -------------------------------------------------------------
env_content = '''
<div class="page-banner" style="background-image: linear-gradient(rgba(16, 55, 41, 0.9), rgba(22, 75, 54, 0.85)), url('assets/images/tree-planting-children.jpg');">
    <div class="container">
        <ul class="breadcrumbs">
            <li><a href="index.html">Home</a></li>
            <li><a href="our-work.html">Our Programs</a></li>
            <li>Environment & Tree Plantation</li>
        </ul>
        <h1 class="page-banner-title">Environment & Monthly Tree Plantation</h1>
        <p class="page-banner-sub">Our signature commitment: planting at least 20 native trees every month with village school children.</p>
    </div>
</div>

<section class="section">
    <div class="container">
        <div class="grid-2-col align-center mb-5">
            <div>
                <span class="section-tag">Signature Green Action</span>
                <h2 class="section-title">20 Native Trees Every Single Month, Planted with Local Children</h2>
                <p class="lead-text">
                    Delhi-NCR consistently battles some of the world's highest air pollution indexes (AQI). The rapid concretization of outer Delhi has stripped away traditional village groves.
                </p>
                <p>
                    Rather than empty promises, <strong>Enlighting Humanity Trust</strong> made a binding pledge: <em>to plant and nurture a minimum of 20 native trees every single month</em>.
                </p>
                <p>
                    We organize monthly tree-planting drives in Village Neelwal, Tikri Kalan, and rural government schools. Most importantly, local school children are our partners. Each child adopts a sapling as their "Tree Buddy", taking personal responsibility for watering and weeding it.
                </p>
            </div>
            <div>
                <img src="assets/images/tree-planting-children.jpg" alt="Village school children planting native trees" class="rounded-img shadow-lg">
                <p class="img-caption text-center mt-2">Authentic Field Photo: Monthly tree plantation drive in Village Neelwal, West Delhi.</p>
            </div>
        </div>

        <div class="content-box bg-light p-4 rounded mb-5">
            <h3 class="mb-3 text-center">Why Native Indian Trees?</h3>
            <p class="text-center text-muted mb-4">We strictly avoid invasive ornamental shrubs. We only plant time-tested native species that support local biodiversity and withstand extreme Delhi temperatures.</p>
            <div class="grid-3-col">
                <div class="p-3 bg-white rounded shadow-sm">
                    <h4>Neem (Azadirachta indica)</h4>
                    <p>Natural air purifier, natural insect repellent, and provider of dense cooling shade during scorching summer months.</p>
                </div>
                <div class="p-3 bg-white rounded shadow-sm">
                    <h4>Peepal (Ficus religiosa)</h4>
                    <p>The sacred powerhouse of 24-hour oxygen generation, carbon sequestration, and nesting shelter for local birds.</p>
                </div>
                <div class="p-3 bg-white rounded shadow-sm">
                    <h4>Jamun & Amla (Syzygium / Emblica)</h4>
                    <p>Hardy fruit-bearing native trees providing nutritious organic fruits for village children and soil water retention.</p>
                </div>
            </div>
        </div>

        <div class="stat-highlight-box mb-5">
            <div class="highlight-val">240+</div>
            <div class="highlight-text">
                <strong>Native trees planted every year with active tree guards</strong>
                <p>Each sapling is protected by a sturdy metal or bamboo tree guard to protect against grazing animals, ensuring over 90% long-term survival.</p>
            </div>
        </div>

        <div class="sponsor-tier-card bg-light p-4 rounded mb-5">
            <h3 class="text-center mb-3">Sponsor a Native Tree Today</h3>
            <div class="grid-3-col text-center">
                <div class="p-3 bg-white rounded shadow-sm">
                    <h4 class="text-primary">₹251</h4>
                    <p class="small text-muted">1 Native Tree Sapling</p>
                    <p>Covers a healthy 4-foot native sapling, organic manure, and planting drive logistics.</p>
                    <a href="donate.html?campaign=environment" class="btn btn-primary btn-sm mt-2">Plant 1 Tree (₹251)</a>
                </div>
                <div class="p-3 bg-white rounded shadow-sm">
                    <h4 class="text-primary">₹501</h4>
                    <p class="small text-muted">Sapling + Protective Guard</p>
                    <p>Funds 1 native sapling along with a durable metal guard and 1 year of monitored watering.</p>
                    <a href="donate.html?campaign=environment" class="btn btn-primary btn-sm mt-2">Sponsor Guard (₹501)</a>
                </div>
                <div class="p-3 bg-white rounded shadow-sm">
                    <h4 class="text-primary">₹5,020</h4>
                    <p class="small text-muted">Sponsor 1 Month's Drive (20 Trees)</p>
                    <p>Sponsor our entire monthly commitment of 20 native trees planted with village children with your name dedicated!</p>
                    <a href="donate.html?campaign=environment" class="btn btn-primary btn-sm mt-2">Sponsor Drive (₹5,020)</a>
                </div>
            </div>
        </div>
    </div>
</section>
'''

render_page(
    filename="environment.html",
    active_nav="work",
    title="Environment | 20 Native Trees Every Month",
    meta_desc="Enlighting Humanity Trust's signature environmental drive: planting at least 20 native trees every month with village children in New Delhi.",
    content_html=env_content
)

# -------------------------------------------------------------
# 12. APNA-AANGAN.HTML
# -------------------------------------------------------------
aangan_content = '''
<div class="page-banner" style="background-image: linear-gradient(rgba(16, 55, 41, 0.9), rgba(22, 75, 54, 0.85)), url('assets/images/community-drive.jpg');">
    <div class="container">
        <ul class="breadcrumbs">
            <li><a href="index.html">Home</a></li>
            <li><a href="our-work.html">Our Programs</a></li>
            <li>Apna Aangan Hub</li>
        </ul>
        <h1 class="page-banner-title">Apna Aangan Community Hub</h1>
        <p class="page-banner-sub">Our flagship community sanctuary: a safe space for study, women's training, elder gatherings, and health checkups.</p>
    </div>
</div>

<section class="section">
    <div class="container">
        <div class="grid-2-col align-center mb-5">
            <div>
                <span class="section-tag">Flagship Grassroots Center</span>
                <h2 class="section-title">"Our Courtyard": A Haven of Dignity and Collective Growth</h2>
                <p class="lead-text">
                    In congested resettlement colonies, multi-family households live in cramped one-room tenements. Children have no quiet corner to open a book, women have no safe space to learn trades, and elderly people have no dignified social gathering point.
                </p>
                <p>
                    <strong>Apna Aangan</strong> (meaning "Our Courtyard") is Enlighting Humanity Trust's flagship physical initiative in West Delhi. It is conceived as a vibrant community center open to all residents free of charge.
                </p>
                <p>
                    By consolidating our remedial education pods, women's tailoring workshops, youth computer lab, and free weekly health checkups under one roof, Apna Aangan serves as a lighthouse of community resilience.
                </p>
            </div>
            <div>
                <img src="assets/images/community-drive.jpg" alt="Community members gathered for Apna Aangan discussion" class="rounded-img shadow-lg">
            </div>
        </div>

        <div class="grid-3-col mb-5">
            <div class="feature-card">
                <div class="feature-icon">📚</div>
                <h3>Children's Open Library</h3>
                <p>A quiet, well-lit reading room with storybooks, school textbooks, encyclopedias, and study tables where students can do homework peacefully.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">✂️</div>
                <h3>Women's Craft Workshop</h3>
                <p>Equipped with sewing machines and cutting tables, hosting daily tailoring and embroidery training for local homemakers.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🩺</div>
                <h3>Community Wellness Clinic</h3>
                <p>A consultation room where visiting doctors and healthcare volunteers hold free eye checkups, blood pressure screenings, and hygiene counseling.</p>
            </div>
        </div>

        <div class="content-box bg-light p-4 rounded mb-5">
            <h3 class="mb-3 text-center">Apna Aangan Blueprint & Infrastructure Needs</h3>
            <p class="text-center text-muted mb-4">Help us equip this vital sanctuary with sustainable amenities.</p>
            <div class="grid-2-col">
                <div>
                    <ul class="custom-check-list">
                        <li><strong>Solar Inverter Power Backup:</strong> Ensuring un-interrupted fans and lighting during summer power cuts.</li>
                        <li><strong>Clean RO Drinking Water Station:</strong> Providing safe, tested drinking water for over 200 daily visitors.</li>
                    </ul>
                </div>
                <div>
                    <ul class="custom-check-list">
                        <li><strong>Digital Smart Classroom:</strong> Projector, screen, and 5 refurbished PC stations for youth classes.</li>
                        <li><strong>Sanitary Napkin Vending Unit:</strong> Ensuring 24/7 dignified menstrual hygiene access for village girls.</li>
                    </ul>
                </div>
            </div>
            <div class="text-center mt-4">
                <a href="donate.html?campaign=aangan" class="btn btn-primary btn-lg">Support Apna Aangan Infrastructure</a>
                <a href="csr.html" class="btn btn-outline btn-lg ml-2">Corporate Sponsorship (CSR)</a>
            </div>
        </div>
    </div>
</section>
'''

render_page(
    filename="apna-aangan.html",
    active_nav="work",
    title="Apna Aangan Community Hub | West Delhi Sanctuary",
    meta_desc="Apna Aangan is the flagship community learning and wellness center established by Enlighting Humanity Trust in Tikri Kalan / Neelwal, New Delhi.",
    content_html=aangan_content
)

print("Batch 2 (Pages 7-12) completed successfully.")
