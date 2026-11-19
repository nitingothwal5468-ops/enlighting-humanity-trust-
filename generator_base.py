#!/usr/bin/env python3
"""
Enlighting Humanity Trust - Master Static Site Generator
Generates all 24 production-ready pages with shared responsive header, footer,
SEO metadata, Schema.org JSON-LD, authentic branding, and accessible components.
"""

import os
import json

OUTPUT_DIR = "/home/user/enlighting-humanity"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Shared Header Components
def get_header(active_page="home", page_title="Enlighting Humanity Trust"):
    nav_links = [
        {"id": "home", "title": "Home", "url": "index.html"},
        {"id": "about", "title": "About Us", "url": "about.html", "sub": [
            {"title": "About The Trust", "url": "about.html"},
            {"title": "Our Mission", "url": "mission.html"},
            {"title": "Our Vision", "url": "vision.html"},
            {"title": "Core Values", "url": "values.html"},
            {"title": "Transparency & Governance", "url": "transparency.html"}
        ]},
        {"id": "work", "title": "Our Programs", "url": "our-work.html", "sub": [
            {"title": "All Programs Overview", "url": "our-work.html"},
            {"title": "Food for Hunger", "url": "food-for-hunger.html"},
            {"title": "Child Education", "url": "education.html"},
            {"title": "Women Empowerment", "url": "women-empowerment.html"},
            {"title": "Skill Development", "url": "skill-development.html"},
            {"title": "Environment & Trees (20/Mo)", "url": "environment.html"},
            {"title": "Apna Aangan Hub", "url": "apna-aangan.html"}
        ]},
        {"id": "campaigns", "title": "Campaigns", "url": "campaigns.html"},
        {"id": "involved", "title": "Get Involved", "url": "volunteer.html", "sub": [
            {"title": "Volunteer With Us", "url": "volunteer.html"},
            {"title": "Institutional Partners", "url": "partner.html"},
            {"title": "Corporate CSR", "url": "csr.html"}
        ]},
        {"id": "impact", "title": "Impact & Media", "url": "stories.html", "sub": [
            {"title": "Stories of Change", "url": "stories.html"},
            {"title": "Photo Gallery", "url": "gallery.html"}
        ]},
        {"id": "contact", "title": "Contact", "url": "contact.html"}
    ]

    nav_items_html = ""
    for item in nav_links:
        is_active = "active" if active_page == item["id"] else ""
        if "sub" in item:
            sub_html = "".join([f'<li><a href="{sub["url"]}">{sub["title"]}</a></li>' for sub in item["sub"]])
            nav_items_html += f'''
            <li class="has-dropdown {is_active}">
                <a href="{item['url']}">{item['title']} <span class="dropdown-caret">▾</span></a>
                <ul class="dropdown-menu">
                    {sub_html}
                </ul>
            </li>'''
        else:
            nav_items_html += f'<li class="{is_active}"><a href="{item["url"]}">{item["title"]}</a></li>'

    # Mobile menu items
    mobile_nav_items = ""
    for item in nav_links:
        if "sub" in item:
            sub_html = "".join([f'<li><a href="{sub["url"]}">{sub["title"]}</a></li>' for sub in item["sub"]])
            mobile_nav_items += f'''
            <li class="mobile-dropdown">
                <a href="{item['url']}" class="mobile-dropdown-toggle">{item['title']} <span class="caret">▾</span></a>
                <ul class="mobile-submenu">
                    {sub_html}
                </ul>
            </li>'''
        else:
            mobile_nav_items += f'<li><a href="{item["url"]}">{item["title"]}</a></li>'

    return f'''
    <!-- Top Announcement & Contact Bar -->
    <div class="topbar">
        <div class="container topbar-inner">
            <div class="topbar-left">
                <a href="tel:+919654518368" class="topbar-link"><span class="icon">📞</span> +91 9654518368</a>
                <a href="mailto:nitingothwal5468@gmail.com" class="topbar-link"><span class="icon">✉️</span> nitingothwal5468@gmail.com</a>
                <span class="topbar-tagline">📍 Registered Office: Village Neelwal, PO Tikri Kalan, New Delhi-110041</span>
            </div>
            <div class="topbar-right">
                <span class="tax-badge">Tax Exemption 80G Certified</span>
                <a href="https://wa.me/919654518368?text=Hello%20Enlighting%20Humanity%20Trust" target="_blank" rel="noopener" class="whatsapp-badge">WhatsApp Us</a>
            </div>
        </div>
    </div>

    <!-- Main Navigation Header -->
    <header class="site-header" id="mainHeader">
        <div class="container header-inner">
            <a href="index.html" class="brand-logo" aria-label="Enlighting Humanity Trust Home">
                <img src="assets/images/logo.png" alt="Enlighting Humanity Trust Official Logo" width="56" height="56" class="logo-img">
                <div class="brand-text">
                    <span class="brand-title">Enlighting Humanity Trust</span>
                    <span class="brand-motto">Empowering Lives, Enriching Humanity.</span>
                </div>
            </a>

            <!-- Desktop Navigation -->
            <nav class="desktop-nav" aria-label="Main Navigation">
                <ul class="nav-list">
                    {nav_items_html}
                </ul>
            </nav>

            <div class="header-cta-wrap">
                <a href="donate.html" class="btn btn-primary btn-sm donate-pulse">Donate Now</a>
                <button class="mobile-toggle-btn" id="mobileMenuOpen" aria-label="Open Navigation Menu" aria-expanded="false">
                    <span class="bar"></span>
                    <span class="bar"></span>
                    <span class="bar"></span>
                </button>
            </div>
        </div>
    </header>

    <!-- Mobile Drawer Navigation -->
    <div class="mobile-drawer" id="mobileDrawer" aria-hidden="true">
        <div class="drawer-header">
            <div class="drawer-logo">
                <img src="assets/images/logo.png" alt="Logo" width="40" height="40">
                <span>Enlighting Humanity</span>
            </div>
            <button class="drawer-close-btn" id="mobileMenuClose" aria-label="Close Navigation Menu">&times;</button>
        </div>
        <div class="drawer-body">
            <ul class="mobile-nav-list">
                {mobile_nav_items}
            </ul>
            <div class="drawer-cta">
                <a href="donate.html" class="btn btn-primary btn-block mb-2">Donate Online (UPI)</a>
                <a href="tel:+919654518368" class="btn btn-outline btn-block">Call: +91 9654518368</a>
            </div>
        </div>
    </div>
    <div class="mobile-overlay" id="mobileOverlay"></div>
    '''

