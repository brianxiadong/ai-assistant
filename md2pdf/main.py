import os
import re


def remove_html_tags(text):
    """使用正则表达式移除HTML标签"""
    clean = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    return re.sub(clean, '', text)

def convert_md_to_pdf(root_folder,output_path):
    """
    递归地遍历文件夹，将找到的所有Markdown文件转换为PDF。

    :param root_folder: 要开始搜索的根文件夹路径
    """
    count = 0
    dir = 1
    for foldername, subfolders, filenames in os.walk(root_folder):
        for filename in filenames:

            if filename.endswith('.md'):
                if count == 0:
                    path = output_path  + str(dir) + "/"
                    os.mkdir(path)
                    dir += 1

                # 构建完整的文件路径
                file_path = os.path.join(foldername, filename)

                # 输出PDF文件的路径
                txt_file = path + filename.rsplit('.', 1)[0] + '.txt'

                # 读取Markdown文件内容
                with open(file_path, 'r', encoding='utf-8') as file:
                    md_content = file.read()

                md_content = remove_html_tags(md_content)

                with open(txt_file, 'w', encoding='utf-8') as txt_file:
                    txt_file.write(md_content)
                # 使用pypandoc转换Markdown为PDF
                # converted_pdf = convert_text(md_content,format="markdown", to='txt', outputfile=pdf_file_path)
                #
                # print(f'Converted "{file_path}" to "{pdf_file_path}"')

                count += 1
                if count >= 250:
                    count = 0

if __name__ == '__main__':
    # 示例：从指定的文件夹开始转换
    root_directory = 'D:/教学/课程资料/面试题/'
    output_path = 'D:/教学/课程资料/面试题/txt/'
    convert_md_to_pdf(root_directory,output_path)
