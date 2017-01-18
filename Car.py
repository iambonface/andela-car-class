
"""
	A Car class built from, a Car boiler-plate test and which can be used to instantiate various vehicles.

	Args:
		It takes in arguments that depict the type, model, and name of the vehicle, provided they are set.

"""
class Car(object):

	def __init__(self, name=None, model = None, car_type = None):
		self.car_type = car_type
		self.model = model
		self.name = name
		self.car_properties = []

	def __str__(self):
		if self.name is None and self.car_type is not None and self.model is not None:
			return 'General'

		elif self.name is not None and self.model is None and self.car_type is not None:
			return 'GM'
		else:
			return self.car_type, self.model, self.name

	def num_of_doors(self):
		if self.name is not None and self.model is not None:
			proplist = []
			proplist.append(self.name)

			if self.name =='Porshe':
				return[2]
			elif self.name =='koenigsegg':
				return[2]
			else:
				return [4]

	def num_of_wheels(self):
		if self.name is not None and self.model is not None:
			lowername = self.name.lower()
			if self.name =='trailer':
				return[8]
			else:
				return [4]

	def is_saloon(self):
		if self.name is not None and self.model is not None:
			lowername = self.name.lower()
			if self.name !='trailer':
				return True
			else:
				return False
	def drive(self, n):
		self.n = n
		if self.n <= 0:
			pass
		else:
			return int(str(self.n) + str(self.n))

	def speed(self, n):
		self.n = n 
		self.parked_speed= 0
		self.moving_speed= 0

		self.moving_speed = Car.drive(self, n)

		return [self.parked_speed, self.moving_speed]
			
		
