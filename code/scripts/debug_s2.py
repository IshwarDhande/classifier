import re
with open('/home/eshwar/code/response/research/execution_status/s2/mp/MP01_not_started_in_progress.md', 'r') as f:
    c = f.read()
matches = re.findall(r'\*\*(Not Started|In Progress|Completed):\*\*\s*\n(?:>\s*)?[“"]?([^”"\n]+)[”"]?', c)
print(len(matches))
print(matches[:5])
