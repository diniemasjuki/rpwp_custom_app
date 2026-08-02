# Copyright (c) 2026, RPWP Developer Team and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Flight(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from rpwp_custom_app.traveller_management.doctype.flight_reservation.flight_reservation import FlightReservation

		airline: DF.Link | None
		departure_airport: DF.Link | None
		departure_date: DF.Date | None
		destination_airport: DF.Link | None
		flight_itinerary: DF.TextEditor | None
		flight_reservation: DF.Table[FlightReservation]
		flight_title: DF.Data | None
		return_date: DF.Date | None
		route_type: DF.Literal["Return Flight", "One Way Flight", "Multi-City Flight"]
		status: DF.Literal["Draft", "Open", "To Confirmed", "Confirmed", "Completed"]
	# end: auto-generated types

	_DOCTYPE_NAME = "Flight"
