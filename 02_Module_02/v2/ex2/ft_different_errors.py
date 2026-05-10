def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        5/0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        5 + "abc"
    else:
        print("Operation completed successfully")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
    print("\nAll error types tested successfully!")
    # print("Testing multiple errors with one except...")
    # for i in range(2):
    #    try:
    #        garden_operations(i)
    #    except (ValueError, ZeroDivisionError) as e:
    #        print(f"Caught multiple: {type(e).__name__}: {e}")


if __name__ == "__main__":
    test_error_types()
