class Plant:                                                                                      
	def __init__(self, name, height, age, growth_rate):
		self.name = name
		self.height = height
		self.age = age
		self.growth_rate = growth_rate
	def grow(self):
		self.height += self.growth_rate
	def age_one_day(self):
		self.age += 1
	def __str__(self):
		return f"{self.name}: {self.height:.1f}cm, {self.age} days old"
def simulate_growth(plant, days):
	print("=== Garden Plant Growth ===")

	initial_height = plant.height

	for day in range(1, days + 1):
		print(f"=== Day {day} ===")
		print(plant)

		plant.grow()
		plant.age_one_day()
	growth = plant.height - initial_height
	print(f"Growth this week: {int(growth)}cm")

if __name__ == "__main__":
	rose = Plant("Rose", 25.0, 30, 0.8)
	simulate_growth(rose, 7)
