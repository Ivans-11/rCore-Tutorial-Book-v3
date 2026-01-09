#!/usr/bin/env python3
import re
import shutil
from pathlib import Path

BUILD_DIR = Path("build/md")
SOURCE_DIR = Path("source")

IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}

IMG_PATTERN = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')

def process_markdown(md_file: Path):
    text = md_file.read_text(encoding="utf-8")
    changed = False

    def replacer(match):
        nonlocal changed
        alt_text, img_path_str = match.groups()
        img_path_str = img_path_str.strip()

        if "://" in img_path_str:
            return match.group(0)

        img_path = Path(img_path_str)

        if img_path.suffix.lower() not in IMAGE_EXTS:
            return match.group(0)

        src_img = (SOURCE_DIR / img_path).resolve()

        if not src_img.exists():
            print(f"[WARN] Image not found: {src_img}")
            return match.group(0)

        dst_img = md_file.parent / src_img.name

        if not dst_img.exists():
            shutil.copy2(src_img, dst_img)
            print(f"[COPY] {src_img} -> {dst_img}")

        changed = True
        return f"![{alt_text}](./{dst_img.name})"

    new_text = IMG_PATTERN.sub(replacer, text)

    if changed:
        md_file.write_text(new_text, encoding="utf-8")
        print(f"[UPDATE] {md_file}")


def main():
    md_files = list(BUILD_DIR.rglob("*.md"))
    print(f"Found {len(md_files)} Markdown files")

    for md in md_files:
        process_markdown(md)

if __name__ == "__main__":
    main()
