---
name: humanizer
description: "Humanizer: ubah tulisan beraroma AI jadi terdengar seperti manusia tanpa mengubah isinya. Pakai saat mengedit/mereview prosa: deteksi pola AI (kontras not-X-but-Y, closer satu baris, triad paksa, dash berlebih, klaim bombastis, kata stok AI, bold dekoratif, sisa chat). Berbasis riset Wikipedia 'Signs of AI writing'. Cocok untuk copy Indonesia yang diterjemahkan/ditulis ulang dari pola Inggris."
allowed-tools: Read Write Edit Glob Grep
---

# ext-humanizer — Humanizer: hapus pola tulisan AI

> **Sumber:** [blader/humanizer](https://github.com/blader/humanizer) (MIT) — pola dari Wikipedia
> ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).
> Diadaptasi ke Bahasa Indonesia; pola dan contoh Inggris dipertahankan karena polanya spesifik Bahasa Inggris.

Tulis ulang teks beraroma AI agar terbaca seperti ditulis manusia, bukan chatbot. **Pertahankan isi.** Jangan mengarang fakta baru.

## Kenapa teks AI terdengar seperti itu

Model bahasa menulis kata yang paling mungkin muncul berikutnya — pilihan yang cocok untuk pembaca dan subjek seluas mungkin. Penulis manusia memilih untuk SATU pembaca dan SATU subjek: pilihannya tidak rata dan spesifik. Setiap pola di bawah adalah bentuk "pilihan default" itu:

- **Staging:** kalimat memberi sinyal penting, bukan menambah fakta.
- **Ritme pakai aturan:** triad dan dash dipakai di mana-mana.
- **Inflasi:** fakta biasa didandani jadi pivotal/ahli.
- **Format pakai aturan:** bold dan kapitalisasi di semua item.
- **Sisa chat:** wrapper chat ("Great question!") yang tidak sengaja ikut.
- **Salah pembaca:** balasan menjelaskan ulang latar yang sudah diketahui lawan bicara.

Dua aturan turunan: setiap kalimat yang dipertahankan WAJIB menambah sesuatu yang belum diketahui pembaca. Sebuah "tell" dihitung sebanding dengan seberapa jarang penulis teliti melakukannya dengan sengaja. Pola bernomor terkuat dulu: §1–§5 layak diedit dalam sekali lihat; pola bertanda *lemah sendiri* butuh ditemani pola lain di bagian yang sama.

## Cara kerja

1. **Tandai tell-nya.** Baca seluruh teks sekali, tandai setiap pola yang ketemu, yang terkuat dulu. Perhatikan bentuk paragraf juga.
2. **Draf rewrite.** Pertahankan semua klaim yang didukung sumber. Boleh memadatkan, menggabung/memecah paragraf, mengubah struktur — tapi jangan tambah fakta, nama, angka, tanggal, kutipan, atau sitasi yang tidak ada di sumber/user. Kalau butuh detail yang tidak ada, tanyakan atau tulis kalimat yang lebih sederhana.
3. **Cek draf.** Baca keras-keras. Tanya: apa yang masih terdengar AI? Apakah rewrite menambah/menghilangkan fakta? Cari lagi tell yang paling sering lolos: §1 kontras, §2 closer, §6 triad, §8 dash, §19 bold.
4. **Tulis versi final.** Nyatakan tiap poin secara natural, jangan tambal sulam frasa yang ditandai.

### Suara (voice)

Kalau user memberi contoh tulisan, tiru panjang kalimat, pilihan kata, tanda baca, dan transisinya — contoh mengalahkan semua pola di bawah (termasuk aturan dash §8). Tanpa contoh: ambil suara dari jenis teksnya. Blog/esai/opini boleh berpendapat, ragu, bercanda. Teks referensi/teknis/hukum tetap netral dan lugas. Menghapus tell hanya setengah pekerjaan; hasilnya harus tetap terdengar seperti manusia.

## A. Staging, bukan menyatakan (tell terkuat)

### 1. Not X but Y

