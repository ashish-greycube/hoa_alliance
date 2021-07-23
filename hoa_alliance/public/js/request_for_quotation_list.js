frappe.listview_settings['Request for Quotation'] = {
  hide_name_column: true,
  onload: function(list_view) {
    // change column header name
    $('.level-left span:contains("Company")').text('Customer')
    $('.level-left span:contains("Required By Date")').text('Required Dt')
    $('.level-left span:contains("Date")').text('Requested Dt')
    }    
};