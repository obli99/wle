document.body.style.border = "5px solid black";

var product;
chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
    product = tabs[0].url
});

if (product.includes("https://www.amazon") && product.includes("/dp/")) {
    alert('Item has been successfully added to your Wishlist!');
} else {
    alert('This is not a valid amazon product webpage');
}