import sys, subprocess
sys.stdout.reconfigure(encoding='utf-8')

GIT = r"C:\Program Files\Git\cmd\git.exe"
FOLDER = r"d:\Desktop\Visual Studio Code\Projects\Web_Development\architekt-staniszewski"

def run(args):
    r = subprocess.run([GIT] + args, cwd=FOLDER, capture_output=True, text=True, timeout=120)
    return r.returncode, r.stdout.strip(), r.stderr.strip()

# Stage
code, out, err = run(["add", "-A"])
print(f"[add] rc={code}")

# Status
code, out, err = run(["status", "--short"])
print(f"[status]\n{out}")

# Commit
code, out, err = run(["commit", "-m", "Definitive version: removed all GoDaddy branding, logos, tracking"])
print(f"\n[commit] rc={code}\n{out}")
if err: print(err)

# Push
code, out, err = run(["push", "origin", "main"])
print(f"\n[push] rc={code}\n{out}")
if err: print(err)
