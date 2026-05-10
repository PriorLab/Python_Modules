import sys


def open_ancient_text(path: list[str]) -> None:
    if len(path) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{path[1]}'")

    try:
        with open(path[1], "r", encoding="utf-8") as file:
            text: str = file.read()

            print("---\n")
            print(text)
            print("\n---")
            print(f"File '{path[1]}' closed.")

    except FileNotFoundError:
        print(
            f"Error opening file '{path[1]}':"
            f" [Errno 2] No such file or directory: '{path[1]}'"
        )

    except PermissionError:
        print(
            f"Error opening file '{path[1]}':"
            f" [Errno 13] Permission denied: '{path[1]}'"
        )


if __name__ == "__main__":
    open_ancient_text(sys.argv)
