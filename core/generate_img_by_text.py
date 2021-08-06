# coding=utf-8
from PIL import Image, ImageDraw, ImageFont


# 中文乱码问题  首先找一个中文字体   其次 unicode

# 读取图片
# 读取图片像素点颜色并保存
# 根据文件生成文字图片(每个像素点的颜色和上面截取的颜色一致)
def make_img(text, new_path="../resource/img/img_by_text.png", background_path="../resource/img/background.img",
             font_path="../resource/font/new_leaf_psychic_fonts.otf"):
    # 读取图片
    background = Image.open(background_path)  # type: Image.Image
    b_w, b_h = background.size

    # find font
    font = ImageFont.truetype(font_path, 14)
    f_w, f_h = font.getsize(text[0])
    # new black image which size is equal background image
    # img_out = Image.new('RGB', (b_w, b_h), 'black')
    img_out = Image.new('RGB', (b_w, b_h), (0, 0, 0))

    draw = ImageDraw.Draw(img_out)
    colors = []
    # get color

    for i in range(0, b_h, f_h):
        color = []
        for j in range(1, b_w, f_w):
            pixel = background.getpixel((j, i))
            color.append((pixel[0], pixel[1], pixel[2]))
        colors.append(color)

    for i in range(0, b_h, f_h):
        k = 0
        for j in range(1, b_w, f_w):
            draw.text([j, i], text[k], colors[i // f_h][j // f_w], font)  # 画在哪里, 画什么, 颜色, 字体
            k += 1
            k %= len(text)
    img_out.save(new_path)


if __name__ == "__main__":
    make_img(text=u"超级超级稀罕你的图图", background_path="../resource/img/logo.img",
             new_path="../resource/img/BJT.png",
             font_path="../resource/font/sim_sun.ttf")
    make_img(text=unicode("哇哦 是王一博啊!!!!!!!", "utf-8"), background_path="../resource/img/background.img",
             new_path="../resource/img/wyb.png")
