frappe.listview_settings['Request for Quotation'] = {
  hide_name_column: true,
  onload: function(list_view) {
    // change column header name
    $('.level-left span:contains("Company")').text('Customer')
    $('.level-left span:contains("RFQ Due Date")').text('RFQ Due Dt')
    $('.level-left span:contains("Date")').text('Request Dt')
    }    
};