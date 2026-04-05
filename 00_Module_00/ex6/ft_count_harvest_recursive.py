def ft_count_harvest_recursive(harvy, day0 = 1):
	if day0 > harvy:
		print("Harvest time!")
	else:
		print("Day ", day0)
		ft_count_harvest_recursive(harvy, day0 + 1)

harvy = int(input("Days until harvest: "))
ft_count_harvest_recursive(harvy)
