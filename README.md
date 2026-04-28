# Premium Niche Landing Pages

Koleksi landing page premium yang dibangun untuk lima belas niche bisnis berbeda. Setiap niche memiliki **visual identity, palet warna, tipografi, layout, dan animasi yang independen** — bukan template generik dengan pertukaran teks atau warna.

> Status saat ini: **5 sample preview** untuk review. 10 niche tersisa akan dibangun setelah sample disetujui.

## Sample Preview (5 niche)

| # | Niche | Identity | Folder |
|---|---|---|---|
| 01 | Klinik Kecantikan | Editorial luxury medical · DM Serif Display + Inter · palet bone &amp; mocha | [`klinik/`](./klinik/) |
| 02 | Wedding Organizer | Bridal couture atelier · Italiana + Cormorant · palet bordeaux &amp; gold | [`wedding/`](./wedding/) |
| 03 | Gym &amp; Fitness | Performance brutalism · Antonio + JetBrains Mono · matte black + volt green | [`gym/`](./gym/) |
| 04 | Law Firm | Chambers compendium · Cormorant + EB Garamond · midnight + parchment + oxblood | [`law-firm/`](./law-firm/) |
| 05 | Skincare | Botanical apothecary · Bodoni Moda + Inter · sage + honey | [`skincare/`](./skincare/) |

## Niche Tersisa (akan dibangun)

Supplier · Properti · Kontraktor · Catering · Travel · Corporate · Finance · Digital Agency · Education · Bengkel.

Setiap niche akan dibangun dengan tingkat distinction yang sama dengan lima sample di atas (palet, tipografi, layout, animasi, hero treatment, copywriting).

## Struktur Repo

```
/
├── index.html                # katalog utama (link ke 5 sample)
├── klinik/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   └── assets/
│       ├── img/
│       └── icon/
├── wedding/
│   └── (struktur sama)
├── gym/
├── law-firm/
└── skincare/
```

## Stack

- **Tailwind CSS** (CDN) untuk utility class.
- **Vanilla JavaScript** — no framework, no bundler.
- **Google Fonts** — kombinasi font berbeda per niche.
- **Unsplash** untuk placeholder imagery (mudah diganti dengan asset bisnis).
- **SVG &amp; Unicode** untuk semua icon &amp; ornament. Tidak menggunakan emoji.

## Animasi

Setiap niche memiliki animasi gimmick yang berbeda, antara lain:

- **Klinik:** subtle hero zoom, clip-path image reveal, counter stats.
- **Wedding:** monogram concentric reveal, italic display fade-up, parallax floral.
- **Gym:** hero stats counter, ticker bar bawah, scroll-snap facility rail, metric counters.
- **Law Firm:** SVG seal stroke draw-in, ledger row stagger reveal, italic letterform reveal.
- **Skincare:** bottle floating loop, marquee press strip, soft pastel gradient hero shapes.

Semua animasi memakai easing `cubic-bezier(0.16, 1, 0.3, 1)` untuk feel editorial yang smooth.

## Cara Menjalankan

```bash
# clone repo, lalu serve sebagai static
python3 -m http.server 8080
# buka http://localhost:8080
```

Atau langsung deploy ke GitHub Pages, Netlify, Vercel, atau Cloudflare Pages — tidak perlu build.

## Mengganti Nomor WhatsApp

Semua tombol WhatsApp menggunakan placeholder `6281234567890`. Cari &amp; ganti per folder:

```bash
grep -rl "6281234567890" klinik wedding gym law-firm skincare
# lalu sed -i 's/6281234567890/<NOMOR_KLIEN>/g' <file>
```

## Prinsip Desain

- Tidak ada template generik — setiap niche dibangun terpisah dari nol.
- Tidak ada AI vibes / AI DNA / startup-SaaS aesthetic.
- Tidak ada emoji. SVG &amp; Unicode saja.
- Tidak ada perubahan cursor.
- Whitespace, hierarki tipografi, dan editorial framing menjadi prioritas utama.
