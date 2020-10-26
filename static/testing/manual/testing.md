# Testing

## Table of Contents
1. [**NavBar**](#navbar)
  - [**Superuser**](#superuser)
  - [**Registered User**](#registered-user)
  - [**Anonymous User**](#anonymous-user)
 
2. [**Index**](#index)
  
3. [**Nutrition**](#nutrition)

4. [**Nutrition Menu Management**](#nutrition-menu-management)

5. [**Menu Management**](#menu-management)

6. [**Plan Management**](#plan-management)


7. [**Products**](#products)

8. [**Product Detail**](#product-detail)

9. [**Product Management**](#product-management)
   - [**Add Product**](#add-product)
   - [**Edit Product**](#edit-product)

10. [**My Profile**](#my-profile)

11. [**Shop Bag**](#shop-bag)

12. [**Checkout**](#checkout)

13. [**Checkout Success**](#checkout-success)

 
14. [**Login**](#login)

15. [**Logout**](#logout)

16. [**Sign Up**](#sign-up)

17. [**Toast Success**](#toast-success)

18. [**Toast Error**](#toast-error)

19. [**Toast Info**](#toast-info)

20. [**Toast Warning**](#toast-warning)





## NavBar
I tested to make sure the following worked as designed and all passed.


### Superuser
When logged in as SUPERUSER(OWNER/ADMINISTRATOR), the superuser sees the following pages:
- Index
- Nutrition
- Products
- My profile
   - My details
   - Order History
   - Nutrition Plan (if bought a plan)
   - Product Management
   - Nutrition Menu Management
   - Plan Management
   - Sign Out
- Shop Bag icon


All the views are working accordingly:
1. Click on Index which is 'Body Balance' logo (url path to '/').
2. Click on Nutrition (url path to /subscriptions).
3. Click on Products (url path to /products/).
4. Click on My Profile
   - My details (url path to '/user_profile/')
   - Order History (url path to 'user_profile/'
   - Nutrition Plan - if bought a plan(url path to 'user_profile/'
   - Product Management (url path to /products/add_product/)
   - Nutrition Menu Management (url path to /nutrition/edit_menu_admin/1)
   - Plan Management (url path to /subscriptions/edit_plan_admin/1)
   - My Profile (url path to /user_profile/)
   - Sign Out (url path to /accounts/logout/)
5. Click on Shop Bag icon (url path to /shop_bag/).

### Registered User
When logged in as a REGISTERED USER, the user sees the following pages:
- Index
- Nutrition
- Products
- My profile
   - My details
   - Order History
   - Nutrition Plan (if bought a plan)
   - Sign Out
- Shop Bag icon


All the views are working accordingly:
1. Click on Index which is 'Body Balance' logo (view to '/').
2. Click on Nutrition (url path to /subscriptions).
3. Click on Products (url path to /products/).
4. Click on My Profile
   - My details (url path to '/user_profile/')
   - Order History (url path to 'user_profile/'
   - Nutrition Plan - if bought a plan(url path to 'user_profile/'
   - Sign Out (url path to /accounts/logout/)
5. Click on Shop Bag icon (url path to /shop_bag/).
  

### Anonymous User
When ANONYMOUS USER, the user sees the following pages:
- Index
- Nutrition
- Products
- Sign In
- Shop Bag icon

All the views are working accordingly:
1. Click on Index which is 'Body Balance' logo (url path '/').
2. Click on Nutrition (url path to /subscriptions).
3. Click on Products (url path to /products/)
4. Click on Sign In
   - Sign In (url path to /accounts/login/)
5. Click on Shop Bag icon (url path to /shop_bag/). 

##### back to [top](#table-of-contents)
 
---

## Index
(url path to '/')
#### Logged In users, anonymous users and superusers can:
1. Click on Index which is 'Body Balance' logo (url path to '/').

##### back to [top](#table-of-contents)
 
---

## Nutrition 
(url path /subscriptions)
##### SUPERUSER(OWNER/ADMINISTRATOR) users can:
1.  Click on "Edit" button to verify it redirects the superuser to "Subscription Management" page.


##### Logged In users:
- Who have a subscription plan can:
1. Click on "See your plan" button to verify it redirects the user to "My Nutrition Plan" page containing details of the Menu Nutrition Plan.

- Who don't have subscription plan can: 
1. Click on "Buy Nutrition Plan" button to verify it redirects the user to "Stripe Checkout" page .

##### Anonymous users can:
1. Click on "Register to buy" button (user need to be registered in order to purchase Nutrition Plan) to verify it redirects the user to "Sign Up" page.


##### back to [top](#table-of-contents)
 
---

## Nutrition Menu Management
(url path /nutrition/)
##### SUPERUSER(OWNER/ADMINISTRATOR) users can:
1.  Click on "Edit Plan" to verify it redirects user to "Menu Management" page (url path /nutrition/edit_menu_admin/1). 

##### Logged In users and Anonymous users:
Have no access to this page.


##### back to [top](#table-of-contents)


---

## Menu Management
(url path nutrition/edit_menu_admin/1)
##### SUPERUSER(OWNER/ADMINISTRATOR) users can:
1.  Click on "Plan name*" input and add the plan name.
2.  Click on "Week*" input and add the week day (integer).
3.  Click on "Day*" input and add day (integer).
4.  Click on "Breakfast*" input and add the breakfast menu.
5.  Click on "Am snack*" input and add the Am Snack menu.
6.  Click on "Lunch*" input and add the lunch menu.
7.  Click on "Pm snack*" input and add the Pm Snack menu.
8.  Click on "Dinner*" input and add the Dinner menu.
9.  Click on "Daily total cal*" input and add the Daily total cal (decimal_places=3).
10.  Click on "Protein*" input and add the protein quantity (CharField).
11.  Click on "Carbohydrates*" input and add the Carbohydrates quantity (CharField).
12.  Click on "Fiber*" input and add the Fiber quantity (CharField).
13.  Click on "Sodium*" input and add the Sodium quantity (decimal_places=3).
14.  Click on "Image url" input and add the Image url path.
15.  Click on "Choose File" input and add the Image url path.
16.  Click on "Cancel" button to verify it redirects to "Nutrition" page.
17.  Click on "Update Menu" button to verify it redirects to "Nutrition Management" page.

##### Logged In users and Anonymous users:
Have no access to this page.


##### back to [top](#table-of-contents)
 
---
## Plan Management
(url path/subscriptions/edit_subscription_admin/1)
##### SUPERUSER(OWNER/ADMINISTRATOR) users can:
1.  Click on "Plan duration*" input and add the plan duration.
2.  Click on "Description*" input and add the plan description.
3.  Click on "Price*" input and add price (decimal_places=3).
4.  Click on "Image url" input and add the Image url path.
5.  Click on "Choose File" input and add the Image url path.
6.  Click on "Clear" checkbox to verify it is checked.
7.  Click on "Cancel" button to verify it redirects to "Nutrition" page.
8.  Click on "Update Plan" button to verify it redirects to "Nutrition Plan" page.


##### Logged In users and Anonymous users:
Have no access to this page.

##### back to [top](#table-of-contents)
 
 
---

## Products 
(url path to /products/)
##### SUPERUSER(OWNER/ADMINISTRATOR) users can:
1. Do all the same steps mentioned bellow.
2. Click on "Edit" button placed in each products cards to verify it redirects to the "Edit a Product" Page (/products/edit_product/16/).

#### Logged In Users who has Nutrition Plan can:
1. Click on "Search Input" to search keywords (present on Product name title or product description) to verify it filter your search.
2. On "Filter" section, under Category, click on "Active wear" to verify it display all activewear clothes. 
3. On "Filter" section, under Category,  click on "Gym Equipment" to verify it display all gym equipment products. 
4. On "Filter" section, under Category,  click on "Special Offers" to verify it display all special offers products.
5. On "Filter" section, click on "All Products" to verify it display all products, except the Nutrition Plan.
6. On "Sort by" section, select from dropdown "Price(low to high)" to verify it display all products on ascending price, except the Nutrition Plan.
7. On "Sort by" section, select from dropdown "Price(high to low)" to verify it display all products on descending price, except the Nutrition Plan.
8. On "Sort by" section, select from dropdown "Rating(low to high)" to verify it display all products on ascending rating, except the Nutrition Plan.
9. On "Sort by" section, select from dropdown "Rating(high to low)" to verify it display all products on descending rating, except the Nutrition Plan.
10. On "Sort by" section, select from dropdown "Name(A-Z)" to verify it display all products by ascending product name, except the Nutrition Plan.
11. On "Sort by" section, select from dropdown "Name(Z-A)" to verify it display all products by descending product name, except the Nutrition Plan.
12. On "Sort by" section, select from dropdown "Category(A-Z)" to verify it display all categories selected by ascending category name, except the Nutrition Plan.
13. On "Sort by" section, select from dropdown "Name(Z-A)" to verify it display all categories by descending category name, except the Nutrition Plan.
14. Click on any "Product Image" to verify it redirects to the "Product details" page.
15. Click on "Back to Top" button to verify if on click it brings user back to the top of the page.



#### Logged In Users who don't have Nutrition Plan can:
1. Click on "Search Input" to search keywords (present on Product name title or product description) to verify it filter your search.
2. On "Filter" section, under Category, click on "Active wear" to verify it display all activewear clothes. 
3. On "Filter" section, under Category,  click on "Gym Equipment" to verify it display all gym equipment products. 
4. On "Filter" section, under Category,  click on "Special Offers" to verify it display all special offers products.
4. On "Nutrition Plan" section, under Category,  click on "Special Offers" to verify it display the Nutrition Plan.
5. On "Filter" section, click on "All Products" to verify it display all products.
6. On "Sort by" section, select from dropdown "Price(low to high)" to verify it display all products on ascending price.
7. On "Sort by" section, select from dropdown "Price(high to low)" to verify it display all products on descending price.
8. On "Sort by" section, select from dropdown "Rating(low to high)" to verify it display all products on ascending ratings.
9. On "Sort by" section, select from dropdown "Rating(high to low)" to verify it display all products on descending rating.
10. On "Sort by" section, select from dropdown "Name(A-Z)" to verify it display all products by ascending product name.
11. On "Sort by" section, select from dropdown "Name(Z-A)" to verify it display all products by descending product name.
12. On "Sort by" section, select from dropdown "Category(A-Z)" to verify it display all categories selected by ascending category name.
13. On "Sort by" section, select from dropdown "Name(Z-A)" to verify it display all categories by descending category name.
14. Click on any "Product Image" to verify it redirects to the "Product details" page.
15. Click on "Back to Top" button to verify if on click it brings user back to the top of the page.



#### Anonymous users can:
1. Click on "Search Input" to search keywords (present on Product name title or product description) to verify it filter your search.
2. On "Filter" section, under Category, click on "Active wear" to verify it display all activewear clothes. 
3. On "Filter" section, under Category,  click on "Gym Equipment" to verify it display all gym equipment products. 
4. On "Filter" section, under Category,  click on "Special Offers" to verify it display all special offers products.
5. On "Filter" section, under Category,  click on "Register to buy Nutrition Plan" to verify it redirects to "Sign Up" page.
6. On "Filter" section, click on "All Products" to verify it display all products, except the Nutrition Plan.
7. On "Sort by" section, select from dropdown "Price(low to high)" to verify it display all products on ascending price, except the Nutrition Plan.
8. On "Sort by" section, select from dropdown "Price(high to low)" to verify it display all products on descending price, except the Nutrition Plan.
8. On "Sort by" section, select from dropdown "Rating(low to high)" to verify it display all products on ascending ratings, except the Nutrition Plan.
9. On "Sort by" section, select from dropdown "Rating(high to low)" to verify it display all products on descending rating, except the Nutrition Plan.
10. On "Sort by" section, select from dropdown "Name(A-Z)" to verify it display all products by ascending product name, except the Nutrition Plan.
11. On "Sort by" section, select from dropdown "Name(Z-A)" to verify it display all products by descending product name, except the Nutrition Plan.
12. On "Sort by" section, select from dropdown "Category(A-Z)" to verify it display all categories selected by ascending category name, except the Nutrition Plan.
13. On "Sort by" section, select from dropdown "Name(Z-A)" to verify it display all categories by descending category name, except the Nutrition Plan.
14. Click on any "Product Image" to verify it redirects to the "Product details" page.
15. Click on "Back to Top" button to verify if on click it brings user back to the top of the page.
##### back to [top](#table-of-contents)
 
---

## Product Detail
(url path to /products/13)
#### SUPERUSER(OWNER/ADMINISTRATOR) users can:
1. On "Size" options, click on "XS" to verify it selects the box and change to a darker green.
2. On "Size" options, click on "S" to verify it selects the box and change to a darker green.
3. On "Size" options, click on "M" to verify it selects the box and change to a darker green.
4. On "Size" options, click on "L" to verify it selects the box and change to a darker green.
5. On "Size" options, click on "XL" to verify it selects the box and change to a darker green.
6. Click on "Back to shopping" button to verify it redirects to "Products" page.
7. Click on "Add to Bag" button to verify it displays a "Toast Success"containing information about the products added to the shop bag.

#### For All Products cards except Nutrition Plan card
#### Logged In Users and Anonymous can:
1. On "Size" options, click on "XS" to verify it selects the box and change to a darker green.
2. On "Size" options, click on "S" to verify it selects the box and change to a darker green.
3. On "Size" options, click on "M" to verify it selects the box and change to a darker green.
4. On "Size" options, click on "L" to verify it selects the box and change to a darker green.
5. On "Size" options, click on "XL" to verify it selects the box and change to a darker green.
6. Click on "Back to shopping" button to verify it redirects to "Products" page.
7. Click on "Add to Bag" button to verify it displays a "Toast Success"containing information about the products added to the shop bag.

#### For Nutrition Plan card
#### Logged In Users who have purchased Nutrition Plan are not able to visualize this page.

#### Logged In Users who don't have purchased Nutrition Plan can:
1. Click on "Back to shopping" button to verify it redirects to "Products" page.
2. Click on "Add to Bag" button to verify it displays a "Toast Success" containing information about the products added to the shop bag.
3. After clicked on "Add to Bag" button verify if a message "Item already in bag" displays.

#### Anonymous users are not able to visualize this page.





##### back to [top](#table-of-contents)
 
---

## Product Management

### Add Product
(url path /products/add_product/)

##### SUPERUSER(OWNER/ADMINISTRATOR) users can:
1. Click on "Product name*" input and add the product name.
2. Click on "Description*" input and add the product Description
3. Select from "Category" dropdown the desirable category.
4. Click on "Sku*" input and add the Sku product.
5. Select from "Product Sizes" dropdown the desirable option.
6. Click on "Price*" input and add the product price (decimal_places=2).
7. Click on "Image url" input and add the Image url path.
8.  Click on "Select New Image File" button to verify it adds the new selected image.
9.  Click on "Cancel" button to verify it redirects to "Products" page.
10.  Click on "Add Product" button to verify it redirects to "Product Details" page with the new add product accordingly.


##### Logged In users and Anonymous users:
Have no access to this page.


### Edit Product
(url path /products/edit_product/16)

##### SUPERUSER(OWNER/ADMINISTRATOR) users can:
1. Click on "Product name*" input and add the product name.
2. Click on "Description*" input and add the product Description
3. Select from "Category" dropdown the desirable category.
4. Click on "Sku*" input and add the Sku product.
5. Select from "Product Sizes" dropdown the desirable option.
6. Click on "Price*" input and add the product price (decimal_places=2).
7. Click on "Image url" input and add the Image url path.
8. Click on "Remove" checkbox to verify it is checked.
9. Click on "Select New Image File" button to verify it adds the new selected image.
10. Click on "Cancel" button to verify it redirects to "Products" page.
11. Click on "Update Product" button to verify it redirects to "Product Details" page with the product updated accordingly.


##### Logged In users and Anonymous users:
Have no access to this page.



##### back to [top](#table-of-contents)
 
---
## My Profile
(url path /user_profile/)
##### SUPERUSER(OWNER/ADMINISTRATOR) users can:
1. Click on "My Details" to verify if displays My Details card.
2. Click on "Update Details" button to verify if displays a toast success with the message "User profile updated successfully!" 
3. Click on "Order History" to verify if displays Order History card.
4. Click on Order Number link to check if redirects to the "Order Summary" page (url path /user_profile/product_order_history/9EB2D8F0F9C84BF1B791E2282AFED3D2).
5. Click on "Plan Nutrition" (if have a purchased Nutrition Plan) to verify if displays the Nutrition Plan card.
6. Click on Order Number link to check if redirects to the "Order Summary" page (url path /user_profile/product_order_history/5B053B4D0E0E4541A01ECD5C0A65D9C5).
7. Click on "Products Management" to verify if redirects to "Product Management" page (url path /products/add_product/).
8. Click on "Nutrition Menu Management" to verify if redirects to "Nutrition Menu Management" page (url path /nutrition/).
9. Click on "Plan Management" to verify if redirects to "Plan Management" page (url path /subscriptions/edit_subscription_admin/1).
10. Click on "Sign Out" to verify if redirects to "Sign out" page (url path /accounts/logout/).

#### Logged In users can:
1. Click on "My Details" to verify if displays My Details card.
2. Click on "Update Details" button to verify if displays a toast success with the message "User profile updated successfully!" 
3. Click on "Order History" to verify if displays Order History card.
4. Click on Order Number link to check if redirects to the "Order Summary" page (url path /user_profile/product_order_history/9EB2D8F0F9C84BF1B791E2282AFED3D2).
5. Click on "Plan Nutrition" (if have a purchased Nutrition Plan) to verify if displays the Nutrition Plan card.
6. Click on Order Number link to check if redirects to the "Order Summary" page (url path /user_profile/product_order_history/5B053B4D0E0E4541A01ECD5C0A65D9C5).
7. Click on "Sign Out" to verify if redirects to "Sign out" page (url path /accounts/logout/).
##### back to [top](#table-of-contents)

##### Anonymous users:
Have no access to this page.


---

## Shop Bag
(url path to /shop_bag/)

#### Logged In users, anonymous users and superusers can:
1. On "Quantity" input, click on "+" to verify it increase quantity and price accordingly.
2. On "Quantity" input, click on "-" to verify it decrease quantity and price accordingly.
3. Click on "Update" button to verify if product quantity is updated and price updates accordingly.
4. Click on "Continue Shopping Button" button to verify it redirects to the "Products"page.
5. Click on "Remove" button to verify if product is remover from shopping bag.
6. Click on "Checkout" button to verify it redirects to "Checkout"page.


##### back to [top](#table-of-contents)
 
---

## Checkout
(url path to /checkout/)
#### SUPERUSER(OWNER/ADMINISTRATOR) and Logged In users can:
1. Click on "Complete Order" button without fill out the form to verify if an error message "please fill out this field" appears.
2. Click on "Full Name*" input and add the user full name.
3. Check if "Email Address*" is already filled out.
4. Click on "Phone Number*" input and add the user phone number.
5. Click on "Street Address1*" input and add the user street address.
6. Click on "Street Address2" input and add the user street address.
7. Click on "Town or City*" input and add the town or city from where user lives.
8. Click on "County, State" input and add the County, State from where user lives.
9. Click on "Postal Code" input and add the Postal Code from where user lives.
10. Select from "Country*" dropdown the country where user lives.
11. Click on "Save this delivery information to my profile" checkbox to verify it is checked.
12. Click on "Card Number" input to add card number details, month, year and CVC.
13. Click on "Card Number" input to add wrong card number to verify if an error message "Your card number is invalid" appears.
14. Click on "MM/YY" input to add wrong date to verify if an error message " Your card's expiration year is in the past." appears.
15. Click on "Update Shop Bag " link to verify it redirects to "Shop Bag" page.
16. Click on "Product Image" to verify it redirects user to "Product Details" page.
17. Click on "Complete Order" button to verify it redirects user to "Checkout Success" page where user can see the Order Summary.
18. After previous step check if loading overlay screen appears.



#### Anonymous users can:
1. Click on "Complete Order" button without fill out the form to verify if an error message "please fill out this field" appears.
2. Click on "Full Name*" input and add the user full name.
3. Click on "Email Address*" input and add the user email address.
4. Click on "Phone Number*" input and add the user phone number.
5. Click on "Street Address1*" input and add the user street address.
6. Click on "Street Address2" input and add the user street address.
7. Click on "Town or City*" input and add the town or city from where user lives.
8. Click on "County, State" input and add the County, State from where user lives.
9. Click on "Postal Code" input and add the Postal Code from where user lives.
10. Select from "Country*" dropdown the country where user lives.
11. Click on "Create an account" link to verify it redirects to "Sign Up" page.
12. Click on "Login" link to verify it redirects to "Sign In" page.
13. Click on "Card Number" input to add card number details, month, year and CVC.
14. Click on "Card Number" input to add wrong card number to verify if an error message "Your card number is invalid" appears.
15. Click on "MM/YY" input to add wrong date to verify if an error message " Your card's expiration year is in the past." appears.
16. Click on "Update Shop Bag " link to verify it redirects to "Shop Bag" page.
17. Click on "Product Image" to verify it redirects user to "Product Details" page.
18. Click on "Complete Order" button to verify it redirects user to "Checkout Success" page where user can see the Order Summary.
19. After previous step check if loading overlay screen appears.


##### back to [top](#table-of-contents)
 
---

## Checkout Success
(url path to /checkout/checkout_success/)
This page only displays Order Summary for information purposes. There is no queried action.
##### back to [top](#table-of-contents)
 
---



## Sign In
(url path to /accounts/login/)

1. Click on "Sign In".
2. Try to insert a username or e-mail address in the input "username or e-mail". 
3. Try to insert a password in the input "password". 
4. Try to insert a username or e-mail address and click on "Sign In" to verify if the input "password" is required.
5. Try to insert a wrong username and click on "Sign In" to verify if an alert message "The username and/or password you specified are not correct" pops up.
6. Try to insert a wrong password and click on "Sign In" to verify if an alert message "The username and/or password you specified are not correct" pops up.
7. Try to insert a correct username and password and click on "Sign in" to verify if logs in.
8. Try to click on link "Sign Up Now" to verify it redirects the user to "Sign Up" page.
9. Try to click on button "Sign In" to verify it redirects the user to "Homepage" and appears a successful toast with the message "Successfully signed in as Thomas".
10. Try to click on link "Forgot Password" to verify it redirects the user to "Password Reset" page.

##### back to [top](#table-of-contents)
 
---

## Sign Out
(url path to /accounts/logout/)
1. Click on "Sign Out" button to verify if redirects to the "Homepage" and appears a successful toast with the message "You have signed out".
2. Click on "Cancel" button to verify if redirects to the "Homepage".
3.  Click on "X" to verify if the toast closes.

##### back to [top](#table-of-contents)
 
---

## Sign Up 
(url path to /accounts/signup/):
1. Click on "Sign Up".
2. Try to insert a e-mail address in the input "e-mail address".
3. Try to insert a e-mail address in the input "e-mail address confirmation".
4. Try to insert a username in the input "username". 
5. Try to insert a password in the input "password".
6. Try to insert a password in the input "password (again)".
7. Try to insert a e-mail address and click on "Sign Up" to verify if the input "e-mail address" is required.
8. Try to insert a e-mail address confirmation and click on "Sign Up" to verify if the input "e-mail address" is required.
9. Try to insert a short username (ca) and click on "Sign Up" to verify if the input "username" show an error "please lengthen this text to 4 characters or more (if you are currently using 2 characters).
10. Try to insert a username and click on "Sign Up" to verify if the input "password" is required.
11. Try to insert a password and click on "Sign up" to verify if the input "password (again)" is required.
12. Try to to click on "Sign Up" to verify if an alert messages "A user is already registered with this e-mail address, A user with that username already exists, This password is too short. It must contain at least 8 characters " pops up.
13. Try to click on link "Back" to verify it redirects the user to previous page.

##### back to [top](#table-of-contents)
 
---








