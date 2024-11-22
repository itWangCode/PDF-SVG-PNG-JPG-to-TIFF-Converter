# import os
# from pdf2image import convert_from_path
# from PIL import Image
# import cairosvg
# import shutil  # 用于删除空文件夹
# import io
#
# def svg_to_tiff(svg_path, tiff_path, dpi=300):
#     """将 SVG 文件转换为 TIFF 文件，并设置 DPI"""
#     png_data = cairosvg.svg2png(url=svg_path, output_width=dpi * 8.27, output_height=dpi * 11.69)
#     with open(tiff_path, "wb") as tiff_file:
#         image = Image.open(io.BytesIO(png_data))
#         image.save(tiff_file, format="TIFF", dpi=(dpi, dpi))
#     print(f"成功将 {svg_path} 转换为 {tiff_path}")
#
# def png_to_tiff(png_path, tiff_path, dpi=300):
#     """将 PNG 文件转换为 TIFF 文件，并设置 DPI"""
#     with Image.open(png_path) as image:
#         image.save(tiff_path, format="TIFF", dpi=(dpi, dpi))
#     print(f"成功将 {png_path} 转换为 {tiff_path}")
#
# def pdf_to_tiff(pdf_path, tiff_folder, dpi=300):
#     """将 PDF 文件转换为 TIFF 文件，并设置 DPI"""
#     try:
#         pages = convert_from_path(pdf_path, dpi=dpi)  # 使用 pdf2image 转换
#         for page_number, page in enumerate(pages, start=1):
#             tiff_path = os.path.join(tiff_folder, f"{os.path.splitext(os.path.basename(pdf_path))[0]}_page{page_number}.tiff")
#             page.save(tiff_path, format="TIFF")
#             print(f"成功将 {pdf_path} 的第 {page_number} 页转换为 {tiff_path}")
#     except Exception as e:
#         print(f"处理 PDF 文件 {pdf_path} 时出错: {e}")
#
# def clean_empty_tiff_folders(folder_path):
#     """递归删除空的 TIFF 文件夹"""
#     for root, dirs, _ in os.walk(folder_path, topdown=False):
#         for dir_name in dirs:
#             dir_path = os.path.join(root, dir_name)
#             if dir_name == "tiff" and not os.listdir(dir_path):  # 检查是否为空
#                 shutil.rmtree(dir_path)
#                 print(f"删除空文件夹: {dir_path}")
#
# def process_folder_recursive(folder_path, dpi=300):
#     """递归处理文件夹中的 SVG、PNG 和 PDF 文件"""
#     for root, _, files in os.walk(folder_path):
#         # 仅在找到合适文件时创建 TIFF 文件夹
#         tiff_folder_created = False
#
#         for file in files:
#             file_path = os.path.join(root, file)
#             base_name, ext = os.path.splitext(file)
#
#             if ext.lower() in [".svg", ".png", ".pdf"]:
#                 if not tiff_folder_created:
#                     # 延迟创建 tiff 文件夹，仅在需要时创建
#                     tiff_folder = os.path.join(root, "tiff")
#                     os.makedirs(tiff_folder, exist_ok=True)
#                     tiff_folder_created = True
#
#                 try:
#                     if ext.lower() == ".svg":
#                         tiff_path = os.path.join(tiff_folder, f"{base_name}.tiff")
#                         svg_to_tiff(file_path, tiff_path, dpi)
#                     elif ext.lower() == ".png":
#                         tiff_path = os.path.join(tiff_folder, f"{base_name}.tiff")
#                         png_to_tiff(file_path, tiff_path, dpi)
#                     elif ext.lower() == ".pdf":
#                         pdf_to_tiff(file_path, tiff_folder, dpi)
#                 except Exception as e:
#                     print(f"错误处理文件 {file_path}: {e}")
#
#     # 清理空的 TIFF 文件夹
#     clean_empty_tiff_folders(folder_path)
#
# if __name__ == "__main__":
#     # 提示用户输入文件夹路径
#     folder = input("请输入文件夹路径: ").strip()
#     dpi = input("请输入 DPI 值（默认 300）: ").strip()
#     if dpi:
#         dpi = int(dpi)
#     else:
#         dpi = 300
#     if os.path.isdir(folder):
#         process_folder_recursive(folder, dpi)
#         print("所有文件已成功转换为 TIFF 文件！")
#     else:
#         print(f"路径 {folder} 无效，请输入有效的文件夹路径！")


