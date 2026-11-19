/**
 * Enlighting Humanity Trust - Dynamic UPI & Donation Engine
 */

let selectedAmount = 501;
let selectedCampaign = "General Donation";
let qrInstance = null;

document.addEventListener("DOMContentLoaded", function () {
  initDonationForm();
});

function initDonationForm() {
  const amountBtns = document.querySelectorAll(".amount-pill");
  const customInput = document.getElementById("customAmountInput");
  const campaignSelect = document.getElementById("campaignSelect");

  if (amountBtns.length > 0) {
    amountBtns.forEach((btn) => {
      btn.addEventListener("click", function () {
        amountBtns.forEach((b) => b.classList.remove("active"));
        this.classList.add("active");
        const val = this.getAttribute("data-amount");
        if (val === "custom") {
          if (customInput) {
            customInput.style.display = "block";
            customInput.focus();
            selectedAmount = parseFloat(customInput.value) || 500;
          }
        } else {
          if (customInput) customInput.style.display = "none";
          selectedAmount = parseFloat(val);
        }
        updatePaymentDetails();
      });
    });
  }

  if (customInput) {
    customInput.addEventListener("input", function () {
      const val = parseFloat(this.value);
      if (val && val > 0) {
        selectedAmount = val;
        updatePaymentDetails();
      }
    });
  }

  if (campaignSelect) {
    campaignSelect.addEventListener("change", function () {
      selectedCampaign = this.value;
      updatePaymentDetails();
    });
  }

  // Pre-select campaign if passed in query string (?campaign=food)
  const urlParams = new URLSearchParams(window.location.search);
  const campParam = urlParams.get("campaign");
  if (campParam && campaignSelect) {
    for (let opt of campaignSelect.options) {
      if (opt.value.toLowerCase().includes(campParam.toLowerCase())) {
        campaignSelect.value = opt.value;
        selectedCampaign = opt.value;
        break;
      }
    }
  }

  updatePaymentDetails();
}

function generateUpiUri(amount, campaign) {
  const upiId = (window.CONFIG && window.CONFIG.upiId) || "9654518368@paytm";
  const payee = (window.CONFIG && window.CONFIG.upiPayeeName) || "Enlighting Humanity Trust";
  const note = encodeURIComponent(`Donation - ${campaign}`);
  const amtFormatted = parseFloat(amount).toFixed(2);
  
  return `upi://pay?pa=${upiId}&pn=${encodeURIComponent(payee)}&am=${amtFormatted}&cu=INR&tn=${note}`;
}

function updatePaymentDetails() {
  const upiUri = generateUpiUri(selectedAmount, selectedCampaign);
  
  // Update displayed amount tags
  const amtDisplays = document.querySelectorAll(".current-amount-display");
  amtDisplays.forEach((el) => {
    el.textContent = `₹${selectedAmount.toLocaleString("en-IN")}`;
  });

  // Update Pay via UPI mobile link
  const payBtn = document.getElementById("directUpiBtn");
  if (payBtn) {
    payBtn.href = upiUri;
  }

  // Update QR Code
  const qrContainer = document.getElementById("qrcodeCanvas");
  if (qrContainer && typeof QRCode !== "undefined") {
    qrContainer.innerHTML = "";
    qrInstance = new QRCode(qrContainer, {
      text: upiUri,
      width: 180,
      height: 180,
      colorDark: "#103729",
      colorLight: "#ffffff",
      correctLevel: QRCode.CorrectLevel.M
    });
  }

  // Update Raw UPI ID Display
  const upiIdText = document.getElementById("displayUpiId");
  if (upiIdText && window.CONFIG) {
    upiIdText.textContent = window.CONFIG.upiId;
  }
}

function copyUpiId() {
  const upiId = (window.CONFIG && window.CONFIG.upiId) || "9654518368@paytm";
  navigator.clipboard.writeText(upiId).then(() => {
    const feedback = document.getElementById("copyFeedback");
    if (feedback) {
      feedback.style.display = "inline-block";
      setTimeout(() => {
        feedback.style.display = "none";
      }, 2500);
    }
  }).catch(() => {
    alert(`UPI ID: ${upiId}`);
  });
}

function submitDonorNotice(e) {
  e.preventDefault();
  const name = document.getElementById("donorName") ? document.getElementById("donorName").value : "Kind Supporter";
  const phone = document.getElementById("donorPhone") ? document.getElementById("donorPhone").value : "";
  const email = document.getElementById("donorEmail") ? document.getElementById("donorEmail").value : "";
  const txnId = document.getElementById("donorTxnId") ? document.getElementById("donorTxnId").value : "";

  const summary = `Thank you, ${name}! Your donation notification for ₹${selectedAmount} (${selectedCampaign}) has been recorded. Please share your transaction UTR (${txnId || "pending"}) via WhatsApp at +91 9654518368 for immediate 80G tax receipt dispatch.`;
  
  const statusBox = document.getElementById("donorSubmitSuccess");
  if (statusBox) {
    statusBox.textContent = summary;
    statusBox.style.display = "block";
    statusBox.scrollIntoView({ behavior: "smooth" });
  } else {
    alert(summary);
  }
}
