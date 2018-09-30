# python提供的这个struct来解决bytes和其他二进制数据类型的转换
import struct

pack = struct.pack('>I', 10240099)
print(pack)
