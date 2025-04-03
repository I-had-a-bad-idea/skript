def main():
    """
    A dummy PDF file generator.
    For now, it generates an 8MB file size of PDF with garbage data.
    """
    output_file = "dummy.pdf"
    total_size = 8 * 1024 * 1024

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
