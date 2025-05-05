# Memory Forensics Toolkit

## Overview

This project is a cross-platform memory forensics toolkit developed as part of the CY341 semester project. It automates the process of acquiring and analyzing volatile memory on **Linux** and **Windows** systems using powerful open-source tools. The toolkit also supports scanning memory dumps with custom **YARA** rules to detect malicious signatures.

---

##  Features

- Memory acquisition for both Linux and Windows
- Memory analysis using the Volatility framework
- YARA-based malware detection
- Platform-specific automation scripts
- HTML report generation from forensic analysis

---

## Repository Structure
CY341_Semester_Project/
│
├── linux/
│ ├── acquire.sh # Memory acquisition using LiME
│ └── analyze.sh # Memory analysis using Volatility + YARA
│
├── Windows/
│ ├── acquire.bat # Memory acquisition using WinPmem
│ └── analyze.bat # Memory analysis using Volatility + YARA
│
├── yara_rules/
│ ├── rule1.yar # Sample YARA rule
│ └── rule2.yar
│
├── memory_forensics_tool.py # Cross-platform automation script
├── sloth_report.html # HTML report template
└── README.md # Project documentation

---

## Tools Used

### Linux
- [LiME](https://github.com/504ensicsLabs/LiME): Linux Memory Extractor
- [Volatility](https://github.com/volatilityfoundation/volatility): Memory forensics framework
- [YARA](https://github.com/VirusTotal/yara): Pattern matching engine for malware detection

### Windows
- [WinPmem](https://github.com/Velocidex/WinPmem): Windows memory acquisition
- Volatility and YARA (same as Linux)

---

##  Requirements

- Python 3.x
- Volatility
- YARA
- Linux: LiME kernel module (compiled for your running kernel)
- Windows: WinPmem

---

## Linux Usage

1. **Acquire Memory**  
   ```bash
   cd linux
   sudo ./acquire.sh




