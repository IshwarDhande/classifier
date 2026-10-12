import create_exec_s2_s3b_v2 as c
import glob
for f in sorted(glob.glob('/home/eshwar/code/response/research/execution_status/s2/**/*.md', recursive=True)):
    recs = c.process_file(f, '2')
    print(f"{f}: {len(recs)}")
