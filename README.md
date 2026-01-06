# 🦅 MetaExif Pro

**The Ultimate Metadata Editor & Digital Mimicry Tool**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)]()

---

## 🎯 What It Does

MetaExif Pro lets you **edit any file's metadata** and perform **complete digital mimicry** — making files look like they came directly from a phone camera, never touched by a computer.

### Key Capabilities:

| Feature | Description |
|---------|-------------|
| **🪄 Auto-Fake Mimicry** | One-click transformation to iPhone, Samsung, Xiaomi, Huawei, or Canon camera signatures |
| **🕒 Time Travel** | Changes both Exif dates AND Windows Created/Modified timestamps |
| **🧹 Trace Removal** | Removes `Zone.Identifier` (downloaded from internet marker) |
| **📁 Smart Renaming** | Renames files to authentic device format (`IMG_1234.JPG`, `20240101_120000.jpg`) |
| **📝 Full Tag Editor** | Edit any Exif, XMP, IPTC tag manually |

---

## 📱 Supported Device Presets

| Device | Software | Filename Format |
|--------|----------|-----------------|
| iPhone 14 Pro | iOS 16.5 | `IMG_XXXX.JPG` |
| Samsung S23 Ultra | Android | `YYYYMMDD_HHMMSS.jpg` |
| Huawei P60 Pro | HarmonyOS 4.0 | `IMG_YYYYMMDD_HHMMSS.jpg` |
| Xiaomi 13 Ultra | MIUI 14 | `IMG_YYYYMMDD_HHMMSS.jpg` |
| Canon EOS R5 | Firmware | `IMG_XXXX.JPG` |
| Windows 11 PC | Win11 Pro | `Screenshot YYYY-MM-DD...` |
| macOS Sonoma | macOS 14 | `Screenshot ... at HH.MM.SS` |
| Ubuntu 22.04 | GNOME | `Screenshot from ...` |

---

## 🛠 Installation

```bash
# 1. Clone repository
git clone https://github.com/hindipython/MetaExifPro.git
cd MetaExifPro

# 2. Create virtual environment (recommended for clean builds)
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run
python main.py
```

---

## 🏗 Build Standalone EXE

For a lightweight (~25MB) portable executable:

```bash
# Using batch script (Windows)
compile_lightweight.bat

# Or manually
python build.py
```

The executable will be in `dist/MetaExifPro.exe`

---

## 💎 Supported File Formats

| Type | Extensions |
|------|------------|
| **Images** | JPG, JPEG, PNG, TIFF, WEBP, BMP, GIF, HEIC |
| **Audio** | MP3, FLAC, WAV, M4A, OGG, AAC, OPUS |
| **Video** | MP4, MOV, MKV, WEBM |
| **Documents** | PDF, DOCX, XLSX |
| **Any File** | Date editing works on ALL files |

---

## ⚠️ Important Notes

- **PNG files** do not support traditional Exif — use JPG for full mimicry
- **File:Size** is read-only (physical file size cannot be faked)
- **Zone.Identifier** removal only works on Windows NTFS

---

## ☕ Support the Project

If you find this tool useful, consider buying me a coffee:

**Bitcoin (BTC):**
```
bc1qnnh20ehd88a9jxzqhe4ahq6z5xfkhk4p5pgnhn
```

---

## 📝 License

MIT License — See [LICENSE](LICENSE)
