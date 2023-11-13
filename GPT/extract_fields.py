import json

# 设置环境变量
import requests

api_key = 'your gpt key'
# 设置请求头
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}

# API端点
url = 'https://api.openai.com/v1/chat/completions'
# 设置代理
proxies = {
    'http': "http://127.0.0.1:7890",
    'https': "http://127.0.0.1:7890"
}
# 请求数据

prompt = ''' Extract field and length information from the ASCII chart below
    0                   1                   2                   3
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |     Type      |     Code      |          Checksum             |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |           Identifier          |        Sequence Number        |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |     Data ...
   +-+-+-+-+-
expected answer format: Type: 1 byte; Code:1 byte
don't contain other words
'''

data = {
    'model': 'gpt-3.5-turbo',
    'messages': [{"role": "system",
                  "content": "You are an assistant with a good understanding of ICMP-related protocol knowledge."},
                 {'role': 'user', 'content': prompt}],
    'temperature': 0.7
}

# 发送POST请求
response = requests.post(url, headers=headers, json=data, proxies=proxies)

# 获取JSON响应内容
json_response = response.json()

# 保存JSON到文件
with open('extract_fields.json', 'w') as json_file:
    json.dump(json_response, json_file, indent=2)

# 打印成功消息
print("JSON response saved to 'extract_fields.json'.")
