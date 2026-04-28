/* Wirjadinata & Partners — interactions */
document.addEventListener('DOMContentLoaded', () => {
  const navbar = document.getElementById('navbar');
  if (navbar) {
    const update = () => navbar.classList.toggle('scrolled', window.scrollY > 60);
    update();
    window.addEventListener('scroll', update, { passive: true });
  }

  const reveals = document.querySelectorAll('.reveal-up, .reveal-image');
  const io = new IntersectionObserver((entries, obs) => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('is-revealed'); obs.unobserve(e.target); } });
  }, { threshold: 0.14, rootMargin: '0px 0px -8% 0px' });
  reveals.forEach(el => io.observe(el));

  // Parallax
  const parallax = document.querySelectorAll('.parallax-bg');
  if (parallax.length) {
    let ticking = false;
    const onScroll = () => {
      if (ticking) return;
      window.requestAnimationFrame(() => {
        parallax.forEach(img => {
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

  const year = document.querySelector('[data-year]');
  if (year) year.textContent = new Date().getFullYear();

  document.querySelectorAll('form[data-newsletter]').forEach(form => {
    form.addEventListener('submit', e => {
      e.preventDefault();
      const email = form.querySelector('input[type="email"]').value;
      const msg = encodeURIComponent(`Halo Wirjadinata & Partners, mohon daftarkan saya pada surat berkala. Email: ${email}`);
      window.open(`https://wa.me/6281234567890?text=${msg}`, '_blank', 'noopener');
      form.reset();
    });
  });

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
