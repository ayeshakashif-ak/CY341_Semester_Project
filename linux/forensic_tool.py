
#!/usr/bin/env python3

import os
import sys
import subprocess
import argparse
from datetime import datetime
import platform
import hashlib

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

BANNER = f"""{Colors.OKGREEN}{Colors.BOLD}
  _____ _       _______  ____________ ___      ___
 / ____|  |   /  ____  \ ____   ____|   |    |  |>
| (___ |  |   | |    | |    |  |    |   |____|  |>|>|>|>|>
 \___ \|  |   | |    | |>|> |  |    |    ____   |>|>
 ____) |  |___| |____| |>   |  |    |   |    |  |>|>|>
|_____/|______|\_______/    |__|    |___|    |__|>|>|>|>|>|>
{Colors.ENDC}
{Colors.OKBLUE}Automated Live Memory Forensic Tool{Colors.ENDC}
{Colors.WARNING}LiME + Volatility + YARA Integration{Colors.ENDC}
"""

def display_banner():
    print(BANNER)
    print(f"{Colors.HEADER}[*] Date: {datetime.now()}")
    print(f"[*] System: {platform.system()} {platform.release()}{Colors.ENDC}\n")

def check_root():
    if os.geteuid() != 0:
        print(f"{Colors.FAIL}[!] Requires root privileges.{Colors.ENDC}")
        sys.exit(1)

def verify_tool(path, name):
    if not os.path.isfile(path):
        print(f"{Colors.FAIL}[!] Missing {name}: {path}{Colors.ENDC}")
        sys.exit(1)

def setup_dirs():
    for d in ["memory_dumps", "reports", "volatility_results"]:
        os.makedirs(d, exist_ok=True)

def hash_file(path):
    sha256 = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

def capture_memory(output_file="memory_dumps/memdump.lime"):
    print(f"{Colors.OKGREEN}[*] Capturing memory...{Colors.ENDC}")
    module_path = "tools/lime/src/lime.ko"
    verify_tool(module_path, "LiME kernel module")

    try:
        # Unload if already loaded
        subprocess.run(["rmmod", "lime"], stderr=subprocess.DEVNULL)
# Insert LiME with parameters
        subprocess.run(["insmod", module_path, f"path={output_file}", "format=lime"], check=True)
        if os.path.exists(output_file):
            size_mb = os.path.getsize(output_file) / (1024 * 1024)
            sha = hash_file(output_file)
            print(f"{Colors.OKGREEN}[+] Memory captured: {output_file} ({size_mb:.2f} MB){Colors.ENDC}")
            print(f"{Colors.OKBLUE}[+] SHA-256: {sha}{Colors.ENDC}")
            return output_file
        else:
            raise FileNotFoundError("Memory dump not created.")
    except Exception as e:
        print(f"{Colors.FAIL}[!] Memory capture failed: {e}{Colors.ENDC}")
        sys.exit(1)

def detect_profile(vol_path, memory_file):
    try:
        output = subprocess.check_output([
            "python3", vol_path, "-f", memory_file, "linux_banner"
        ]).decode(errors="ignore")
        if "Linux version" in output:
            print(f"{Colors.OKGREEN}[+] Profile detected: Linux{Colors.ENDC}")
            return "Linux"
    except Exception as e:
        print(f"{Colors.WARNING}[!] Could not detect profile: {e}{Colors.ENDC}")
    return "Linux"