def get_footer():
    return '''
    <!-- Global Site Footer -->
    <footer class="site-footer">
        <div class="container footer-top">
            <div class="footer-grid">
                <!-- Col 1: About Trust -->
                <div class="footer-col footer-about">
                    <div class="footer-brand">
                        <img src="assets/images/logo.png" alt="Enlighting Humanity Trust" width="54" height="54" class="footer-logo">
                        <div>
                            <span class="footer-title">Enlighting Humanity Trust</span>
                            <span class="footer-sub">Empowering Lives, Enriching Humanity.</span>
                        </div>
                    </div>
                    <p class="footer-desc">
                        A registered public charitable trust in New Delhi, India (Trust Reg. Act 1882), dedicated to hunger relief, education, women empowerment, skill building, and ecological stewardship since 2017.
                    </p>
                    <div class="footer-badges">
                        <span class="badge-item">✓ Indian Trusts Act</span>
                        <span class="badge-item">✓ NGO Darpan Registered</span>
                        <span class="badge-item">✓ 80G & 12A Certified</span>
                    </div>
                </div>

                <!-- Col 2: Quick Links -->
                <div class="footer-col">
                    <h3 class="footer-heading">Quick Links</h3>
                    <ul class="footer-links">
                        <li><a href="about.html">About The Trust</a></li>
                        <li><a href="mission.html">Our Mission & Goals</a></li>
                        <li><a href="vision.html">Vision for 2030</a></li>
                        <li><a href="values.html">Core Organizational Values</a></li>
                        <li><a href="transparency.html">Governance & Transparency</a></li>
                        <li><a href="stories.html">Field Impact Stories</a></li>
                        <li><a href="gallery.html">Photo & Media Gallery</a></li>
                    </ul>
                </div>

                <!-- Col 3: Key Programs -->
                <div class="footer-col">
                    <h3 class="footer-heading">Our Core Programs</h3>
                    <ul class="footer-links">
                        <li><a href="food-for-hunger.html">Food for Hunger Relief</a></li>
                        <li><a href="education.html">Child Education & Remedial Support</a></li>
                        <li><a href="women-empowerment.html">Women Self-Reliance & SHGs</a></li>
                        <li><a href="skill-development.html">Youth Vocational Training</a></li>
                        <li><a href="environment.html">Environment & 20 Trees Monthly</a></li>
                        <li><a href="apna-aangan.html">Apna Aangan Community Center</a></li>
                        <li><a href="campaigns.html">Active Seasonal Campaigns</a></li>
                    </ul>
                </div>

                <!-- Col 4: Contact & Tax Exemption -->
                <div class="footer-col footer-contact-col">
                    <h3 class="footer-heading">Contact & Office</h3>
                    <p class="office-address">
                        <strong>Registered Office:</strong><br>
                        Village Neelwal, Post Office Tikri Kalan,<br>
                        West Delhi, New Delhi – 110041, India.
                    </p>
                    <p class="contact-line"><strong>Phone:</strong> <a href="tel:+919654518368">+91 9654518368</a> (Nitin Gothwal)</p>
                    <p class="contact-line"><strong>Official Email:</strong> <a href="mailto:nitingothwal5468@gmail.com">nitingothwal5468@gmail.com</a></p>
                    <p class="contact-line"><strong>Trust Email:</strong> <a href="mailto:enlightinghumanitytrust@gmail.com">enlightinghumanitytrust@gmail.com</a></p>
                    
                    <div class="footer-donation-box">
                        <span class="upi-label">Direct Verified UPI ID:</span>
                        <div class="upi-code-badge" onclick="copyUpiId()" title="Click to copy UPI ID">
                            <span>9654518368@paytm</span>
                            <span class="copy-tag">📋 Copy</span>
                        </div>
                        <small class="tax-note">Eligible for 80G Tax Exemption. Receipts issued promptly upon UTR submission.</small>
                    </div>
                </div>
            </div>
        </div>

        <!-- Footer Bottom Bar -->
        <div class="footer-bottom">
            <div class="container footer-bottom-inner">
                <p class="copyright-text">
                    &copy; 2026 Enlighting Humanity Trust. All Rights Reserved. Empowering Underprivileged Communities with Dignity.
                </p>
                <div class="legal-links">
                    <a href="privacy-policy.html">Privacy Policy</a>
                    <span class="sep">•</span>
                    <a href="terms.html">Terms of Service</a>
                    <span class="sep">•</span>
                    <a href="refund-policy.html">Donation & Refund Policy</a>
                    <span class="sep">•</span>
                    <a href="transparency.html">Annual Disclosures</a>
                </div>
            </div>
        </div>
    </footer>

    <!-- Back to top button -->
    <button class="back-to-top" id="backToTop" aria-label="Back to top">↑</button>

    <!-- Core Scripts -->
    <script src="js/config.js"></script>
    <script src="js/qrcode.min.js"></script>
    <script src="js/donation.js"></script>
    <script src="js/forms.js"></script>
    <script src="js/main.js"></script>
    '''

