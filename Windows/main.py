import os  # Import the os module
import subprocess
import platform
import json
import datetime

# Load Configuration
with open('config.json', 'r') as f:
    config = json.load(f)

def detect_os():
    os_type = platform.system()
    if os_type == "Windows":
        return "Windows"
    elif os_type == "Linux":
        return "Linux"
    else:
        return "Unsupported"

def timestamped_output_folder():
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    folder = os.path.join(config['output_dir'], f"dump_{now}")
    os.makedirs(folder, exist_ok=True)
    return folder

def dump_memory_windows(output_folder):
    print("[*] Dumping memory using WinPmem...")
    # Check the correct flag for output file for go-winpmem
    # Update the flag from "-o" to "--output" or another valid flag
    # If you're still unsure about the correct flag, run 'go-winpmem_amd64_1.0-rc1.exe --help' to confirm.
    dump_file = os.path.join(output_folder, "memory_dump.raw")
    subprocess.run([
    r'D:/memory_forensics/Tools/go-winpmem_amd64_1.0-rc1.exe',
    'acquire',
    dump_file
], check=True)


def run_volatility_analysis(dump_path, output_folder):
    print("[*] Running Volatility analysis...")
    
    # Specify the path to your Volatility 3 executable
    volatility_path = r'D:/volatility3'  # Update with your Volatility 3 path
    
    for plugin in config['volatility_plugins']:
        output_file = os.path.join(output_folder, f"{plugin}.txt")
        
        # Command for running Volatility 3 analysis
        cmd = [
            volatility_path,  # Full path to volatility3.exe
            '-f', dump_path,  # Path to the memory dump
            plugin            # Plugin to run
        ]
        
        # Run the subprocess and save the output to a file
        with open(output_file, "w") as f:
            subprocess.run(cmd, stdout=f)
        
        print(f"[+] {plugin} results saved.")

def run_yara_scan(target_path, output_folder):
    print("[*] Running YARA scan...")
    yara_rules_folder = config['yara_rules_folder']
    yara_output = os.path.join(output_folder, "yara_results.txt")
    
    # Ensure that 'yara' is available in your PATH or specify the full path to the executable
    cmd = ["yara", "-r", yara_rules_folder, target_path]
    
    with open(yara_output, "w") as f:
        subprocess.run(cmd, stdout=f)
    
    print(f"[+] YARA scan completed: {yara_output}")

def main():
    os_type = detect_os()
    output_folder = timestamped_output_folder()
    dump_path = os.path.join(output_folder, "memory_dump.raw")

    if os_type == "Windows":
        dump_memory_windows(output_folder)
    elif os_type == "Linux":
        print("[-] Linux memory dumping is not yet implemented for this project.")
        return
    else:
        print("[-] Unsupported OS. Exiting.")
        return

    run_volatility_analysis(dump_path, output_folder)
    run_yara_scan(dump_path, output_folder)
    print(f"[✓] All tasks completed. Results saved in {output_folder}")

if __name__ == "__main__":
    main()
