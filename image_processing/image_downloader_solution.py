# -*- coding: utf-8 -*-

import requests

# 画像のURLを指定する
url = "http://****.jpg"

# 画像をゲットする
response = requests.get(url)

# ゲットした画像をファイルに保存する
fout = open("images/profile.jpg", 'wb')
fout.write(response.content)
fout.close()
