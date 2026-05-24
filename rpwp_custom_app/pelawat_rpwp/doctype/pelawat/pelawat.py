# Copyright (c) 2026, RPWP Developer Team and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Pelawat(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		company: DF.Data | None
		email: DF.Data | None
		first_name: DF.Data | None
		full_name: DF.Data | None
		id_no: DF.Data | None
		last_name: DF.Data | None
		middle_name: DF.Data | None
		phone: DF.Data | None
		visitor_image: DF.AttachImage | None
	# end: auto-generated types

	pass
