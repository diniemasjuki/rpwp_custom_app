# Copyright (c) 2026, RPWP Developer Team and contributors
# For license information, please see license.txt

import frappe
import re
from frappe.model.document import Document


class TravellerHealth(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from rpwp_custom_app.traveller_management.doctype.traveller_health_medication.traveller_health_medication import TravellerHealthMedication

		age: DF.Int
		full_name: DF.Data | None
		gender: DF.Data | None
		ic_no: DF.Link | None
		medical_history_allergic: DF.TextEditor | None
		medication_list: DF.Table[TravellerHealthMedication]
		passport_image: DF.AttachImage | None
		passportno: DF.Data | None
		pnr: DF.Data | None
		trip_group: DF.Data | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Medical Background"

	def validate(self):

		if self.ic_no:
			self.ic_no = re.sub(r'[^a-zA-Z0-9]', '', self.ic_no).upper().replace(" ","")