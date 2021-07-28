from __future__ import unicode_literals
import json
import frappe
from frappe import _
from frappe.utils import flt, has_common
from frappe.utils.user import is_website_user
from erpnext.controllers.website_list_for_contact import get_customers_suppliers

no_cache = 1

def get_context(context):
	filters=None
	limit_start=0
	limit_page_length=20
	user = frappe.session.user
	ignore_permissions = True
	parties_doctype='Request for Quotation Supplier'
	doctype='Request for Quotation'
	customers, suppliers = get_customers_suppliers(parties_doctype, user)
	parties = customers or suppliers
	if not filters: filters = []

	if (user != 'Guest' and is_website_user()) or doctype == 'Request for Quotation':
		parties_doctype = 'Request for Quotation Supplier' if doctype == 'Request for Quotation' else doctype
		# find party for this contact
		customers, suppliers = get_customers_suppliers(parties_doctype, user)

		if doctype == 'Request for Quotation':
			parties = customers or suppliers
			data = frappe.db.sql(
			"""SELECT  
			CASE
				when RFQS.quote_status='To Review & Submit' THEN CONCAT('/supplier-quotations/',SQ.name)
				when RFQS.quote_status='Received' THEN CONCAT('/supplier-quotations/',SQ.name)
				when RFQS.quote_status='Pending' THEN	 CONCAT('/rfq/',RFQ.name)
			END as name,
				CASE
				when RFQS.quote_status='To Review & Submit' THEN SQ.name
				when RFQS.quote_status='Received' THEN SQ.name
				when RFQS.quote_status='Pending' THEN RFQ.name
			END as doc_name,		
			CASE
				when RFQS.quote_status='To Review & Submit' THEN 'Applied'
				when RFQS.quote_status='Received' THEN 'Applied'
				when (RFQS.quote_status='Pending' and RFQ.required_by_due_date_cf < CURDATE()) THEN 'Closed'
				ELSE 'Open'
			END as supplier_rfq_status,
			RFQ.company as company, usercf.full_name as requester ,RFQ.transaction_date as requested_date,RFQ.required_by_due_date_cf as required_date 
			FROM `tabRequest for Quotation` RFQ
			inner join `tabRequest for Quotation Supplier` RFQS 
			on RFQ.name=RFQS.parent 
			inner join `tabUser` as usercf
			on RFQ.requester_cf =usercf.name		
			left join `tabSupplier Quotation Item` SQI
			on 	SQI.request_for_quotation=RFQ.name
			left join `tabSupplier Quotation` SQ
			on SQ.name=SQI.parent
			where RFQS.supplier='{supplier}'
			order by RFQS.modified desc limit {start}, {len}
			""".format(supplier=parties[0],start=limit_start, len = limit_page_length), as_dict=1)	
		context.supplier_rfq_list=data
		context.supplier=parties[0]
		context.title=_("Request for quotation list of supplier")
		context.show_sidebar=False
		context.no_breadcrumbs=True
		return context