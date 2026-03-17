# Aegur
## 🛡️ Aegur — Offline Python Password Generator

**Aegur** is an offline, open-source, and highly secure password generator written in Python. It is designed as a digital shield against brute-force attacks and visual phishing.

---

### 🎯 Project Goals

* **Cryptographic Randomness:** Maximum entropy using the `secrets` module.
* **Visual Anti-Spoofing:** Strict exclusion of ambiguous characters.
* **Total Offline Isolation:** Zero network connection at any time.
* **Auditability:** Clean code with zero external dependencies.

---

### 🛡️ Generation Modes

| Flag | Description | Character Set |
| :--- | :--- | :--- |
| `--bank-mode` | Ultra-conservative | Secure alphanumeric only |
| `--ascii-only` | Standard Web | Safe printable ASCII |
| `--strong-mode` | High Security | ASCII + distinct Unicode symbols |
| `--paranoid-mode`| Maximum Safety | Memory wiping & SHA3 hash audit |

---

### 🚀 Installation and Usage (Windows)

**1. Clone the Repository**
```powershell
git clone [https://github.com/vdecamargo/Aegur](https://github.com/vdecamargo/Aegur)
cd aegur
# Default mode (strong-mode, 16 chars)
python Aegur.py

# Bank mode with 12 characters
python Aegur.py --bank-mode --length 12

# Paranoid mode with entropy statistics
python Aegur.py --paranoid-mode --length 24 --show-password --verbose
python Aegur.py --bank-mode --length 12 | Set-Clipboard
### 🔍 Visual Anti-Spoofing Filter

Aegur strictly removes visually confusing characters:

* **Confusing Digits/Letters:** `0/O/o`, `1/l/I/i`.
* **Homoglyphs:** Cyrillic or Greek letters that mimic Latin ones (e.g., `а` vs `a`).
* **Legacy Issues:** Removes symbols that break in older databases.

---

### 📊 Entropy Statistics ($H$)

When using the `--verbose` flag, Aegur calculates the mathematical strength:

$$H = L \cdot \log_2(N)$$

Where $L$ is the length and $N$ is the size of the character pool.

---

### 📝 Security Principles

* **Cryptographic Randomness:** Exclusive use of `secrets.SystemRandom()`.
* **Zero Trace:** Sensitive strings are overwritten in memory after use.
* **Audit-Ready:** No hidden code. No external libraries.

---

**Aegur is not just a tool — it's a principle.**