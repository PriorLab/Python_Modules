import sys

def inventory_analysis(args: list[str]) -> None:
    print('=== Inventory System Analysis ===')
    inventory = {}

    for arg in args[1:]:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue

        item, qty = arg.split(":")

        if item in inventory:
            print(f"Redundant item {item} - discarding")
            continue

        try:
            inventory[item] = int(qty)
        except ValueError as e:
            print(f"Quantity error for '{item}': {e}")

    print(f"Got inventory: {inventory}")

    items = list(inventory.keys())
    print(f"Item list: {items}")

    total = sum(inventory.values())
    print(f"Total quantity of the {len(inventory.items())} items: {total}")

    for item in inventory:
        percent = (inventory[item]/total) * 100
        print(f"Item {item} represents {percent:.1f}%")

    most = max(inventory, key=inventory.get)
    least = min(inventory, key=inventory.get)
    print(f"Item most abundant: {most} with quantity {inventory[most]}")
    print(f"Item most abundant: {least} with quantity {inventory[least]}")
    
    inventory["magic_item"] = 1
    print(f"Updated inventory: {inventory}")

def main() -> None:
    inventory_analysis(sys.argv)

if __name__ == "__main__":
    main()


