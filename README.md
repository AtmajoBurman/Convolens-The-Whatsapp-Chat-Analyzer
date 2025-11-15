# **CONVOLENS – The WhatsApp Chat Analyzer**

A powerful and elegant **WhatsApp Chat Analyzer** built with **Streamlit**, capable of breaking down conversations into meaningful metrics, patterns, and visual insights.

Upload your exported WhatsApp chat (`.txt` file) and instantly get deep analytics — perfect for personal insights, research, or fun group analysis.

🔗 **Live App:**
👉 [https://convolens-the-whatsapp-chat-analyzer.streamlit.app/](https://convolens-the-whatsapp-chat-analyzer.streamlit.app/)

---

## 🚀 **Features**

### 🔢 Chat Statistics

* Total messages
* Total words
* Total media shared
* Total links shared

### 📅 Timeline Analysis

* Monthly timeline
* Daily timeline

### 🗺️ Activity Maps

* Most active day
* Most active month
* Weekly heatmap (Day × Hour)

### 👥 User Insights

* Busiest users (chart + table)
* Individual user's contribution

### 🌥️ Word Analysis

* WordCloud
* Top 20 most common words

### 😀 Emoji Analytics

* Most used emojis
* Emoji usage percentage

---

## 🖼️ **Screenshots**

Paste your 5 screenshot links below:

```
![Screenshot 1](https://example.com/screenshot1.png)
![Screenshot 2](https://example.com/screenshot2.png)
![Screenshot 3](https://example.com/screenshot3.png)
![Screenshot 4](https://example.com/screenshot4.png)
![Screenshot 5](https://example.com/screenshot5.png)
```

---

## 📂 **Project Structure**

```
├── main.py                # Streamlit interface & visualizations
├── helper.py              # Helper functions for analysis
├── preprocessor.py        # Chat preprocessing logic
├── combined_stopwords.txt # Custom stopwords
├── stop_hinglish.txt      # Extra stopwords
└── requirements.txt       # Dependencies for Streamlit Cloud
```

---

## 🛠️ **How to Run Locally**

### 1️⃣ Clone the repository

```
git clone https://github.com/AtmajoBurman/Convolens-The-Whatsapp-Chat-Analyzer.git
cd Convolens-The-Whatsapp-Chat-Analyzer
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run the app

```
streamlit run main.py
```

---

## 🌐 **Deploying on Streamlit Cloud**

1. Push this project to GitHub
2. Visit → [https://share.streamlit.io](https://share.streamlit.io)
3. Connect your repo
4. Configure:

   * **Main file:** `main.py`
   * **Branch:** `main`
   * **Dependencies:** `requirements.txt`
5. Click **Deploy**

Your app will auto-build and go live.

---

## 🤝 **Contributing**

Contributions, issues, and suggestions are welcome!
Feel free to fork the repository and submit a PR.

---

## 📜 **License**

This project is open-source and available under the MIT License.

---

