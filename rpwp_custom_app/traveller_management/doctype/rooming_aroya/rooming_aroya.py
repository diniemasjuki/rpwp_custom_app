# Copyright (c) 2026, RPWP Developer Team and contributors
# For license information, please see license.txt

import frappe
import re

from frappe.model.document import Document


class RoomingAroya(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amended_from: DF.Link | None
		birth_date: DF.Data | None
		city: DF.Data | None
		country_of_birth: DF.Data | None
		delegate_no: DF.Data | None
		email: DF.Data | None
		first_name: DF.Data | None
		gender: DF.Data | None
		guest_no: DF.Data | None
		id_no: DF.Data | None
		intlcode: DF.Data | None
		intlcode_country: DF.Data | None
		language: DF.Data | None
		last_name: DF.Data | None
		localized_first_name: DF.Data | None
		localized_last_name: DF.Data | None
		package_types: DF.Data | None
		partner_name: DF.Data | None
		passport_image: DF.AttachImage | None
		passport_no: DF.Data | None
		readytosend: DF.Literal["", "Ready to Send", "Update Sent", "7 Day Reminder Sent", "2 Day Reminder Sent"]
		reservation_contact: DF.Data | None
		residency: DF.Data | None
		room_partner_relationship: DF.Data | None
		sail_date_from: DF.Date | None
		sail_date_to: DF.Date | None
		select_traveller: DF.Link | None
		ship: DF.Data | None
		sms_can_contact: DF.Data | None
		state: DF.Data | None
		stateroom_category: DF.Autocomplete | None
		stateroom_no: DF.Data | None
		telephone: DF.Data | None
		trip_group_name: DF.Data | None
		voyage_no: DF.Int
	# end: auto-generated types

	_DOCTYPE_NAME = "Rooming Aroya"


	def validate(self):

		if self.reservation_contact:
			self.reservation_contact = self.reservation_contact.upper()

		if self.sms_can_contact:
			self.sms_can_contact = self.sms_can_contact.upper()

		if self.residency:
			self.residency = self.residency.upper()

		if self.gender:
			self.gender = self.gender.upper()


		if self.country_of_birth:
			self.country_of_birth = self.country_of_birth.upper()

			if not self.state or self.state.upper():
				if self.country_of_birth.upper() == "MALAYSIA":
					self.state = "SELANGOR"
				else:
					self.state = self.country_of_birth.upper()

			if not self.city or self.city.upper():
				if self.country_of_birth.upper() == "MALAYSIA":
					self.city = "KAJANG"
				else:
					self.city = self.country_of_birth.upper()

			if self.telephone:
				self.intlcode = self.extract_country_code(self.telephone)

			if not self.intlcode_country:
				if self.intlcode == "60":
					self.intlcode_country = "MALAYSIA"
				if self.intlcode == "65":
					self.intlcode_country = "SINGAPORE"
				if self.intlcode == "44":
					self.intlcode_country = "UNITED KINGDOM"
				# capitilizekan nama negara
				if self.intlcode_country:
					self.intlcode_country = self.intlcode_country.upper()
		
		if self.telephone == "":
			self.intlcode = ""
			self.intlcode_country = ""

		if not self.select_traveller or self.select_traveller == "":
			self.last_name = ""
			self.first_name = ""
			self.gender = ""
			self.birth_date = ""
			self.residency = ""
			self.email = ""
			self.intlcode = ""
			self.intlcode_country = ""
			self.telephone = ""
			self.country_of_birth = ""
			self.city = ""
			self.localized_first_name = ""
			self.localized_last_name = ""
			self.state = ""
			self.id_no = ""



	def extract_country_code(self,phone_number):
		
		# buang whitespace
		phone_number = phone_number.strip()
		
		# regex cari + diikuti digit
		match = re.match(r'^\+?(\d{1,2})', phone_number)
		if match:
			return match.group(1)
		return None
	

	def after_insert(self):
		self.update_traveller_room()

	def on_update(self):
		self.update_traveller_room()

	def update_traveller_room(self):

		# Cari traveller berdasarkan ic_no dan update traveller
		if self.id_no:
			traveller_name = frappe.db.exists("Passport Traveller", {"ic_no": self.id_no})

			if traveller_name:
				traveller = frappe.get_doc("Passport Traveller", traveller_name)

				# recursive stopper
				# if traveller.state_room_no == self.stateroom_no:
				# 	return ""

				# Update field dalam Traveller ikut data Rooming
				traveller.room_category_code = self.stateroom_category
				traveller.state_room_no = self.stateroom_no
				traveller.delegate_no = self.delegate_no
				traveller.guest_no = self.guest_no
				traveller.cabin_reservation = self.name

				# Save perubahan
				traveller.save(ignore_permissions=True)
		
		# atau nak clearkan semula nombor bilik
		elif not self.id_no or self.id_no == "":
			traveller_name = frappe.db.exists("Passport Traveller", {"cabin_reservation": self.name})

			# kalau update content passport dan traveller exist
			if traveller_name:
				traveller = frappe.get_doc("Passport Traveller", traveller_name)

				# recursive stopper
				# if traveller.state_room_no == "" or not traveller.state_room_no:
				# 	return ""

				# Update field dalam Traveller ikut data Rooming
				traveller.cabin_reservation = ""
				traveller.room_category_code = ""
				traveller.state_room_no = ""
				traveller.delegate_no = ""
				traveller.guest_no = ""

				# Save perubahan
				traveller.save(ignore_permissions=True)
