# Copyright (c) 2026, RPWP Developer Team and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class DokumenKenderaanRPWP(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		vdoc_attachment: DF.Attach | None
		vdoc_cost: DF.Currency
		vdoc_expiry: DF.Date | None
		vdoc_name: DF.Data | None
		vdoc_validfrom: DF.Date | None
	# end: auto-generated types

	pass
