def secure_archives(
        file_name: str, action: str = "r", content: str = ""
) -> tuple[bool, str]:
    try:
        if action == "r":
            with open(file_name, "r", encoding="utf-8") as file:
                print("Using 'secure_archive' to read from a regular file:")
                text: str = file.read()
                print(f"(True, {text})")
        print(
            "Using 'secure_archive' to write previous content to a new file:"
        )
        new_file_name: str = "file"
        try:
            with open(new_file_name, "w", encoding="utf-8") as file:
                file.write(file_name)
            print("(True, 'Content successfully written to file')")
        except OSError:
            print("Error writing new file")
        return (True, new_file_name)

    except FileNotFoundError as e:
        print("Using 'secure_archive' to read from a nonexistent file:")
        print(f"False, {e}")
        return (False, "FileNotFoundError")

    except PermissionError as e:
        print("Using 'secure_archive' to read from an inaccessible file:")
        print(f"False, {e}")
        return (False, "PermissionError")


def main() -> None:
    print("=== Cyber Archives Security ===")
    secure_archives("/not/existing/file")
    secure_archives("/etc/shadow")
    secure_archives("ancient_fragment.txt")


if __name__ == "__main__":
    main()
