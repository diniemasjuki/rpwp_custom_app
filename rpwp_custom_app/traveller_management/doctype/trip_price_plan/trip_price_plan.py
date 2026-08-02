# Copyright (c) 2026, RPWP Developer Team and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class TripPricePlan(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		age_price: DF.Currency
		children_price: DF.Currency
		infant: DF.Currency
		package_type: DF.Link | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		status: DF.Literal["active", "unlisted", "deactivated"]
		upperberth_price: DF.Currency
	# end: auto-generated types

	_DOCTYPE_NAME = "Trip Price Plan"
