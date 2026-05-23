# Copyright (c) 2026, RPWP Developer Team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from dateutil.relativedelta import relativedelta
from frappe.utils import getdate, today
import re

from frappe.model.document import Document


class PassportTraveller(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		address_city: DF.Data | None
		address_country: DF.Link | None
		address_postcode: DF.Data | None
		address_state: DF.Data | None
		address_street: DF.SmallText | None
		age: DF.Int
		age_categ: DF.Literal["", "Adult", "Child", "Infant", "Youth", "Invalid"]
		airline: DF.Literal["", "Emirates Airline", "Turkish Airlines", "Qatar Airways", "Saudi Airline", "Oman AIr", "Other"]
		cabin_occupancy: DF.Literal["", "Single", "Double", "Triple", "Quad", "Five", "Six"]
		cabin_type: DF.Literal["", "Balcony Cabin", "Superior Balcony Cabin", "Seaview Cabin", "Superior Seaview Cabin", "Interior Cabin", "Khuzama Presidential Villa", "Khuzama Superior Suite", "Others"]
		chat_link: DF.Data | None
		date_of_birth: DF.Date | None
		delegate_no: DF.Int
		departure_date: DF.Data | None
		email: DF.Data | None
		firstname: DF.Data
		flight_info_sent: DF.Check
		flight_itinerary: DF.TextEditor | None
		full_name: DF.Data | None
		fullname_format: DF.Literal["First Name + Last Name", "Last Name + First Name"]
		gender: DF.Literal["", "Male", "Female"]
		guest_no: DF.Int
		ic_no: DF.Data | None
		lastname: DF.Data
		nationality: DF.Link | None
		partner_fullname: DF.Data | None
		partner_relationship: DF.Literal["", "I am solo traveller", "I am the husband", "I am the wife of", "I am the children of", "I am the parent of", "I am a sibling of", "I am a friend of", "Other"]
		passport_checked: DF.Check
		passport_expired: DF.Date | None
		passport_image: DF.AttachImage | None
		passport_is_submitted: DF.Check
		passport_no: DF.Data | None
		phone: DF.Data | None
		pnr_no: DF.Data | None
		room_category_code: DF.Literal["", "PV", "SS", "BSC", "BC", "IC", "SC"]
		room_name: DF.Data | None
		ticket_type: DF.Literal["", "GIT", "FIT"]
		titlesalute: DF.Literal["", "MR", "MS", "MSTR", "MISS"]
		trip_group: DF.Data | None
		trip_name: DF.Data | None
		trip_package: DF.Data | None
		validity: DF.Data | None
	# end: auto-generated types

	def calculate_age(self):
		
		if self.departure_date:
			today_date = getdate(self.departure_date)
		else:
			today_date = getdate(today())
		
		dob = getdate(self.date_of_birth)

		self.age = today_date.year - dob.year

		# Adjust jika birthday belum sampai tahun ini
		if (today_date.month, today_date.day) < (dob.month, dob.day):
			self.age -= 1

		# define age category and title salutation
		if self.age < 0:
			self.age_categ = "Invalid"
			self.titlesalute = ""

		elif self.age < 2:
			self.age_categ = "Infant"
			self.titlesalute = "MSTR"

		elif self.age < 12:
			self.age_categ = "Child"
			if self.gender == "Male":
				self.titlesalute = "MSTR"
			elif self.gender == "Female":
				self.titlesalute = "MISS"

		else:
			self.age_categ = "Adult"
			if self.gender == "Male":
				self.titlesalute = "MR"
			elif self.gender == "Female":
				self.titlesalute = "MS"

	
	def passport_validity(self):
		
		if self.departure_date:
			datefrom = getdate(self.departure_date)
		else:
			datefrom = getdate(today())
		passport_expiry = getdate(self.passport_expired)

		diff = relativedelta(passport_expiry, datefrom)
		total_months = diff.years * 12 + diff.months

		if self.departure_date:
			if total_months > 6:
				if self.passport_checked:
					self.validity = "Valid"
				else:
					self.validity = "Pending Review"
			else:
				self.validity = "Expired"
		else:
			if total_months > 6:
				if self.passport_checked:
					self.validity = "Passport Checked"
				else:
					self.validity = "Pending Review"
			else:
				self.validity = "Expired"


	def validate(self):

		if self.partner_fullname: 
			self.partner_fullname = self.partner_fullname.strip().upper() 
		else: 
			self.partner_fullname = ""
		
		if self.firstname: 
			self.firstname = self.firstname.strip().upper() 
		else: 
			self.firstname = ""

		if self.lastname: 
			self.lastname = self.lastname.strip().upper() 
		else: 
			self.lastname = ""

		if self.fullname_format == "First Name + Last Name":
			self.full_name = "" + self.firstname + " " + self.lastname
		elif self.fullname_format == "Last Name + First Name":
			self.full_name = "" + self.lastname + " " + self.firstname

		if self.pnr_no:
			self.pnr_no = re.sub(r'[^a-zA-Z0-9]', '', self.pnr_no).upper().replace(" ","")

		if self.ic_no:
			self.ic_no = re.sub(r'[^a-zA-Z0-9]', '', self.ic_no).upper().replace(" ","")

		if self.passport_no:
			self.passport_no = re.sub(r'[^a-zA-Z0-9]', '', self.passport_no).upper().replace(" ","")

		if self.phone:
			self.phone = re.sub(r'[^a-zA-Z0-9]', '', self.phone).replace(" ","")

		if self.email:
			self.email = self.email.lower().strip().replace(" ","")
		
		if self.trip_name:
			self.trip_name = self.trip_name.upper().strip()
		
		if self.trip_group:
			self.trip_group = self.trip_group.upper().strip()
		
		if self.date_of_birth:
			self.calculate_age()
		
		if self.passport_expired:
			self.passport_validity()

		if self.partner_relationship == "I am solo traveller" \
			or self.partner_relationship == "I am the husband" \
			or self.partner_relationship == "I am the main contact":
			self.partner_fullname = self.full_name

		# if not self.passport_checked:
		# 	self.passport_is_submitted = None

		# if self.passport_no and self.ic_no:
		# 	self.traveller_id = f"{self.ic_no}-{self.passport_no}"
		# elif not self.passport_no and self.ic_no: 
		# 	self.traveller_id = f"TRAVELLER{self.ic_no}"
		# else:
		# 	self.traveller_id = f"{self.full_name}"
		# self.name = self.traveller_id