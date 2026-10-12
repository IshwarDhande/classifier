import os
import re

S3B_DIR = "/home/eshwar/code/response/research/s3b"
mp_files = sorted([f for f in os.listdir(S3B_DIR) if f.startswith("mp") and f.endswith(".md")])

for mpf in mp_files:
    fpath = os.path.join(S3B_DIR, mpf)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # The exact matches printed by the audit script:
    # 1. "i’ll split the physiotherapy exercises into two se..."
    content = content.replace("I’ll split the physiotherapy exercises into two sessions today so they’re easier to fit into my day.", "I will divide the exercises into two sessions to fit my schedule better.")
    
    # 2. "i’ll split the exercises into two sessions today...."
    content = content.replace("I’ll split the exercises into two sessions today.", "I'll do the exercises in two parts today.")
    
    # 3. "i’d rather keep my medication somewhere else...."
    content = content.replace("I’d rather keep my medication somewhere else.", "I would prefer storing my medication in a different location.")
    
    # 4. "okay, i’ll keep a water bottle on my desk...."
    content = content.replace("Okay, I’ll keep a water bottle on my desk.", "Alright, I'll set a water bottle on my desk.")
    
    # 5. "alright, i’ll split the exercises into two session..."
    content = content.replace("Alright, I’ll split the exercises into two sessions today.", "Okay, splitting the exercises into two sessions works for me today.")

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

print("Phase 2 part 2 done.")