# import os
# import subprocess
# import shutil
#
#
# def convert_pdf_to_tiff(pdf_path, tiff_folder):
#     """将 PDF 文件转换为彩色 TIFF 文件，并保存到指定的 tiff 文件夹中"""
#     try:
#         # 获取 PDF 文件的基础名称（不带扩展名）
#         base_name = os.path.splitext(os.path.basename(pdf_path))[0]
#         tiff_path = os.path.join(tiff_folder, f"{base_name}.tiff")
#
#         # 使用 Ghostscript 将 PDF 转换为彩色 TIFF
#         subprocess.run([
#             "gs", "-dBATCH", "-dNOPAUSE", "-sDEVICE=tiff24nc",  # 使用 tiff24nc 生成彩色 TIFF
#             "-r300", "-sCompression=lzw",  # LZW 压缩，分辨率 300 DPI
#             "-sOutputFile=" + tiff_path, pdf_path
#         ], check=True)
#
#         print(f"成功将 {pdf_path} 转换为 {tiff_path}")
#     except subprocess.CalledProcessError as e:
#         print(f"处理 PDF 文件 {pdf_path} 时出错: {e}")
#
#
# def clean_empty_tiff_folders(input_dir):
#     """递归删除空的 TIFF 文件夹"""
#     for root, dirs, _ in os.walk(input_dir, topdown=False):
#         for dir_name in dirs:
#             dir_path = os.path.join(root, dir_name)
#             if dir_name == "tiff" and not os.listdir(dir_path):  # 如果 tiff 文件夹为空
#                 shutil.rmtree(dir_path)
#                 print(f"删除空文件夹: {dir_path}")
#
#
# def process_directory_recursive(input_dir):
#     """递归处理目录中的 PDF 文件"""
#     for root, _, files in os.walk(input_dir):
#         # 在每个目录中创建 tiff 文件夹
#         tiff_folder = os.path.join(root, "tiff")
#         tiff_folder_created = False  # 标记是否创建了 tiff 文件夹
#
#         # 遍历文件，处理 PDF
#         for file in files:
#             if file.lower().endswith(".pdf"):
#                 if not tiff_folder_created:
#                     os.makedirs(tiff_folder, exist_ok=True)
#                     tiff_folder_created = True
#                 pdf_path = os.path.join(root, file)
#                 convert_pdf_to_tiff(pdf_path, tiff_folder)
#
#     # 清理空的 TIFF 文件夹
#     clean_empty_tiff_folders(input_dir)
#
#
# if __name__ == "__main__":
#     # 提示用户输入目录
#     input_dir = input("请输入要处理的目录路径: ").strip()
#
#     if os.path.isdir(input_dir):
#         process_directory_recursive(input_dir)
#         print("所有 PDF 文件已成功转换为彩色 TIFF 文件！")
#     else:
#         print(f"路径无效：{input_dir}")


'''
Created on 2024-11-22

@author: wangyang(<itwangyang@gmail.comL>)
批量处理 PDF、SVG、PNG 和 JPG 文件，将它们转换为彩色 TIFF 文件，并保存到指定的 tiff 文件夹中。
使用 Ghostscript 和 cairosvg 库进行转换。

使用方法：
1. 打开命令行窗口，切换到脚本所在目录。
2. 输入命令：python 批量处理tiff.py
3. 按照提示输入要处理的目录路径和 DPI 值（默认 300）。
4. 等待脚本处理完毕，所有文件将被转换为彩色 TIFF 文件并保存到 tiff 文件夹中。
5. 脚本会自动删除空的 tiff 文件夹。

注意：
1. 脚本依赖 Ghostscript 和 cairosvg 库，请先安装它们。
2. 脚本仅处理 PDF、SVG、PNG 和 JPG 文件，其他文件将被忽略。
'''

import os
import subprocess
import shutil
from PIL import Image
import cairosvg
import io  # 修复未定义的 io 模块问题


