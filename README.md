# Premium Landing Pages — 15 Niche · 15 Visual Identity

Repositori ini berisi **15 landing page premium**, di mana setiap halaman memiliki
**design language sendiri** — palet warna, sistem tipografi, layout, irama spasial,
dan visual rhythm yang dirancang berdasarkan psikologi pembeli (buyer psychology)
masing-masing niche.

> **Tidak ada shared CSS template.**
> Setiap halaman menggunakan file CSS terpisah dengan `:root` tokens, font stack,
> dan layout system yang dirancang sebagai bisnis nyata — bukan sebagai showcase
> komponen yang dipukul rata.

## Struktur

```
.
├── index.html                          # Katalog 15 halaman
├── assets/
│   ├── css/
│   │   ├── index.css
│   │   ├── supplier-distributor.css
│   │   ├── klinik-kecantikan-kesehatan.css
│   │   ├── properti-real-estate.css
│   │   ├── kontraktor-interior.css
│   │   ├── catering-food-service.css
│   │   ├── travel-umroh-tour.css
│   │   ├── wedding-organizer.css
│   │   ├── gym-fitness-studio.css
│   │   ├── skincare-beauty-product.css
│   │   ├── corporate-company-profile.css
│   │   ├── law-firm-konsultan-hukum.css
│   │   ├── finance-insurance-consultant.css
│   │   ├── digital-marketing-agency.css
│   │   ├── education-kursus-academy.css
│   │   └── bengkel-automotive-service.css
│   └── site.js                         # Tahun footer + form WhatsApp
└── pages/
    └── ...                             # 15 file HTML, 1 untuk tiap niche
```

## Daftar halaman & visual identity

| № | Halaman | Visual identity |
| --- | --- | --- |
| 01 | Supplier &amp; Distributor | Industrial corporate · ledger aesthetic · steel monospace |
| 02 | Klinik Kecantikan &amp; Kesehatan | Luxury medical · botanical sage rose · editorial centered |
| 03 | Properti &amp; Real Estate | Cinematic dark · brass accent · magazine editorial |
| 04 | Kontraktor &amp; Interior | Atelier studio · terracotta walnut · drafting numbered sections |
| 05 | Catering &amp; Food Service | Apothecary fine dining · claret &amp; gold · dot-leader pricing |
| 06 | Travel · Umroh · Tour | Spiritual premium · deep teal · arch motif · itinerary timeline |
| 07 | Wedding Organizer | Bridal couture · bordeaux &amp; rose · monogrammed atelier |
| 08 | Gym &amp; Fitness Studio | Performance · matte black · volt green · live data ticker |
| 09 | Skincare &amp; Beauty Product | Botanical apothecary · sage &amp; peach · hero bottle display |
| 10 | Corporate Company Profile | Annual report · navy &amp; copper · holding multi-divisi |
| 11 | Law Firm &amp; Konsultan Hukum | Legal authority · oxblood &amp; gilt · compendium symbols |
| 12 | Finance &amp; Insurance Consultant | Private banking · midnight teal &amp; mint · dashboard chart |
| 13 | Digital &amp; Marketing Agency | Boutique editorial · oversized type · asymmetric portfolio |
| 14 | Education Center &amp; Kursus | Scholastic prospectus · forest green &amp; ivory |
| 15 | Bengkel &amp; Automotive Service | Industrial workshop · matte black + hi-vis amber · work-order ticket |

## Cara menjalankan

Buka `index.html` langsung di browser, atau jalankan server statis:

```bash
python3 -m http.server 8080
# lalu buka http://localhost:8080
```

## Mengganti nomor WhatsApp

Setiap CTA pada halaman menggunakan format:

```
https://wa.me/<nomor>?text=<pesan>
```

Saat ini nomor placeholder adalah `6281234567890`. Untuk mengubah seluruhnya:

```bash
# di root repository
grep -rl "6281234567890" pages/ | xargs sed -i 's/6281234567890/<nomor-baru>/g'
```

## Deployment

Halaman ini adalah HTML/CSS murni tanpa framework, dapat di-deploy ke:

- GitHub Pages
- Netlify
- Vercel
- Cloudflare Pages
- Hosting statis lainnya

## Prinsip desain

- Tidak ada shared CSS template — setiap halaman berdiri sendiri.
- Tidak ada AI vibes / AI gradient / template generator aesthetic.
- Tidak ada emoji dekoratif — hanya SVG icon dan Unicode symbol.
- Setiap halaman dirancang sebagai bisnis nyata, dengan identitas yang
  konsisten di header, hero, sections, testimonial, FAQ, dan final CTA.
- Setiap halaman menutup dengan WhatsApp CTA yang relevan dengan konversi
  utama niche tersebut (booking, konsultasi, inquiry, atau order).
