frappe.ui.form.on("Request for Quotation",{
	onload: function(frm) {
		if (frm.doc.required_by_due_date_cf==undefined) {
			frm.set_value('required_by_due_date_cf',frappe.datetime.add_days(frappe.datetime.nowdate(), 7))
		}
	}
})