import sys


def show_args(args: list[str]) -> None:
    print("=== Command Quest ===")
    print(f"Program name: {args[0]}")
    i: int = 0
    length = len(args)
    if length == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {length - 1}")
        for i in range(length):
            print(f"Argument {i + 1}: {args[i]}")
    print(f"Total arguments: {len(args)}")


def main() -> None:
    show_args(sys.argv)


if __name__ == "__main__":
    main()
