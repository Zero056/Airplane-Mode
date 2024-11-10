# Copyright (c) 2024, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import random
import string

class AirplaneTicket(Document):
	def validate(self):

		total_add_ons = 0
		for flight in self.add_ons:
			flight.total_amount = flight.flight_price * flight.qty
			total_add_ons += flight.total_amount
		self.total_amount = self.flight_price + total_add_ons

		random_integer = random.randint(1, 100)  
		random_letter = random.choice('ABCDE')   
		self.seat = f"{random_integer}{random_letter}"

