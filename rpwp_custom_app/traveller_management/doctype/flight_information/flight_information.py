# Copyright (c) 2026, RPWP Developer Team and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class FlightInformation(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		airline: DF.Literal["", "Qatar Airways", "Emirates Airline", "Turkish Airline", "Air Asia", "Malaysia Airline", "Singapore Airline"]
		departure_airport: DF.Literal["", "KLIA 1 (KUL)", "KLIA 2 (KUL2)", "Changi (SIN)"]
		departure_date: DF.Date | None
		flight_class: DF.Literal["Economy", "Economy Plus", "Business", "First"]
		flight_itinerary: DF.TextEditor | None
		flight_title: DF.Data | None
		max_cabin_luggage: DF.Data | None
		max_hand_luggage: DF.Data | None
		max_passenger: DF.Int
		min_passenger: DF.Int
		pnr_no: DF.Data
		return_airport: DF.Data | None
		return_date: DF.Date | None
		route_type: DF.Literal["Return Flight", "One Way Flight", "Multi-City Flight"]
		status: DF.Literal["Open", "To Confirmed", "Confirmed", "Completed"]
		ticket_type: DF.Literal["", "GIT", "FIT"]
	# end: auto-generated types

	_DOCTYPE_NAME = "Flight Management"

	def validate(self):
		
		if(self.name):
			self.name = self.name.upper()

		if(self.pnr_no):
			self.pnr_no = self.pnr_no.upper()
		
		if(self.flight_title):
			self.flight_title = self.flight_title.upper()


		# if(self.flight_title):
		# 	self.flight_title = self.pnr_no + " " + self.airline + " " + self.departure_airport + " " + self.departure_date
		# 	self.flight_title = self.flight_title.upper()