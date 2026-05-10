import sys


def inventory_analysis(players: list[str]) -> None:
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}
    for arg in players[1:]:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue
        item, qtty = arg.split(":")
        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue
        try:
            inventory[item] = int(qtty)
        except ValueError as e:
            print(f"Quantity error for '{item}' , {e}")
    item_list: list[str] = list(inventory.keys())
    total = len(inventory.keys())
    sumatory = sum(inventory.values())
    most: str = max(inventory, key=lambda k: inventory[k])
    least: str = min(inventory, key=lambda k: inventory[k])
    print(f"Got inventory: {inventory}")
    print(f"Item list: {item_list}")
    print(f"Total quantity of {total} items: {sumatory}")
    for i in inventory:
        perc = inventory[i] / sum(inventory.values())
        print(f"Item {i} represents {perc:.1%}")
    print(f"Item most abundant: {most}")
    print(f"Item least abundant: {least}")
    inventory['magic_item'] = 1
    print(f"Updated inventory: {inventory}")


def main() -> None:
    inventory_analysis(sys.argv)


if __name__ == "__main__":
    main()
