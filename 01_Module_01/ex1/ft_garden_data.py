class Plant:
	def __init__(self, name, height, age):
		self.name = name
		self.height = height
		self.age = age
	def show(self):
		return f"{self.name}: {self.height}cm, {self.age} days old"
"""
if __name__ == "__main__":
	print ("=== Garden Plant Registry ===")
	plant1 = Plant("Rose", 25, 30)
	plant2 = Plant("Sunflower", 80, 45)
	plant3 = Plant("Cactus", 15, 120)

	plant1.show()
	plant2.show()
	plant3.show()
"""
def create_plants():
	return [
		Plant("Rose", 25, 30),
		Plant("Sunflower", 80, 45),
		Plant("Cactus", 15, 120),
	]
def display_plants(plants):
	print("=== Garden Plant Registry ===")
	for plant in plants:
		print (plant.show())
if __name__ == "__main__":
	plants = create_plants()
	display_plants(plants)
