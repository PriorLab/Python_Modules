class Plant:
	def __init__ (self, name, height, age, growth_rate):
		self.name = name
		self.height = height
		self.age = age
		self.growth_rate = growth_rate
	def grow (self):
		self.height += self.growth_rate
	def __str__(self):
		return f"{self.name}: {self.height:.1f}cm, {self.age} days old"
def create_plants():
	return [ 
		Plant("Rose", 25.0, 30, 1),
		Plant("Oak", 200.0, 365, 1),
		Plant("Cactus", 5.0, 90, 1),
		Plant("Sunflower", 80.0, 45, 1),
		Plant("Fern", 15.0, 120, 1),
		]
if __name__ == "__main__":
	plants = create_plants()
	print("=== Plant Factory Output ===")
	for plant in plants:
		print (f"Created: {plant}")
