import json

# Read the JSON file with UTF-8 encoding
with open('your_file.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Modify the value of the "Job-link" key
for item in data:
    job_link = item.get('Job-Link', '')
    if job_link and not job_link.startswith('https://'):
        item['Job-link'] = 'https://jobs.undp.org/' + job_link

# Write the modified JSON data back to the file
with open('your_file.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
