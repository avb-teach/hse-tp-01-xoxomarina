import os
import shutil
import sys

def collect_files(input_dir, output_dir, max_depth=None):
    seen_files = {}  # Для отслеживания одинаковых имен файлов

    for root, dirs, files in os.walk(input_dir):
        rel_path = os.path.relpath(root, input_dir)
        depth = rel_path.count(os.sep)

        # Ограничиваем глубину обхода
        if max_depth is not None and depth >= max_depth:
            dirs[:] = []  # Не заходить глубже

        for file in files:
            input_path = os.path.join(root, file)

            # Определяем выходной путь
            if max_depth is None:
                output_path = os.path.join(output_dir, file)
            else:
                # Сохраняем структуру до max_depth
                truncated_rel_path = os.path.relpath(root, input_dir)
                output_subdir = os.path.join(output_dir, truncated_rel_path)
                os.makedirs(output_subdir, exist_ok=True)
                output_path = os.path.join(output_subdir, file)

            # Разруливаем одинаковые имена файлов только если нет структуры
            if max_depth is None:
                if file not in seen_files:
                    seen_files[file] = 0
                else:
                    seen_files[file] += 1
                    name, ext = os.path.splitext(file)
                    file = f"{name}_{seen_files[file]}{ext}"
                    output_path = os.path.join(output_dir, file)

            shutil.copy2(input_path, output_path)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: collect_files.py <input_dir> <output_dir> [max_depth]")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    max_depth = int(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[3] else None

    collect_files(input_dir, output_dir, max_depth)
