import yaml
import csv

with open('depression.yml', 'r') as f:
    doc = yaml.safe_load(f)

with open('depression.tsv', 'wt', newline='') as out_file:
	tsv_writer = csv.writer(out_file, delimiter='\t')
	tsv_writer.writerow(['question', 'answer'])
	for c in doc["conversations"]:
		q = c[0]
		for a in c[1:]:
			tsv_writer.writerow([q, a])
