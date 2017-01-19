
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
		if self.name is None:
			self.name == 'General'

		elif self.model is None:
			self.model == 'GM'

		elif self.car_type is None:
			self.car_type == 'saloon'

		else:
			return self.name, self.model, self.car_type

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
			return self.car_type == 'saloon'
			
	def drive(self, n):
		if self.name is not None and self.model is not None:
			lowername = self.name.lower()
			if self.name !='trailer':
				self.n = 3
				return 10 ** self.n
			else:
				self.n= 7
				return 77
		#self.n = n
		#if self.n <= 0:
		#	pass

		#else:
		#	return int(str(self.n) + str(self.n))
		

	def speed(self, n):
		self.n = n 
		self.parked_speed= 0
		self.moving_speed= 0

		self.moving_speed = Car.drive(self, n)

		return [self.parked_speed, self.moving_speed]
			
		

