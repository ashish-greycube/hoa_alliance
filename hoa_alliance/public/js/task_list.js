frappe.listview_settings['Task'] = {
  onload: function(list_view) {
    // change column header name
    $('.level-left span:contains("Expected Start Date")').text('Start Date')
    $('.level-left span:contains("Expected End Date")').text('End Date')
    $('.level-left span:contains("Dependent #")').text('Dp.#')
    }  
};
