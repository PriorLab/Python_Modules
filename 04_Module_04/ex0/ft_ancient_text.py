def recover_text() -> None:
    print('=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n')
    print('Accessing Storage Vault: ancient_fragment.txt')
    try:
        with open("ancient_fragment.txt", "r") as file:
            print('Connection established...')
            print('RECOVERED DATA:')
            print(file.read())
            print('Data recovery complete. Storage unit disconnected.')
    except FileNotFoundError:
        print('Error: Storage Vault not found. Try running data generator first')

def main()-> None:
    recover_text()

if __name__ == "__main__":
    main()
