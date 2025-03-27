
# 🛡️ HostTracer — Name Server and Hosting Provider Checker  

HostTracer is a powerful Python tool designed to quickly identify the **name servers** and **hosting provider** of a target domain. It’s a lightweight and fast utility, ideal for **bug bounty hunters** and **penetration testers** to gather critical reconnaissance data.  

---

## 🚀 Features  
✅ Fast and accurate name server lookup  
✅ Identify hosting provider using WHOIS data  
✅ Lightweight and easy to use  
✅ Works on Windows, macOS, and Linux  

---

## 🕵️‍♂️ Why HostTracer is Useful for Bug Bounty  
🔎 **Reconnaissance** – Identify the target's infrastructure for attack surface mapping  
🌐 **Subdomain Enumeration** – Cross-check name servers to discover hidden subdomains  
💡 **Infrastructure Cloning** – Determine hosting provider to mimic target environments  
🔒 **Security Hardening** – Verify misconfigured name servers and WHOIS privacy leaks  

---

## 🏗️ Installation  

### 1. **Clone the repository**  
```bash
git clone https://github.com/your-username/HostTracer.git
cd HostTracer
```

### 2. **Create a virtual environment (optional)**  
```bash
python -m venv venv
```

Activate the virtual environment:  
- **Linux/macOS:**  
```bash
source venv/bin/activate
```
- **Windows:**  
```bash
.\venv\Scripts\activate
```

### 3. **Install dependencies**  
```bash
pip install dnspython python-whois
```

---

## 🎯 Usage  
1. Run the script:  
```bash
python host_tracer.py
```

2. Enter the domain when prompted:  
```bash
Enter domain: example.com
```

3. Example Output:
```
🔍 Checking Name Servers...
➡️ a.iana-servers.net.
➡️ b.iana-servers.net.

🌐 Finding Hosting Provider...
➡️ IANA
```

---

## 📝 Code Structure  
```plaintext
├── host_tracer.py     # Main script
├── README.md          # Project documentation
└── requirements.txt   # List of dependencies
```

---

## 🛠️ How It Works  
- **dns.resolver** → Retrieves the domain's name servers  
- **whois.whois** → Checks the WHOIS data for the hosting provider  

---

## 🏆 Future Improvements  
✅ Bulk domain checking  
✅ Export results to CSV/JSON  
✅ Add GUI with `tkinter` or `PyQt`  

---

## 🤝 Contributing  
Feel free to fork the repo and submit a pull request!  

---

## 📄 License  
This project is licensed under the **MIT License**.  