**Waspadai:** not X but Y; not just/not only/not merely X, but Y; it's not X, it's Y; bentuk terbalik X rather than Y; kontras yang dipecah dua kalimat ("This does not mean X. It means Y."); ekor negatif terpangkas ("..., no guessing").
**Masalah:** paruh negatif menyebut sesuatu yang tidak diklaim siapa pun, sehingga paruh positif terdengar lebih besar. Nyatakan langsung. Pertahankan kontras hanya jika paruh negatif mengoreksi keyakinan yang benar-benar dipegang pembaca.
**Contoh:**
> Sebelum: *It's not just about the beat; it's part of the aggression.*
> Sesudah: *The heavy beat adds to the aggressive tone.*

### 2. Closer satu baris & fragmen dramatis

**Waspadai:** paragraf satu kalimat yang mengulang paragraf sebelumnya ("That is the real win.", "That distinction matters.", "Read that again."); barisan fragmen ("No aesthetic prior. No nostalgia."); SATU KATA KAPITAL atau diberi titik per kata (every. single. day.).
**Masalah:** baris itu meminta pembaca berhenti pada klaim, bukan menambah klaim. Potong closer yang mengulang.

### 3. Pepatah yang terdengar dalam

**Waspadai:** the real question is, at its core, fundamentally, the heart of the matter, X is the Y of Z, X becomes a trap, the language/currency/architecture of.
**Masalah:** poin biasa didandani jadi kebenaran tersembunyi. Ganti dengan klaim spesifik.

### 4. Pemanasan sebelum poin (staged run-up)

**Waspadai:** Let's dive in, here's what you need to know, without further ado, Honestly?, Look, Here's the thing, Real talk.
**Masalah:** penulis mengumumkan poin alih-alih menyampaikan poin. Hapus pemanasannya.

### 5. Berdebat dengan siapa pun (arguing with no one)

**Waspadai:** This isn't about, I'm not saying, To be clear, Don't get me wrong, Some might say... but, You might think... but.
**Masalah:** teks menjawab keberatan yang tidak ada di mana pun — biasanya sisa draf lama. Hapus pembelaannya.

## B. Ritme pakai aturan

### 6. Triad paksa

**Masalah:** ide datang bertiga agar terdengar lengkap ("innovation, inspiration, and insights") — padahal maknanya tidak punya tiga bagian. Pastikan tiap item menambah ide berbeda; gabung atau kembangkan yang terkuat.

### 7. Awalan kalimat berulang

**Masalah:** beberapa kalimat beruntun mulai dengan subjek yang sama. Gabung kalimatnya atau mulai dari aksinya.

### 8. Dash sebagai konektor universal

**Aturan:** rewrite final TIDAK BOLEH mengandung em dash (—) atau en dash (–), kecuali contoh suara penulis memakainya. Ganti dengan titik, koma, kolon, atau kurung. Abaikan dash di dalam code/URL/path. Satu dash = *lemah sendiri*; teks penuh dash bukan.

### 9. Tumpukan qualifier

**Waspadai:** to be fair, could potentially, might arguably, in some cases it may. *Lemah sendiri.*
**Masalah:** klaim ditambal qualifier berlapis-lapis sampai terdengar tidak yakin. Pertahankan qualifier hanya jika sumber mendukungnya.

### 10. Pasangan hyphen di mana-mana

**Waspadai:** high-quality, well-known, long-term dipakai SETELAH kata benda ("the report is high-quality").
**Perbaikan:** hyphen hanya sebelum kata benda ("a high-quality report"); setelah kata benda tanpa hyphen ("the report is high quality"). *Lemah sendiri.*

### 11. Pasif & subjek hilang

**Masalah:** teks menyembunyikan siapa pelakunya. Pakai aktif jika memperjelas. *Lemah sendiri.*

## C. Inflasi & otoritas pinjaman

### 12. Kata AI yang overused

**Waspadai:** delve, additionally, crucial, deep dive, enduring, enhance, garner, intricate, pivotal, robust (kiasan), showcase, tapestry, testament, underscore (kata kerja), vibrant, landscape (abstrak), meticulous.
**Masalah:** model memakai kata-kata ini jauh lebih sering dari manusia, apalagi berkelompok.

### 13. Signifikansi yang digelembungkan

**Waspadai:** stands as a testament, a pivotal moment, plays a key role, underscores its importance, lasting legacy, setting the stage for; "Despite these challenges... continues to thrive"; paragraf perpisahan ("The future looks bright", "Exciting times ahead").
**Perbaikan:** pertahankan faktanya, buang signifikansinya. Akhiri di fakta konkret terakhir.

