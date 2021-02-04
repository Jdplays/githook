import subprocess
import os

print("Starting auto-pull...")
os.chdir("/home/[username]]/[path]]/[repo]")
subprocess.run(["git", "pull"])
print("Done!")
