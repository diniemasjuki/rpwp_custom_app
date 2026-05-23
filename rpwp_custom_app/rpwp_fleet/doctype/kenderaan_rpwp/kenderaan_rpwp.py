# Copyright (c) 2026, RPWP Developer Team and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class KenderaanRPWP(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from rpwp_custom_app.rpwp_fleet.doctype.dokumen_kenderaan_rpwp.dokumen_kenderaan_rpwp import DokumenKenderaanRPWP

		chasis_no: DF.Data | None
		engine_no: DF.Data | None
		manu_year: DF.Data | None
		reg_year: DF.Data | None
		regsitration_number: DF.Link | None
		table_eddy: DF.Table[DokumenKenderaanRPWP]
		vehicle_cc: DF.Data | None
		vehicle_color: DF.Data | None
		vehicle_fuel: DF.Literal["", "Petrol", "Diesel", "Petrol + Hybrid", "EV"]
		vehicle_image: DF.AttachImage | None
		vehicle_manufacturer: DF.Link | None
		vehicle_model: DF.Data | None
		vehicle_name: DF.Data | None
		vehicle_seat: DF.Int
		vehicle_type: DF.Data | None
	# end: auto-generated types

	pass