def convert_pdf_to_tiff(pdf_path, tiff_folder, dpi=300):
    """将 PDF 文件转换为彩色 TIFF 文件，并保存到指定的 tiff 文件夹中"""
    try:
        base_name = os.path.splitext(os.path.basename(pdf_path))[0]
        tiff_path = os.path.join(tiff_folder, f"{base_name}.tiff")

        subprocess.run([
            "gs", "-dBATCH", "-dNOPAUSE", "-sDEVICE=tiff24nc",
            f"-r{dpi}", "-sCompression=lzw",
            "-sOutputFile=" + tiff_path, pdf_path
        ], check=True)

        print(f"成功将 PDF {pdf_path} 转换为 {tiff_path}")
    except subprocess.CalledProcessError as e:
        print(f"处理 PDF 文件 {pdf_path} 时出错: {e}")


def convert_svg_to_tiff(svg_path, tiff_folder, dpi=300):
    """将 SVG 文件转换为彩色 TIFF 文件"""
    try:
        base_name = os.path.splitext(os.path.basename(svg_path))[0]
        tiff_path = os.path.join(tiff_folder, f"{base_name}.tiff")

        # 使用 cairosvg 将 SVG 转为 TIFF
        png_data = cairosvg.svg2png(url=svg_path, dpi=dpi)
        with open(tiff_path, "wb") as tiff_file:
            img = Image.open(io.BytesIO(png_data))
            img.save(tiff_file, format="TIFF", dpi=(dpi, dpi))

        print(f"成功将 SVG {svg_path} 转换为 {tiff_path}")
    except Exception as e:
        print(f"处理 SVG 文件 {svg_path} 时出错: {e}")


def convert_image_to_tiff(image_path, tiff_folder, dpi=300):
    """将 PNG 或 JPG 文件转换为彩色 TIFF 文件"""
    try:
        base_name = os.path.splitext(os.path.basename(image_path))[0]
        tiff_path = os.path.join(tiff_folder, f"{base_name}.tiff")

        with Image.open(image_path) as img:
            img.save(tiff_path, format="TIFF", dpi=(dpi, dpi))

        print(f"成功将 {image_path} 转换为 {tiff_path}")
    except Exception as e:
        print(f"处理图像文件 {image_path} 时出错: {e}")


def clean_empty_tiff_folders(input_dir):
    """递归删除空的 TIFF 文件夹"""
    for root, dirs, _ in os.walk(input_dir, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if dir_name == "tiff" and not os.listdir(dir_path):  # 如果 tiff 文件夹为空
                shutil.rmtree(dir_path)
                print(f"删除空文件夹: {dir_path}")


def process_directory_recursive(input_dir, dpi=300):
    """递归处理目录中的 PDF、SVG、PNG 和 JPG 文件"""
    for root, _, files in os.walk(input_dir):
        # 在每个目录中创建 tiff 文件夹
        tiff_folder = os.path.join(root, "tiff")
        tiff_folder_created = False  # 标记是否创建了 tiff 文件夹

        # 遍历文件，处理 PDF、SVG、PNG 和 JPG
        for file in files:
            file_path = os.path.join(root, file)
            if file.lower().endswith((".pdf", ".svg", ".png", ".jpg", ".jpeg")):
                if not tiff_folder_created:
                    os.makedirs(tiff_folder, exist_ok=True)
                    tiff_folder_created = True

                if file.lower().endswith(".pdf"):
                    convert_pdf_to_tiff(file_path, tiff_folder, dpi)
                elif file.lower().endswith(".svg"):
                    convert_svg_to_tiff(file_path, tiff_folder, dpi)
                elif file.lower().endswith((".png", ".jpg", ".jpeg")):
                    convert_image_to_tiff(file_path, tiff_folder, dpi)

    # 清理空的 TIFF 文件夹
    clean_empty_tiff_folders(input_dir)


if __name__ == "__main__":
    # 提示用户输入目录
    input_dir = input("请输入要处理的目录路径: ").strip()
    dpi_input = input("请输入 DPI 值（默认 300）: ").strip()

    try:
        dpi = int(dpi_input) if dpi_input else 300
    except ValueError:
        print("无效的 DPI 值，使用默认值 300")
        dpi = 300

    if os.path.isdir(input_dir):
        process_directory_recursive(input_dir, dpi)
        print("所有文件已成功转换为彩色 TIFF 文件！")
    else:
        print(f"路径无效：{input_dir}")

