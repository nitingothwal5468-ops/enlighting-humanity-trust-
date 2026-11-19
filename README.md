# Enlighting Humanity Trust - Official Website Architecture & Deployment Guide

> **"Empowering Lives, Enriching Humanity."**  
> A complete, international-standard, production-ready website for **Enlighting Humanity Trust**, a registered public charitable trust in New Delhi (Village Neelwal, Post Office Tikri Kalan - 110041).

---

## 🌟 Executive Summary

This repository contains the complete 24-page static website for Enlighting Humanity Trust, built to modern web standards with pure vanilla HTML5, semantic CSS3, and modular JavaScript. It contains zero heavyweight framework bloat, loads instantly across 2G/3G/4G/5G and mobile devices, has offline-capable client-side dynamic UPI QR generation, and is 100% ready for immediate production hosting on GitHub Pages, Netlify, Vercel, or custom server infrastructure.

---

## 📁 Repository Structure

```text
enlighting-humanity/
├── index.html                 # 01. Homepage with Hero, Programs, Live Donate Box, Stories
├── about.html                 # 02. About The Trust: History, Philosophy, Leadership
├── mission.html               # 03. Mission Manifesto, 5 Pillars, 2024–2027 Goals
├── vision.html                # 04. 2030 Vision for Grassroots Dignity & Apna Aangan
├── values.html                # 05. Six Foundational Values (Satya, Karuna, Prakriti)
├── our-work.html              # 06. Master Program Overview & Intervention Model
├── food-for-hunger.html       # 07. Project Annapurna: Hot Meals & Dry Ration Kits
├── education.html             # 08. Remedial Learning Pods & Dropout Re-enrollment
├── women-empowerment.html     # 09. Vocational Tailoring, SHGs & Menstrual Dignity
├── skill-development.html     # 10. Youth Computer Literacy & Job Readiness
├── environment.html           # 11. Signature 20 Native Trees/Month Commitment
├── apna-aangan.html           # 12. Flagship Community Hub & Learning Sanctuary
├── campaigns.html             # 13. Active & Seasonal Relief Campaigns
├── volunteer.html             # 14. Volunteer Portal (Integrated Google Form)
├── partner.html               # 15. Institutional Partnerships (Colleges, NGOs)
├── csr.html                   # 16. Corporate CSR Portal (Schedule VII Compliant)
├── donate.html                # 17. Master Donation Hub: Dynamic UPI QR, NEFT/RTGS
├── gallery.html               # 18. Filterable Impact Photo Gallery
├── stories.html               # 19. Authentic Case Studies & Beneficiary Stories
├── transparency.html          # 20. Legal Status, 12A/80G, Financial Stewardship
├── contact.html               # 21. Contact Desk, Village Neelwal Address, Transit
├── privacy-policy.html        # 22. DPDP Act & IT Act Compliant Privacy Policy
├── terms.html                 # 23. Terms of Service & Intellectual Property
├── refund-policy.html         # 24. Donation Cancellation & Refund Policy
│
├── css/
│   └── style.css              # Master Design System (Forest Green palette, Responsive)
│
├── js/
│   ├── config.js              # Centralized Configuration (UPI, Emails, Endpoints)
│   ├── qrcode.min.js          # Pure client-side offline QR Code generator
│   ├── donation.js            # Dynamic UPI QR & mobile deep link engine
│   ├── forms.js               # Native CSR & General Contact form validator
│   └── main.js                # Navigation drawer, accordions, gallery filters
│
├── assets/
│   └── images/
│       ├── logo.png                   # High-res authentic transparent logo (2048x2048)
│       ├── hero-banner.jpg            # Genuine field photo: Community leaders
│       ├── tree-planting-children.jpg # Authentic photo: Children planting native trees
│       ├── children-activity.jpg      # Authentic photo: Remedial learning session
│       └── community-drive.jpg        # Authentic photo: Village community mobilization
│
├── sitemap.xml                # Search Engine Sitemap for all 24 URLs
├── robots.txt                 # Search Engine Crawler Guidance
└── README.md                  # Complete Technical Documentation & Deployment Guide
```

---

## ⚙️ Central Configuration (`js/config.js`)

All critical contact points, UPI parameters, and form endpoints are decoupled into `js/config.js`. If your phone number, email, or Google Apps Script URL changes in the future, you only need to update this single file:

```javascript
window.CONFIG = {
  trustName: "Enlighting Humanity Trust",
  tagline: "Empowering Lives, Enriching Humanity.",
  
  // Official Banking & UPI Coordinates
  upiId: "9654518368@paytm",
  upiPayeeName: "Enlighting Humanity Trust",
  
  // Official Trustee Contacts
  contactPhone: "+919654518368",
  contactPhoneFormatted: "+91 9654518368",
  contactPerson: "Nitin Gothwal",
  contactEmailPrimary: "nitingothwal5468@gmail.com",
  contactEmailTrust: "enlightinghumanitytrust@gmail.com",
  
  // Official Registered Office
  officeAddress: "Village Neelwal, Post Office Tikri Kalan, New Delhi – 110041, India",
  
  // Backend Forms Endpoints
  volunteerGoogleFormUrl: "https://forms.gle/WL4mJWV7Gi2GaAT38",
  csrFormEndpoint: "", // Insert Google Apps Script Executable URL here
  donationPaymentUrl: "" // Optional gateway webhook
};
```

