# Copyright (c) 2026, RPWP Developer Team and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class NomborKenderaan(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		attached_vehicle: DF.Link | None
		purchase_cost: DF.Currency
		registration_number: DF.Data | None
	# end: auto-generated types

	pass
