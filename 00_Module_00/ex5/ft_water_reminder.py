def ft_water_reminder() -> None:
    thirst = int(input("Days since last watering: "))
    if thirst > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")


ft_water_reminder()
