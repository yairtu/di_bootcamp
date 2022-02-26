from typing import List
import datetime

"""
Company Attributes: 
- id (str) A two letters code
- name (str)
- planes (List of Plane) Every plane that belong to this airlines
"""


class Company:
	def __init__(self, id: str, name: str, planes: List = []):
		self.id = id
		self.name = name
		self.planes = planes


"""Airport Attributes:
- city (str) The code of the city where the airport is
- planes (List of Airplane) A list of every plane that is currently in this airport
- scheduled_departures (List of Flight) Every future flight from this airport, sorted by date
- scheduled_arrivals (List of Flight) Every future arrival to this airport, sorted by date"""
"""
schedule_flight(self, destination, datetime) This method finds when an available airplane from an 
airline that serve the origine and the destination and schedule a flight for it.

info(self, start_date, end_date) Display every scheduled flight from start_date to end_date.
"""


class Airport:
	def __init__(self, city: str, scheduled_departures: List = [], scheduled_arrivals: List = [], planes: List = []):
		self.city = city
		self.scheduled_departures = scheduled_departures
		self.scheduled_arrivals = scheduled_arrivals
		self.planes = planes

	def schedule_flight(self, destination, datetime: datetime):
		for plane in self.planes:
			if plane.next_flight.date != datetime:
				plane.next_flight.append(destination)

	def info(self, start_date, end_date):
		print("\tArrivals:")
		for arrivals in self.scheduled_arrivals:
			if start_date < arrivals.date:
				if arrivals.date < end_date:
					print(f"{arrivals.id}: Arriving from: {arrivals.origin.city}")
		
		print("\n\tDepartures")
		for departures in self.scheduled_departures:
			if start_date < departures.date:
				if departures.date < end_date:
					print(f"{departures.id}: Destination: {departures.destination.city}")



"""
Airplane Attributes: id (int)
- current_location (Airport)
- company (Company) The airlines
- next_flights (List of Flight) Every future flight of the airplane, this list should always be sorted by datetime.
"""


class Airplane:
	def __init__(self, id: int, current_location: Airport, company, next_flights: List = []):
		self.id = id
		self.current_location = current_location
		self.company = company
		self.next_flights = next_flights

	def fly(self, destination):
		print(f"Flying from {self.current_location} to {destination}")
		return

	"""Returns where the plane will be on this date"""

	def location_on_date(self, date):
		for flight in self.next_flights:
			if date == flight.date:
				return flight.destination

	"""Returns True if the plane can fly from this location on this date (it can fly if it is in this 
		location on this date and if it doesn’t already have a flight planned)."""

	def available_on_date(self, date, location):
		for flight in self.next_flights:
			if location == self.current_location and date not in flight.date:
				return True
		return False


class Flight:
	def __init__(self, date: datetime.datetime, destination: Airport, origin: Airport, plane: Airplane, id: str):
		self.date = date
		self.destination = destination
		self.origin = origin
		self.plane = plane
		self.id = id

	"""Methods (Those methods are here only to update the rest of the system, for example,
		to change the location of the plane when he arrives):"""

	def take_off(self):
		print(f"Taking off from {self.origin.city}")
		self.origin.scheduled_departures.pop()
		return

	def land(self):
		print(f"Landing at {self.destination.city}")
		self.destination.scheduled_arrivals.pop()
		self.plane.current_location = self.destination
		return


jetblue = Company("JB", "JetBlue", planes=[])
united_air = Company("UA", "United_Air", planes=[])

tlv = Airport(city="Tel_Aviv", scheduled_arrivals=[], scheduled_departures=[], planes=[])
bos = Airport(city="Boston", scheduled_departures=[], scheduled_arrivals=[], planes=[])
rkv = Airport(city="Reykjavik", scheduled_departures=[], scheduled_arrivals=[], planes=[])

plane1 = Airplane(id=747, current_location=bos, company=jetblue, next_flights=[])
plane2 = Airplane(id=747, current_location=rkv, company=united_air, next_flights=[])

bos_to_tlv = Flight(datetime.datetime(year=2022, month=4, day=5, hour=0, minute=0),
					destination=tlv,
					origin=bos,
					plane=plane1,
					id="BT01")

jetblue.planes.append(plane1)
united_air.planes.append(plane2)

bos.scheduled_departures.append(bos_to_tlv)
tlv.scheduled_arrivals.append(bos_to_tlv)

tlv.info(datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2023, 1, 1, 0, 0))

print()
print("-"*20)
bos_to_tlv.take_off()
bos_to_tlv.land()
print("-"*20 + "\n")
tlv.info(datetime.datetime(2022, 1, 1, 0, 0), datetime.datetime(2023, 1, 1, 0, 0))

