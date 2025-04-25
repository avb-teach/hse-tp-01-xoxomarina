import os
import sys
import shutil
from collections import defaultdict

def flatten_copy(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    name_counter = defaultdict(int)

    for root, _, files in os.walk(input_dir):
        for filename in files:
            original_path = os.path.join(root, filename)
            target_path = os.path.join(output_dir, filename)

            if os.path.exists(target_path):
                name_counter[filename] += 1
                name, ext = os.path.splitext(filename)
                new_name = f"{name}{name_counter[filename]}{ext}"
                target_path = os.path.join(output_dir, new_name)
            else:
                name_counter[filename] = 1

            shutil.copy2(original_path, target_path)

def main():
    if len(sys.argv) < 3:
        print("Usage: collect_files.py input_dir output_dir")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    flatten_copy(input_dir, output_dir)

if __name__ == "__main__":
    main()
