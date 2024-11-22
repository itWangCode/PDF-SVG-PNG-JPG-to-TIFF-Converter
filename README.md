# PDF/SVG/PNG/JPG to TIFF Converter

## 项目简介

这是一个 Python 脚本工具，用于递归处理指定目录下的 **PDF**、**SVG**、**PNG** 和 **JPG** 文件，将它们转换为 **TIFF** 格式的彩色图像，并将生成的 TIFF 文件存储在每个目录下的 `tiff` 文件夹中。

脚本支持用户输入自定义分辨率（DPI），默认值为 **300 DPI**，并会自动删除生成的空 `tiff` 文件夹。

------

## 功能特性

- **支持的文件类型**：
  - **PDF**：通过 Ghostscript 转换为彩色 TIFF。
  - **SVG**：通过 CairoSVG 转换为彩色 TIFF。
  - **PNG/JPG**：通过 Pillow 转换为彩色 TIFF。
- **递归处理**：遍历用户指定目录及其所有子目录，找到支持的文件类型并进行处理。
- **按需创建文件夹**：仅在需要时创建 `tiff` 文件夹，自动清理空的 `tiff` 文件夹。
- **分辨率可控**：用户可通过输入指定分辨率（DPI 值）。

------

## 环境要求

### Python 版本

- **Python 3.7** 或更高版本

### 必要的依赖库

使用以下命令安装依赖：

```
bash


Copy code
pip install pillow cairosvg
```

### 依赖工具

1. **Ghostscript**（用于 PDF 转 TIFF）：

   - macOS

     ：

     ```
     bash
     
     
     Copy code
     brew install ghostscript
     ```

   - Ubuntu/Linux

     ：

     ```
     bash
     
     
     Copy code
     sudo apt install ghostscript
     ```

   - **Windows**： [下载 Ghostscript](https://ghostscript.com/) 并安装。

2. **CairoSVG**（用于 SVG 转 TIFF）：

   - 脚本中自动调用 CairoSVG，无需额外安装工具。

------

## 使用方法

### 运行脚本

1. 将脚本保存为 `convert_to_tiff.py`。

2. 打开终端或命令行，运行以下命

   ```
   
   python convert_to_tiff.py







本工具是一个 Python 脚本，用于批量将指定目录及其子目录中的以下类型文件转换为彩色的 TIFF 格式文件：

- **PDF 文件**
- **SVG 文件**
- **PNG 文件**
- **JPG/JPEG 文件**

转换后的文件将自动存储在每个目录的 `tiff` 文件夹中。如果某个目录的 `tiff` 文件夹为空，会自动删除该文件夹。

用户可以指定处理目录以及输出 TIFF 文件的分辨率（默认 300 DPI）。

------

## 功能特点

1. **支持的格式**：
   - PDF → TIFF
   - SVG → TIFF
   - PNG → TIFF
   - JPG/JPEG → TIFF
2. **递归处理**：
   - 会自动遍历所有子目录并处理其中的文件。
3. **高质量输出**：
   - 所有生成的 TIFF 文件均为彩色，默认使用 LZW 压缩，分辨率为 300 DPI（可自定义）。
4. **自动清理**：
   - 如果某个目录下的 `tiff` 文件夹为空（无有效输出），会自动删除该文件夹。

------

## 安装依赖

在运行脚本之前，请确保安装了以下依赖项：

1. **Python 版本**：需要 Python 3.6 或更高版本。

2. 必要库

   ： 使用 

   ```
   pip
   ```

    安装以下库：

   ```
   
   pip install pillow cairosvg
   ```

3. Ghostscript

   ： 确保 Ghostscript 已安装，用于 PDF 转换：

   - macOS:

     ```
     
     brew install ghostscript
     ```

   - Ubuntu:

     ```
     
     sudo apt install ghostscript
     ```

   - Windows: 从 [Ghostscript 官方网站](https://ghostscript.com/) 下载并安装。

验证 Ghostscript 是否可用：

```

gs --version
```

------

## 使用方法

1. 将代码保存为 `convert_to_tiff.py` 文件。

2. 打开终端或命令提示符，运行以下命令：

   ```
   
   python convert_to_tiff.py
   ```

3. 按提示输入处理的目录路径和 DPI 值（可选）。

### 示例运行

#### 输入：

```

请输入要处理的目录路径: /Users/username/Documents/my_folder
请输入 DPI 值（默认 300）: 400
```

#### 输出：

```

成功将 PDF /Users/username/Documents/my_folder/file1.pdf 转换为 /Users/username/Documents/my_folder/tiff/file1.tiff
成功将 SVG /Users/username/Documents/my_folder/diagram.svg 转换为 /Users/username/Documents/my_folder/tiff/diagram.tiff
成功将 PNG /Users/username/Documents/my_folder/image.png 转换为 /Users/username/Documents/my_folder/tiff/image.tiff
成功将 JPG /Users/username/Documents/my_folder/photo.jpg 转换为 /Users/username/Documents/my_folder/tiff/photo.tiff
删除空文件夹: /Users
```
