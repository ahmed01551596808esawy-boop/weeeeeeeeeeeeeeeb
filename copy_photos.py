import shutil
import os

src_dir = r"c:\Users\ELMOKHTAR\Desktop\Desktop"
dst_dir = r"c:\Users\ELMOKHTAR\Desktop\Desktop\rahma_website\images"

files_map = {
    "ChatGPT Image Jul 23, 2026, 03_12_02 P.png": "photo1.png",
    "WhatsApp Image 2026-04-18 at 7.39.31 PM.jpeg": "photo2.jpg",
    "WhatsApp Image 2026-05-25 at 12.57.36 PM.jpeg": "photo3.jpg",
    "WhatsApp Image 2026-06-20 at 3.57.28 PM (1).jpeg": "photo4.jpg",
    "WhatsApp Image 2026-06-20 at 3.57.28 PM.jpeg": "photo5.jpg"
}

for src_name, dst_name in files_map.items():
    src_path = os.path.join(src_dir, src_name)
    dst_path = os.path.join(dst_dir, dst_name)
    if os.path.exists(src_path):
        shutil.copy(src_path, dst_path)
        print(f"Copied {src_name} -> {dst_name}")
    else:
        print(f"File not found: {src_name}")
