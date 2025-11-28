import argparse

def remove_highlight_lines(input_file, output_file, pattern):
    with open(input_file, "r", encoding="utf-8") as f_in:
        lines = f_in.readlines()

    with open(output_file, "w", encoding="utf-8") as f_out:
        for line in lines:
            if (pattern in line) and ("Options" in line):
                # skip this line
                continue
            f_out.write(line)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Remove highlight metadata lines from a Kindle export.")
    parser.add_argument("input_file", help="Path to the original highlights file.")
    parser.add_argument("output_file", help="Destination path for the cleaned file.")
    parser.add_argument(
        "--pattern",
        default="Yellow highlight | Location:",
        help="Highlight pattern to filter out (default: %(default)s)",
    )

    args = parser.parse_args()
    remove_highlight_lines(args.input_file, args.output_file, args.pattern)
