/* Veluria Atelier — interactions */
document.addEventListener('DOMContentLoaded', () => {

  // Nav scroll state
  const navbar = document.getElementById('navbar');
  if (navbar) {
    const update = () => {
      if (window.scrollY > 60) navbar.classList.add('scrolled');
      else navbar.classList.remove('scrolled');
    };
    update();
    window.addEventListener('scroll', update, { passive: true });
  }

  // Reveal observer
  const reveals = document.querySelectorAll('.reveal-up, .reveal-image');
  const io = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-revealed');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.14, rootMargin: '0px 0px -10% 0px' });
  reveals.forEach(el => io.observe(el));

  // Parallax
  const parallaxItems = document.querySelectorAll('.parallax-bg');
  if (parallaxItems.length) {
    let ticking = false;
    const onScroll = () => {
      if (ticking) return;
      window.requestAnimationFrame(() => {
        const scrollY = window.scrollY;
        parallaxItems.forEach(img => {
          const rect = img.getBoundingClientRect();
          if (rect.bottom < 0 || rect.top > window.innerHeight) return;
          const speed = parseFloat(img.dataset.speed || 0.18);
          const center = rect.top + rect.height / 2 - window.innerHeight / 2;
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
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const email = form.querySelector('input[type="email"]').value;
      const msg = encodeURIComponent(`Halo Veluria, mohon daftarkan saya pada surat berkala atelier. Email: ${email}`);
      window.open(`https://wa.me/6281234567890?text=${msg}`, '_blank', 'noopener');
      form.reset();
    });
  });

  // Smooth scroll
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
