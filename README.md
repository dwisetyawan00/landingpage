# Premium Landing Pages

Repositori ini berisi 15 landing page statis untuk berbagai industri bisnis di Indonesia. Semua halaman dibuat sebagai HTML/CSS/JS murni sehingga bisa langsung dibuka di browser atau di-deploy ke GitHub Pages, Netlify, Vercel, Cloudflare Pages, atau hosting statis lain.

## Struktur

- `index.html` — katalog untuk membuka semua landing page.
- `pages/` — 15 halaman landing page terpisah.
- `assets/styles.css` — sistem visual premium bersama.
- `assets/site.js` — enhancement kecil untuk form WhatsApp dan tahun footer.
- `tools/generate_pages.py` — generator konten halaman.

## Cara menjalankan

Buka `index.html` langsung di browser, atau jalankan server statis:

```bash
python3 -m http.server 8080
```

Lalu buka `http://localhost:8080`.

## Mengubah nomor WhatsApp

Nomor WhatsApp masih menggunakan placeholder `6281234567890`. Ubah konstanta `WHATSAPP` di `tools/generate_pages.py`, lalu jalankan:

```bash
python3 tools/generate_pages.py
```

## Daftar halaman

1. Supplier / Distributor
2. Klinik Kecantikan / Kesehatan
3. Properti / Real Estate
4. Kontraktor / Interior
5. Catering / Food Service
6. Travel / Umroh / Tour
7. Wedding Organizer
8. Gym / Fitness Studio
9. Skincare Brand / Beauty Product
10. Corporate Company Profile
11. Law Firm / Konsultan Hukum
12. Finance / Insurance Consultant
13. Digital Agency / Marketing Agency
14. Kursus / Education Center
15. Bengkel / Automotive Service
