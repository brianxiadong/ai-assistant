
import os
import re

#遍历文件夹中所有的html文件
def get_html_file(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".html"):
                #获取file完整路径
                modify_html(os.path.join(root, file))


def modify_html(file):
    #删除html中id为main的style="display:none"属性
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        content = re.sub(r'id="main" style="display:none"', 'id="main" ', content)
        content = re.sub(r'id="doc"', 'id="doc" style="display:none" ', content)

        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

if __name__ == '__main__':
    get_html_file('C:/Users/xiadong/Desktop/100037301 DDD实战课')
