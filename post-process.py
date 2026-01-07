#!/usr/bin/env python3
import re
import os
from pathlib import Path

BUILD_DIR = Path("build")
SOURCE_DIR = Path("source")

# Fix image paths in Markdown files
def fix_image_path(md_file: Path):
    text = md_file.read_text(encoding="utf-8")

    pattern = re.compile(r'(!\[.*?\]\()([^\)]+)(\))')

    def replacer(match):
        prefix, img_path_str, suffix = match.groups()
        img_path = Path(img_path_str)

        if img_path.is_absolute() or "://" in img_path_str:
            return match.group(0)

        original_path = SOURCE_DIR / img_path
        new_rel_path = os.path.relpath(original_path, start=md_file.parent)
        new_rel_path = new_rel_path.replace(os.sep, "/")

        return f"{prefix}{new_rel_path}{suffix}"

    new_text = pattern.sub(replacer, text)

    md_file.write_text(new_text, encoding="utf-8")
    print(f"[Fixed] {md_file}")

def fix_all_markdown(build_dir: Path):
    md_files = list(build_dir.rglob("*.md"))
    print(f"Found {len(md_files)} Markdown files.")
    for md_file in md_files:
        fix_image_path(md_file)

if __name__ == "__main__":
    fix_all_markdown(BUILD_DIR)
