import os
import shutil
import sys

def collect_files(input_dir, output_dir, max_depth=None):
    seen_files = {}

    input_dir = os.path.abspath(input_dir)
    output_dir = os.path.abspath(output_dir)

    for root, dirs, files in os.walk(input_dir):
        rel_path = os.path.relpath(root, input_dir)
        depth = 0 if rel_path == '.' else rel_path.count(os.sep) + 1

        if max_depth is not None and depth > max_depth:
            dirs[:] = []
            continue

        for file in files:
            src_path = os.path.join(root, file)

            if max_depth is None:
                filename = file
                if filename not in seen_files:
                    seen_files[filename] = 0
                else:
                    seen_files[filename] += 1
                    name, ext = os.path.splitext(filename)
                    filename = f"{name}_{seen_files[filename]}{ext}"
                dest_path = os.path.join(output_dir, filename)
                os.makedirs(output_dir, exist_ok=True)
            else:
                dest_dir = os.path.join(output_dir, rel_path)
                os.makedirs(dest_dir, exist_ok=True)
                dest_path = os.path.join(dest_dir, file)

            shutil.copy2(src_path, dest_path)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: collect_files.py <input_dir> <output_dir> [max_depth]")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    max_depth = None

    if len(sys.argv) > 3:
        try:
            max_depth = int(sys.argv[3])
        except ValueError:
            print("max_depth must be an integer")
            sys.exit(1)

    collect_files(input_dir, output_dir, max_depth)
