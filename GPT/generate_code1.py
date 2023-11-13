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

prompt = ''' Fully understand the comments' content and complete the code to ensure that the following code is logical and correct as a whole. 
void fill_icmp_echo_receiver(Echo_or_Echo_Reply_Message_hdr *hdr,
                             uint16_t length, int type_value) {

  // Set code to 0

  // If code equals 0, an identifier may be zero to help match echos and
  // replies.

  // If code equals 0, a sequence number may be zero to help match echos and
  // replies.

  // 0 for echo reply message.

  // For computing the checksum, the checksum field should be zero


  // For computing the checksum, if the total length is odd, the received data
  // is padded with one octet of zeros


  // The checksum is the 16-bit one's complement of the one's complement sum of
  // the ICMP message starting with the ICMP Type

}

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
with open('generate_code1.json', 'w') as json_file:
    json.dump(json_response, json_file, indent=2)

# 打印成功消息
print("JSON response saved to 'generate_code1.json'.")
