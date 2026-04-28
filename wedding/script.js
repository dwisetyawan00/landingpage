/* Maharaja Couture — interactions */
document.addEventListener('DOMContentLoaded', () => {

  const navbar = document.getElementById('navbar');
  const onScrollNav = () => {
    if (window.scrollY > 60) navbar.classList.add('scrolled');
    else navbar.classList.remove('scrolled');
  };
  onScrollNav();
  window.addEventListener('scroll', onScrollNav, { passive: true });

  // reveal observer
  const io = new IntersectionObserver((entries, obs) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('is-revealed');
        obs.unobserve(e.target);
      }
    });
  }, { threshold: 0.14, rootMargin: '0px 0px -8% 0px' });
  document.querySelectorAll('.reveal-up, .reveal-image').forEach(el => io.observe(el));

  // parallax bg — translate based on element's center distance from viewport center
  const parallaxImgs = document.querySelectorAll('.parallax-bg');
  if (parallaxImgs.length) {
    let ticking = false;
    const update = () => {
      const vh = window.innerHeight;
      parallaxImgs.forEach(img => {
        const speed = parseFloat(img.dataset.speed || '0.15');
        const rect = img.parentElement.getBoundingClientRect();
        const center = rect.top + rect.height / 2;
        const distFromCenter = center - vh / 2;
        img.style.transform = `translateY(${-distFromCenter * speed}px)`;
      });
      ticking = false;
    };
    const onScrollPx = () => {
      if (!ticking) { requestAnimationFrame(update); ticking = true; }
    };
    update();
    window.addEventListener('scroll', onScrollPx, { passive: true });
    window.addEventListener('resize', update);
  }

  // smooth hash anchor
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', (e) => {
      const id = a.getAttribute('href');
      if (id.length <= 1) return;
      const t = document.querySelector(id);
      if (!t) return;
      e.preventDefault();
      const top = t.getBoundingClientRect().top + window.scrollY - 80;
      window.scrollTo({ top, behavior: 'smooth' });
    });
  });

  // newsletter -> WA
  document.querySelectorAll('form[data-newsletter]').forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const email = form.querySelector('input[type="email"]').value;
      const msg = encodeURIComponent(`Halo Maharaja Couture, mohon kirimkan surat atelier ke email: ${email}`);
      window.open(`https://wa.me/6281234567890?text=${msg}`, '_blank', 'noopener');
      form.reset();
    });
  });

});
