'use strict'

getCurrentTabUrl();
function getCurrentTabUrl() {  
    var queryInfo = {  
      active: true,  
      currentWindow: true  
    };    
    chrome.tabs.query(queryInfo, (tabs) => {  
      var tab = tabs[0];  
      var url = tab.url;  
      document.getElementById('urltext').innerHTML = url;  
    });  
}
