# Copyright (c) 2026, RPWP Developer Team and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class BookingItem(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		age_category: DF.Literal["Adult", "Infant"]
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		room_type: DF.Link
		ticket_price: DF.Currency
		traveller_info: DF.Link | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Booking Ticket"
