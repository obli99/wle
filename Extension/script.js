document.body.style.border = "5px solid green";
//this variable stores the currenturl
var currentURL;
chrome.tabs.query({'active': true, 'windowId': chrome.windows.WINDOW_ID_CURRENT}, 
function(tabs){
	getCurrentURL(tabs[0].url);
});
function getCurrentURL(tab){
	currentURL = tab;
}