def render_page(filename, active_nav, title, meta_desc, content_html, extra_head=""):
    canonical_url = f"https://enlightinghumanitytrust.org/{filename}"
    og_image = "https://enlightinghumanitytrust.org/assets/images/hero-banner.jpg"

    schema_json = {
        "@context": "https://schema.org",
        "@type": "NGO",
        "name": "Enlighting Humanity Trust",
        "alternateName": "Enlighting Humanity",
        "url": "https://enlightinghumanitytrust.org",
        "logo": "https://enlightinghumanitytrust.org/assets/images/logo.png",
        "image": og_image,
        "description": "Non-profit organization in New Delhi dedicated to zero hunger, quality education, women empowerment, skill development, and planting 20+ trees monthly.",
        "telephone": "+91-9654518368",
        "email": "nitingothwal5468@gmail.com",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "Village Neelwal, Post Office Tikri Kalan",
            "addressLocality": "West Delhi",
            "addressRegion": "Delhi",
            "postalCode": "110041",
            "addressCountry": "IN"
        },
        "founder": {
            "@type": "Person",
            "name": "Nitin Gothwal"
        },
        "sameAs": [
            "https://sites.google.com/view/enlighting-humanity/home",
            "https://forms.gle/WL4mJWV7Gi2GaAT38"
        ]
    }

    full_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Enlighting Humanity Trust</title>
    <meta name="description" content="{meta_desc}">
    <link rel="canonical" href="{canonical_url}">
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="{canonical_url}">
    <meta property="og:title" content="{title} | Enlighting Humanity Trust">
    <meta property="og:description" content="{meta_desc}">
    <meta property="og:image" content="{og_image}">

    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:title" content="{title} | Enlighting Humanity Trust">
    <meta property="twitter:description" content="{meta_desc}">
    <meta property="twitter:image" content="{og_image}">

    <!-- Favicon -->
    <link rel="icon" type="image/png" href="assets/images/logo.png">

    <!-- Stylesheets -->
    <link rel="stylesheet" href="css/style.css">
    
    <!-- Structured Data (JSON-LD) -->
    <script type="application/ld+json">
    {json.dumps(schema_json, indent=2)}
    </script>
    {extra_head}
</head>
<body>
    {get_header(active_nav, title)}

    <main id="mainContent">
        {content_html}
    </main>

    {get_footer()}
</body>
</html>'''

    file_path = os.path.join(OUTPUT_DIR, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Generated: {filename}")

print("Master generator module defined successfully.")
