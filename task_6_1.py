import re

result = []

with open('data/nginx_log.txt', 'r', encoding='utf-8') as logs:
    for line in logs:
        data = line.split()
        result.append((data[0], re.sub(r"[^A-Z]*", '', data[5]), data[6]))

print(result)
