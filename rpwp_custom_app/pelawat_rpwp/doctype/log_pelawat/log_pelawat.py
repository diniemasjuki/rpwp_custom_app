# Copyright (c) 2026, RPWP Developer Team and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class LogPelawat(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		checkintime: DF.Datetime | None
		checkouttime: DF.Datetime | None
		company: DF.Data | None
		email: DF.Data | None
		first_name: DF.Data | None
		full_name: DF.Data | None
		id_no: DF.Data | None
		last_name: DF.Data | None
		location: DF.Data | None
		middle_name: DF.Data | None
		pelawat: DF.Link | None
		phone: DF.Data | None
		purpose_or_event: DF.Data | None
		visitor_image: DF.AttachImage | None
	# end: auto-generated types

	pass
