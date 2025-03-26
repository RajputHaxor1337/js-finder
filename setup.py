import subprocess
import sys
import os

# Function to create and activate a virtual environment
def setup_virtualenv():
    env_name = "myenv"
    if not os.path.exists(env_name):
        print(f"[+] Creating virtual environment: {env_name}...")
        subprocess.check_call([sys.executable, "-m", "venv", env_name])
    else:
        print(f"[✔] Virtual environment '{env_name}' already exists.")
    
    activate_script = os.path.join(env_name, "Scripts" if os.name == "nt" else "bin", "activate")
    print(f"[+] To activate the virtual environment, run: source {activate_script}")
    return env_name

# Function to install a package
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def main():
    env_name = setup_virtualenv()
    required_packages = [
        "requests",
        "cloudscraper",
        "beautifulsoup4",
        "urllib3"
    ]
    
    print("[+] Installing required Python packages...")
    for package in required_packages:
        try:
            print(f"[*] Installing {package}...")
            install(package)
            print(f"[✔] {package} installed successfully.")
        except Exception as e:
            print(f"[!] Failed to install {package}: {e}")
    
    print("[✅] All required packages are installed!")
    print(f"[+] To activate your environment, run: source {env_name}/bin/activate (Linux/macOS) or {env_name}\\Scripts\\activate (Windows)")

if __name__ == "__main__":
    main()
