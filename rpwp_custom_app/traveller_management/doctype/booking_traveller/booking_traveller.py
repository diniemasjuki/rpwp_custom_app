# Copyright (c) 2026, RPWP Developer Team and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class BookingTraveller(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from rpwp_custom_app.traveller_management.doctype.booking_x_traveller.booking_x_traveller import BookingXTraveller

		customer_booking: DF.Link | None
		list_traveller: DF.Table[BookingXTraveller]
	# end: auto-generated types

	pass
