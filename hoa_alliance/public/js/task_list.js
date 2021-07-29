frappe.listview_settings['Task'] = {
  onload: function(list_view) {
    // change column header name
    $('.level-left span:contains("Parent Task")').text('Parent')
    $('.level-left span:contains("Expected Start Date")').text('Start Dt')
    $('.level-left span:contains("Expected End Date")').text('End Dt')
    $('.level-left span:contains("Dependent #")').text('Dp.#')
    }  
};
