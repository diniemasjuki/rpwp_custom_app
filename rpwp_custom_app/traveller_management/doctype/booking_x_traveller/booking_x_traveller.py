# Copyright (c) 2026, RPWP Developer Team and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class BookingXTraveller(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		traveller_name: DF.Data | None
		traveller_passport: DF.Link | None
		traveller_passport_no: DF.Data | None
	# end: auto-generated types

	pass
