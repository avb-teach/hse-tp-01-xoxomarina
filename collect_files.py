import os
import shutil
import sys

def collect_files(input_dir, output_dir, max_depth=None):
    seen_files = {}

    for root, dirs, files in os.walk(input_dir):
        if max_depth is not None:
            rel_path = os.path.relpath(root, input_dir)
            depth = rel_path.count(os.sep)
            if depth >= max_depth:
                dirs[:] = []
                continue

        for file in files:
            input_path = os.path.join(root, file)
            if file not in seen_files:
                seen_files[file] = 0
                output_path = os.path.join(output_dir, file)
            else:
                seen_files[file] += 1
                name, ext = os.path.splitext(file)
                new_name = f"{name}_{seen_files[file]}{ext}"
                output_path = os.path.join(output_dir, new_name)

            shutil.copy2(input_path, output_path)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: collect_files.py <input_dir> <output_dir> [max_depth]")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    max_depth = int(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[3] else None

    collect_files(input_dir, output_dir, max_depth)
