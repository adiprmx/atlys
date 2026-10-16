---
name: stop-slop
description: "Stop Slop: pangkas retorika & basa-basi AI dari prosa. 8 aturan inti (potong filler, hancurkan struktur formulaik, aktif, spesifik, variasi ritme) + daftar frasa yang wajib dibuang + cek kilat + skor 1-10 per dimensi. Pakai saat menulis, mengedit, atau mereview teks agar langsung ke poin."
allowed-tools: Read Write Edit Glob Grep
---

# ext-stop-slop — Stop Slop: pangkas retorika AI

> **Sumber:** [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) (MIT)
> oleh Hardik Pandya. Diadaptasi ke Bahasa Indonesia; daftar frasa Inggris dipertahankan
> karena polanya spesifik Bahasa Inggris.

Hilangkan pola tulisan AI yang predictable dari prosa.

## 8 Aturan Inti

1. **Potong frasa filler.** Hapus pembuka basa-basi, kruk penekanan, dan semua adverb. Lihat daftar frasa di bawah.
2. **Hancurkan struktur formulaik.** Hindari kontras biner, listing negatif, fragmentasi dramatis, setup retoris, agensi palsu. Lihat daftar struktur di bawah.
3. **Pakai active voice.** Setiap kalimat butuh subjek manusia yang melakukan sesuatu. Tanpa pasif. Tanpa benda mati yang melakukan kata kerja manusia ("the complaint becomes a fix").
4. **Spesifik.** Tanpa deklaratif samar ("The reasons are structural"). Sebut bendanya. Tanpa ekstrem malas ("every", "always", "never").
5. **Tempatkan pembaca di ruangan.** Tanpa suara narator-dari-kejauhan. "You" mengalahkan "People". Spesifik mengalahkan abstrak.
6. **Variasikan ritme.** Campur panjang kalimat. Dua item mengalahkan tiga. Akhiri paragraf dengan cara berbeda. Tanpa em dash.
7. **Percayai pembaca.** Nyatakan fakta langsung. Lewati pelembut, justifikasi, dan tuntunan tangan.
8. **Potong quotable.** Kalau terdengar seperti pull-quote, tulis ulang.

## Cek Kilat (sebelum menyerahkan prosa)

- Ada adverb? Bunuh.
- Ada pasif? Cari pelakunya, jadikan subjek.
- Benda mati melakukan kata kerja manusia? Sebut orangnya.
- Kalimat diawali kata Wh-? Susun ulang.
- Ada "here's what/this/that"? Potong, langsung ke poin.
- Ada kontras "not X, it's Y"? Nyatakan Y langsung.
- Tiga kalimat beruntun sama panjangnya? Pecah satu.
- Paragraf diakhiri one-liner punchy? Variasikan.
- Ada em-dash? Hapus.
- Deklaratif samar ("The implications are significant")? Sebut implikasinya apa.
- Narator-dari-kejauhan ("Nobody designed this")? Masukkan pembaca ke adegan.
- Meta-joiner ("The rest of this essay...")? Hapus. Biarkan esai bergerak.

## Skor

Nilai 1–10 per dimensi:

| Dimensi | Pertanyaan |
|---------|-----------|
| Directness | Pernyataan atau pengumuman? |
| Rhythm | Bervariasi atau metronomis? |
| Trust | Menghormati kecerdasan pembaca? |
| Authenticity | Terdengar manusia? |
| Density | Ada yang bisa dipotong? |

Di bawah 35/50: revisi.

## Daftar Frasa yang Dibuang

### Pembuka basa-basi (throat-clearing)
Hapus frasa pengumuman ini; nyatakan isinya langsung:
"Here's the thing:", "Here's what [X]", "Here's why [X]", "The uncomfortable truth is", "It turns out", "The real [X] is", "Let me be clear", "The truth is,", "I'll say it again:", "I'm going to be honest", "Can we talk about", "Here's what I find interesting"

### Kruk penekanan
Tidak menambah makna — hapus: "Full stop." / "Period.", "Let that sink in.", "This matters because", "Make no mistake", "Here's why that matters"

