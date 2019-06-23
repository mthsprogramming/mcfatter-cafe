/*
	cart.js
	JavaScript file used in the cart system on the Menu / Order pages.

	MTHS Programming Team 2017
*/


// Check if the storage's cart is null
function isCartEmpty(){
    if (localStorage.getItem("cart") === null){
        return true;
    }
    return false;
}

// Returns a JavaScript Object Array (cart) from the storage
function getCart(){
    return JSON.parse(localStorage.getItem("cart"));
}

function getJSON(){
    return localStorage.getItem("cart");
}

// Updates the cart using JSON
function updateCart(cartArray){
    if(cartArray.length == 0){
        localStorage.removeItem("cart");
    }
    else{
        var jsonStr = JSON.stringify(cartArray);
        localStorage.setItem("cart", jsonStr);
    }

}

function emptyCartAlert() {
    alert("Your cart is empty");
}

// Adds item to cart, makes sure quantity is legal
function addToCart(item, quantity, price){
    if(quantity>0 && quantity<=5){
        var cart = [];
        // checks if cart has items
        if (isCartEmpty() === false){
            cart = getCart();
        }

        // gets the index of any stackable items, -1 if there are none
        var dupIndex = getDuplicate(item);

        // if item is new to the cart
        if (dupIndex == -1){
            cart.push({item: item, qty: quantity, price: (price*quantity), instructions: ''});
            alert(quantity +" "+ item + "(s) has been added to your cart");
        }
        // handles stacking
        else{
            var testQty = parseInt(cart[dupIndex].qty) + parseInt(quantity);
            if (testQty>0 && testQty<=5){
                cart[dupIndex].price = getPriceOfOne(cart[dupIndex].price, cart[dupIndex].qty) * testQty;
                cart[dupIndex].qty = testQty+'';

                alert("You have added "+quantity+" more "+item+"(s) to your cart");
            }
            else {
                alert("You have too many "+item+"(s)");
            }
        }


        updateCart(cart);

    }
    else {
        alert("Disallowed quantity");
    }
}

// Clears the cart. Removes the cart from the storage and updates the order table.
function clearCart(){
    if (isCartEmpty()===false) {
        var answer = confirm('Are you sure you want to clear your cart?');

        if (answer){
            var cart = getCart();
            var table = document.getElementById('orderTable');

            var amountRows = cart.length;

            clearTable(amountRows);


            localStorage.removeItem("cart");
            setupTable();

            alert("Cart has been cleared");
        }
    }
    else {
        alert("Cart is already empty");
    }
}

function orderSubmission(){
    alert("Your order has been placed.");

    localStorage.removeItem("cart");
}

// Testing Button to see what is in cart
// To-Do: Remove call from HTML when testing is complete
function cartAlert(){
    var cart = [];
    if (isCartEmpty()){
        alert("Cart is empty")
    }
    else {
        cart = getCart();

        var alert_text = "";
        for(i=0; i<cart.length;i++){
            alert_text += cart[i].qty + "x " + cart[i].item;
            if (i<cart.length-1){
                alert_text += ", \n";
            }
        }
        alert("Cart contains " + alert_text);
    }
}

