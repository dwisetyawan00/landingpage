document.querySelectorAll("form[data-whatsapp]").forEach((form) => {
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    const data = new FormData(form);
    const message = Array.from(data.entries())
      .filter(([, value]) => String(value).trim())
      .map(([key, value]) => `${key}: ${value}`)
      .join("%0A");
    const base = form.getAttribute("data-whatsapp");
    window.open(`${base}${encodeURIComponent(message)}`, "_blank", "noopener");
  });
});

const year = document.querySelector("[data-year]");
if (year) {
  year.textContent = new Date().getFullYear();
}
