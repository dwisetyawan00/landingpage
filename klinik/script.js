/* Klara Skin & Aesthetic — interactions */
document.addEventListener('DOMContentLoaded', () => {

  // 1. Nav scroll state
  const navbar = document.getElementById('navbar');
  if (navbar) {
    const updateNav = () => {
      if (window.scrollY > 60) navbar.classList.add('scrolled');
      else navbar.classList.remove('scrolled');
    };
    updateNav();
    window.addEventListener('scroll', updateNav, { passive: true });
  }

  // 2. IntersectionObserver — reveal-up + reveal-image
  const reveals = document.querySelectorAll('.reveal-up, .reveal-image');
  const io = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-revealed');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.14, rootMargin: '0px 0px -8% 0px' });
  reveals.forEach(el => io.observe(el));

  // 3. Smooth parallax for elements with .parallax-bg
  const parallaxItems = document.querySelectorAll('.parallax-bg');
  if (parallaxItems.length) {
    let ticking = false;
    const onScroll = () => {
      if (ticking) return;
      window.requestAnimationFrame(() => {
        const scrolled = window.scrollY;
        parallaxItems.forEach(img => {
          const rect = img.getBoundingClientRect();
          const visible = rect.top < window.innerHeight && rect.bottom > 0;
          if (!visible) return;
          const speed = parseFloat(img.dataset.speed || 0.18);
          const offset = (scrolled - (img.offsetParent ? img.offsetParent.offsetTop : 0)) * speed;
          img.style.transform = `translateY(${-offset * 0.4}px)`;
        });
        ticking = false;
      });
      ticking = true;
    };
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  // 4. Counter animation for hero stats
  const counters = document.querySelectorAll('.counter');
  const counterIO = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      const el = entry.target;
      const target = parseInt(el.dataset.target || '0', 10);
      const duration = 1600;
      const start = performance.now();
      const ease = (t) => 1 - Math.pow(1 - t, 3); // easeOutCubic
      const fmt = (v) => v >= 1000 ? Math.round(v).toLocaleString('id-ID') : Math.round(v);
      const tick = (now) => {
        const t = Math.min(1, (now - start) / duration);
        el.textContent = fmt(target * ease(t));
        if (t < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
      counterIO.unobserve(el);
    });
  }, { threshold: 0.4 });
  counters.forEach(el => counterIO.observe(el));

  // 5. Year auto-fill
  const year = document.querySelector('[data-year]');
  if (year) year.textContent = new Date().getFullYear();

  // 6. Newsletter -> WhatsApp deeplink
  document.querySelectorAll('form[data-newsletter]').forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const email = form.querySelector('input[type="email"]').value;
      const msg = encodeURIComponent(`Halo Klara, tolong daftarkan saya ke newsletter privat. Email: ${email}`);
      window.open(`https://wa.me/6281234567890?text=${msg}`, '_blank', 'noopener');
      form.reset();
    });
  });

  // 7. Smooth scroll for hash anchors
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', (e) => {
      const href = a.getAttribute('href');
      if (!href || href === '#') return;
      const tgt = document.querySelector(href);
      if (!tgt) return;
      e.preventDefault();
      tgt.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });

});