// Setting up the order table to display cart
// To-Do: Add images for items (maybe)
function setupTable(){
    var table = document.getElementById('orderTable');

    var cart = []
    if (isCartEmpty() === false){
        cart = getCart();

        for(i = 0; i < cart.length; i++) {
            var row = table.insertRow(i+1);

            // iterates through the number of header cells
            for(j = 0; j < table.rows[0].cells.length; j++) {
                var cell = row.insertCell(j);

                // cell that contains quantity box
                if (j == 0) {
                    var input = document.createElement('input');
                    input.type = 'number';
                    input.min = '1';
                    input.max = '5';
                    input.value = cart[i].qty;
                    input.id = 'qty'+i;

                    cell.appendChild(input);
                }

                // cell that contains price
                else if (j == 1 ) {
                    cell.innerHTML = cart[i].price;
                    cell.id = 'price'+i;
                }

                // cell that contains item
                else if (j == 2) {
                    // add item image here
                    cell.innerHTML = cart[i].item;
                }

                // cell that contains special instructions
                else if (j == 3) {
                    var input = document.createElement('textarea');
                    input.value = cart[i].instructions;
                    input.id = 'instructions'+i;

                    cell.appendChild(input);
                }

                // cell that contains remove button
                else if (j == 4) {
                    var button = document.createElement('button');
                    button.textContent = 'Remove';

                    button.value=i

                    button.onclick=function() {
                        removeFromCart(this.value);
                    }

                    cell.appendChild(button);
                }
            }
        }

        // get the cart into an HTML element so it can be processed in the form
        var hidden = document.getElementById('hiddenCart');
        hidden.value = getJSON();

        var place = document.getElementById('placeOrder');
        place.setAttribute('type', 'submit');
        place.setAttribute('onclick', 'return confirm("Are you sure you want to place this order?");');
    }

    // if the cart is empty
    else {
        var row = table.insertRow(1);
        var cell = row.insertCell(0);
        cell.innerHTML = 'Your cart is empty.';
        cell.style.paddingTop = '10px';
        cell.style.width = '50px';
        cell.style.textAlign = 'center';

        var place = document.getElementById('placeOrder');
        place.setAttribute('type', 'button');
        place.setAttribute('onclick', 'emptyCartAlert()')
    }
}

// Removing a row from order table and from cart object array
function removeFromCart(indexToRemove){
    // alert(indexToRemove);

    var cart = getCart();
    clearTable(cart.length);
    cart.splice(indexToRemove, 1);

    updateCart(cart);
    setupTable();

}

// Removes all rows from the table (except header row)
function clearTable(amountRows){
    var table = document.getElementById('orderTable');

    for (i = amountRows; i > 0; i--){
        table.deleteRow(i);
    }
}

// Update cart's values based on any changes from table
function updateCartFromTable(){
    var table = document.getElementById('orderTable');

    var cart = getCart();

    if (isCartEmpty()){
        alert("Cart is empty");
    }
    else{
    var flag = false;
    for (i = 0; i < cart.length; i++) {
        var qtyElement = document.getElementById('qty'+i);
        var newQty = qtyElement.value;
        if(newQty<=0 || newQty>5){
            qtyElement.value = cart[i].qty;
            alert("Invalid quantity for "+cart[i].item);
            flag = true;
        }
        else{
            cart[i].price = getPriceOfOne(cart[i].price, cart[i].qty) * newQty;
            cart[i].qty = newQty;
            var priceElement = document.getElementById('price'+i);
            priceElement.innerHTML = cart[i].price;

        }

        var instructionsElement = document.getElementById('instructions'+i);
        cart[i].instructions = instructionsElement.value;


    }


    updateCart(cart);
    if(flag==false){
        alert("Cart has been updated");
    }
    }

}

function getPriceOfOne(price, qty) {
    return price/parseFloat(qty);
}

// Finds the index of a duplicate if it exists, otherwise returns -1
function getDuplicate(item){
    var cart = getCart();

    if(isCartEmpty()===false){
        for (i=0;i<cart.length;i++){
            if (cart[i].item==item) {
                return i;
            }
        }
    }

    return -1;
}

// Features that currently lack implementation
// To-Do: Expansion - update cart as changes are detected in real time


/*

COOKIE CODE - NO LONGER USED

function setCookie(cName, cVal, cExDays){
	var d = new Date();
	d.setTime(d.getTime() + (cExDays*24*60*60*1000));
	var expires = "expires:" + d.toUTCString();
	document.cookie = cName + "=" + cVal + ";" + expires + ";path=/";
	addToCart();
}

function getCookie(cName){
	var name = cName + "=";
}

function addToOrder(itemQuantity, itemName){
	setCookie()
}
*/