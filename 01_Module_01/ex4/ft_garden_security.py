class Plant:
	def __init__ (self, name, height, age):
		self._name = name
		
		if (height < 0):
			print (f"{self._name}: Error, height can't be negative")
			print ("Height update rejected")
			self._height = 15.0
		else:
			self._height = height
		if (age < 0):
			print (f"{self._name}: Error, age can't be negative")
			print ("Age update rejected")
			self._age = 10
		else:
			self._age = age

	def set_height (self, height):
		if height < 0:
			print (f"{self._name}: Error, height can't be negative")
			print ("Height update rejected")
			return
		self._height = height
		print (f"Height updated: {height}cm")

	def set_age (self, age):
		if age < 0:
			print (f"{self._name}: Error, age can't be negative")
			print ("Age update rejected\n")
			return
		self._age = age
		print (f"Age updated: {age} days\n")
	
	def get_height (self):
		return self._height
	def get_age (self):
		return self._age
	def __str__(self):
		return f"{self._name}: {self._height:.1f}cm, {self._age} days old"
	
if __name__ == "__main__":
	plant = Plant("Rose", 15.0, 10)

	print("=== Garden Security System ===")
	print(f"Plant created: {plant}\n")

	plant.set_height(25)
	plant.set_age(30)
	plant.set_height(-5)
	plant.set_age(-2)

	print(f"Current state: {plant}")
