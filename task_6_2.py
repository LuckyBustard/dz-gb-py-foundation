request_count = {}


def find_max(request_count):
    requests = 0
    source = ''
    for ip, count in request_count.items():
        if count > requests:
            source = ip
            requests = count
    return source, requests


with open('data/nginx_log.txt', 'r', encoding='utf-8') as logs:
    for line in logs:
        data = line.split()
        request_count[data[0]] = (request_count[data[0]] + 1) if data[0] in request_count else 1

print(find_max(request_count))
