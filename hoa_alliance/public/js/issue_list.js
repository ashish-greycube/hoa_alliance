frappe.listview_settings['Issue'] = {
  onload: function(list_view) {
    // change column header name
    $('.level-left span:contains("Raised By (Email)")').text('Raised By')
    $('.level-left span:contains("Opening Date")').text('Opening Dt')
    }  
};
