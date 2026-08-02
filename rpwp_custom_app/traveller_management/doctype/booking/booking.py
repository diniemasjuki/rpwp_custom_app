# Copyright (c) 2026, RPWP Developer Team and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Booking(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from rpwp_custom_app.traveller_management.doctype.booking_item.booking_item import BookingItem

		booking_ticket: DF.Table[BookingItem]
		customer: DF.Data | None
		total_booking_price: DF.Currency
		trip_name: DF.Data | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Trip Booking"
