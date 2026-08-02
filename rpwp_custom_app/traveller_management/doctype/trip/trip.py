# Copyright (c) 2026, RPWP Developer Team and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Trip(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from rpwp_custom_app.traveller_management.doctype.trip_destination_stop_select.trip_destination_stop_select import TripDestinationStopSelect
		from rpwp_custom_app.traveller_management.doctype.trip_price_plan.trip_price_plan import TripPricePlan
		from rpwp_custom_app.traveller_management.doctype.trip_schedule.trip_schedule import TripSchedule

		banner_image: DF.AttachImage | None
		destination_list: DF.TableMultiSelect[TripDestinationStopSelect]
		trip_description: DF.TextEditor | None
		trip_package_name: DF.Data | None
		trip_package_name_view: DF.Data | None
		trip_pricing_list: DF.Table[TripPricePlan]
		trip_schedule_list: DF.Table[TripSchedule]
		vendor: DF.Data | None
		with_flights: DF.Check
	# end: auto-generated types

	_DOCTYPE_NAME = "Trip Destination"
