import re
with open('/home/eshwar/code/response/research/execution_status/s2/hn/HN01_not_started_in_progress.md', 'r') as f:
    c = f.read()
blocks = re.split(r'#{3,4} HN', c)
for block in blocks[1:]:
    st_match = re.search(r'\*\*(?:Execution Status|Parent state):\*\*\s*(Not Started|In Progress|Completed)', block)
    utt_match = re.search(r'>\s*(.*?)\n', block)
    if st_match and utt_match:
        print(st_match.group(1), "||", utt_match.group(1))
