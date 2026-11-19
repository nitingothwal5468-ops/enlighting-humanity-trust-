/**
 * Enlighting Humanity Trust - Master Configuration
 * All official contact details, links, and endpoints are centralized here.
 */
const CONFIG = {
  organisationName: "Enlighting Humanity Trust",
  tagline: "Empowering Lives, Enriching Humanity.",
  registeredOffice: "Village Neelwal, Post Office Tikri Kalan, New Delhi - 110041, India",
  email: "nitingothwal5468@gmail.com",
  altEmail: "enlightinghumanitytrust@gmail.com",
  phone: "+91 9654518368",
  phoneRaw: "+919654518368",
  whatsapp: "919654518368",
  whatsappUrl: "https://wa.me/919654518368",
  instagram: "https://www.instagram.com/enlighting_humanity?dmpr=aXJja29pMXJsMnQy",
  existingGoogleSite: "https://sites.google.com/view/enlighting-humanity/home",
  
  // Volunteer & Contact Form Endpoints
  volunteerFormUrl: "https://forms.gle/WL4mJWV7Gi2GaAT38",
  volunteerSheetUrl: "https://docs.google.com/spreadsheets/d/1Z08j2TGLoha1_fdz3r9j4PKKstEJLtiVP1O1NcZ-Uck/edit?usp=drive_link",
  contactSheetUrl: "https://docs.google.com/spreadsheets/d/10o82aWZJ9xSTUBE9ha2MVLNFM8TI2wBrAk0ilaYn5pQ/edit?usp=drive_link",
  contactFormUrl: "", // Optional published Google Form for Contact
  csrFormEndpoint: "", // Webhook for CSR form (e.g. Google Apps Script)
  
  // UPI Donation Configuration
  upiId: "9654518368@paytm",
  upiPayeeName: "Enlighting Humanity Trust",
  currency: "INR",
  baseUpiUri: "upi://pay?pa=9654518368@paytm&pn=Enlighting%20Humanity%20Trust&cu=INR",
  donationPaymentUrl: "", // Optional Razorpay or Gateway URL

  // Impact Commitments
  treePlantingCommitment: "20 native trees planted every month with children",
  experienceYears: "9+ Years of Community Development & Grassroots Action",
  
  // Accreditations & Transparency
  accreditations: {
    section80G: "50% Tax Exemption on Eligible Donations under Section 80G",
    section12A: "Registered Public Charitable Trust under Section 12A",
    ngoDarpan: "Registered on NITI Aayog Portal (Government of India)",
    jurisdiction: "New Delhi, India"
  }
};

// Export for module or browser window
if (typeof window !== "undefined") {
  window.CONFIG = CONFIG;
}
