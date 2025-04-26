#!/bin/bash


if [ "$#" -lt 2 ]; then
    echo "Usage: $0 <input_dir> <output_dir> [--max_depth N]"
    exit 1
fi

INPUT_DIR="$1"
OUTPUT_DIR="$2"
MAX_DEPTH=""

if [ "$3" == "--max_depth" ]; then
    MAX_DEPTH="$4"
fi


if [ ! -d "$INPUT_DIR" ]; then
    echo "Input directory does not exist: $INPUT_DIR"
    exit 1
fi

if [ ! -d "$OUTPUT_DIR" ]; then
    echo "Output directory does not exist: $OUTPUT_DIR"
    exit 1
fi

python3 collect_files.py "$INPUT_DIR" "$OUTPUT_DIR" "$MAX_DEPTH"
