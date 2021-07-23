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

