import subprocess

print("")
print("Cleaning the database...")
subprocess.run(["python", "wipe.py"])

print("")
print("Fetching Reddit posts...")
subprocess.run(["python", "fetch_reddit.py"])

print("")
print("Performing Sentiment Analysis...")
subprocess.run(["python", "analyze.py"])

print("")
print("KPI for the data...")
subprocess.run(["python", "senti_count.py"])

print("")
print("Visualization...")
subprocess.run(["python", "visuals.py"])

print("")
print("All tasks completed!")
print("")