### 14. Koneksi samar

**Waspadai:** associated with, connected to, linked to, tied to — tanpa menjelaskan BAGAIMANA terhubungnya.
**Perbaikan:** sebutkan hubungan yang diberikan sumber; kalau sumber tidak bilang, jangan karang.

### 15. Ekor -ing yang dangkal

**Waspadai:** highlighting, underscoring, ensuring, reflecting, symbolizing, fostering, showcasing yang ditempel ke fakta sederhana agar terdengar dalam.

### 16. Bahasa sales

**Waspadai:** nestled, breathtaking, stunning, renowned, groundbreaking (kiasan), must-visit, in the heart of, rich (kiasan).
**Perbaikan:** nyatakan apa bendanya, langsung.

### 17. Otoritas pinjaman

**Waspadai:** experts argue, observers have cited, some critics, several publications; daftar outlet prestis; jumlah followers sebagai bukti.
**Perbaikan:** pakai sumber nyata yang disebut sumber teks; selainnya potong.

### 18. Menghindari is/are/has

**Waspadai:** serves as, stands as, functions as, boasts, features, offers.
**Perbaikan:** pakai *is*, *are*, *has* yang sederhana.

## D. Format pakai aturan

### 19. Bold sebagai dekorasi

**Masalah:** kata di-bold tanpa alasan; list yang setiap itemnya berlabel bold + kolon. Hapus bold-nya; ubah labeled list jadi prosa jika labelnya tidak membawa informasi.

### 20. Heading dekoratif

**Masalah:** setiap kata kapital, emoji/panah (→) di heading, garis horizontal di antara semua seksi. Pakai sentence case, hapus dekorasi.

### 21. Tanda kutip keriting

**Masalah:** "..." di tempat yang memakai "..." lurus. *Lemah sendiri.*

## E. Sisa chat & draf

Hapus langsung, tidak perlu ditulis ulang.

### 22. Residu chatbot

**Waspadai:** I hope this helps, Of course!, Certainly!, Great question!, You're absolutely right, Would you like..., Want me to...?, let me know, here is a...
**Masalah:** sapaan/pujian/penawaran chatbot tertinggal di teks. Ini tell paling pasti. Hapus wrapper-nya, pertahankan isinya.

### 23. Disclaimer batas pengetahuan & tebakan

**Waspadai:** as of [date], up to my last training update, based on available information, not publicly available, likely [grew up/studied], it is believed that.
**Masalah:** teks menyebut batas pengetahuan model lalu mengisi celah dengan tebakan yang masuk akal. Nyatakan apa yang tidak ditunjukkan sumber — atau hapus kalimatnya.

### 24. Heading diulang di kalimat pertama

**Masalah:** heading diikuti paragraf satu baris yang mengulanginya. Hapus kalimat ulangannya.

### 25. Menulis tentang dokumen, bukan subjeknya

**Waspadai:** "was added to replace", "generated from", "the table below compares", "this section is organized by".
**Masalah:** teks mendeskripsikan dirinya sendiri. Sebut versi sebelumnya hanya di changelog/migrasi.

## F. Menulis untuk pembaca yang salah

### 26. Menjelaskan ulang yang sudah diketahui pembaca

**Waspadai:** balasan singkat yang menyusun ulang masalah, diagnosis, dan bukti sebelum sampai ke keputusan; jawaban yang baru muncul di baris terakhir.
**Masalah:** dalam balasan, pembaca sudah punya konteksnya. Dahulukan keputusan; pertahankan hanya penalaran yang mengubah persetujuan pembaca.

## Kapan TIDAK bertindak

Setiap pola adalah pilihan default — manusia boleh melakukannya dengan sengaja. Abaikan frasa yang diawasi di dalam kutipan, judul, nama diri, atau bagian yang MEMBAHAS frasa itu. Salam/pembuka surat bukan tell. Teks sebelum 30 November 2022 bukan tulisan AI. Pertahankan detail spesifik yang membawa suara penulis (alamat nyata, kutipan aneh, referensi era, aside jujur, koreksi diri).

---
*Diadaptasi dari [blader/humanizer](https://github.com/blader/humanizer) v3.1.0 (MIT).*
*Pola berasal dari Wikipedia ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).*
