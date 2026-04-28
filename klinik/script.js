document.addEventListener("DOMContentLoaded", () => {
  // navbar scroll
  const navbar = document.getElementById("navbar");
  const onScroll = () => {
    if (window.scrollY > 50) navbar.classList.add("scrolled");
    else navbar.classList.remove("scrolled");
  };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // reveal observer
  const io = new IntersectionObserver((entries, obs) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add("is-revealed");
        obs.unobserve(e.target);
      }
    });
  }, { rootMargin: "0px 0px -10% 0px", threshold: 0.12 });
  document.querySelectorAll(".reveal-up, .reveal-image").forEach(el => io.observe(el));

  // parallax bg
  const parallaxes = document.querySelectorAll(".parallax-bg");
  const onPx = () => {
    const y = window.scrollY;
    parallaxes.forEach(img => {
      const rect = img.parentElement.getBoundingClientRect();
      const speed = parseFloat(img.dataset.speed || 0.18);
      const offset = (rect.top + rect.height / 2 - window.innerHeight / 2) * -speed;
      img.style.transform = `translateY(${offset}px)`;
    });
  };
  window.addEventListener("scroll", onPx, { passive: true });
  onPx();

  // hash anchor smooth
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener("click", e => {
      const href = a.getAttribute("href");
      if (href.length < 2) return;
      const target = document.querySelector(href);
      if (!target) return;
      e.preventDefault();
      target.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  });
});
