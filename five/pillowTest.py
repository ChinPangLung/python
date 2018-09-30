from PIL import Image, ImageFilter

# 打开一个png图片
image_open = Image.open('image.png')
# 获取图片的尺寸
w, h = image_open.size
print('image size is:w:%s h:%s' % (w, h))
# 缩放50%
thumbnail = image_open.thumbnail((w // 2, h // 2))
print('resize image to: w=%s h=%s' % (w // 2, h // 2))
# 保存缩放的图片
image_open.save('thumbnail.png', 'png')

# 模糊图片
im = Image.open('thumbnail.png')
im_filter = im.filter(ImageFilter.BLUR)
im_filter.save('blur.png', 'png')

# 生成字母验证码图片
from PIL import ImageDraw, ImageFont
import random


# 随机字母
def rndChar():
    return chr(random.randint(65, 90))


# 随机颜色
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


# 随机颜色2
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


# 240*60
height = 60
width = 60 * 4
image_new = Image.new('RGB', (width, height), (255, 255, 255))
# 创建font对象
font = ImageFont.truetype('Arial.ttf', 36)
# 创建Draw对象
draw = ImageDraw.Draw(image_new)
# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊图片
new_filter = image_new.filter(ImageFilter.BLUR)
image_new.save('code.png', 'png')
new_filter.save('codefilter.jpg', 'jpeg')
# new_filter.show()
