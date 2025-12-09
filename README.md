<div align="center">

# 🎬 YouTube Video Downloader + Analyzer  
### A Powerful Python Tool to Download YouTube Videos & Analyze Metadata & Text

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Active-success)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20MacOS-lightgrey)
![License](https://img.shields.io/badge/License-Free-brightgreen)

</div>

---

## 📌 Overview  

This project is a **complete YouTube video analytics tool** built in Python.  
It allows you to:

✔ Download any YouTube video  
✔ Extract metadata  
✔ Analyze description text  
✔ Identify top keywords  
✔ Store video information  

Perfect for beginners, students, and professionals exploring **APIs, Python automation, text analytics, and data extraction**.

---

## 🚀 Features  

### 🎥 **1. YouTube Video Downloader**
- Downloads the **highest resolution** video available  
- Automatically saves content to `/downloads/`

### 🧾 **2. Metadata Extraction**
Extracts:
- Video Title  
- Author  
- Views  
- Length (seconds)  
- Description text  

### 🔍 **3. Text Analysis Engine**
- Tokenizes description  
- Counts top keywords  
- Provides insights about video content  

### 🧱 **4. Modular Code Structure**
Easy to understand & extend:
- `downloader.py` → handles download operations  
- `analyzer.py` → handles description analysis  
- `app.py` → main runner  

---

## 📁 Project Structure  

```
📦 youtube-video-downloader-analyzer
│
├── app.py                 # Main application
├── downloader.py          # Handles downloading
├── analyzer.py            # Text analytics module
├── requirements.txt       # Dependencies
└── downloads/             # Stores downloaded videos & video_info.json
```

---

## 🛠️ Tech Stack  

- **Python 3.8+**  
- **Pytube** (video download)  
- **Regex** (text processing)  
- **Collections** (Counter for keyword frequency)

---

## ⚙️ Installation  

Clone the repository:

```
git clone https://github.com/yourusername/youtube-video-downloader-analyzer
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ How to Run  

Run the main script:

```
python app.py
```

Enter a YouTube URL:

```
Enter YouTube video URL:
```

---

## 📊 Sample Output  

```
Downloading: Python Tutorial For Beginners

🎯 Video Analysis
Title: Python Tutorial
Author: Programming Channel
Views: 2,345,678
Top Words in Description:
[('python', 10), ('tutorial', 6), ('learn', 4)]
```

---

## 🔮 Future Enhancements  

- 📌 GUI version (Tkinter / PyQt)  
- 📌 Playlist Downloader  
- 📌 Transcript Analysis (NLP)  
- 📌 Sentiment Analysis  
- 📌 Full Video Analytics Dashboard  

---

## 🤝 Contributing  

Contributions, issues, and feature requests are welcome!  
Feel free to open a PR.

---

## 👤 Author  

**Shreyash Hedaoo**  
Python Developer | Data Analyst | ML Enthusiast  
📧 Email: shreyash.hedaoo@yahoo.com 
🔗 LinkedIn: www.linkedin.com/in/shreyash-hedaoo-745960234

---

<div align="center">
✨ Thank you for exploring this project! If you liked it, don't forget to ⭐ the repo!
</div>

<p align="center">
  <img src="banner.png" width="800"/>
</p>
