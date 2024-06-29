# Using Telegram via Tor 

[Telegram](https://web.telegram.org/k/) was blocked by local network admin. So made a script to by-pass that firewall using Tor.

---

## 📎 Requirements 
- [Tor](https://www.torproject.org/download/) - This downloads Tor Browser and the services with it.
- [Stem](https://pypi.org/project/stem/) - for interacting with Tor services.
- [Selenium](https://pypi.org/project/selenium/) - Opening and controlling browser.
- [Python 3.11](https://www.python.org/downloads/) - made it with version 3.11

---

# 🔧 SETUP 

## ⚙️ Working 
It first creates a Tor service. Check the code's [line 16 and 17](./tgViaTor.py#L16) and see if `9050` or `9150` or other port which works for you.
It opens Chrome on that port and then launches Telegram web.

- Clone this repo
- make a new [venv](https://docs.python.org/3/library/venv.html) (recommended) for this project in the same folder and install the [requirements](./requirements.txt).

### 🪛 Change PATH lines 
in your system, change the paths of
- `user_data` folder path in [this line](./tgViaTor.py#L11) and `tor_pathh` in [this line](./tgViaTor.py#L13) with Tor.exe path in [tgViaTor.py](./tgViaTor.py) file
- `venv_path` in [tgViaTor.bat](./tgViaTor.bat#L9).

### ⚠️ Possible Issues 
- if the setup is done correctly, it may happen that it doesn't connect in one go. you may need to re-launch it a couple of times for it to work.
- Sometimes it may take [upto 5 mins to connect to Tor](./tgViaTor.py#L53).
- Internet speed in Tor is slow.

---

# ⭕ Important Security Considerations: 

- Tor Exit Nodes: 
    - Be aware that Tor exit nodes are not guaranteed to be private or secure. They can potentially monitor or modify your traffic.
- Illegal Activities: 
    - Using Tor for illegal activities is strongly discouraged. It can put you and others at risk.
- Project Scope: 
    - This project is for educational purposes only. It does not offer a comprehensive anonymity solution.
