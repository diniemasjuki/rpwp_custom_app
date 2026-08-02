# Copyright (c) 2026, RPWP Developer Team and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class FlightReservation(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		booking_class: DF.Literal["Economy", "Premium Economy", "Business", "First"]
		booking_type: DF.Literal["", "GIT", "FIT"]
		current_capacity: DF.Int
		max_cabin_luggage_kg: DF.Int
		max_hand_luggage_kg: DF.Int
		maximum_capacity: DF.Int
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		pnr_no: DF.Data | None
		status: DF.Literal["open", "closed", "ready to fly", "completed", "canceled"]
		targeted_capacity: DF.Int
		vendor: DF.Data | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Flight Booking"
