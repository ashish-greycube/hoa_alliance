import frappe
from frappe import _

def update_issue_doctype_connected_task(issue_name)  :  
		linked_task_count_for_issues=frappe.db.get_list('Task',
				filters={'issue': ['=', issue_name]},
				fields=['count(name) as count'])  
		frappe.db.set_value('Issue', issue_name, 'no_of_issue_connected_task_cf', linked_task_count_for_issues[0].count)  

def update_project_doctype_connected_task(project_name):
		linked_task_count_for_project=frappe.db.get_list('Task',
				filters={'project': ['=', project_name]},
				fields=['count(name) as count'])  
		frappe.db.set_value('Project', project_name, 'no_of_project_connected_task_cf', linked_task_count_for_project[0].count)      

def update_connected_task_count(self,method):
	if (self.doctype=='Issue' and method=='on_update'):
		update_issue_doctype_connected_task(issue_name=self.name)
	if (self.doctype=='Task' and method == 'on_update' and self.issue) :
		update_issue_doctype_connected_task(issue_name=self.issue)
	if (self.doctype=='Task' and method == 'after_delete' and self.issue):
		update_issue_doctype_connected_task(issue_name=self.issue)

	if (self.doctype=='Project'and method=='on_update') :
		update_project_doctype_connected_task(project_name=self.name)
	if (self.doctype=='Task' and method == 'on_update' and self.project):
		update_project_doctype_connected_task(project_name=self.project)
	if (self.doctype=='Task' and method == 'after_delete' and self.project):
		update_project_doctype_connected_task(project_name=self.project)


def update_dependent_task_count_for_task_doctype(self,method):
		depends_on_tasks = 0
		for d in self.depends_on:
			if d.task :
				depends_on_tasks += 1
		self.no_of_dependent_task_cf = depends_on_tasks      


def update_supplier_status_in_RFQ(self,method):
	include_me=1
	if self.docstatus==0:
		rfq_list = set([])
		for item in self.items:
			if item.request_for_quotation:
				rfq_list.add(item.request_for_quotation)
		for rfq in rfq_list:
			doc = frappe.get_doc('Request for Quotation', rfq,ignore_permissions=True)
			doc_sup = frappe.get_all('Request for Quotation Supplier', filters=
				{'parent': doc.name, 'supplier': self.supplier}, fields=['name', 'quote_status'])

			doc_sup = doc_sup[0] if doc_sup else None
			if  doc_sup:

				quote_status = _('To Review & Submit')
				for item in doc.items:
					sqi_count = frappe.db.sql("""
						SELECT
							COUNT(sqi.name) as count
						FROM
							`tabSupplier Quotation Item` as sqi,
							`tabSupplier Quotation` as sq
						WHERE sq.supplier = %(supplier)s
							AND sqi.docstatus = 1
							AND sq.name != %(me)s
							AND sqi.request_for_quotation_item = %(rqi)s
							AND sqi.parent = sq.name""",
						{"supplier": self.supplier, "rqi": item.name, 'me': self.name}, as_dict=1)[0]
					self_count = sum(my_item.request_for_quotation_item == item.name
						for my_item in self.items) if include_me else 0
					if (sqi_count.count + self_count) == 0:
						quote_status = _('Pending')
					frappe.db.set_value('Request for Quotation Supplier', doc_sup.name, 'quote_status', quote_status)