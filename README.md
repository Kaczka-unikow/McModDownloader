# 🧰 simple-mc-mod-downloader


A simple Python script that automatically downloads Minecraft mods listed in a `mods.json` file.  
Perfect for quickly setting up a modpack **without manually downloading each mod or using heavy mod managers**.
---

## 📥 Features

- 📦 Downloads mods from URLs listed in `mods.json`  
- 💾 Saves mods in the same directory as the script  
- ⚡ Lightweight and easy to use — no complicated setup required

---

## 🧑‍💻 Requirements

- [Python 3.7+](https://www.python.org/downloads/)  
- [Requests](https://pypi.org/project/requests/) library

Install dependencies with:

```bash
pip install requests
```


## 📂 Project Structure

simple-mc-mod-downloader/
├── mods.json
├── main.py
└── README.md


## 🧾 mods.json Example

{
    "ModName1": "https://example.com/mod1.jar",
    "ModName2": "https://example.com/mod2.jar",
    "ModName3": "https://example.com/mod3.jar"
}


## 📜 License

This project is licensed under **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)**.

 - If you fork this project, you must clearly state that it is a fork of the original.
 - Forks must be licensed under the same license
 - Commercial use is not allowed - you can't make money from this project

For more details, see the full license here: [https://creativecommons.org/licenses/by-nc-sa/4.0/](https://creativecommons.org/licenses/by-nc-sa/4.0/)


## 🧑‍🔧 Future Improvements

✅ Progress bar for downloads

📦 Automatic mod folder detection in .minecraft

🌐 Maybe support for Modrinth API

📝 Easier way to add mods — no need to manually edit `mods.json`

🚀 C++ version