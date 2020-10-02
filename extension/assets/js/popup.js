'use strict'
var product;
chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
    product = tabs[0].url
});

let button = document.getElementById("add-btn");

document.getElementById('add-btn').onclick = function() {
    if (product.includes("https://www.amazon") && product.includes("/dp/")) {
        alert('Item has been successfully added to your Wishlist!');
        button.addEventListener("click", function() {

            //get the value which the user types
            let link = product;
        
            //make object
            var data = {
        
                link:link
            }
        
            //save the data to teh firebase
            var database = firebase.database(); //which gets the database
        
            var ref = database.ref("record");
        
            // pushing the object to the refernce records
            ref.push(data);
        
        })

    } else {
        alert('This is not a valid amazon product webpage');
    }
};

