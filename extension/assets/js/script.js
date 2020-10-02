var url;
chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function 
(tabs) {
    url = tabs[0].url;
   
});

// url = "https://price-tracker-extension.herokuapp.com/link/" + url;

let button = document.getElementById("add-btn");

button.addEventListener("click", function() {

    let link = url;
    var data = {

        link:link
    }

    var database = firebase.database(); 

    var ref = database.ref("record");

    
    ref.push(data);
    alert('Item has been successfully added to your Wishlist!');

})