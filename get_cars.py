import requests
from lxml import etree
import os
url = 'http://www.netbian.com/qiche/'
resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'})
resp.encoding = 'gbk'
print(resp.text)

xp = etree.HTML(resp.text)
img_urls = xp.xpath('//ul/li/a/img/@src')
img_names = xp.xpath('//ul/li/a/img/@alt')
# 获取当前工作目录
current_path = os.getcwd()

# 拼接目标文件夹路径
target_folder = os.path.join(current_path, 'download', 'img_f')

# 如果目标文件夹不存在，则创建
if not os.path.exists(target_folder):
    os.makedirs(target_folder)
for u, n in zip(img_urls, img_names):
    print(f'正在下载:图片名：{n}')
    # 拼接目标文件路径
    target_file = os.path.join(target_folder, f'{n}.jpg')

    img_resp = requests.get(u, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'})
    with open(target_file, 'wb') as f:
        f.write(img_resp.content)

