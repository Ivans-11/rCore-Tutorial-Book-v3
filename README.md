# rCore-Tutorial-Book-v3
Documentation of rCore-Tutorial version 3 in Chinese.

## Convert to Markdown

1. Prepare the requirements (It is recommended to use a virtual environment)

```sh
pip install sphinx-markdown-builder sphinx-comments sphinxcontrib-mermaid
```

2. Clone the repository

```sh
git clone --recurse-submodules https://github.com/Ivans-11/rCore-Tutorial-Book-v3.git
cd rCore-Tutorial-Book-v3
```

3. Build and Post-process

```sh
sphinx-build -b markdown source build
python post-process.py
```

4. The generated markdown files are in the `build` directory.
