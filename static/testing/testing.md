## Testing

#### NavBar:
I tested to make sure the following worked as designed and All passed

###### When logged in as SUPERUSER(OWNER/ADMINISTRATOR), the superuser sees the following pages:
- Index
- Nutrition
- Products
- My Account
   - Product Management
   - Nutrition Management
   - My Profile
   - Logout
- Bag Icon
- ??? User Nav - Username (redirect the user to My recipes page) & Log Out

All the views are working accordingly:
1. Click on Index which is 'Body Balance' logo (view to '/').
2. Click on Nutrition (url path to /subscriptions).
3. Click on Products (url path to /products/).
4. Click on My Account
   - Product Management (url path to /products/add_product/)
   - Nutrition Management (url path to /nutrition/add_nutrition_plan/)
   - My Profile (url path to /user_profile/)
   - Logout (url path to /accounts/logout/)
5. Click on Bag Icon (url path to /shop_bag/).

###### When logged in as USER, the user sees the following pages:
- Index
- Nutrition
- Products
- My Account
   - Register
   - Login
- Bag Icon
- ??? User Nav - Username (redirect the user to My recipes page) & Log Out

All the views are working accordingly:
1. Click on Index which is 'Body Balance' logo (view to '/').
2. Click on Nutrition (url path to /subscriptions).
3. Click on Products (url path to /products/).
4. Click on My Account
   - My Profile (url path to /user_profile/)
   - Logout (url path to /accounts/logout/)
5. Click on Bag Icon (url path to /shop_bag/).  

###### When not logged in, the user sees the following pages:
- Index
- Nutrition
- Products
- My Account
   - Register
   - Login
- Bag Icon
- ??? User Nav - Username (redirect the user to My recipes page) & Log Out

All the views are working accordingly:
1. Click on Index which is 'Body Balance' logo (url path to '/').
2. Click on Nutrition (url path to /subscriptions).
3. Click on Products (url path to /products/)
4. Click on My Account
   - Register (url path to /accounts/signup/)
   - Login (url path to /accounts/login/)
5. Click on Bag Icon (url path to /shop_bag/). 


#### Index(url path to '/')
###### Logged In users and anonimous users can:
1. Click on Index which is 'Boby Balance' logo (url path to '/').


#### Nutrition (url path to /subscriptions)
###### SUPERUSER(OWNER/ADMINISTRATOR) users can:
1.
2.
3.

###### Logged In users can:
1.
2.
3.

###### Anonimous users can:
1.
2.
3.


#### Products (url path to /products/)
###### SUPERUSER(OWNER/ADMINISTRATOR) users can:
1.
2.
3.

###### Logged In users can:
1.
2.
3.

###### Anonimous users can:
1.
2.
3.


#### My Account 
###### SUPERUSER(OWNER/ADMINISTRATOR) users can:
##### Product Management (url path to /products/add_product/)
1.
2.
3.
##### Nutrition Management (url path to /nutrition/add_nutrition_plan/)
1.
2.
3.

##### My profile (url path to /user_profile/)
1.
2.
3.

##### Logout (url path to /accounts/logout/)
1.
2.
3.


###### Logged In users can:
##### My profile (url path to /user_profile/)
1.
2.
3.

##### Logout (url path to /accounts/logout/)
1.
2.
3.


###### Anonimous users can see:
#### Register (url path to /accounts/signup/):
1. Click on "Register".
2. Try to insert a username. 
3. Try to insert a password. 
4. Try to insert a username and click on "Log In" to verify if the input password and avatar are required.
5. Try to insert a password and click on "Log In" to verify if the input username and avatar are required.
6. Try to insert a wrong username and click on "Login" to verify if an alert message "Invalid username or password" pops up.
7. Try to insert a wrong password and click on "Login" to verify if an alert message "Invalid username or password" pops up.
8. Try to insert a correct username, password, avatar and click on "Register" to verify redirects to "Log In" page.
9. Try to click on link "Click Here to Login." to verify it redirects the user to "Log In" page.


##### Login (url path to /accounts/login/)
1. Click on "Login".
2. Try to insert a username. 
3. Try to insert a password. 
4. Try to insert a username and click on "Log In" to verify if the input password is required.
5. Try to insert a password and click on "Log In" to verify if the input username is required.
6. Try to insert a wrong username and click on "Login" to verify if an alert message "Invalid username or password" pops up.
7. Try to insert a wrong password and click on "Login" to verify if an alert message "Invalid username or password" pops up.
8. Try to insert a correct username and password and click on "Login" to verify if logs in.
9. Try to click on link "Click Here To Register Account" to verify it redirects the user to "Register" page.
