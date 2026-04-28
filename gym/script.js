/* FORGE Athletic Club — interactions */
document.addEventListener('DOMContentLoaded', () => {
  const navbar = document.getElementById('navbar');
  if (navbar) {
    const update = () => navbar.classList.toggle('scrolled', window.scrollY > 60);
    update();
    window.addEventListener('scroll', update, { passive: true });
  }

  // Reveal
  const reveals = document.querySelectorAll('.reveal-up, .reveal-image');
  const io = new IntersectionObserver((entries, obs) => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('is-revealed'); obs.unobserve(e.target); } });
  }, { threshold: 0.14, rootMargin: '0px 0px -8% 0px' });
  reveals.forEach(el => io.observe(el));

  // Counters
  const counters = document.querySelectorAll('.counter');
  const cIO = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      const el = entry.target;
      const target = parseFloat(el.dataset.target || '0');
      const suffix = el.dataset.suffix || '';
      const duration = 1700;
      const start = performance.now();
      const ease = (t) => 1 - Math.pow(1 - t, 3);
      const fmt = (v) => (v >= 1000 ? Math.round(v).toLocaleString('id-ID') : Math.round(v));
      const tick = (now) => {
        const t = Math.min(1, (now - start) / duration);
        el.textContent = fmt(target * ease(t)) + (t === 1 ? suffix : (suffix && t > 0.95 ? suffix : ''));
        if (t < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
      cIO.unobserve(el);
    });
  }, { threshold: 0.4 });
  counters.forEach(el => cIO.observe(el));

  // Parallax
  const parallaxItems = document.querySelectorAll('.parallax-bg');
  if (parallaxItems.length) {
    let ticking = false;
    const onScroll = () => {
      if (ticking) return;
      window.requestAnimationFrame(() => {
        parallaxItems.forEach(img => {
          const r = img.getBoundingClientRect();
          if (r.bottom < 0 || r.top > window.innerHeight) return;
          const speed = parseFloat(img.dataset.speed || 0.18);
          const center = r.top + r.height / 2 - window.innerHeight / 2;
          img.style.transform = `translateY(${-center * speed}px)`;
        });
        ticking = false;
      });
      ticking = true;
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  // Year
  const year = document.querySelector('[data-year]');
  if (year) year.textContent = new Date().getFullYear();

  // Newsletter
  document.querySelectorAll('form[data-newsletter]').forEach(form => {
    form.addEventListener('submit', e => {
      e.preventDefault();
      const email = form.querySelector('input[type="email"]').value;
      const msg = encodeURIComponent(`Halo Forge, daftarkan saya ke newsletter performance. Email: ${email}`);
      window.open(`https://wa.me/6281234567890?text=${msg}`, '_blank', 'noopener');
      form.reset();
    });
  });

  // Smooth scroll
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      const href = a.getAttribute('href');
      if (!href || href === '#') return;
      const tgt = document.querySelector(href);
      if (!tgt) return;
      e.preventDefault();
      tgt.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });
});
