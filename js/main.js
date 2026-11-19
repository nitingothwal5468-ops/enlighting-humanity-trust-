/* Enlighting Humanity Trust — shared interface behaviour */
(function () {
  'use strict';

  function copyText(text) {
    if (navigator.clipboard && window.isSecureContext) return navigator.clipboard.writeText(text);
    return new Promise(function (resolve, reject) {
      var area = document.createElement('textarea');
      area.value = text;
      area.style.position = 'fixed';
      area.style.opacity = '0';
      document.body.appendChild(area);
      area.select();
      try { document.execCommand('copy'); resolve(); } catch (err) { reject(err); }
      document.body.removeChild(area);
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    var drawer = document.getElementById('mobileDrawer');
    var overlay = document.getElementById('mobileOverlay');
    var opener = document.getElementById('mobileMenuOpen');
    var closer = document.getElementById('mobileMenuClose');
    var header = document.getElementById('mainHeader');
    var backToTop = document.getElementById('backToTop');

    function closeDrawer() {
      if (!drawer) return;
      drawer.classList.remove('is-open');
      if (overlay) overlay.classList.remove('is-visible');
      document.body.classList.remove('menu-open');
      drawer.setAttribute('aria-hidden', 'true');
      if (opener) opener.setAttribute('aria-expanded', 'false');
    }

    function openDrawer() {
      if (!drawer) return;
      drawer.classList.add('is-open');
      if (overlay) overlay.classList.add('is-visible');
      document.body.classList.add('menu-open');
      drawer.setAttribute('aria-hidden', 'false');
      if (opener) opener.setAttribute('aria-expanded', 'true');
      if (closer) closer.focus();
    }

    if (opener) opener.addEventListener('click', openDrawer);
    if (closer) closer.addEventListener('click', closeDrawer);
    if (overlay) overlay.addEventListener('click', closeDrawer);
    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape') closeDrawer();
    });

    document.querySelectorAll('.mobile-dropdown-toggle').forEach(function (link) {
      link.addEventListener('click', function (event) {
        /* First tap expands submenu; the title itself remains a normal accessible link on desktop. */
        if (window.innerWidth <= 980) {
          event.preventDefault();
          var parent = link.closest('.mobile-dropdown');
          parent.classList.toggle('is-expanded');
        }
      });
    });

    function onScroll() {
      var y = window.scrollY || document.documentElement.scrollTop;
      if (header) header.classList.toggle('is-scrolled', y > 8);
      if (backToTop) backToTop.classList.toggle('is-visible', y > 420);
    }
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();

    if (backToTop) {
      backToTop.addEventListener('click', function () {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      });
    }

    document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
      anchor.addEventListener('click', function (event) {
        var id = anchor.getAttribute('href');
        var target = id && id.length > 1 ? document.querySelector(id) : null;
        if (target) {
          event.preventDefault();
          closeDrawer();
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      });
    });

    document.querySelectorAll('.filter-btn').forEach(function (button) {
      button.addEventListener('click', function () {
        var filter = button.getAttribute('data-filter') || 'all';
        document.querySelectorAll('.filter-btn').forEach(function (item) {
          item.classList.toggle('active', item === button);
        });
        document.querySelectorAll('.gallery-item').forEach(function (item) {
          var categories = (item.getAttribute('data-category') || '').split(' ');
          var show = filter === 'all' || categories.indexOf(filter) !== -1;
          item.classList.toggle('is-hidden', !show);
        });
      });
    });

    document.querySelectorAll('.faq-question').forEach(function (question) {
      question.setAttribute('aria-expanded', 'false');
      question.addEventListener('click', function () {
        var item = question.closest('.faq-item');
        var expanded = item.classList.toggle('is-open');
        question.setAttribute('aria-expanded', String(expanded));
      });
    });

    document.querySelectorAll('.upi-code-badge').forEach(function (badge) {
      badge.addEventListener('keydown', function (event) {
        if (event.key === 'Enter' || event.key === ' ') {
          event.preventDefault();
          if (typeof window.copyUpiId === 'function') window.copyUpiId();
          else copyText('9654518368@paytm');
        }
      });
      badge.setAttribute('tabindex', '0');
      badge.setAttribute('role', 'button');
    });
  });
}());
