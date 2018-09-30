#chardet 用来检测编码的,简单易用
import chardet

detect = chardet.detect(b'hello,world')
print(detect)

data='中文文字在这里，检测一下？'.encode('gbk')
chardet_detect = chardet.detect(data)
print(chardet_detect)
