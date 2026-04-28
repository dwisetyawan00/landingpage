from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / "pages"
WHATSAPP = "https://wa.me/6281234567890?text="


LANDINGS = [
    {
        "slug": "supplier-distributor",
        "number": "01",
        "brand": "Nusantara Supply Co.",
        "category": "Supplier / Distributor",
        "eyebrow": "B2B Supply Partner",
        "title": "Pasokan material skala besar dengan kontrol mutu yang tegas.",
        "lead": "Landing page untuk supplier bahan bangunan, industrial supplier, dan distributor besar yang membutuhkan tampilan serius, kredibel, dan siap mengubah pengunjung menjadi inquiry bisnis.",
        "cta": "Konsultasi Kebutuhan via WhatsApp",
        "secondary": "Lihat Kategori Produk",
        "visual_title": "Reliable procurement for demanding business operations.",
        "visual_items": [
            ("Material bangunan", "ready stock"),
            ("Industrial parts", "curated vendor"),
            ("Distribusi nasional", "B2B terms"),
        ],
        "assurance": [
            ("Kontrak B2B", "Skema suplai jelas untuk pembelian rutin dan proyek."),
            ("Mutu terverifikasi", "Produk dikurasi berdasarkan standar penggunaan lapangan."),
            ("Respons cepat", "Tim sales siap menyiapkan penawaran dan ketersediaan stok."),
        ],
        "metrics": [
            ("12+", "tahun pengalaman suplai"),
            ("680+", "SKU aktif"),
            ("34", "kota distribusi"),
            ("98%", "repeat order korporat"),
        ],
        "sections": [
            {
                "kicker": "Company Trust Value",
                "title": "Dibangun untuk pembelian korporat yang membutuhkan kepastian.",
                "body": "Setiap alur disusun agar calon klien langsung memahami kapasitas, kredibilitas, dan cara memulai permintaan penawaran.",
                "items": [
                    ("Dokumen lengkap", "Profil perusahaan, quotation, invoice, dan kebutuhan administrasi procurement disiapkan rapi."),
                    ("Stok terencana", "Perencanaan kebutuhan proyek dan pembelian bulanan ditangani dengan kontrol ketersediaan."),
                    ("Harga bisnis", "Penawaran disesuaikan berdasarkan volume, jadwal pengiriman, dan cakupan area."),
                ],
            },
            {
                "kicker": "Product Categories",
                "title": "Kategori produk untuk kebutuhan pembangunan dan operasional industri.",
                "body": "Struktur kategori dibuat jelas agar pembeli B2B cepat menemukan kebutuhan utama.",
                "items": [
                    ("Bahan bangunan", "Semen, baja ringan, cat, waterproofing, sanitasi, dan material finishing."),
                    ("Peralatan industri", "Tools, safety equipment, spare part mesin, fastener, dan kebutuhan workshop."),
                    ("Kebutuhan proyek", "Pengadaan volume besar, jadwal bertahap, dan koordinasi logistik lapangan."),
                    ("MRO supply", "Maintenance, repair, and operations untuk pabrik, gudang, dan fasilitas bisnis."),
                    ("Logistik distribusi", "Pengiriman regional dan nasional dengan koordinasi dokumen yang tertata."),
                    ("Procurement support", "Pendampingan pemilihan produk sesuai spesifikasi teknis proyek."),
                ],
            },
            {
                "kicker": "Why Choose Us",
                "title": "Alasan calon klien percaya sebelum mengirim inquiry.",
                "body": "Bagian ini menegaskan kemampuan operasional, bukan sekadar tampilan katalog.",
                "items": [
                    ("Account manager khusus", "Komunikasi lebih ringkas untuk quotation, revisi, dan tindak lanjut pembelian."),
                    ("Vendor network kuat", "Akses produk luas untuk kebutuhan standar maupun spesifikasi khusus."),
                    ("Pengiriman terkoordinasi", "Jadwal pengiriman disusun sesuai prioritas proyek dan ketersediaan lokasi."),
                ],
            },
            {
                "kicker": "Industries Served",
                "title": "Melayani sektor dengan kebutuhan supply yang konsisten.",
                "body": "Dari konstruksi hingga manufaktur, halaman diarahkan untuk membangun relevansi dengan segmen B2B.",
                "items": [
                    ("Kontraktor & developer", "Material proyek, finishing, dan kebutuhan lapangan."),
                    ("Pabrik & manufaktur", "Spare part, safety, MRO, dan kebutuhan operasional."),
                    ("Retail & reseller", "Pasokan grosir dengan dukungan harga dan ketersediaan."),
                ],
            },
        ],
        "testimonials": [
            ("Procurement Manager, Grup Konstruksi", "Penawaran jelas, stok cepat dikonfirmasi, dan pengiriman material ke proyek berjalan sesuai jadwal."),
            ("Owner, Distributor Regional", "Timnya memahami kebutuhan grosir. Komunikasi rapi dan proses repeat order sangat mudah."),
            ("Facility Manager, Manufaktur", "Kami terbantu untuk kebutuhan MRO rutin karena respons quotation konsisten dan profesional."),
        ],
        "faq": [
            ("Apakah bisa pembelian volume besar?", "Bisa. Tim sales akan menyesuaikan harga, jadwal pengiriman, dan dokumen berdasarkan volume kebutuhan."),
            ("Apakah melayani perusahaan di luar kota?", "Ya, pengiriman dapat dikoordinasikan ke berbagai area dengan estimasi biaya dan jadwal yang transparan."),
            ("Bagaimana cara meminta quotation?", "Kirim daftar item, volume, dan lokasi pengiriman melalui WhatsApp agar tim dapat menyiapkan penawaran."),
        ],
        "contact": ("Kirim daftar kebutuhan, volume, lokasi pengiriman, dan target waktu. Tim sales akan menyiapkan konsultasi awal dan estimasi penawaran."),
    },
    {
        "slug": "klinik-kecantikan-kesehatan",
        "number": "02",
        "brand": "Aurelia Clinic",
        "category": "Klinik Kecantikan / Kesehatan",
        "eyebrow": "Luxury Medical Care",
        "title": "Perawatan estetika dan kesehatan dengan pengalaman klinik premium.",
        "lead": "Dirancang untuk klinik kecantikan atau kesehatan yang ingin menonjolkan kepercayaan medis, kenyamanan konsultasi, dan presentasi layanan high-end.",
        "cta": "Booking Konsultasi",
        "secondary": "Lihat Treatment",
        "visual_title": "Personalized care with calm, clinical confidence.",
        "visual_items": [
            ("Medical assessment", "doctor led"),
            ("Signature treatment", "premium protocol"),
            ("Aftercare guidance", "personal plan"),
        ],
        "assurance": [
            ("Dokter berpengalaman", "Konsultasi dilakukan dengan pendekatan profesional dan terukur."),
            ("Protokol higienis", "Setiap tindakan mengikuti standar kenyamanan dan keamanan klinik."),
            ("Hasil natural", "Fokus pada perawatan bertahap yang tetap elegan dan proporsional."),
        ],
        "metrics": [
            ("8+", "tahun praktik klinis"),
            ("18k+", "kunjungan pasien"),
            ("4.9", "rating pengalaman"),
            ("21", "pilihan treatment"),
        ],
        "sections": [
            {
                "kicker": "Treatment Highlights",
                "title": "Layanan unggulan yang dipresentasikan secara premium dan meyakinkan.",
                "body": "Tiap treatment disusun untuk membantu calon pasien memahami manfaat sebelum melakukan booking.",
                "items": [
                    ("Skin rejuvenation", "Perawatan untuk tampilan kulit lebih halus, cerah, dan segar."),
                    ("Acne care program", "Program bertahap untuk kulit berjerawat dengan evaluasi kondisi kulit."),
                    ("Anti-aging treatment", "Pendekatan elegan untuk garis halus, elastisitas, dan tekstur kulit."),
                    ("Body wellness", "Perawatan kesehatan dan kebugaran dengan suasana klinik yang nyaman."),
                    ("Brightening facial", "Treatment wajah premium untuk kulit kusam dan tidak merata."),
                    ("Medical consultation", "Analisis kebutuhan perawatan sebelum menentukan prosedur."),
                ],
            },
            {
                "kicker": "Doctor Credibility",
                "title": "Kepercayaan dibangun melalui komunikasi medis yang jelas.",
                "body": "Halaman menonjolkan kredibilitas tanpa klaim berlebihan, cocok untuk brand klinik yang ingin terlihat profesional.",
                "items": [
                    ("Assessment personal", "Rencana treatment disesuaikan dengan kondisi dan target pasien."),
                    ("Edukasi transparan", "Pasien mendapat penjelasan manfaat, proses, dan aftercare."),
                    ("Pendampingan lanjutan", "Evaluasi setelah treatment membantu menjaga hasil tetap optimal."),
                ],
            },
            {
                "kicker": "Before After",
                "title": "Narasi transformasi yang elegan dan tetap realistis.",
                "body": "Area visual before-after dibuat premium untuk menunjukkan progres tanpa kesan berlebihan.",
                "items": [
                    ("Texture refinement", "Kulit tampak lebih halus melalui perawatan bertahap."),
                    ("Healthy glow", "Fokus pada tampilan segar, bersih, dan natural."),
                    ("Personalized result", "Setiap hasil bergantung pada kondisi kulit dan konsistensi aftercare."),
                ],
            },
        ],
        "testimonials": [
            ("Nadia, Entrepreneur", "Konsultasinya tenang dan detail. Saya merasa paham sebelum memilih treatment."),
            ("Ratri, Professional", "Kliniknya bersih, layanannya premium, dan hasilnya terlihat natural."),
            ("Dewi, Bride-to-be", "Program sebelum acara sangat membantu. Timnya teliti dan komunikatif."),
        ],
        "faq": [
            ("Apakah harus konsultasi dulu?", "Disarankan konsultasi agar dokter dapat membaca kondisi kulit dan menentukan treatment yang tepat."),
            ("Apakah bisa booking via WhatsApp?", "Bisa. Pilih jadwal, layanan yang diminati, dan tim klinik akan membantu konfirmasi."),
            ("Apakah ada paket perawatan?", "Ada. Paket dapat disesuaikan berdasarkan tujuan kulit, durasi program, dan rekomendasi klinis."),
        ],
        "contact": ("Booking konsultasi awal, pilih treatment yang diminati, dan kirim preferensi jadwal. Tim klinik akan membantu konfirmasi kunjungan."),
    },
    {
        "slug": "properti-real-estate",
        "number": "03",
        "brand": "Aruna Estates",
        "category": "Properti / Real Estate",
        "eyebrow": "Luxury Property Advisory",
        "title": "Properti premium untuk hunian, investasi, dan keputusan besar bernilai tinggi.",
        "lead": "Landing page real estate dengan struktur high-ticket sales yang menonjolkan trust, kelayakan investasi, dan konsultasi properti via WhatsApp.",
        "cta": "Booking Site Visit",
        "secondary": "Lihat Properti",
        "visual_title": "Curated properties for confident acquisition.",
        "visual_items": [
            ("Prime residence", "limited units"),
            ("Investment value", "growth area"),
            ("Agent advisory", "private viewing"),
        ],
        "assurance": [
            ("Listing terkurasi", "Properti dipilih berdasarkan lokasi, nilai, dan profil pembeli."),
            ("Konsultasi privat", "Diskusi kebutuhan, budget, dan tujuan investasi secara personal."),
            ("Dokumen jelas", "Informasi legalitas dan skema pembelian disampaikan transparan."),
        ],
        "metrics": [
            ("240+", "unit terjual"),
            ("16", "area premium"),
            ("7.8%", "rata potensi yield"),
            ("91%", "referral client"),
        ],
        "sections": [
            {
                "kicker": "Featured Properties",
                "title": "Pilihan properti yang dipresentasikan seperti aset bernilai tinggi.",
                "body": "Setiap kartu properti dapat digunakan untuk mengarahkan calon pembeli ke inquiry cepat.",
                "items": [
                    ("The Hill Residence", "Rumah premium 3 lantai di kawasan berkembang dengan akses bisnis cepat."),
                    ("Marina Executive Suite", "Apartemen high-end untuk profesional dan investor sewa jangka panjang."),
                    ("Garden Cluster Villa", "Hunian keluarga dengan desain modern, keamanan, dan lingkungan tenang."),
                    ("Commercial Avenue", "Ruko strategis untuk brand, klinik, kantor, atau usaha premium."),
                    ("Urban Townhouse", "Unit terbatas dengan desain compact luxury di area perkotaan."),
                    ("Land Banking Lot", "Kavling prospektif untuk pembeli yang fokus pada capital gain."),
                ],
            },
            {
                "kicker": "Investment Benefits",
                "title": "Argumen investasi yang membantu pembeli mengambil keputusan.",
                "body": "Halaman menyeimbangkan emosi visual dan alasan finansial yang rasional.",
                "items": [
                    ("Lokasi bertumbuh", "Dekat akses utama, pusat bisnis, pendidikan, dan fasilitas kota."),
                    ("Limited inventory", "Ketersediaan unit terbatas memperkuat sense of priority."),
                    ("Potensi sewa", "Cocok untuk pembeli yang mengincar pemasukan pasif."),
                ],
            },
            {
                "kicker": "Why Choose This Property",
                "title": "Dibuat untuk memperkuat keyakinan sebelum site visit.",
                "body": "Calon pembeli diarahkan untuk bertanya, konsultasi, dan menjadwalkan kunjungan properti.",
                "items": [
                    ("Presentasi jelas", "Harga, tipe, fasilitas, dan skema pembayaran mudah dipahami."),
                    ("Agent responsif", "Follow-up cepat untuk jadwal viewing dan simulasi pembelian."),
                    ("Konsultasi objektif", "Rekomendasi disesuaikan dengan kebutuhan dan profil investasi."),
                ],
            },
        ],
        "testimonials": [
            ("Hendra, Investor", "Agent menjelaskan peluang area dengan detail dan membantu shortlist unit paling masuk akal."),
            ("Maya, Buyer", "Site visit tertata, informasinya lengkap, dan proses follow-up terasa profesional."),
            ("Rizal, Business Owner", "Saya terbantu memilih ruko yang sesuai kebutuhan usaha dan target market."),
        ],
        "faq": [
            ("Apakah bisa jadwal site visit akhir pekan?", "Bisa, selama slot tersedia. Tim agent akan membantu konfirmasi jadwal terbaik."),
            ("Apakah tersedia simulasi cicilan?", "Ya, simulasi dapat disiapkan berdasarkan harga unit, uang muka, dan tenor yang diinginkan."),
            ("Apakah properti cocok untuk investasi?", "Tim akan membantu membaca lokasi, prospek area, potensi sewa, dan strategi exit sesuai tujuan Anda."),
        ],
        "contact": ("Sampaikan budget, area incaran, tujuan pembelian, dan jadwal site visit. Agent akan mengirim rekomendasi properti yang relevan."),
    },
    {
        "slug": "kontraktor-interior",
        "number": "04",
        "brand": "Atelier Ruang",
        "category": "Kontraktor / Interior",
        "eyebrow": "Design Build Authority",
        "title": "Eksekusi interior dan konstruksi dengan standar premium yang terukur.",
        "lead": "Untuk jasa kontraktor dan interior design yang ingin terlihat berotoritas, rapi, mahal, dan siap mengonversi calon klien ke konsultasi proyek.",
        "cta": "Konsultasi Proyek",
        "secondary": "Lihat Portfolio",
        "visual_title": "From concept to completion with disciplined execution.",
        "visual_items": [
            ("Residential interior", "bespoke"),
            ("Commercial fit-out", "turnkey"),
            ("Project control", "on schedule"),
        ],
        "assurance": [
            ("Desain terarah", "Konsep ruang dibuat berdasarkan fungsi, estetika, dan budget."),
            ("RAB transparan", "Biaya pekerjaan disusun jelas agar keputusan proyek lebih tenang."),
            ("Tim lapangan rapi", "Koordinasi produksi dan instalasi dijaga dengan workflow profesional."),
        ],
        "metrics": [
            ("132", "proyek selesai"),
            ("9+", "tahun pengalaman"),
            ("28", "vendor partner"),
            ("94%", "klien merekomendasikan"),
        ],
        "sections": [
            {
                "kicker": "Services",
                "title": "Layanan kontraktor dan interior untuk ruang bernilai tinggi.",
                "body": "Setiap layanan diarahkan untuk membuat calon klien merasa aman memulai diskusi proyek.",
                "items": [
                    ("Interior residence", "Desain dan pengerjaan rumah, apartemen, pantry, kamar, dan living area."),
                    ("Commercial fit-out", "Office, clinic, showroom, cafe, retail, dan area komersial lain."),
                    ("Custom furniture", "Produksi kabinet, wardrobe, display, dan built-in furniture."),
                    ("Renovasi bangunan", "Perbaikan layout, finishing, plafon, lantai, dan elemen konstruksi ringan."),
                    ("Project supervision", "Kontrol pekerjaan, timeline, material, dan komunikasi progres."),
                    ("Design consultation", "Konsultasi konsep, moodboard, dan estimasi awal kebutuhan ruang."),
                ],
            },
            {
                "kicker": "Portfolio",
                "title": "Presentasi karya yang menonjolkan ketelitian dan selera ruang.",
                "body": "Area portfolio membangun keyakinan visual sebelum calon klien mengirim brief.",
                "items": [
                    ("Luxury apartment", "Interior warm modern dengan detail storage tersembunyi."),
                    ("Executive office", "Ruang kerja profesional dengan layout produktif dan material berkarakter."),
                    ("Boutique clinic", "Interior komersial yang clean, nyaman, dan sesuai standar brand."),
                ],
            },
            {
                "kicker": "Process Workflow",
                "title": "Alur kerja jelas dari brief sampai serah terima.",
                "body": "Workflow membantu menurunkan keraguan calon klien terhadap proses proyek.",
                "items": [
                    ("01. Konsultasi", "Diskusi kebutuhan ruang, ukuran, referensi, dan target budget."),
                    ("02. Konsep & estimasi", "Penyusunan arah desain, material, timeline, dan gambaran biaya."),
                    ("03. Produksi & instalasi", "Pekerjaan lapangan dikontrol sesuai spesifikasi dan jadwal."),
                    ("04. Serah terima", "Pemeriksaan akhir, finishing detail, dan dokumentasi proyek."),
                ],
            },
        ],
        "testimonials": [
            ("Aditya, Homeowner", "Timnya rapi dari desain sampai instalasi. RAB jelas dan hasil akhir terasa premium."),
            ("Siska, Klinik Owner", "Renovasi klinik selesai sesuai timeline dan tampilan ruang sangat meningkatkan brand kami."),
            ("Kevin, Business Owner", "Komunikasi proyek mudah dipantau. Setiap revisi dibahas dengan profesional."),
        ],
        "faq": [
            ("Apakah bisa mulai dari konsultasi konsep?", "Bisa. Konsultasi awal membantu menentukan scope, gaya desain, dan estimasi kebutuhan."),
            ("Apakah menerima proyek luar kota?", "Tergantung scope dan lokasi. Tim akan menilai kebutuhan survey, produksi, dan instalasi."),
            ("Bagaimana estimasi biaya dibuat?", "Biaya dihitung dari ukuran ruang, material, kompleksitas desain, dan jadwal pengerjaan."),
        ],
        "contact": ("Kirim ukuran ruang, lokasi, kebutuhan, referensi desain, dan target budget untuk konsultasi proyek awal."),
    },
    {
        "slug": "catering-food-service",
        "number": "05",
        "brand": "Maison Rasa",
        "category": "Catering / Food Service",
        "eyebrow": "Premium Catering Service",
        "title": "Catering elegan untuk acara yang membutuhkan rasa, presentasi, dan ketepatan.",
        "lead": "Landing page catering premium yang fokus pada inquiry WhatsApp, paket menu, event catering, dan bukti kepercayaan pelanggan.",
        "cta": "Order via WhatsApp",
        "secondary": "Lihat Paket Menu",
        "visual_title": "Refined menus prepared for meaningful gatherings.",
        "visual_items": [
            ("Corporate lunch", "daily & event"),
            ("Wedding dining", "curated menu"),
            ("Private gathering", "chef prepared"),
        ],
        "assurance": [
            ("Rasa konsisten", "Menu diuji agar kualitas tetap terjaga untuk pesanan kecil maupun besar."),
            ("Presentasi rapi", "Setiap paket disiapkan dengan tampilan bersih dan berkelas."),
            ("Tepat waktu", "Koordinasi produksi dan pengiriman menjadi prioritas layanan."),
        ],
        "metrics": [
            ("65k+", "porsi tersaji"),
            ("1.200+", "event ditangani"),
            ("4.8", "rating pelanggan"),
            ("24", "paket menu"),
        ],
        "sections": [
            {
                "kicker": "Hero Promo",
                "title": "Paket premium untuk acara kantor, keluarga, dan momen spesial.",
                "body": "Promo dibuat elegan agar tetap terlihat berkualitas, bukan sekadar diskon massal.",
                "items": [
                    ("Paket corporate", "Lunch box premium, buffet kantor, meeting package, dan snack box."),
                    ("Paket wedding", "Buffet, stall, dessert table, dan menu keluarga besar."),
                    ("Paket private event", "Menu intimate gathering, arisan, ulang tahun, dan syukuran."),
                ],
            },
            {
                "kicker": "Package Menu",
                "title": "Pilihan menu yang mudah dipahami dan cepat dipesan.",
                "body": "Kartu menu memudahkan calon pelanggan memilih sebelum menghubungi WhatsApp.",
                "items": [
                    ("Signature Nusantara", "Nasi daun jeruk, ayam rempah, tumis sayur, sambal, dan dessert."),
                    ("Executive Lunch Box", "Menu kantor premium dengan pilihan protein dan kemasan rapi."),
                    ("Buffet Elegance", "Hidangan prasmanan lengkap untuk acara formal dan keluarga."),
                    ("Stall Experience", "Aneka live stall untuk menghadirkan suasana event lebih hidup."),
                    ("Healthy Catering", "Menu seimbang untuk kantor, komunitas, dan program wellness."),
                    ("Dessert Corner", "Pilihan dessert premium untuk pelengkap acara dan hampers."),
                ],
            },
            {
                "kicker": "Event Catering",
                "title": "Didukung tim yang memahami alur acara.",
                "body": "Bukan hanya makanan, tetapi juga koordinasi agar event berjalan lebih tenang.",
                "items": [
                    ("Koordinasi jumlah porsi", "Estimasi kebutuhan disesuaikan dengan format dan durasi acara."),
                    ("Setup rapi", "Tampilan meja, alat saji, dan flow pelayanan dibuat nyaman."),
                    ("Tim service", "Personel dapat disiapkan untuk event tertentu sesuai kebutuhan."),
                ],
            },
        ],
        "testimonials": [
            ("Intan, HR Manager", "Pesanan meeting selalu tepat waktu, kemasan rapi, dan tamu kantor suka menunya."),
            ("Dimas, Event Planner", "Buffet terlihat elegan dan koordinasi tim lapangan sangat membantu."),
            ("Laras, Bride", "Rasa makanannya konsisten dari test food sampai hari acara."),
        ],
        "faq": [
            ("Berapa minimal order?", "Minimal order tergantung paket. Tim akan membantu memberikan opsi sesuai jumlah tamu."),
            ("Apakah bisa test food?", "Bisa untuk paket tertentu dan jadwal yang tersedia."),
            ("Apakah menu bisa disesuaikan?", "Bisa. Menu dapat disesuaikan dengan tema acara, budget, dan preferensi rasa."),
        ],
        "contact": ("Kirim tanggal acara, lokasi, jumlah tamu, jenis acara, dan paket yang diminati untuk estimasi cepat."),
    },
    {
        "slug": "travel-umroh-tour",
        "number": "06",
        "brand": "Safara Journey",
        "category": "Travel / Umroh / Tour",
        "eyebrow": "Trusted Journey Planner",
        "title": "Perjalanan umroh dan tour yang dirancang aman, nyaman, dan berkesan.",
        "lead": "Landing page travel premium untuk membangun kepercayaan, menampilkan paket, galeri, testimonial, dan konsultasi booking.",
        "cta": "Konsultasi Paket",
        "secondary": "Lihat Paket Travel",
        "visual_title": "Thoughtful travel planning with dependable guidance.",
        "visual_items": [
            ("Umroh premium", "guided trip"),
            ("Private tour", "custom route"),
            ("Family package", "comfortable stay"),
        ],
        "assurance": [
            ("Izin dan mitra jelas", "Informasi perjalanan disampaikan transparan untuk membangun rasa aman."),
            ("Pendamping profesional", "Tim membantu persiapan, keberangkatan, perjalanan, dan kepulangan."),
            ("Hotel terkurasi", "Pilihan akomodasi dipilih untuk kenyamanan dan akses yang baik."),
        ],
        "metrics": [
            ("10+", "tahun pengalaman"),
            ("7.500+", "jamaah & traveler"),
            ("38", "destinasi"),
            ("4.9", "rating layanan"),
        ],
        "sections": [
            {
                "kicker": "Hero Package Offer",
                "title": "Paket perjalanan dengan detail fasilitas yang jelas.",
                "body": "Calon pelanggan diarahkan untuk bertanya paket, jadwal, harga, dan ketersediaan seat.",
                "items": [
                    ("Umroh reguler", "Program terjadwal dengan hotel nyaman dan pendamping berpengalaman."),
                    ("Umroh premium", "Akomodasi lebih dekat, layanan lebih personal, dan itinerary lebih nyaman."),
                    ("Private tour", "Rute custom untuk keluarga, corporate trip, atau perjalanan eksklusif."),
                ],
            },
            {
                "kicker": "Travel Packages",
                "title": "Paket populer untuk kebutuhan spiritual, liburan, dan corporate.",
                "body": "Setiap paket disusun dengan bahasa yang mudah dibandingkan sebelum konsultasi.",
                "items": [
                    ("Umroh 9 hari", "Paket efisien dengan fokus ibadah, pendampingan, dan hotel strategis."),
                    ("Umroh plus Turki", "Perjalanan ibadah dengan tambahan pengalaman wisata bersejarah."),
                    ("Halal tour Jepang", "Itinerary nyaman dengan pilihan makanan dan jadwal yang tertata."),
                    ("Europe classic", "Tour kota ikonik dengan akomodasi dan transportasi terencana."),
                    ("Family escape", "Paket keluarga dengan aktivitas fleksibel dan pace perjalanan nyaman."),
                    ("Corporate incentive", "Program perjalanan untuk reward karyawan dan relasi bisnis."),
                ],
            },
            {
                "kicker": "Why Trust Us",
                "title": "Kepercayaan menjadi inti keputusan booking travel.",
                "body": "Halaman menegaskan transparansi fasilitas, jadwal, dan pendampingan agar calon pelanggan nyaman menghubungi.",
                "items": [
                    ("Briefing keberangkatan", "Peserta mendapat informasi dokumen, perlengkapan, dan alur perjalanan."),
                    ("Support komunikasi", "Tim siap membantu pertanyaan sebelum dan selama perjalanan."),
                    ("Galeri nyata", "Dokumentasi perjalanan membantu calon peserta melihat kualitas pengalaman."),
                ],
            },
        ],
        "testimonials": [
            ("Rahma, Jamaah Umroh", "Pendampingnya sabar, hotel nyaman, dan jadwal ibadah terasa tertata."),
            ("Farid, Family Trip", "Tour keluarga kami berjalan lancar karena itinerary fleksibel dan jelas."),
            ("Anita, HR Director", "Corporate trip kami ditangani profesional dari proposal hingga kepulangan."),
        ],
        "faq": [
            ("Apakah harga sudah termasuk tiket?", "Tergantung paket. Detail fasilitas akan dijelaskan di brosur dan konsultasi WhatsApp."),
            ("Apakah bisa pilih jadwal keberangkatan?", "Bisa. Tim akan mengirim opsi jadwal, seat, dan paket yang tersedia."),
            ("Apakah membantu dokumen perjalanan?", "Ya, tim memberikan panduan dokumen sesuai kebutuhan paket dan destinasi."),
        ],
        "contact": ("Kirim tujuan, jumlah peserta, perkiraan tanggal, dan preferensi budget untuk rekomendasi paket terbaik."),
    },
    {
        "slug": "wedding-organizer",
        "number": "07",
        "brand": "Vow Atelier",
        "category": "Wedding Organizer",
        "eyebrow": "Luxury Wedding Planning",
        "title": "Perayaan pernikahan yang terasa intim, elegan, dan tertata sempurna.",
        "lead": "Landing page wedding organizer dengan desain emosional premium untuk mengarahkan calon pasangan ke booking konsultasi.",
        "cta": "Booking Konsultasi Wedding",
        "secondary": "Lihat Paket",
        "visual_title": "A composed celebration crafted around your story.",
        "visual_items": [
            ("Full wedding plan", "end to end"),
            ("Intimate ceremony", "personal detail"),
            ("Vendor direction", "curated team"),
        ],
        "assurance": [
            ("Konsep personal", "Setiap perayaan dirancang berdasarkan cerita, karakter, dan kebutuhan pasangan."),
            ("Vendor terkurasi", "Rekomendasi vendor disesuaikan dengan gaya, kapasitas, dan budget."),
            ("Timeline rapi", "Perencanaan dibuat sistematis agar hari acara terasa tenang."),
        ],
        "metrics": [
            ("420+", "wedding handled"),
            ("12", "tahun pengalaman"),
            ("80+", "vendor partner"),
            ("4.9", "rating pasangan"),
        ],
        "sections": [
            {
                "kicker": "Service Packages",
                "title": "Paket layanan untuk berbagai skala perayaan.",
                "body": "Paket dirancang jelas agar calon pasangan mudah menentukan kebutuhan sebelum konsultasi.",
                "items": [
                    ("Full planning", "Pendampingan dari konsep awal, budget, vendor, hingga hari acara."),
                    ("Wedding day management", "Koordinasi intensif menjelang dan saat hari pernikahan."),
                    ("Intimate wedding", "Paket elegan untuk perayaan kecil dengan detail personal."),
                    ("Luxury reception", "Perencanaan resepsi besar dengan flow tamu dan vendor lengkap."),
                    ("Engagement event", "Pengelolaan acara lamaran yang rapi dan berkesan."),
                    ("Destination wedding", "Perencanaan lokasi khusus dengan koordinasi travel dan venue."),
                ],
            },
            {
                "kicker": "Portfolio Gallery",
                "title": "Galeri nuansa untuk menunjukkan rasa dan kualitas eksekusi.",
                "body": "Visual portfolio membangun emosi dan keyakinan sebelum calon klien menghubungi.",
                "items": [
                    ("Classic ballroom", "Elegan, timeless, dan formal untuk resepsi besar."),
                    ("Garden intimate", "Hangat, natural, dan personal untuk keluarga dekat."),
                    ("Modern cultural", "Menggabungkan tradisi dan detail kontemporer."),
                ],
            },
            {
                "kicker": "Process",
                "title": "Perencanaan yang menenangkan dari meeting pertama sampai acara selesai.",
                "body": "Alur proses membuat calon pasangan merasa ditemani dan dipandu.",
                "items": [
                    ("Discover", "Mengenali cerita, prioritas, tamu, budget, dan harapan pasangan."),
                    ("Design", "Menyusun moodboard, vendor direction, layout, dan timeline."),
                    ("Coordinate", "Mengatur komunikasi vendor, technical meeting, dan checklist."),
                    ("Celebrate", "Mengawal flow acara agar pasangan dan keluarga dapat menikmati momen."),
                ],
            },
        ],
        "testimonials": [
            ("Alya & Raka", "Hari pernikahan kami terasa tenang karena semua detail dikawal dengan rapi."),
            ("Nabila & Dito", "Konsepnya sesuai kepribadian kami, elegan tanpa berlebihan."),
            ("Mira, Mother of Bride", "Timnya sangat membantu keluarga, vendor, dan tamu sepanjang acara."),
        ],
        "faq": [
            ("Kapan sebaiknya mulai konsultasi?", "Idealnya 6 sampai 12 bulan sebelum acara, namun tim tetap dapat menilai kebutuhan untuk timeline lebih dekat."),
            ("Apakah bisa menyesuaikan budget?", "Bisa. Rekomendasi vendor dan konsep akan disesuaikan dengan prioritas pasangan."),
            ("Apakah tersedia paket intimate wedding?", "Ya, paket intimate tersedia untuk acara kecil yang tetap elegan dan tertata."),
        ],
        "contact": ("Kirim tanggal rencana, kota acara, jumlah tamu, dan gaya wedding yang diinginkan untuk konsultasi awal."),
    },
    {
        "slug": "gym-fitness-studio",
        "number": "08",
        "brand": "Forge Performance Club",
        "category": "Gym / Fitness Studio",
        "eyebrow": "Premium Fitness Studio",
        "title": "Studio fitness premium untuk tubuh lebih kuat, disiplin, dan terarah.",
        "lead": "Landing page gym dengan visual kuat, profesional, dan fokus pada konversi membership serta free trial.",
        "cta": "Daftar Free Trial",
        "secondary": "Lihat Membership",
        "visual_title": "Train with structure, intensity, and measurable progress.",
        "visual_items": [
            ("Strength program", "coach led"),
            ("Private training", "goal based"),
            ("Recovery zone", "complete facility"),
        ],
        "assurance": [
            ("Program terukur", "Latihan disusun berdasarkan tujuan, level, dan progres member."),
            ("Trainer profesional", "Pendampingan teknik membantu latihan lebih aman dan efektif."),
            ("Fasilitas premium", "Studio bersih, nyaman, dan dirancang untuk performa."),
        ],
        "metrics": [
            ("2.800+", "active members"),
            ("26", "certified trainers"),
            ("58", "class per week"),
            ("4.8", "member rating"),
        ],
        "sections": [
            {
                "kicker": "Membership Packages",
                "title": "Paket membership untuk komitmen yang jelas.",
                "body": "Penawaran membership dibuat mudah dibandingkan dan diarahkan ke free trial.",
                "items": [
                    ("Essential", "Akses gym reguler, program dasar, dan fasilitas utama."),
                    ("Performance", "Akses kelas, evaluasi berkala, dan training plan."),
                    ("Private coaching", "Sesi personal trainer dengan target dan progres detail."),
                    ("Transformation plan", "Program 12 minggu untuk body recomposition dan kebiasaan baru."),
                    ("Corporate wellness", "Paket untuk tim perusahaan dan komunitas profesional."),
                    ("Day pass", "Pilihan kunjungan harian untuk mencoba fasilitas."),
                ],
            },
            {
                "kicker": "Facilities",
                "title": "Lingkungan latihan yang mendukung konsistensi.",
                "body": "Fasilitas ditampilkan sebagai alasan utama untuk mencoba studio.",
                "items": [
                    ("Strength floor", "Rack, barbell, cable, dan equipment untuk progressive training."),
                    ("Functional zone", "Area conditioning, mobility, dan class training."),
                    ("Recovery amenities", "Locker, shower, lounge, dan area recovery yang nyaman."),
                ],
            },
            {
                "kicker": "Trainer Profile",
                "title": "Pendampingan yang membuat latihan lebih percaya diri.",
                "body": "Bagian trainer membangun rasa aman untuk calon member baru.",
                "items": [
                    ("Technique coaching", "Trainer mengoreksi gerakan dan membantu mengurangi risiko cedera."),
                    ("Goal setting", "Target dibuat realistis berdasarkan kondisi awal dan jadwal latihan."),
                    ("Progress tracking", "Evaluasi rutin untuk menjaga motivasi dan arah latihan."),
                ],
            },
        ],
        "testimonials": [
            ("Bimo, Executive", "Programnya jelas dan trainer membantu saya konsisten meski jadwal kerja padat."),
            ("Sari, Member", "Studio bersih, tidak terlalu ramai, dan kelasnya terasa premium."),
            ("Andre, Entrepreneur", "Saya suka evaluasi progresnya. Latihan jadi lebih terarah."),
        ],
        "faq": [
            ("Apakah pemula bisa ikut?", "Bisa. Trainer akan membantu menentukan program sesuai level awal."),
            ("Bagaimana cara free trial?", "Daftar via WhatsApp, pilih jadwal, lalu tim akan mengonfirmasi slot."),
            ("Apakah ada personal trainer?", "Ada. Paket private coaching tersedia dengan program yang disesuaikan."),
        ],
        "contact": ("Kirim nama, tujuan fitness, jadwal yang diinginkan, dan pengalaman latihan untuk booking free trial."),
    },
    {
        "slug": "skincare-beauty-product",
        "number": "09",
        "brand": "Velour Skin",
        "category": "Skincare Brand / Beauty Product",
        "eyebrow": "Luxury Skincare Brand",
        "title": "Ritual skincare premium untuk kulit yang tampak sehat, halus, dan bercahaya.",
        "lead": "Landing page beauty product yang elegan, fokus pada highlight produk, manfaat, testimonial, promo, dan konsultasi WhatsApp.",
        "cta": "Konsultasi Produk",
        "secondary": "Lihat Produk",
        "visual_title": "Elevated daily care with refined beauty positioning.",
        "visual_items": [
            ("Brightening serum", "hero product"),
            ("Barrier cream", "daily repair"),
            ("Complete routine", "bundle offer"),
        ],
        "assurance": [
            ("Formula terkurasi", "Komunikasi manfaat dibuat elegan dan tidak berlebihan."),
            ("Routine guidance", "Pelanggan diarahkan memilih produk sesuai kebutuhan kulit."),
            ("Brand premium", "Visual dan copywriting mendukung positioning produk high-value."),
        ],
        "metrics": [
            ("120k+", "produk terjual"),
            ("38k+", "pelanggan aktif"),
            ("4.8", "rating produk"),
            ("6", "signature formulas"),
        ],
        "sections": [
            {
                "kicker": "Product Highlights",
                "title": "Produk utama yang ditampilkan dengan bahasa konversi premium.",
                "body": "Highlight produk memudahkan pelanggan memahami fungsi setiap item.",
                "items": [
                    ("Luminous Serum", "Serum harian untuk tampilan kulit lebih cerah dan segar."),
                    ("Hydra Barrier Cream", "Pelembap untuk membantu menjaga kenyamanan skin barrier."),
                    ("Velvet Cleanser", "Pembersih lembut untuk rutinitas pagi dan malam."),
                    ("Renewal Toner", "Toner eksfoliasi lembut untuk tekstur yang terlihat lebih halus."),
                    ("Radiance Sunscreen", "Proteksi harian dengan finish nyaman untuk aktivitas."),
                    ("Complete Glow Set", "Bundle rutinitas lengkap untuk pelanggan baru."),
                ],
            },
            {
                "kicker": "Benefits",
                "title": "Manfaat dijelaskan secara meyakinkan dan tetap elegan.",
                "body": "Fokus pada hasil yang realistis agar brand terlihat premium dan tepercaya.",
                "items": [
                    ("Healthy glow", "Membantu kulit tampak lebih segar dengan penggunaan rutin."),
                    ("Texture care", "Mendukung tampilan permukaan kulit yang lebih halus."),
                    ("Hydration comfort", "Memberikan rasa lembap tanpa kesan berat."),
                ],
            },
            {
                "kicker": "Promo CTA",
                "title": "Penawaran bundle yang mendorong keputusan pembelian.",
                "body": "CTA promo diposisikan premium untuk meningkatkan nilai order tanpa terasa murahan.",
                "items": [
                    ("Starter ritual", "Paket dasar untuk memulai rutinitas skincare harian."),
                    ("Glow intensive", "Bundle serum, moisturizer, dan sunscreen untuk hasil lebih lengkap."),
                    ("Consult to cart", "Konsultasi singkat membantu pelanggan memilih rangkaian produk."),
                ],
            },
        ],
        "testimonials": [
            ("Tania, Customer", "Teksturnya nyaman dan packaging terasa premium. Saya suka panduan routinenya."),
            ("Meiska, Beauty Enthusiast", "Produk mudah dipakai harian dan hasilnya terlihat natural."),
            ("Clara, Repeat Buyer", "Konsultasi via WhatsApp membantu memilih produk yang sesuai kulit saya."),
        ],
        "faq": [
            ("Apakah bisa konsultasi jenis kulit?", "Bisa. Tim akan membantu merekomendasikan produk berdasarkan kebutuhan dan kebiasaan pemakaian."),
            ("Apakah produk bisa dibeli bundle?", "Bisa. Bundle tersedia untuk rutinitas dasar dan perawatan lebih lengkap."),
            ("Berapa lama hasil terlihat?", "Setiap kulit berbeda. Penggunaan rutin dan pemilihan produk yang tepat membantu hasil lebih optimal."),
        ],
        "contact": ("Kirim jenis kulit, concern utama, produk yang pernah dipakai, dan target perawatan untuk rekomendasi rangkaian."),
    },
    {
        "slug": "corporate-company-profile",
        "number": "10",
        "brand": "Ardent Global Group",
        "category": "Corporate Company Profile",
        "eyebrow": "Executive Company Profile",
        "title": "Profil perusahaan yang menampilkan kredibilitas, kapasitas, dan nilai bisnis.",
        "lead": "Landing page company profile untuk korporasi yang ingin terlihat mapan, profesional, dan siap menerima inquiry kemitraan.",
        "cta": "Hubungi Corporate Office",
        "secondary": "Lihat Layanan",
        "visual_title": "Institutional presentation for serious business conversations.",
        "visual_items": [
            ("Business units", "integrated"),
            ("Industry expertise", "multi sector"),
            ("Partnership inquiry", "executive desk"),
        ],
        "assurance": [
            ("Struktur jelas", "Profil perusahaan disusun untuk membangun pemahaman cepat dan kepercayaan."),
            ("Citra eksekutif", "Tipografi, layout, dan bahasa mendukung positioning korporat."),
            ("Inquiry terarah", "CTA mengarahkan calon klien atau partner ke kontak yang tepat."),
        ],
        "metrics": [
            ("18+", "tahun operasi"),
            ("6", "lini bisnis"),
            ("120+", "klien institusi"),
            ("32", "wilayah layanan"),
        ],
        "sections": [
            {
                "kicker": "Company Overview",
                "title": "Narasi perusahaan yang ringkas, kuat, dan mudah dipercaya.",
                "body": "Bagian overview menjelaskan siapa perusahaan, apa yang dikerjakan, dan mengapa layak diajak bicara.",
                "items": [
                    ("Operational strength", "Kapabilitas layanan dibangun melalui tim, proses, dan jaringan partner."),
                    ("Governance mindset", "Pendekatan kerja menekankan transparansi, kepatuhan, dan kualitas."),
                    ("Long-term partnership", "Fokus pada relasi bisnis jangka panjang dan nilai berkelanjutan."),
                ],
            },
            {
                "kicker": "Services",
                "title": "Layanan bisnis yang dipresentasikan untuk audiens eksekutif.",
                "body": "Setiap layanan dibuat jelas agar pengunjung dapat langsung mengidentifikasi relevansi.",
                "items": [
                    ("Strategic supply", "Pengadaan dan distribusi untuk kebutuhan bisnis skala menengah hingga besar."),
                    ("Project management", "Pengelolaan proyek, koordinasi vendor, dan kontrol pelaksanaan."),
                    ("Business advisory", "Pendampingan strategis untuk ekspansi, efisiensi, dan kemitraan."),
                    ("Facility support", "Layanan pendukung operasional untuk gedung, kantor, dan fasilitas komersial."),
                    ("Trading division", "Aktivitas perdagangan produk dan komoditas bisnis terpilih."),
                    ("Partnership desk", "Pengembangan kerja sama institusi, vendor, dan strategic alliance."),
                ],
            },
            {
                "kicker": "Industries Served",
                "title": "Pengalaman lintas industri untuk kebutuhan bisnis yang kompleks.",
                "body": "Bagian industri meningkatkan relevansi dengan berbagai calon klien korporat.",
                "items": [
                    ("Construction & property", "Dukungan suplai, proyek, dan operasional."),
                    ("Manufacturing", "Kebutuhan procurement, facility, dan efisiensi proses."),
                    ("Public & institutional", "Dukungan administrasi, dokumentasi, dan layanan terstruktur."),
                ],
            },
            {
                "kicker": "Why Choose Us",
                "title": "Alasan perusahaan terlihat layak menjadi partner strategis.",
                "body": "Pesan utama diarahkan pada trust, track record, dan kesiapan menangani inquiry serius.",
                "items": [
                    ("Leadership experience", "Tim manajemen memiliki pengalaman lintas sektor."),
                    ("Reliable execution", "Proses kerja mengutamakan ketepatan, dokumentasi, dan komunikasi."),
                    ("Scalable capacity", "Struktur layanan dapat menyesuaikan kebutuhan proyek dan kemitraan."),
                ],
            },
        ],
        "testimonials": [
            ("Director, Property Group", "Presentasi bisnis dan alur koordinasi mereka selalu profesional."),
            ("Procurement Lead, Manufacturer", "Tim Ardent memahami kebutuhan institusi dan proses administrasi kami."),
            ("Partner, Regional Office", "Komunikasi manajemen jelas dan eksekusi proyek dapat dipantau dengan baik."),
        ],
        "faq": [
            ("Apakah menerima kerja sama institusi?", "Ya, inquiry partnership dapat dikirim melalui kontak corporate office."),
            ("Apakah company profile bisa digunakan untuk banyak lini bisnis?", "Struktur halaman ini mendukung presentasi multi layanan dan multi industri."),
            ("Bagaimana memulai diskusi bisnis?", "Kirim kebutuhan, profil perusahaan, dan jenis kerja sama yang diinginkan melalui formulir atau WhatsApp."),
        ],
        "contact": ("Kirim profil perusahaan, kebutuhan layanan, dan tujuan kerja sama agar tim corporate dapat menindaklanjuti."),
    },
    {
        "slug": "law-firm-konsultan-hukum",
        "number": "11",
        "brand": "Mahendra & Partners",
        "category": "Law Firm / Konsultan Hukum",
        "eyebrow": "Legal Advisory Office",
        "title": "Pendampingan hukum profesional untuk keputusan bisnis dan personal yang krusial.",
        "lead": "Landing page law firm dengan nuansa authority, corporate, dan premium untuk mendorong booking konsultasi hukum.",
        "cta": "Booking Konsultasi Hukum",
        "secondary": "Lihat Layanan Hukum",
        "visual_title": "Measured legal counsel for complex decisions.",
        "visual_items": [
            ("Corporate legal", "business counsel"),
            ("Dispute advisory", "strategic review"),
            ("Contract drafting", "risk control"),
        ],
        "assurance": [
            ("Analisis terstruktur", "Setiap perkara dipahami melalui fakta, dokumen, risiko, dan tujuan klien."),
            ("Kerahasiaan dijaga", "Komunikasi konsultasi dikelola dengan standar profesional."),
            ("Saran objektif", "Rekomendasi hukum disampaikan secara jelas dan dapat ditindaklanjuti."),
        ],
        "metrics": [
            ("14+", "tahun praktik"),
            ("560+", "matter ditangani"),
            ("42", "klien korporat"),
            ("9", "area praktik"),
        ],
        "sections": [
            {
                "kicker": "Legal Services",
                "title": "Layanan hukum untuk kebutuhan bisnis, kontrak, dan sengketa.",
                "body": "Kategori layanan dibuat tegas agar calon klien cepat menemukan relevansi.",
                "items": [
                    ("Corporate legal", "Pendirian perusahaan, perizinan, tata kelola, dan aksi korporasi."),
                    ("Contract drafting", "Penyusunan, review, dan negosiasi perjanjian bisnis."),
                    ("Dispute resolution", "Pendampingan strategi sengketa perdata dan komersial."),
                    ("Employment law", "Kebijakan tenaga kerja, kontrak karyawan, dan penyelesaian perselisihan."),
                    ("Property legal", "Review dokumen properti, transaksi, dan perikatan."),
                    ("Legal consultation", "Konsultasi awal untuk membaca posisi hukum dan opsi tindakan."),
                ],
            },
            {
                "kicker": "Expertise",
                "title": "Keahlian yang menggabungkan presisi hukum dan pemahaman bisnis.",
                "body": "Bagian expertise memperkuat kesan firma hukum yang matang dan dapat dipercaya.",
                "items": [
                    ("Risk mapping", "Memetakan risiko hukum sebelum keputusan bisnis diambil."),
                    ("Document strategy", "Menyusun dokumen yang jelas, kuat, dan sesuai konteks transaksi."),
                    ("Negotiation support", "Mendampingi proses negosiasi dengan posisi yang lebih siap."),
                ],
            },
            {
                "kicker": "Why Trust Us",
                "title": "Pendekatan profesional untuk perkara yang membutuhkan kehati-hatian.",
                "body": "Kepercayaan dibangun melalui proses, komunikasi, dan kualitas analisis.",
                "items": [
                    ("Case assessment", "Review awal membantu menentukan langkah paling rasional."),
                    ("Clear communication", "Klien memahami opsi, konsekuensi, dan prioritas tindakan."),
                    ("Professional discretion", "Informasi klien diperlakukan dengan serius dan terbatas."),
                ],
            },
        ],
        "testimonials": [
            ("CEO, Trading Company", "Review kontrak sangat detail dan membantu kami menghindari klausul berisiko."),
            ("Founder, Startup Lokal", "Penjelasan hukumnya mudah dipahami tanpa mengurangi ketelitian."),
            ("Private Client", "Konsultasi terasa tenang, objektif, dan menjaga kerahasiaan."),
        ],
        "faq": [
            ("Apakah konsultasi bisa online?", "Bisa. Konsultasi dapat dijadwalkan online atau tatap muka sesuai kebutuhan."),
            ("Apa yang perlu disiapkan sebelum konsultasi?", "Siapkan kronologi singkat, dokumen terkait, dan tujuan konsultasi."),
            ("Apakah biaya konsultasi diinformasikan di awal?", "Ya, estimasi biaya dan scope akan dijelaskan sebelum sesi dikonfirmasi."),
        ],
        "contact": ("Kirim ringkasan perkara, jenis layanan hukum, dan preferensi jadwal konsultasi untuk penjadwalan awal."),
    },
    {
        "slug": "finance-insurance-consultant",
        "number": "12",
        "brand": "Pradana Wealth Advisory",
        "category": "Finance / Insurance Consultant",
        "eyebrow": "Financial Protection Advisory",
        "title": "Perencanaan finansial dan proteksi yang dibangun berdasarkan kepercayaan.",
        "lead": "Landing page finance consultant atau insurance service dengan struktur trust-based untuk lead generation dan konsultasi.",
        "cta": "Konsultasi Finansial",
        "secondary": "Lihat Layanan",
        "visual_title": "Structured financial guidance for long-term security.",
        "visual_items": [
            ("Protection plan", "family first"),
            ("Wealth planning", "goal based"),
            ("Insurance review", "policy clarity"),
        ],
        "assurance": [
            ("Analisis kebutuhan", "Rekomendasi dibuat berdasarkan profil, tujuan, dan kemampuan finansial."),
            ("Penjelasan transparan", "Manfaat, risiko, biaya, dan ketentuan dibahas secara jelas."),
            ("Pendampingan jangka panjang", "Klien dibantu memahami review dan penyesuaian rencana."),
        ],
        "metrics": [
            ("1.800+", "klien dibantu"),
            ("11+", "tahun advisory"),
            ("4.9", "rating konsultasi"),
            ("76%", "referral lead"),
        ],
        "sections": [
            {
                "kicker": "Services",
                "title": "Layanan konsultasi untuk perlindungan, tujuan, dan keputusan finansial.",
                "body": "Layanan dirancang agar calon klien merasa aman untuk memulai percakapan.",
                "items": [
                    ("Insurance planning", "Rekomendasi proteksi jiwa, kesehatan, dan keluarga."),
                    ("Policy review", "Evaluasi polis yang sudah dimiliki agar manfaat lebih dipahami."),
                    ("Education fund", "Perencanaan dana pendidikan berdasarkan target waktu dan kebutuhan."),
                    ("Retirement planning", "Rencana jangka panjang untuk kesiapan finansial masa pensiun."),
                    ("Business protection", "Proteksi untuk pemilik usaha, partner, dan aset bisnis."),
                    ("Financial consultation", "Konsultasi awal untuk memetakan prioritas dan gap proteksi."),
                ],
            },
            {
                "kicker": "Client Trust",
                "title": "Trust dibangun dari edukasi, bukan tekanan penjualan.",
                "body": "Copywriting dibuat profesional agar layanan terasa konsultatif dan kredibel.",
                "items": [
                    ("Needs-based advice", "Rekomendasi mengikuti kebutuhan klien, bukan paket generik."),
                    ("Readable explanation", "Istilah polis dan manfaat dijelaskan dengan bahasa sederhana."),
                    ("Ongoing review", "Rencana dapat ditinjau ulang ketika kondisi hidup berubah."),
                ],
            },
            {
                "kicker": "Why Choose Us",
                "title": "Konsultasi yang membantu calon klien mengambil keputusan tenang.",
                "body": "Halaman fokus pada lead generation melalui rasa aman dan profesionalitas.",
                "items": [
                    ("Profiling personal", "Membaca pemasukan, tanggungan, aset, dan tujuan."),
                    ("Scenario planning", "Menyusun opsi proteksi dan rencana berdasarkan prioritas."),
                    ("Claim guidance", "Pendampingan informasi klaim membantu klien memahami proses."),
                ],
            },
        ],
        "testimonials": [
            ("Rendy, Business Owner", "Saya akhirnya paham gap proteksi bisnis dan keluarga setelah konsultasi."),
            ("Mitha, Professional", "Penjelasannya objektif dan tidak terasa memaksa."),
            ("Hana, Parent", "Rencana dana pendidikan jadi lebih jelas dan realistis."),
        ],
        "faq": [
            ("Apakah konsultasi pertama berbayar?", "Tergantung program. Tim akan menginformasikan skema konsultasi saat penjadwalan."),
            ("Apakah harus membeli produk setelah konsultasi?", "Tidak. Konsultasi bertujuan membantu memahami kebutuhan dan opsi yang tersedia."),
            ("Apa yang perlu disiapkan?", "Siapkan tujuan finansial, tanggungan, kisaran budget, dan polis yang sudah dimiliki bila ada."),
        ],
        "contact": ("Kirim tujuan finansial, usia, tanggungan, dan kebutuhan proteksi untuk konsultasi awal yang lebih relevan."),
    },
    {
        "slug": "digital-marketing-agency",
        "number": "13",
        "brand": "Northline Digital",
        "category": "Digital Agency / Marketing Agency",
        "eyebrow": "High-Ticket Growth Partner",
        "title": "Strategi digital premium untuk brand yang ingin tumbuh dengan arah jelas.",
        "lead": "Landing page agency dengan positioning high-ticket, menonjolkan layanan, portfolio, results, testimonial, dan CTA konsultasi.",
        "cta": "Konsultasi Growth",
        "secondary": "Lihat Portfolio",
        "visual_title": "Marketing systems for brands ready to scale deliberately.",
        "visual_items": [
            ("Performance ads", "conversion"),
            ("Brand strategy", "positioning"),
            ("Content engine", "consistent growth"),
        ],
        "assurance": [
            ("Strategi berbasis data", "Keputusan campaign dibangun dari riset, tracking, dan evaluasi."),
            ("Eksekusi premium", "Creative, landing page, dan media buying dijaga dalam satu arah."),
            ("Fokus revenue", "Layanan diarahkan untuk lead, conversion, dan pertumbuhan bisnis."),
        ],
        "metrics": [
            ("86", "brand ditangani"),
            ("4.3x", "avg ROAS selected campaigns"),
            ("12+", "tahun tim inti"),
            ("31%", "avg lead cost reduction"),
        ],
        "sections": [
            {
                "kicker": "Services",
                "title": "Layanan agency untuk brand yang serius dengan pertumbuhan.",
                "body": "Setiap layanan diposisikan sebagai investasi, bukan jasa eksekusi biasa.",
                "items": [
                    ("Brand strategy", "Positioning, messaging, dan arah komunikasi untuk market yang jelas."),
                    ("Performance marketing", "Meta Ads, Google Ads, funnel tracking, dan optimasi conversion."),
                    ("Landing page conversion", "Halaman penjualan premium untuk campaign lead generation."),
                    ("Content marketing", "Sistem konten untuk awareness, trust, dan nurturing."),
                    ("Creative production", "Visual campaign, copywriting, dan asset iklan berstandar brand."),
                    ("Growth consulting", "Audit funnel dan roadmap pertumbuhan digital."),
                ],
            },
            {
                "kicker": "Portfolio",
                "title": "Karya yang menonjolkan arah brand dan performa campaign.",
                "body": "Portfolio agency dibuat ringkas namun kuat untuk mendukung konsultasi high-ticket.",
                "items": [
                    ("Luxury clinic launch", "Strategi funnel untuk booking konsultasi treatment premium."),
                    ("Property lead system", "Campaign site visit untuk properti high-ticket."),
                    ("Retail growth program", "Optimasi iklan dan landing page untuk meningkatkan order."),
                ],
            },
            {
                "kicker": "Results",
                "title": "Hasil yang dibingkai dengan konteks bisnis.",
                "body": "Bagian results menekankan outcome tanpa klaim berlebihan.",
                "items": [
                    ("Lead quality uplift", "Form dan copy diarahkan untuk inquiry lebih relevan."),
                    ("Cost efficiency", "Optimasi creative dan audience membantu menekan biaya lead."),
                    ("Conversion clarity", "Tracking membuat tim lebih paham sumber hasil campaign."),
                ],
            },
        ],
        "testimonials": [
            ("CMO, Beauty Brand", "Mereka membantu merapikan positioning dan funnel sehingga inquiry lebih berkualitas."),
            ("Founder, Property Agency", "Landing page dan campaign baru membuat tim sales lebih mudah follow-up."),
            ("Owner, Clinic Group", "Presentasi strateginya matang dan eksekusi campaign terasa premium."),
        ],
        "faq": [
            ("Apakah menerima project kecil?", "Agency memprioritaskan brand dengan target growth jelas dan kesiapan eksekusi."),
            ("Apakah bisa mulai dari audit?", "Bisa. Audit funnel membantu menentukan prioritas sebelum retainer atau project."),
            ("Berapa lama melihat hasil?", "Tergantung kondisi market, aset brand, budget iklan, dan kecepatan optimasi."),
        ],
        "contact": ("Kirim jenis bisnis, target growth, channel yang sudah digunakan, dan budget campaign untuk assessment awal."),
    },
    {
        "slug": "kursus-education-center",
        "number": "14",
        "brand": "Cendekia Prime Center",
        "category": "Kursus / Education Center",
        "eyebrow": "Premium Learning Center",
        "title": "Pusat kursus profesional untuk hasil belajar yang lebih terarah.",
        "lead": "Landing page education center dengan desain premium, trust-focused, dan CTA pendaftaran siswa.",
        "cta": "Daftar Konsultasi Program",
        "secondary": "Lihat Program",
        "visual_title": "Structured learning designed for measurable student progress.",
        "visual_items": [
            ("Academic tutoring", "small class"),
            ("Language program", "certified mentor"),
            ("Career skill", "practical path"),
        ],
        "assurance": [
            ("Kurikulum jelas", "Program belajar disusun berdasarkan target dan level siswa."),
            ("Mentor berpengalaman", "Pengajar memahami kebutuhan akademik, bahasa, dan skill praktis."),
            ("Progress monitoring", "Perkembangan siswa dipantau agar orang tua dan peserta lebih tenang."),
        ],
        "metrics": [
            ("6.400+", "siswa terdaftar"),
            ("38", "mentor aktif"),
            ("92%", "completion rate"),
            ("4.8", "rating orang tua"),
        ],
        "sections": [
            {
                "kicker": "Programs",
                "title": "Program kursus untuk akademik, bahasa, dan skill masa depan.",
                "body": "Setiap program dibuat mudah dipahami agar calon siswa cepat memilih jalur belajar.",
                "items": [
                    ("Academic excellence", "Bimbingan Matematika, Sains, Bahasa, dan persiapan ujian."),
                    ("English program", "Kelas bahasa Inggris untuk anak, remaja, profesional, dan test prep."),
                    ("Digital skills", "Program coding, design, spreadsheet, dan skill produktivitas."),
                    ("Private tutoring", "Pembelajaran personal untuk kebutuhan khusus dan jadwal fleksibel."),
                    ("College preparation", "Persiapan masuk kampus, scholarship, dan interview."),
                    ("Corporate class", "Pelatihan karyawan untuk bahasa, komunikasi, dan skill digital."),
                ],
            },
            {
                "kicker": "Why Choose Us",
                "title": "Kepercayaan dibangun melalui metode, mentor, dan hasil belajar.",
                "body": "Halaman mengarahkan pengunjung untuk mendaftar konsultasi program sebelum masuk kelas.",
                "items": [
                    ("Placement test", "Siswa ditempatkan berdasarkan level agar belajar lebih efektif."),
                    ("Small class format", "Interaksi lebih fokus dan mentor lebih mudah memantau perkembangan."),
                    ("Learning report", "Laporan belajar membantu melihat progres dan area perbaikan."),
                ],
            },
        ],
        "testimonials": [
            ("Ibu Rina, Parent", "Anak saya lebih percaya diri karena kelasnya kecil dan mentornya sabar."),
            ("Daffa, Student", "Materinya jelas dan saya bisa bertanya lebih banyak dibanding kelas besar."),
            ("HR Manager, Corporate Client", "Program training karyawan berjalan profesional dan terstruktur."),
        ],
        "faq": [
            ("Apakah ada trial class?", "Tersedia untuk program tertentu. Tim akan membantu cek jadwal dan slot."),
            ("Bagaimana menentukan program yang tepat?", "Siswa dapat mengikuti konsultasi atau placement test untuk menentukan level."),
            ("Apakah kelas bisa online?", "Beberapa program tersedia online, offline, atau hybrid sesuai kebutuhan."),
        ],
        "contact": ("Kirim nama siswa, usia, tujuan belajar, program yang diminati, dan preferensi jadwal untuk pendaftaran awal."),
    },
    {
        "slug": "bengkel-automotive-service",
        "number": "15",
        "brand": "Prime Auto Works",
        "category": "Bengkel / Automotive Service",
        "eyebrow": "Premium Automotive Service",
        "title": "Servis kendaraan premium dengan diagnosis jelas dan pengerjaan profesional.",
        "lead": "Landing page bengkel atau automotive service dengan desain terpercaya untuk mendorong booking servis via WhatsApp.",
        "cta": "Booking Servis",
        "secondary": "Lihat Layanan",
        "visual_title": "Precision maintenance for vehicles that deserve careful handling.",
        "visual_items": [
            ("General service", "scheduled care"),
            ("Engine diagnosis", "scanner check"),
            ("Detailing premium", "finish care"),
        ],
        "assurance": [
            ("Diagnosis transparan", "Keluhan dicek dan dijelaskan sebelum pekerjaan dilakukan."),
            ("Teknisi berpengalaman", "Pengerjaan dilakukan oleh tim yang memahami standar servis modern."),
            ("Estimasi jelas", "Biaya dan opsi part diinformasikan agar pelanggan bisa memutuskan dengan tenang."),
        ],
        "metrics": [
            ("18k+", "kendaraan ditangani"),
            ("15", "service bay"),
            ("4.8", "rating pelanggan"),
            ("11+", "tahun pengalaman"),
        ],
        "sections": [
            {
                "kicker": "Services",
                "title": "Layanan bengkel untuk perawatan rutin hingga pemeriksaan detail.",
                "body": "Layanan disusun untuk membuat pelanggan cepat memilih booking yang tepat.",
                "items": [
                    ("Periodic maintenance", "Ganti oli, filter, pengecekan rem, kaki-kaki, dan komponen rutin."),
                    ("Engine diagnosis", "Pemeriksaan keluhan mesin dengan scanner dan analisis teknisi."),
                    ("Brake & suspension", "Perbaikan sistem pengereman, shock, bushing, dan kenyamanan berkendara."),
                    ("AC service", "Pengecekan performa AC, kebocoran, evaporator, dan pengisian refrigerant."),
                    ("Battery & electrical", "Pemeriksaan aki, alternator, lampu, dan sistem kelistrikan."),
                    ("Premium detailing", "Perawatan eksterior, interior, polishing, dan protection coating."),
                ],
            },
            {
                "kicker": "Why Choose Us",
                "title": "Bengkel yang membangun rasa aman sebelum pelanggan datang.",
                "body": "Trust dibuat melalui proses diagnosa, komunikasi, dan transparansi pengerjaan.",
                "items": [
                    ("Inspection report", "Pelanggan mendapat ringkasan kondisi kendaraan dan rekomendasi."),
                    ("Part options", "Opsi spare part disampaikan sesuai kebutuhan dan budget."),
                    ("Booking slot", "Jadwal servis membantu mengurangi antrean dan waktu tunggu."),
                ],
            },
        ],
        "testimonials": [
            ("Daniel, Owner SUV", "Keluhan mesin dijelaskan dengan detail dan estimasi biaya tidak mengejutkan."),
            ("Novi, Daily Driver", "Booking mudah, bengkel bersih, dan servis selesai sesuai janji."),
            ("Arman, Car Enthusiast", "Detailingnya rapi dan timnya memahami mobil premium."),
        ],
        "faq": [
            ("Apakah harus booking dulu?", "Disarankan booking agar slot servis dan estimasi waktu lebih jelas."),
            ("Apakah tersedia pengecekan awal?", "Ya, teknisi dapat melakukan inspeksi awal sebelum rekomendasi pekerjaan."),
            ("Apakah bisa konsultasi keluhan via WhatsApp?", "Bisa. Kirim tipe kendaraan, tahun, keluhan, dan foto atau video bila ada."),
        ],
        "contact": ("Kirim tipe kendaraan, tahun, kilometer, keluhan, dan jadwal yang diinginkan untuk booking servis."),
    },
]


