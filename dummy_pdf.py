import argparse


def main():
    """
    A dummy PDF file generator.
    For now, it generates an 8MB file size of PDF with garbage data.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--size", type=int, required=False)
    parser.add_argument("--name", type=str, required=False)
    parser.add_argument("--count", type=int, required=False)
    args = parser.parse_args()

    total_size = (args.size or 8) * 1024 * 1024
    file_count = args.count or 1

    for i in range(file_count):
        if (i == 0):
            output_file = f"{args.name}.pdf" if args.name else "dummy.pdf"
        else:
            output_file = f"{args.name}_{i}.pdf" if args.name else f"dummy_{i}.pdf"

        header = b"%PDF-1.4\n"
        footer = b"\n%%EOF"

        filler_size = total_size - len(header) - len(footer)
        filler = b"0" * filler_size

        with open(output_file, "wb") as f:
            f.write(header)
            f.write(filler)
            f.write(footer)

        print(f"new {output_file} file created")


if __name__ == "__main__":
    main()
