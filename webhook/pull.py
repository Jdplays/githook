import subprocess
import os

print("Starting auto-pull...")
os.chdir("/home/[username]/[path]")
subprocess.run(["git", "pull"])
print("Done!")