def icon():
    return """<svg width="22" height="22" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M5 12.5L9.2 16.5L19 7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>"""


def card_items(items, class_name="grid-3"):
    return f'<div class="{class_name}">' + "".join(
        f"""
        <article class="card">
          <div class="symbol">{icon()}</div>
          <h3>{title}</h3>
          <p>{body}</p>
        </article>
        """
        for title, body in items
    ) + "</div>"


def testimonials(items):
    return '<div class="grid-3">' + "".join(
        f"""
        <blockquote class="testimonial">
          <p>“{quote}”</p>
          <cite>{name}</cite>
        </blockquote>
        """
        for name, quote in items
    ) + "</div>"


def faq(items):
    return '<div class="faq">' + "".join(
        f"""
        <details>
          <summary>{question}</summary>
          <p>{answer}</p>
        </details>
        """
        for question, answer in items
    ) + "</div>"


def page(data):
    section_html = []
    for index, section in enumerate(data["sections"]):
        section_html.append(
            f"""
            <section id="section-{index + 1}">
              <div class="site-shell">
                <div class="section-heading">
                  <div>
                    <span class="eyebrow">{section["kicker"]}</span>
                    <h2>{section["title"]}</h2>
                  </div>
                  <p>{section["body"]}</p>
                </div>
                {card_items(section["items"], "grid-3" if len(section["items"]) != 4 else "grid-2")}
              </div>
            </section>
            """
        )

    return f"""<!doctype html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{data["category"]} | {data["brand"]}</title>
  <meta name="description" content="{data["lead"]}">
  <link rel="stylesheet" href="../assets/styles.css">
</head>
<body>
  <header class="topbar">
    <div class="site-shell nav">
      <a class="brand" href="../index.html" aria-label="Kembali ke katalog">
        <span class="brand-mark">{data["number"]}</span>
        <span>{data["brand"]}</span>
      </a>
      <nav class="nav-links" aria-label="Navigasi utama">
        <a href="#section-1">Layanan</a>
        <a href="#testimonials">Testimoni</a>
        <a href="#faq">FAQ</a>
        <a href="#contact">Kontak</a>
      </nav>
      <a class="button" href="{WHATSAPP}{data["cta"].replace(" ", "%20")}">{data["cta"]}</a>
    </div>
  </header>

  <main>
    <section class="hero">
      <div class="site-shell hero-grid">
        <div>
          <span class="eyebrow">{data["eyebrow"]}</span>
          <h1>{data["title"]}</h1>
          <p class="hero-lead">{data["lead"]}</p>
          <div class="hero-actions">
            <a class="button" href="{WHATSAPP}{data["cta"].replace(" ", "%20")}">{data["cta"]}</a>
            <a class="button secondary" href="#section-1">{data["secondary"]}</a>
          </div>
          <div class="assurance">
            {''.join(f'<div class="assurance-card"><strong>{title}</strong><span>{body}</span></div>' for title, body in data["assurance"])}
          </div>
        </div>
        <aside class="hero-visual" aria-label="Highlight layanan">
          <div class="visual-content">
            <div>
              <div class="visual-kicker">{data["category"]}</div>
              <div class="visual-title">{data["visual_title"]}</div>
            </div>
            <div class="visual-list">
              {''.join(f'<div><strong>{title}</strong><span>{label}</span></div>' for title, label in data["visual_items"])}
            </div>
          </div>
        </aside>
      </div>
    </section>

    <div class="trust-strip">
      <div class="site-shell metrics">
        {''.join(f'<div class="metric"><strong>{value}</strong><span>{label}</span></div>' for value, label in data["metrics"])}
      </div>
    </div>

    {''.join(section_html)}

    <section id="testimonials">
      <div class="site-shell">
        <div class="section-heading">
          <div>
            <span class="eyebrow">Client Testimonials</span>
            <h2>Kepercayaan dari klien yang sudah merasakan layanan.</h2>
          </div>
          <p>Testimoni disusun untuk memperkuat kredibilitas, membantu calon klien merasa yakin, dan mendorong langkah konsultasi.</p>
        </div>
        {testimonials(data["testimonials"])}
      </div>
    </section>

    <section id="faq">
      <div class="site-shell split">
        <div>
          <span class="eyebrow">FAQ</span>
          <h2>Pertanyaan yang sering muncul sebelum konsultasi.</h2>
        </div>
        {faq(data["faq"])}
      </div>
    </section>

    <section>
      <div class="site-shell cta-band">
        <div class="cta-inner">
          <div>
            <span class="eyebrow">Consultation CTA</span>
            <h2>Siap membahas kebutuhan Anda secara lebih serius?</h2>
            <p>{data["contact"]}</p>
          </div>
          <a class="button" href="{WHATSAPP}{data["cta"].replace(" ", "%20")}">{data["cta"]}</a>
        </div>
      </div>
    </section>

    <section id="contact">
      <div class="site-shell contact-grid">
        <div class="contact-card">
          <div class="symbol">{icon()}</div>
          <h2>Hubungi {data["brand"]}</h2>
          <p>{data["contact"]}</p>
          <p><strong>WhatsApp:</strong> +62 812 3456 7890<br><strong>Email:</strong> contact@example.com<br><strong>Alamat:</strong> Jakarta, Indonesia</p>
        </div>
        <form class="form-panel" data-whatsapp="{WHATSAPP}">
          <div class="form-grid">
            <label>Nama
              <input name="Nama" autocomplete="name" required>
            </label>
            <label>Nomor WhatsApp
              <input name="WhatsApp" autocomplete="tel" required>
            </label>
            <label class="full">Kebutuhan
              <select name="Kebutuhan">
                <option>Konsultasi awal</option>
                <option>Minta penawaran</option>
                <option>Booking jadwal</option>
                <option>Tanya paket layanan</option>
              </select>
            </label>
            <label class="full">Pesan
              <textarea name="Pesan" placeholder="Tuliskan kebutuhan, jadwal, lokasi, atau pertanyaan utama Anda."></textarea>
            </label>
          </div>
          <div class="hero-actions">
            <button class="button" type="submit">Kirim Inquiry WhatsApp</button>
          </div>
        </form>
      </div>
    </section>
  </main>

  <footer class="footer">
    <div class="site-shell">
      <span>© <span data-year></span> {data["brand"]}. All rights reserved.</span>
      <a href="../index.html">Kembali ke katalog landing page</a>
    </div>
  </footer>
  <script src="../assets/site.js"></script>
</body>
</html>
"""


