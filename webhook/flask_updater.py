import subprocess

# Stop server service
subprocess.run(["service", "flask_wh", "stop"])
print("flask_wh Stopped")

# Pull the repo down
subprocess.run(["/home/[username]/[path]/venv/bin/python3",
                "/home/[username]]/[path]]/[repo]]/webhook/pull.py"])
print("Repo Pulled")

# Restart server service
subprocess.run(["service", "flask_wh", "start"])
print("flask_wh Started")
