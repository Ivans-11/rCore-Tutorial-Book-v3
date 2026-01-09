# rCore-Tutorial-Book-v3 Markdown 转换

## 更改说明

1. Fork 自 [rCore-Tutorial-Book-v3](https://github.com/rcore-os/rCore-Tutorial-Book-v3)，在其基础上增加了对 Markdown 转换的支持。

2. 主要利用 `sphinx-markdown-builder` 工具进行转换。

3. 在 `source/conf.py` 中添加了 `transform_nodes` 函数，对生成的文档树进行处理，以解决部分节点无法正确转换的问题：

   - 将 `caption` 节点转换为普通段落（即代码块标题和图片注解等）
   - 将各种 `admonition` 节点转换为带标题的段落，保留原有内容结构（如错误、警告、提示等）
   - 将 `mermaid` 图表节点转换为代码块。

4. 增加了 `post-process.py` 脚本, 用于迁移 Markdown 中引用的图片资源。

## 转换步骤

1. 准备环境（建议使用虚拟环境）

```sh
pip install sphinx-markdown-builder sphinx-comments sphinxcontrib-mermaid
```

2. 克隆仓库

```sh
git clone --recurse-submodules https://github.com/Ivans-11/rCore-Tutorial-Book-v3.git
cd rCore-Tutorial-Book-v3
```

3. 转换并进行后处理

```sh
sphinx-build -b markdown source build/md
python post-process.py
```

4. 生成的 Markdown 文件位于 `build/md` 目录中。