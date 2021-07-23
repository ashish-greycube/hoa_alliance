frappe.listview_settings['Project'] = {
  onload: function(list_view) {
  // change column header name
  $('.level-left span:contains("Expected Start Date")').text('Start Date')
  $('.level-left span:contains("Expected End Date")').text('End Date')
  }
};
