from . import __version__ as app_version

app_name = "hoa_alliance"
app_title = "Hoa Alliance"
app_publisher = "GreyCube Technologies"
app_description = "Customization for House Owner Association business"
app_icon = "octicon octicon-home-fill"
app_color = "green"
app_email = "admin@greycube.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/hoa_alliance/css/hoa_alliance.css"
# app_include_js = "/assets/hoa_alliance/js/hoa_alliance.js"

# include js, css files in header of web template
# web_include_css = "/assets/hoa_alliance/css/hoa_alliance.css"
# web_include_js = "/assets/hoa_alliance/js/hoa_alliance.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "hoa_alliance/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_list_js = {
	"Project" : "public/js/project_list.js",
	"Task" : "public/js/task_list.js",
	"Issue" : "public/js/issue_list.js",
	"Request for Quotation":"public/js/request_for_quotation_list.js",
	}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# website_route_rules = [
# 	{"from_route": "/rfq", "to_route": "/list"}
# ]
# Installation
# ------------

# before_install = "hoa_alliance.install.before_install"
# after_install = "hoa_alliance.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "hoa_alliance.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Project": {
		"on_update": "hoa_alliance.hoa_alliance.api.update_connected_task_count",
	},
	"Issue": {
		"on_update": "hoa_alliance.hoa_alliance.api.update_connected_task_count",
	},
	"Task": {
		"on_update": "hoa_alliance.hoa_alliance.api.update_connected_task_count",
		"after_delete": "hoa_alliance.hoa_alliance.api.update_connected_task_count",
		"validate": "hoa_alliance.hoa_alliance.api.update_dependent_task_count_for_task_doctype"
	}	
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"hoa_alliance.tasks.all"
# 	],
# 	"daily": [
# 		"hoa_alliance.tasks.daily"
# 	],
# 	"hourly": [
# 		"hoa_alliance.tasks.hourly"
# 	],
# 	"weekly": [
# 		"hoa_alliance.tasks.weekly"
# 	]
# 	"monthly": [
# 		"hoa_alliance.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "hoa_alliance.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "hoa_alliance.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "hoa_alliance.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"hoa_alliance.auth.validate"
# ]

fixtures = [
      {
        "dt": "Custom Field", 
        "filters": [["name", "in", [
				"Request for Quotation-required_by_due_date_cf",
				"Request for Quotation-requester_cf",
				"Issue-no_of_issue_connected_task_cf",
				"Project-no_of_project_connected_task_cf",
				"Task-no_of_dependent_task_cf"
				]]]
      },	

      {
        "dt": "List View Settings", 
        "filters": [["name", "in", [
					"Request for Quotation","Issue","Task","Project"
					]]]
      }		   			     

]