# base64是一种用64个字符表示的任意二进制数据的方法

import base64

encode = base64.b64encode(b'binary\x00string')
print(encode)
decode = base64.b64decode(encode)
print(decode)
print(base64.b64encode(b'BC'))

#url safe bases64
b_encode = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(b_encode)
urlsafe_b_encode = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(urlsafe_b_encode)
b_url_decode = base64.urlsafe_b64decode(urlsafe_b_encode)
print(b_url_decode)