def run_volatility(memory_file):
    print(f"\n{Colors.OKGREEN}[*] Running Volatility plugins...{Colors.ENDC}")
    vol_path = "tools/volatility/vol.py"
    verify_tool(vol_path, "Volatility")

    profile = detect_profile(vol_path, memory_file)
    commands = [
        ("pslist", "Running processes"),
        ("pstree", "Process tree"),
        ("netscan", "Network connections"),
        ("linux_check_modules", "Kernel modules"),
        ("linux_check_tty", "TTY devices"),
        ("linux_malfind", "Injected code"),
    ]

    results = {}
    for cmd, desc in commands:
        print(f"{Colors.OKBLUE}[>] {cmd}: {desc}{Colors.ENDC}")
        output_file = f"volatility_results/{cmd}.txt"
        try:
            with open(output_file, "w") as f:
                subprocess.run([
                    "python3", vol_path, "-f", memory_file,
                    "--profile", profile, cmd
                ], stdout=f, stderr=subprocess.PIPE, check=True)
            with open(output_file, "r") as f:
                results[cmd] = f.read()
            print(f"{Colors.OKGREEN}[+] {cmd} completed.{Colors.ENDC}")
        except subprocess.CalledProcessError as e:
            error_msg = e.stderr.decode(errors="ignore")
            print(f"{Colors.WARNING}[!] {cmd} failed: {error_msg[:200]}...{Colors.ENDC}")
            results[cmd] = f"Error: {error_msg.strip()}"
    return results

def run_yara(memory_file, rules_dir="yara_rules"):
    print(f"\n{Colors.OKGREEN}[*] Scanning with YARA...{Colors.ENDC}")
    vol_path = "tools/volatility/vol.py"
    verify_tool(vol_path, "Volatility")

    if not os.path.isdir(rules_dir):
        print(f"{Colors.WARNING}[!] No YARA rules directory found: {rules_dir}{Colors.ENDC}")
        return None

    rule_files = [
        os.path.join(rules_dir, f)
        for f in os.listdir(rules_dir)
        if f.endswith(('.yar', '.yara'))
    ]

    if not rule_files:
        print(f"{Colors.WARNING}[!] No YARA rule files found in {rules_dir}{Colors.ENDC}")
        return None

    try:
        output_file = "volatility_results/yara_scan.txt"
        subprocess.run([
            "python3", vol_path, "-f", memory_file,
            "--profile", "Linux", "yarascan",
            "-y", ",".join(rule_files)
        ], stdout=open(output_file, "w"), check=True)

        with open(output_file, "r") as f:
            result = f.read()
        print(f"{Colors.OKGREEN}[+] YARA scan complete.{Colors.ENDC}")
        return result
    except subprocess.CalledProcessError as e:
        print(f"{Colors.FAIL}[!] YARA scan failed: {e.stderr.decode(errors='ignore')}{Colors.ENDC}")
        return None

def generate_report(results, yara, memory_file):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    html_path = f"reports/report_{timestamp}.html"
    txt_path = f"reports/report_{timestamp}.txt"

    with open(html_path, "w") as f:
        f.write(f"<h1>Memory Report - {timestamp}</h1>\n")
        f.write(f"<p><strong>Memory File:</strong> {memory_file}</p>\n")
        for cmd, output in results.items():
            f.write(f"<h2>{cmd}</h2><pre>{output}</pre>\n")
        if yara:
            f.write(f"<h2>YARA Results</h2><pre>{yara}</pre>\n")

    with open(txt_path, "w") as f:
        f.write(f"Memory Report - {timestamp}\n")
        f.write("=" * 60 + "\n")
        for cmd, output in results.items():
            f.write(f"\n[{cmd}]\n{output}\n")
        if yara:
            f.write(f"\n[YARA]\n{yara}\n")

    print(f"{Colors.OKGREEN}[+] Reports written successfully:{Colors.ENDC}")
    print(f"{Colors.OKBLUE} - {html_path}\n - {txt_path}{Colors.ENDC}")

def main():
    parser = argparse.ArgumentParser(description="Automated Memory Forensics Tool (LiME + Volatility + YARA)")
    parser.add_argument("-o", "--output", default="memory_dumps/memdump.lime", help="Output memory file path")
    parser.add_argument("-y", "--yara", default="yara_rules", help="Directory with YARA rule files")
    args = parser.parse_args()

    display_banner()
    check_root()
    setup_dirs()

    mem_file = capture_memory(args.output)
    results = run_volatility(mem_file)
    yara_out = run_yara(mem_file, args.yara)
    generate_report(results, yara_out, mem_file)

    print(f"{Colors.OKGREEN}{Colors.BOLD}[+] Memory analysis complete. Stay paranoid.{Colors.ENDC}")

if __name__ == "__main__":
    main()
