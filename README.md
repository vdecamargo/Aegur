# Aegur

## Offline Python Password Generator

**Aegur** is an open-source password generator written in Python and designed for local, offline use. It focuses on strong randomness, reduced visual ambiguity, and a simple, auditable codebase with no external dependencies.

---

## Project Goals

- **Cryptographic randomness:** Uses Python's `secrets` module for password generation.
- **Visual anti-spoofing:** Excludes ambiguous characters that are commonly confused in manual reading.
- **Offline local use:** Designed to run locally without external services.
- **Auditability:** Small codebase with no third-party runtime dependencies.

---

## Generation Modes

| Flag | Description | Character Set |
| :-- | :-- | :-- |
| `--bank-mode` | Conservative mode | Alphanumeric characters only |
| `--ascii-only` | ASCII-safe mode | Printable ASCII without ambiguous characters |
| `--strong-mode` | Extended mode | ASCII-safe characters plus selected Unicode symbols |
| `--paranoid-mode` | Restricted-output mode | ASCII-safe generation with optional hash output and overwrite attempt |

---

## Installation and Usage

### Requirements

- Python 3.10 or higher

### Clone the repository

```powershell
git clone https://github.com/vdecamargo/Aegur.git
cd Aegur
```

### Run examples

Default mode:

```powershell
python Aegur.py
```

Bank mode with 12 characters:

```powershell
python Aegur.py --bank-mode --length 12
```

Paranoid mode with verbose output:

```powershell
python Aegur.py --paranoid-mode --length 24 --show-password --verbose
```

Copy a generated password to clipboard in PowerShell:

```powershell
python Aegur.py --bank-mode --length 12 | Set-Clipboard
```

---

## Visual Anti-Spoofing

Aegur excludes characters that are often confused during visual reading or manual transcription, such as:

- `0`, `O`, `o`
- `1`, `l`, `I`, `i`

This helps reduce mistakes in contexts where passwords are read, copied, or typed manually.

---

## Entropy Estimate

When using the `--verbose` flag, Aegur displays an entropy estimate based on password length and character pool size.

The estimate follows:

\(H = L \cdot \log_2(N)\)

Where:
- `L` is the password length
- `N` is the size of the character pool

This value is an estimate of password strength, not a guarantee of resistance in every real-world attack scenario.

---

## Security Notes

- Password generation uses Python's `secrets` module.
- The tool is intended for local offline execution.
- The project does not require external Python packages at runtime.
- Memory overwrite attempts in Python may reduce residual exposure, but should not be treated as a guaranteed secure erasure mechanism.

---

## Project Structure

```text
Aegur/
├── Aegur.py
├── generators.py
├── entropy.py
├── charsets.py
├── README.md
└── LICENSE
```

---

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

## Disclaimer

This project is provided **"as is"**, without warranty of any kind, as described in the MIT License.