# 🧰 simple-mc-mod-downloader

A simple Python script that automatically downloads Minecraft mods from either a basic `mods.json` list **or** a Modrinth `modrinth.index.json` file.  

Perfect for quickly setting up a modpack **without manually downloading each mod or using heavy mod managers**.

---

## 📥 Features

- 📦 Download mods from URLs listed in a `mods.json` file  
- ⚡ OR automatically fetch mods from a Modrinth modpack  
- 💾 Saves mods in the same directory as the script  
- 🧭 Creates required folder structure automatically  
- 🪶 Lightweight — no complicated setup required

---

## 🧑‍💻 Requirements

- [Python 3.7+](https://www.python.org/downloads/)  
- [Requests](https://pypi.org/project/requests/)  
- [python-dotenv](https://pypi.org/project/python-dotenv/) *(only required for Modrinth modpacks)*

Install dependencies:

```bash
pip install requests python-dotenv
```


## 📂 Project Structure

simple-mc-mod-downloader/
├── mods.json                  # (optional) Simple mod list
├── modpackdownloader.py       # Main script
├── .env                       # (optional) For Modrinth modpacks
└── README.md



## ⚡ Two Ways to Use the Downloader

### 1. 📄 Basic mods.json (Simple Mode)

Ideal for small modpacks or manually collected mod links.
🧾 Example mods.json:


```json
{
    "ModName1": "https://example.com/mod1.jar",
    "ModName2": "https://example.com/mod2.jar",
    "ModName3": "https://example.com/mod3.jar"
}
```

### 2. 🧰 Modrinth modrinth.index.json (Advanced Mode)

For full Modrinth modpacks with automatic folder structure and downloads.

✅ Setup

Create a .env file in the project directory
example: MODPACK_PATH=C:\Users\Me\Downloads\Better MC [NEOFORGE] BMC5 v31\modrinth.index.json



## 📜 License

This project is licensed under **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)**.

 - If you fork this project, you must clearly state that it is a fork of the original.
 - Forks must be licensed under the same license
 - Commercial use is not allowed - you can't make money from this project

For more details, see the full license here: [https://creativecommons.org/licenses/by-nc-sa/4.0/](https://creativecommons.org/licenses/by-nc-sa/4.0/)


## 🧑‍🔧 Future Improvements

✅ Progress bar for downloads

📦 Automatic mod folder detection in .minecraft

📝 Easier way to add mods — no need to manually edit `mods.json`

🚀 C++ version