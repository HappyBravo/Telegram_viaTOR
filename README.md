# Using Telegram via Tor 

[Telegram](https://web.telegram.org/k/) was blocked by local network admin. So made a script to by-pass that firewall using Tor.

---

## 📎 Requirements 
- [Tor](https://www.torproject.org/download/) - This downloads Tor Browser and the services with it.
- [Stem](https://pypi.org/project/stem/) - for interacting with Tor services.
- [Selenium](https://pypi.org/project/selenium/) - Opening and controlling browser.

---

## ⚙️ Working 
It first creates a Tor service. Check the code's [line 16 and 17](./tgViaTor.py#L16) and see if 9050 or 9150 or other port which works for you.
It opens Chrome on that port and then launches Telegram web.

---

### 🔧 Change PATH lines 
Change the path of
- `user_data` folder and `tor_pathh` with Tor.exe path in [tgViaTor.py](./tgViaTor.py) 
- `venv_path` in [tgViaTor.bat](./tgViaTor.bat).

---

# ⭕ Important Security Considerations: 

- Tor Exit Nodes: 
    - Be aware that Tor exit nodes are not guaranteed to be private or secure. They can potentially monitor or modify your traffic.
- Illegal Activities: 
    - Using Tor for illegal activities is strongly discouraged. It can put you and others at risk.
- Project Scope: 
    - This project is for educational purposes only. It does not offer a comprehensive anonymity solution.
