def ft_count_harvest_recursive(harvest=None, day0=1) -> None:
    if harvest is None:
        harvest = int(input("Days until harvest: "))
    if harvest <= 0:
        print("Invalid argument")
        return
    if day0 > harvest:
        print("Harvest time!")
        return
    print(f"Day {day0}")
    ft_count_harvest_recursive(harvest, day0 + 1)


ft_count_harvest_recursive()
