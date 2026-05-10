import sys


def open_ancient_text(path: list[str]) -> None:
    if len(path) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{path[1]}'")

    try:
        with open(path[1], "r", encoding="utf-8") as file:
            text: str = file.read()

            print("---\n")
            print(text)
            print("\n---")
            print(f"File '{path[1]}' closed.")

    except FileNotFoundError as e:
        print(f"[STDERR] Error opening file '{path[1]}': {e}", file=sys.stderr)
        return

    except PermissionError as e:
        print(
            f"[STDERR] Error opening file '{path[1]}': {e}", file=sys.stderr)
        print("Data not saved.")
        return

    print("\nTransform data:\n---\n")
    try:
        transform: str = ""
        for char in text:
            if char == "\n":
                transform += "#\n"
            else:
                transform += char
        if not transform.endswith("#"):
            transform += "#"
        print(transform)
        print("---")
    except OSError:
        print("Error transforming data")
        return
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    file_name: str = sys.stdin.readline().strip()
    if file_name == "":
        print("Not saving data.")
        return
    else:
        print(f"Saving data to {file_name}")
        try:
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(transform)
                print(f"Data saved in file {file_name}")
        except OSError as e:
            print(f"[STDERR] Error opening file {file_name}: {e}")
            print("Data not saved.")
        return


if __name__ == "__main__":
    open_ancient_text(sys.argv)
