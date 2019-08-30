# Price Notifier

**Things To Do** (*delete after completion of project*)

    - A web extension that will retrieve the customer's wishlist from it's shopping website (preliminary works with amazon.in) and store it in a database.

    - That database will store the item_names along with item_price and item_link
    under customer's email-id

    - Another program that will access the database on a particular interval of time and update the database, item_price. If decreases, it will send email to the user.
    
    Note:-
        item_price might increase or decrease. The customer will only recieve email if the current_price decreases from the initial item_price of item stored.
          