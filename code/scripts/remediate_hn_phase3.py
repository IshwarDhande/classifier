import os
import re

S3B_DIR = "/home/eshwar/code/response/research/s3b"
hn_files = sorted([f for f in os.listdir(S3B_DIR) if f.startswith("hn") and f.endswith(".md")])

replacements = {
    "You always come up with these ambitious habit changes, but for this one, sure, I’ll do the two short sessions today.": "You frequently suggest ambitious routine shifts, but in this specific instance, sure, I’ll split the exercises into two sessions today.",
    "I know it’s a sensible routine and I’m still thinking about fitness overall, but I really don’t want to leave my walking shoes by the door today.": "I realize having a routine is helpful and fitness matters to me, but I really don’t want to leave my walking shoes by the door today.",
    "That sounds like a fantastic strategy on paper, but realistically I’m still weighing whether I want a water bottle on my desk today.": "Your strategy makes a lot of sense in theory, though I'm still deciding if I'll actually keep a water bottle on my desk today.",
    "You always encourage me to be proactive about physiotherapy, and two sessions could work, but I’m going to think about it before committing.": "I appreciate your constant encouragement regarding my physical therapy, which is why I'm contemplating doing two sessions.",
    "I don’t normally keep drinks near my laptop, but I really like this plan and I’m putting the bottle on my desk now.": "Having drinks near my computer usually makes me nervous, but I'll make an exception and keep a water bottle on my desk today.",
    "That’s a creative way to build the habit, and I appreciate the thought, but drinking an extra glass whenever I make tea doesn’t work for me.": "I really admire how creative that habit-building approach is, yet I still decline to drink an extra glass with tea.",
    "I usually enjoy taking on new routines, but splitting my physiotherapy into two sessions is too disruptive; I’d rather do one session.": "While I'm typically open to embracing new habits, dividing my exercises into two separate sessions today feels like overkill.",
    "Okay, I’ll follow that schedule—actually, no, evenings don’t work for me; I’d rather take my medication on my own schedule.": "Sure, I can stick to that—wait, actually, taking medication in the evening is just too exhausting right now.",
    "I understand why you suggest it and I do want to stay hydrated, but tying the water to lunch doesn’t suit me, so I’ll skip that.": "I totally get the reasoning behind your suggestion and value hydration, yet I prefer not to tie it to lunch.",
    "I’ve never liked keeping pills by my bed, but alright, I’ll put the pillbox beside the clock.": "Normally I hate having pills anywhere near my sleep space, but fine, I'll place them next to the clock.",
    "I really dislike desk clutter, but okay, I’ll keep a water bottle there today.": "I absolutely detest having a cluttered workspace, however I will keep a bottle of water there.",
    "Sure, that sounds convenient—actually, no. Stop telling me how to organize my medication; I’m sick of these suggestions.": "Alright, that seems handy—wait, no it doesn't. Stop telling me how to organize my pills.",
    "I know you’re trying to help with hydration, but stop pushing drinking reminders; I don’t want to be micromanaged.": "I recognize your good intentions regarding my hydration, but please stop nagging me with these reminders.",
    "Stop assuming that’s the only option; it might work, but I’m still considering whether I want to keep the medication there.": "Don't act like that's my only choice; it could work, but I'll make up my own mind.",
    "Leave me out of your fitness programs; going for a walk is something I might do, but I haven’t decided yet.": "Keep your exercise programs to yourself; a walk is a possibility, but I'll do it my way."
}

for hnf in hn_files:
    fpath = os.path.join(S3B_DIR, hnf)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Apply all replacements if they exist in the file
    for old_text, new_text in replacements.items():
        content = content.replace(old_text, new_text)
        
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

print("Phase 3 (retry) applied to HN files.")
