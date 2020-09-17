'use strict'
var product;
chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
    product = tabs[0].url
});

document.getElementById('add-btn').onclick = function() {
    if (product.includes("https://www.amazon") && product.includes("/dp/")) {
        alert('Item has been successfully added to your Wishlist!');
    } else {
        alert('This is not a valid amazon product webpage');
    }
};

/*
document.getElementById('show-btn').onclick = function() {
    // add wishlist html 
}
*/