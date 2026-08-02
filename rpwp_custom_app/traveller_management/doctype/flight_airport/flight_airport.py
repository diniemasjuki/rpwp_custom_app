# Copyright (c) 2026, RPWP Developer Team and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class FlightAirport(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		aiport_country: DF.Link | None
		airport_code: DF.Data | None
		airport_name: DF.Data | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Flight Airport"
