# Sloth Memory Forensic Toolkit

> **LiME + Volatility + YARA Integration**  
> "Slow and thorough memory forensics"

## Project Structure
/live_memory_forensic/
│── /tools/
│ ├── lime/ # LiME kernel module source
│ └── volatility/ # Volatility analysis framework
│── /yara_rules/ # Custom YARA signatures
│── sloth_forensic.py # Main analysis script
│── sloth_report.html # HTML report template
└── README.md

## Installation

```bash
# Clone repository
git clone https://github.com/ayeshakashif-ak/CY341_Semester_Project.git
cd live_memory_forensic

# Install dependencies
sudo apt update && sudo apt install -y build-essential python3 dwarfdump linux-headers-$(uname -r)

# Build LiME module
cd tools/lime/src && make && cd ../../..

# Make script executable
chmod +x sloth_forensic.py

sudo ./sloth_forensic.py [options]

Options:
  -o, --output FILE    Memory dump output path (default: memory_dumps/memdump.lime)
  -y, --yara DIR       Custom YARA rules directory (default: yara_rules/)
  -v, --verbose        Show detailed analysis progress



