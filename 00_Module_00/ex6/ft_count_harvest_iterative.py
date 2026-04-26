def ft_count_harvest_iterative() -> None:
    harvest = int(input("Days until harvest: "))
    day0 = 1
    if harvest <= 0:
        print("Invalid argument")
    while day0 <= harvest:
        print(f"Day {day0}")
        day0 += 1
    print("Harvest time!")


ft_count_harvest_iterative()
