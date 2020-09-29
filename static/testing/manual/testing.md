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
   - Subscription Management
   - My Profile
   - Logout
- Shop Bag icon


All the views are working accordingly:
1. Click on Index which is 'Body Balance' logo (url path to '/').
2. Click on Nutrition (url path to /subscriptions).
3. Click on Products (url path to /products/).
4. Click on My Account
   - Product Management (url path to /products/add_product/)
   - Nutrition Management (url path to /nutrition/add_nutrition_plan/)
   - Subscrition Management (url path to /subscriptions/edit_plan_admin/1)
   - My Profile (url path to /user_profile/)
   - Logout (url path to /accounts/logout/)
5. Click on Bag icon (url path to /shop_bag/).

###### When logged in as a REGISTERED USER, the user sees the following pages:
- Index
- Nutrition
- Products
- My Account
   - My profile
   - Logout
- Bag icon


All the views are working accordingly:
1. Click on Index which is 'Body Balance' logo (view to '/').
2. Click on Nutrition (url path to /subscriptions).
3. Click on Products (url path to /products/).
4. Click on My Account
   - My Profile (url path to /user_profile/)
   - Logout (url path to /accounts/logout/)
5. Click on Bag Icon (url path to /shop_bag/).  

###### When ANONYMOUS USER, the user sees the following pages:
- Index
- Nutrition
- Products
- My Account
   - Register
   - Login
- Bag Icon

All the views are working accordingly:
1. Click on Index which is 'Body Balance' logo (url path to '/').
2. Click on Nutrition (url path to /subscriptions).
3. Click on Products (url path to /products/)
4. Click on My Account
   - Register (url path to /accounts/signup/)
   - Login (url path to /accounts/login/)
5. Click on Bag Icon (url path to /shop_bag/). 


#### Index(url path to '/')
###### Logged In users, anonymous users and superusers can:
1. Click on Index which is 'Boby Balance' logo (url path to '/').



#### Nutrition (url path to /subscriptions)
###### SUPERUSER(OWNER/ADMINISTRATOR) users can:
1.  Click on "Edit" button to verify it redirects the user to "????" page.


###### Logged In users:
 - Who have a subscription plan can:
1. Click on "See your plan" button to verify it redirects the user to "Nutrition" page containing details of the Nutrition Plan.

 - Who don't have subscription plan can: 
1. Click on "Subscribe" button to verify it redirects the user to "Stripe Checkout" page .

###### Anonymous users can:
1. Click on "Register" button (user need to be registered in order to subscribe) to verify it redirects the user to "Register" page.



#### Products (url path to /products/)
###### SUPERUSER(OWNER/ADMINISTRATOR) users can:
1.
2.
3.

###### Logged In users can:
1.
2.
3.

###### Anonymous users can:
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
1. Click on "Logout" to verify if user is able to logout.
2. Click on "Cancel" button to verify if redirects to the "Homepage".
3. Click on "Sign Out" button to verify if redirects to the "Homepage" and appears a succesfull toast with the message "You have signed out".
4.  Click on "X" to verify if the toast closes.


###### Logged In users can:
##### My profile (url path to /user_profile/)
1. Click on "My profile".

##### Logout (url path to /accounts/logout/)
1. Click on "Logout" to verify if user is able to logout.
2. Click on "Cancel" button to verify if redirects to the "Homepage".
3. Click on "Sign Out" button to verify if redirects to the "Homepage" and appears a succesfull toast with the message "You have signed out".
4.  Click on "X" to verify if the toast closes.


###### anonymous users can see:
#### Register (url path to /accounts/signup/):
1. Click on "Register".
2. Try to insert a e-mail address in the input "e-mail address".
3. Try to insert a e-mail address in the input "e-mail address confirmation".
4. Try to insert a username in the input "username". 
5. Try to insert a password in the input "password".
6. Try to insert a password in the input "password (again)".
7. Try to insert a e-mail address and click on "Sign Up" to verify if the input "e-mail address" is required.
8. Try to insert a e-mail address confirmation and click on "Sign Up" to verify if the input "e-mail address" is required.
9. Try to insert a short username (ca) and click on "Sign Up" to verify if the input "username" show an error "please lenghten this text to 4 caracters or more (if you are currently using 2 caracters).
10. Try to insert a username and click on "Sign Up" to verify if the input "password" is required.
11. Try to insert a password and click on "Log In" to verify if the input "password (again)" is required.
12. Try to to click on "Sign Up" to verify if an alert messages "A user is already registered with this e-mail address, A user with that username already exists, This password is too short. It must contain at least 8 characters " pops up.
13. Try to click on link "sign in" to verify it redirects the user to "Sign In" page.
14. Try to click on link "back to login" to verify it redirects the user to "Sign In" page.


##### Login (url path to /accounts/login/)
1. Click on "Login".
2. Try to insert a username or e-mail address in the input "username or e-mail". 
3. Try to insert a password in the input "password". 
4. Try to insert a username or e-mail address and click on "Sign In" to verify if the input "password" is required.
5. Try to insert a wrong username and click on "Sign In" to verify if an alert message "The username and/or password you specified are not correct" pops up.
6. Try to insert a wrong password and click on "Sign In" to verify if an alert message "The username and/or password you specified are not correct" pops up.
7. Try to insert a correct username and password and click on "Sigh in" to verify if logs in.
8. Try to click on link "sign up" to verify it redirects the user to "Sign Up" page.
9. Try to click on button "home" to verify it redirects the user to "Homepage".
10. Try to click on button "sign in" to verify it redirects the user to "Homepage" and appears a successfull toast with the message "Successfully signed in as Thomas".
11. Try to click on link "Forgot Password" to verify it redirects the user to "Password Reset" page.


#### Password Reset (url path to /accounts/password/reset/)
1.
2.


#### My Nutrition Plan (url path to /nutrition/)
1.
2.

#### Thanks (url path to /subscriptions/thanks/)
1.
2.


