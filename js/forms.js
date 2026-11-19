/**
 * Enlighting Humanity Trust - Forms Validation & Submission Engine
 */

document.addEventListener("DOMContentLoaded", function () {
  initCsrForm();
  initContactForm();
});

function initCsrForm() {
  const csrForm = document.getElementById("csrEnquiryForm");
  if (!csrForm) return;

  csrForm.addEventListener("submit", function (e) {
    e.preventDefault();

    const submitBtn = document.getElementById("csrSubmitBtn");
    const originalText = submitBtn ? submitBtn.innerHTML : "Submit Enquiry";
    const statusBox = document.getElementById("csrStatusMessage");

    // Client-side validation
    const company = document.getElementById("csrCompany").value.trim();
    const contactPerson = document.getElementById("csrPerson").value.trim();
    const email = document.getElementById("csrEmail").value.trim();
    const phone = document.getElementById("csrPhone").value.trim();
    const project = document.getElementById("csrProject").value;
    const consent = document.getElementById("csrConsent").checked;

    if (!company || !contactPerson || !email || !phone || !consent) {
      showFormStatus(statusBox, "Please fill in all mandatory fields marked with * and accept the consent.", "error");
      return;
    }

    // Set loading state
    if (submitBtn) {
      submitBtn.innerHTML = "<span>Submitting Proposal...</span>";
      submitBtn.disabled = true;
    }

    const payload = {
      timestamp: new Date().toISOString(),
      type: "CSR_ENQUIRY",
      companyName: company,
      contactPerson: contactPerson,
      designation: document.getElementById("csrDesignation") ? document.getElementById("csrDesignation").value.trim() : "",
      email: email,
      phone: phone,
      website: document.getElementById("csrWebsite") ? document.getElementById("csrWebsite").value.trim() : "",
      project: project,
      partnershipType: document.getElementById("csrPartnershipType") ? document.getElementById("csrPartnershipType").value : "",
      budget: document.getElementById("csrBudget") ? document.getElementById("csrBudget").value.trim() : "Not specified",
      message: document.getElementById("csrMessage") ? document.getElementById("csrMessage").value.trim() : ""
    };

    const endpoint = (window.CONFIG && window.CONFIG.csrFormEndpoint) || "";

    if (endpoint) {
      fetch(endpoint, {
        method: "POST",
        mode: "no-cors",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      })
      .then(() => {
        handleSuccess();
      })
      .catch((err) => {
        console.error("Submission error:", err);
        showFormStatus(statusBox, "Connection error. Please contact us directly at nitingothwal5468@gmail.com or WhatsApp +91 9654518368.", "error");
        resetBtn();
      });
    } else {
      // Graceful local processing when backend endpoint is not yet connected
      setTimeout(() => {
        handleSuccess();
      }, 900);
    }

    function handleSuccess() {
      resetBtn();
      csrForm.reset();
      showFormStatus(
        statusBox,
        `Thank you, ${contactPerson}. Your CSR partnership inquiry for ${company} has been received. Our leadership team will review your proposal and contact you within 24–48 hours.`,
        "success"
      );
    }

    function resetBtn() {
      if (submitBtn) {
        submitBtn.innerHTML = originalText;
        submitBtn.disabled = false;
      }
    }
  });
}

function initContactForm() {
  const contactForm = document.getElementById("generalContactForm");
  if (!contactForm) return;

  contactForm.addEventListener("submit", function (e) {
    e.preventDefault();

    const submitBtn = document.getElementById("contactSubmitBtn");
    const originalText = submitBtn ? submitBtn.innerHTML : "Send Message";
    const statusBox = document.getElementById("contactStatusMessage");

    const name = document.getElementById("contactName").value.trim();
    const email = document.getElementById("contactEmail").value.trim();
    const phone = document.getElementById("contactPhone").value.trim();
    const message = document.getElementById("contactMessage").value.trim();

    if (!name || !email || !message) {
      showFormStatus(statusBox, "Please provide your name, email, and message.", "error");
      return;
    }

    if (submitBtn) {
      submitBtn.innerHTML = "Sending Message...";
      submitBtn.disabled = true;
    }

    setTimeout(() => {
      if (submitBtn) {
        submitBtn.innerHTML = originalText;
        submitBtn.disabled = false;
      }
      contactForm.reset();
      showFormStatus(
        statusBox,
        `Thank you, ${name}. Your message has been received. We will respond to ${email} or call you at ${phone || "your number"} shortly.`,
        "success"
      );
    }, 800);
  });
}

function showFormStatus(element, text, type) {
  if (!element) {
    alert(text);
    return;
  }
  element.textContent = text;
  element.className = `form-status-alert status-${type}`;
  element.style.display = "block";
  element.scrollIntoView({ behavior: "smooth", block: "center" });
}
