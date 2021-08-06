# coding=utf-8
import qrcode
from PIL import Image


def make_qrcode(data, new_path, logo_path='', background_path=''):
    qr = qrcode.QRCode(
        version=2,  # version:(值从 1-40, 最小的是1，用21 x 21像素表示)， 填None 的话电脑会给你设置一个合适的像素
        # error_correction:ERROR_CORRECT_L/ERROR_CORRECT_M/ERROR_CORRECT_Q/ERROR_CORRECT_H，7%/15%/25%/30%的容错率，一般设置7%就行了
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,  # box_size:设置每个方块二维码的像素
        border=2  # border:设置二维码的边界
    )
    qr.make()
    qr.add_data(data)
    img = qr.make_image(fill_color="#000", back_color="#FFF")  # RGB的方式指定颜色 必须带参数 否则logo是黑白的
    if not bool(logo_path) and not bool(background_path):
        img.save(new_path)
        return
    w, h = img.size
    if bool(logo_path):
        logo = Image.open(logo_path)  # type: Image.Image
        logo_w, logo_h = logo.size
        factor = 4
        s_w, s_h = w / factor, h / factor
        if logo_w > s_w or logo_h > s_h:
            logo_w = s_w
            logo_h = s_h
        logo = logo.resize((logo_w, logo_h), Image.ANTIALIAS).convert("RGBA")
        l_w = int((w - logo_w) / 2)  # logo 位置
        l_h = int((h - logo_h) / 2)
        # img.paste(img, (l_w, l_h), logo)
        img.paste(logo, (l_w, l_h), logo)
        if not bool(background_path):
            img.save(new_path)
            return
    img = img.convert("RGBA")  # 转换很重要
    background = Image.open(background_path)  # type: Image.Image
    background = background.resize((w, h), Image.ANTIALIAS).convert("RGBA")
    img = Image.blend(img, background, 0.6)
    img.save(new_path)


if __name__ == '__main__':
    path = '../resource/img/'
    make_qrcode('surprise', path + 'qrcode.img')
    make_qrcode('surprise', path + 'qrcode_logo.img', logo_path=path + "logo.img")
    make_qrcode('surprise', path + 'qrcode_background.png', background_path=path + "background.img")  # 生成的新图片后缀得是png
    make_qrcode('surprise', path + 'qrcode_logo_background.png', path + "logo.img", path + "background.img")