### Jargon bisnis → bahasa lugas
| Hindari | Pakai |
|---------|-------|
| Navigate (challenges) | Handle, address |
| Unpack (analysis) | Explain, examine |
| Lean into | Accept, embrace |
| Landscape (context) | Situation, field |
| Game-changer | Significant, important |
| Double down | Commit, increase |
| Deep dive | Analysis, examination |
| Moving forward | Next, from now |
| Circle back | Return to, revisit |
| On the same page | Aligned, agreed |

### Adverb — bunuh semua
Tanpa kata -ly. Tanpa pelembut, penguat, atau hedge: "really", "just", "literally", "genuinely", "honestly", "simply", "actually", "deeply", "truly", "fundamentally", "inherently", "inevitably", "interestingly", "importantly", "crucially".
Juga potong: "At its core", "In today's [X]", "It's worth noting", "At the end of the day", "When it comes to", "In a world where", "The reality is"

### Meta-komentar
Hapus aside yang merujuk ke struktur teks sendiri: "Hint:", "Plot twist:", "You already know this, but", "But that's another post", "The rest of this essay explains...", "Let me walk you through...", "In this section, we'll...", "I want to explore..."

### Deklaratif samar
Kalimat yang mengumumkan pentingnya sesuatu tanpa menyebut bendanya — bunuh: "The reasons are structural", "The implications are significant", "This is the deepest problem", "The stakes are high", "The consequences are real"

## Daftar Struktur yang Dihindari

### Kontras biner (drama palsu)
"Not because X. Because Y." / "[X] isn't the problem. [Y] is." / "The answer isn't X. It's Y." / "It feels like X. It's actually Y." / "The question isn't X. It's Y." / "not X, it's Y" / "stops being X and starts being Y" / "not just X but also Y"
**Ganti:** nyatakan Y langsung. "The problem is Y."

### Listing negatif
Menyebut apa yang BUKAN sebelum mengungkap apa yang sebenarnya: "Not a X... Not a Y... A Z." / "It wasn't X. It wasn't Y. It was Z."
**Ganti:** nyatakan Z. Pembaca tidak butuh landasan pacu.

### Fragmentasi dramatis
Fragmen kalimat untuk penekanan = kedalaman buatan: "[Noun]. That's it. That's the [thing]." / "X. And Y. And Z." / "This unlocks something. [Word]."
**Ganti:** kalimat lengkap. Percayai isi, bukan presentasi.

### Setup retoris
Mengumumkan wawasan alih-alih menyampaikannya: "What if [reframe]?" / "Here's what I mean:" / "Think about it:" / "And that's okay."

### Agensi palsu (false agency)
Benda mati diberi kata kerja manusia — AI suka ini karena menghindari menyebut pelaku:
"a complaint becomes a fix" → seseorang memperbaikinya. "a bet lives or dies in days" → seseorang menghentikan proyeknya. "the decision emerges" → seseorang memutuskan. "the culture shifts" → orang mengubah perilaku. "the data tells us" → seseorang membaca dan menyimpulkan. "the market rewards" → pembeli membayar.
**Ganti:** sebut manusianya. "The team fixed it that week."

### Narator-dari-kejauhan
Mel floating di atas adegan: "Nobody designed this." / "This happens because..." / "People tend to..."
**Ganti:** masukkan pembaca ke ruangan. "You don't sit down one day and decide to..."

### Pasif
"X was created" → sebut siapa. "It is believed that" → sebut siapa yang percaya. "Mistakes were made" → sebut siapa yang salah.

### Awalan kalimat yang dihindari
Kalimat diawali What/When/Where/Which/Who/Why/How → susun ulang. Paragraf diawali "So" → mulai dari isi. Kalimat diawali "Look," → hapus.

### Pola ritme
List tiga item → pakai dua atau satu. Pertanyaan yang langsung dijawab sendiri → biarkan bernapas atau potong. Setiap paragraf diakhiri punchy → variasikan. Em-dash → hapus total. "Not always. Not perfectly." → hedge menyamar sebagai reassurance.

### Pola kata
Ekstrem malas (every, always, never, everyone, nobody) = otoritas palsu → pakai spesifik. Semua adverb = penekanan kosong.

---
*Diadaptasi dari [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) (MIT).*
