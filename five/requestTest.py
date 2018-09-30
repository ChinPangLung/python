import requests

r = requests.get('https://www.douban.com/')
print(r.status_code)
# print(r.text)

r1 = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
print(r1.url)
print(r1.encoding)
# print(r1.text)
print(r1.content)  # 获取到的是bytes对象

# 如果传输json数据
rjson = requests.get(
    'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
json = rjson.json()
print(json)

# 传入header 传入dict作为header参数
r_header = requests.get('https://www.douban.com/',
                        headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
# print(r_header.text)

# 发送post
post_url = requests.post('https://accounts.douban.com/login',
                     data={'form_email': 'abc@example.com', 'form_password': '123456'})
# print(post_url.json())

#post 如果要传递JSON数据
post_url_json = requests.post('https://accounts.douban.com/login',
                     json={'form_email': 'abc@example.com', 'form_password': '123456'})

