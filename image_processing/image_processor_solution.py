# -*- coding: UTF-8 -*-

from PIL import Image

# 画像を開く
name = "images/pyladies-tokyo.png"
img = Image.open(name)


#################################
#
# 画像の色彩を変更する (白黒グレー)
#
#################################

# カラフルな画像をグレーに変換して保存してみましょう
gray_img = img.convert('L')
gray_img.save('images/pyladies-tokyo-gray.png')

# カラフルな画像を白黒に変換して保存してみましょう
bw_img = img.convert('1')
bw_img.save('images/pyladies-tokyo-bw.png')


#################################
#
# 画像の色彩を変更する (RGB)
#
#################################

# 画像の色味を青系に変換してみましょう
r, g, b = img.split()
blue_img = Image.merge("RGB", (b, g, r))
blue_img.save('images/pyladies-tokyo-blue.png')

# 画像の色味を緑系に変換してみましょう
r, g, b = img.split()
green_img = Image.merge("RGB", (g, r, b))
green_img.save('images/pyladies-tokyo-green.png')