---

## 💳 Dynamic UPI Donation Engine

The donation flow (`donate.html` and the homepage widget) implements a client-side dynamic QR generator:
1. **Donor selects an amount** (`₹101`, `₹251`, `₹501`, `₹1,001`, `₹2,501`, or Custom).
2. **Selects a program** (e.g., Food for Hunger, Tree Plantation, Education).
3. **Engine instantly builds a standard UPI URI**:
   `upi://pay?pa=9654518368@paytm&pn=Enlighting%20Humanity%20Trust&am=501.00&cu=INR&tn=Donation%20-%20Education`
4. **Pure Client-Side Rendering:** Uses `js/qrcode.min.js` to render the scannable code locally without sending data to external third-party QR generation APIs (ensures 100% uptime, zero latency, and total privacy).
5. **Mobile Deep Links:** Automatically populates a direct click-to-pay button that launches Paytm, PhonePe, BHIM, or Google Pay on mobile devices.
6. **One-Click UPI Copy:** Lets donors copy `9654518368@paytm` to clipboard with real-time feedback.
7. **80G Tax Exemption Notice:** Reminds donors to share the 12-digit transaction UTR via WhatsApp at `+91 9654518368` for instant 80G tax receipt dispatch.

---

## 🚀 Deployment Instructions

### Method 1: GitHub Pages (Recommended)

1. **Create or Open Your GitHub Repository:**
   - For example: `https://github.com/nitingothwal5468-ops/enlighting-humanity`
2. **Push the Files to the `main` branch:**
   ```bash
   git init
   git remote add origin https://github.com/nitingothwal5468-ops/enlighting-humanity.git
   git add .
   git commit -m "Deploy complete 24-page Enlighting Humanity Trust website"
   git branch -M main
   git push -u origin main --force
   ```
3. **Enable GitHub Pages:**
   - In GitHub, go to **Settings** > **Pages**.
   - Under **Build and deployment** > **Source**, choose **Deploy from a branch**.
   - Select branch: `main` and folder: `/ (root)`.
   - Click **Save**.
4. **Your Live Site:**
   - The site will be instantly live at `https://<username>.github.io/<repo-name>/`.
   - To connect a custom domain (e.g., `enlightinghumanitytrust.org`), enter it in the **Custom domain** box and follow standard DNS CNAME/A record mapping.

### Method 2: Netlify / Vercel Drag-and-Drop

1. Log in to [Netlify](https://app.netlify.com/) or [Vercel](https://vercel.com/).
2. Drag and drop the unzipped `enlighting-humanity` folder directly into the dashboard.
3. Your production website will be deployed in under 10 seconds with free automated HTTPS SSL certificates!

### Method 3: Standard Web Hosting (cPanel / Apache / Nginx)

1. Upload all contents of the `enlighting-humanity/` directory into your server's `public_html/` or root directory.
2. The website requires no PHP, Python, or database backend — it executes entirely in the client browser with blazing fast load times.

---

## 📊 Connected Backends & Data Flows

1. **Volunteer Recruitment:**
   - Form: `https://forms.gle/WL4mJWV7Gi2GaAT38`
   - Response Sheet: `1Z08j2TGLoha1_fdz3r9j4PKKstEJLtiVP1O1NcZ-Uck`
2. **Contact Queries:**
   - Response Sheet: `10o82aWZJ9xSTUBE9ha2MVLNFM8TI2wBrAk0ilaYn5pQ`
3. **Application Portal:**
   - Live URL: `https://nitingothwal5468-ops.github.io/apply/`
   - Connected Google Apps Script: `https://script.google.com/macros/s/AKfycbwuNdKTkcVg2T7ACqBgsnd5o3Zi4-HRm73ieOarwZGNtZX_YimWiFKHmFLN1jUpqyK1/exec`

---

## 🔒 Verification & Compliance Notes

- **Indian Trusts Act, 1882:** Public Charitable Trust registered in West Delhi.
- **Section 80G & 12A:** Donations eligible for 50% deduction under Section 80G of the Indian Income Tax Act, 1961.
- **Section 135 Companies Act (CSR):** Eligible under Schedule VII Clauses (i) Eradicating hunger, (ii) Education & skill development, (iii) Women empowerment, (iv) Environmental sustainability, and (x) Rural community development.
- **Non-Fabricated Metrics:** The site highlights authentic, verifiable commitments (minimum 20 native trees planted monthly with local school children, 9+ years grassroots journey since 2017) without making unsubstantiated claims.

---

*© 2026 Enlighting Humanity Trust. All Rights Reserved. Built with transparent social responsibility.*
