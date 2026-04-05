class Plant:
	def __init__(self, name, height, age):
		self.name = name
		self.height = height
		self.age = age
	
	def grow(self):
		self.height += 2.1
	def age_one_day(self):
		self.age += 1
	def show(self):
		print (f"{self.name}: {self.height:.1f}cm, {self.age} days old")

class Flower(Plant):
	def __init__(self, name, height, age, color):
		super().__init__(name, height, age)
		self.color = color
		self.has_bloomed = False
	
	def bloom(self):
		self.has_bloomed = True
	
	def show(self):
		super().show()
		print(f"Color: {self.color}")
		if self.has_bloomed == True:
			print(f"{self.name} is blooming beautifully!\n")
		else:
			print(f"{self.name} has not bloomed yet")

class Tree(Plant):
	def __init__(self, name, height, age, trunk_diameter):
		super().__init__(name, height, age)
		self.trunk_diameter = trunk_diameter

	def produce_shade(self):
		print(
			f"Tree {self.name} now produces a shade of "
			f"{self.height:.1f}cm long and {self.trunk_diameter:.1f}cm wide.\n")
		
	def show(self):
		super().show()
		print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")

class Vegetable(Plant):
	def __init__ (self, name, height, age, season, nutrit_value):
		super().__init__(name, height, age)
		self.season = season
		self.nutrit_value = nutrit_value
	
	def grow(self):
		super().grow()
		self.nutrit_value += 1

	def age_one_day(self):
		super().age_one_day()

	def show(self):
		super().show()
		print(f"Harvest season: {self.season}")
		print(f"Nutritional value: {self.nutrit_value}")
	
print("=== Garden Plant Types ===")
print("=== Flower")
rose = Flower("Rose", 15.0, 10, "red")
rose.show()
print("[asking the rose to bloom]")
rose.bloom()
rose.show()

print("=== Tree")
oak = Tree("Oak", 200.0, 365, 5.0)
oak.show()
print("[asking the oak to produce shade]")
oak.produce_shade()

print("=== Vegetable")
tomato = Vegetable("Tomato", 5.0, 10, "April", 0)
tomato.show()
print("[make tomato grow and age for 20 days]")
for _ in range(20):
    tomato.grow()
    tomato.age_one_day()
tomato.show()