def index_page():
    cards = "".join(
        f"""
        <a class="index-card" href="pages/{item["slug"]}.html">
          <span>{item["number"]} — {item["category"]}</span>
          <h3>{item["brand"]}</h3>
          <p>{item["title"]}</p>
        </a>
        """
        for item in LANDINGS
    )
    return f"""<!doctype html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Premium Landing Page Collection</title>
  <meta name="description" content="Koleksi 15 landing page premium untuk berbagai industri bisnis.">
  <link rel="stylesheet" href="assets/styles.css">
</head>
<body>
  <header class="topbar">
    <div class="site-shell nav">
      <a class="brand" href="index.html">
        <span class="brand-mark">LP</span>
        <span>Premium Landing Pages</span>
      </a>
      <nav class="nav-links" aria-label="Navigasi katalog">
        <a href="#collection">Collection</a>
        <a href="pages/supplier-distributor.html">Sample</a>
      </nav>
      <a class="button" href="pages/supplier-distributor.html">Buka Halaman</a>
    </div>
  </header>
  <main>
    <section class="index-hero">
      <div class="site-shell">
        <span class="eyebrow">15 Premium Business Landing Pages</span>
        <h1>Landing page profesional untuk bisnis yang membutuhkan trust, inquiry, dan konversi.</h1>
        <p class="hero-lead">Setiap halaman dibuat dengan layout corporate premium, whitespace bersih, typography elegan, struktur high-conversion, dan CTA WhatsApp.</p>
      </div>
    </section>
    <div id="collection" class="site-shell index-grid">
      {cards}
    </div>
  </main>
  <footer class="footer">
    <div class="site-shell">
      <span>© <span data-year></span> Premium Landing Pages.</span>
      <span>Static HTML, CSS, and JavaScript.</span>
    </div>
  </footer>
  <script src="assets/site.js"></script>
</body>
</html>
"""


def main():
    PAGES.mkdir(exist_ok=True)
    for data in LANDINGS:
        (PAGES / f"{data['slug']}.html").write_text(page(data), encoding="utf-8")
    (ROOT / "index.html").write_text(index_page(), encoding="utf-8")


if __name__ == "__main__":
    main()
