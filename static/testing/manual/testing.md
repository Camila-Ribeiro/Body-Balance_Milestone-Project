# Body Balance
### [Heroku App](https://body-balance-milestone-project.herokuapp.com/)
### [GitHub](https://github.com/Camila-Ribeiro/Body-Balance_Milestone-Project)
 
![devices image](static/img/web-app-devices.png)
 
Body Balance is a Milestone Project created for the "Full Stack Frameworks With Django" module of my FullStack Software Development Course offered by [Code Institute](https://codeinstitute.net/).
 
## Table of Contents
1. [**Project overview**](#project-overview)


2. [**UX**](#ux)
  - [**User Stories**](#user-stories)
  - [**Design**](#design)
    - [**Color Scheme**](#color-scheme)
    - [**Typography**](#typography)
  - [**Wireframes**](#wireframes)
 

3. [**Features**](#features)
   - [**Existing Features**](#existing-features)
   - [**Features Left to Implement**](#features-left-to-implement)


4. [**Information Architecture**](#information-architecture)
   - [**Database choice**](#database-choice)
   - [**Data Models**](#data-models)
     - [**Products App Model**](#products-app-model)
     - [**Shop Bag App Model**](#shop-bag-app-model)
     - [**Checkout App Model**](#checkout-app-model)
     - [**User Profile App Model**](#user-profile-app-model)

 
5. [**Technologies Used**](#technologies-used)
    - [**Libraries**](#libraries)

 
6. [**Databases Used**](#databases-used)
   - [**Stripe API**](#stripe-api)
   - [**PostgresSQL**](#sostgressql)
   - [**SQlite3**](#sqlite3)
 

7. [**Testing**](#testing)
  - [**Validators**](#validators)
  - [**Manual Testing**](#manual-testing)

 
8. [**Deployment**](#deployment)
  - [**Deploying to Heroku**](#deploying-to-heroku)
  - [**Local development**](#local-development)
  - [**Amazon Web Services(AWS) - S3**](#amazon-web-services(aws)-s3)
      - [**Media And Static Folders**](#media-and-static-folders)
      

9. [**Credits**](#credits)
  - [**Content**](#content)
  - [**Media**](#media)
  - [**Acknowledgements**](#acknowledgements)
 

---
 
## Project overview
Body Balance was built using [Python](https://www.python.org/) - programming language, [Django](https://docs.djangoproject.com/en/3.1/) - which is a high-level Python Web framework that encourages rapid development and clean, pragmatic design and [Hekoru Postgres](https://www.mongodb.com/) - a document-based database.
 
 
## UX
 
Body Balance is an online web application designed for users with interest in gathering information about fitness healthy lifestyle as Nutritional plans and also Gym Equipments and Activewear. The website is simple and structured in a way that is easy and intuitive to navigate through. The application is designed for two types of users: 

- The site owner/ administrator (logging as a special user - superuser) and external users (as anonymous user, or logged in users).


- The anonymous user (users not logged in) can:
 - Navigate through the website and see Nutrition and Products page.
 - Search for products
 - Purchase products and nutrition plan
 - Register an account


- The user can:
 - Register an account
 - If registered already, user can log in into their account
 - Search for products
 - Purchase products and nutrition plan
 - Access "My profile" page
 - Access Order history
 - Access weekly nutritional plan


- The site owner/administrator (superuser) can:
 - log in into their account
 - Search for products
 - Purchase products and nutrition plan
 - Access "Product Management" page
 - Access "Nutrition Management" page
 - Access "Subscription Management" page
 - Access "My profile" page
 - Access Order history
 - Access weekly nutritional plan
 - Add, edit and delete product and all it's specifications
 - Add, edit and delete nutrition plan details
 - Edit subscription plan details 
 - Access the Django Admin page through `https://body-balance-milestone-project.herokuapp.com/admin` and using superuser's authorization as `username` or `email address` and `password`:
    - Add, edit and delete product and all it's specifications
    - Add, edit and delete nutrition plan details
    - Edit subscription plan details 
    - Access Accounts
    - Access Authentication and Authorization
    - Access a list of Product Orders
    - Access a list of Subscriptions Orders
    - Access a list of Products and Products Categories 
    
    
    

 
### User Stories

See a list of [User Stories](static/UX/My-cookbook-desktop-wireframe.pdf) built in an Agile method.


 
### Design
 
A standard layout is fully responsive on mobile devices and larger screens.
 

 
#### Color Scheme
 
- ![#61a5a0](https://placehold.it/15/61a5a0/#61a5a0)
- ![#90c0bc](https://placehold.it/15/90c0bc/90c0bc)
- ![#55928d](https://placehold.it/15/55928d/55928d)
- ![#dcdcdc](https://placehold.it/15/dcdcdc/dcdcdc)
- ![#f2c277](https://placehold.it/15/f2c277/f2c277)
 
#### Typography
 
3 [Google Fonts](https://fonts.google.com/) were used across the site:
 - [Roboto](https://fonts.google.com/specimen/Roboto) : body text
 - [Noto Sans](https://fonts.google.com/specimen/Noto+Sans?query=noto) : h1, h2, h3, h4, h5 ?????

 
### Wireframes
 
My wireframes for this project can be found in the UX folder.
 
- [Desktop Wireframe](static/UX/body-balance-desktop-wireframe.pdf)
- [Mobile Wireframe](static/UX/body-balance-mobile-wireframe.pdf)
 
##### back to [top](#table-of-contents)
 
---
 
## Features
 
### Existing Features
- Index - simple page containing an image, small text and navigation.

- Nutrition - this page displays a Nutrition Plan available for subscription. 
   - Registared users can purchase the plan clicking on "Subscribe" button where redirects the user to the "Stripe checkout".
   - For anonimous users it displays a "Subscribe" button where redirects the user to the "Register"page.
   - For superusers it displays an "Edit" button where redirects to the "Edit Plan"page.

- Products - this page displays all products:
   - it can be filtered by category, price, rating or show all products
   - There is a search input where the user can search keyword found on product name or product description
   - Also users can sort products by price (low to high or high to low), rating (low to high or high to low), name (A-Z or Z-a) and category (A-Z or Z-a).
   - Users, anonimous users and superuser can see the same content described above.

- Products Details - this page displays product details such as produc name, rating, category, price, size, quantity and a button "buy" which redirect the user to the "shop bag" page.
   - Registared users can purchase the plan clicking on "Subscribe" button where redirects the user to the "Stripe checkout".
   - For anonimous users it displays the same content.
   - For superusers it displays the same content described above plus an "Edit" button where redirects to the "Edit Product"page.

- User Profile - this page displays the user profile details, Order history and a Weekly Nutritional Plan detail (for subscribers only).
  - Registered user and superuser can:
     - Update their personal details
     - Check their Product Order history
     - Subscribers can access to their weekly Nutritional Plan detail
  - Anonimus don't have access to this page.
  

- Product Management - this page is designed only for superusers. It allows them to add products. 

- Nutrition Management - this page is designed only for superusers. It allows them to add nutrition details to the Nutrition Plan.

- Subscription Management - this page is designed only for superusers. It allows them to edit the Nutrition Plan Subscription such as plan name, description, and price.

- Register - this page has five inputs: e-mail address, e-mail address confirmation, username, password and password(again). It also displays two buttons:
  - "Back to Login" button where redirects the user to the Login page
  - "Sign Up" where redirects the user to a corfirmation e-mail page with a message " We have sent an e-mail to you for verification. Follow the link provided to finalize the signup process. Please contact us if you do not receive it within a few minutes." After user confirms the e-mail (link sent to their email address), the user can log in.

- Log In - this page has two inputs, username or e-mail and password. It also displays two buttons:
  - "Home" button where redirects the user to the index page
  - "Sigh In" button where redirects the user to the index page
  - Underneath those buttons there is a link "Forgot Password?" which redirects to a "Password Reset" page where the user have to type in their e-mail address and click on the "Reset My Password" button, then wait for an e-mail to arrive with instructions to reset the password.

- Log out - this page displays a question "Are you sure you want to sign out?" and two buttons: "Cancel and Sign out". Both buttons redirects the user back to index page.

- Error page - this page handles an error page in case the route wasn't found. There is a link to redirect the user back to index.
 
### Features Left to Implement
- Add additional Nutrition Plans - ???/

##### back to [top](#table-of-contents)
 
---

## Information Architecture

### Data Choice

### Data Models

#### Nutrition App Model
- Within the `nutrition app`:
   - the `Nutrition model` holds all the data needed for nutrition plan details (available for subscribers only) in the "My profile" page.

#### Subscriptions App Model
- Within the `subscriptions app`:
   - the `Plan model` holds all the fields needed to populate the "Nutrition" page which contain the nutrition plan card where users can subscribe to it.

#### Products App Model
- Within the `products app`:
   - the `Product model` holds all the data needed for the products in the shop bag.
   - the `Category model` holds all the categories needed to insert products in it.

#### Checkout App Model
- Within the `checkout app`:
   - the `ProductOrder model` holds all the data needed to generate a product order number and additional fields to have an order summary.
   - the `ProductLineOrder model` holds all the data needed to generate a product line order inside the Product Order (admin).
   - the `SubscriptionOrder model` holds all the data needed to generate a subscription order number and additional fields to have an order summary.

#### User Profile App Model
The User model utilized for this project is the standard one provided by `django.contrib.auth.models`
- Within the `user_profile app`:
   - the `UserProfile model` maintain default delivery information order history.


##### back to [top](#table-of-contents)

---
 
## Technologies Used
 
 
<b>Built with</b>
 
1. ![AWS S3 Bucket](https://img.shields.io/badge/Bson-Version%201.1-blue)
 - [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3) -  is an object storage service that offers industry-leading scalability, data availability, security, and performance.
2. ![Boto3](https://img.shields.io/badge/Bson-Version%201.1-blue)
 - [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - is the Amazon Web Services (AWS) SDK for Python. It enables Python developers to create, configure, and manage AWS services, such as EC2 and S3.
2. ![Chrome Developer Tools](https://img.shields.io/badge/Chrome%20Dev%20Tools-Google%20Chrome-blue)
 - [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools) - is a set of web developer tools built directly into the Google Chrome browser.
3. ![CSS3](https://img.shields.io/static/v1?label=CSS&message=3&color=1572B6&logo=css3&logoColor=ffffff)
 - [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3) - Used as the base for cascading styles.
4. ![Django3](https://docs.djangoproject.com/en/3.1/)
 - [Django3](https://django-crispy-forms.readthedocs.io/en/latest/) - is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
4. ![Django-Allauth](https://docs.djangoproject.com/en/3.1/)
 - [Django-Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) - is an integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication. A very well written library thanks to Raymond Penners. 
4. ![Django Crispy Forms](https://docs.djangoproject.com/en/3.1/)
 - [Django Crispy Forms](https://docs.djangoproject.com/en/3.1/) - is an application that helps to manage Django forms.
4. ![Django Storages](https://docs.djangoproject.com/en/3.1/)
 - [Django Storages](https://django-storages.readthedocs.io/en/latest/) -  is a collection of custom storage backends for Django to work with boto3 and AWS S3.
4. ![Flask](https://img.shields.io/badge/Flask-Version%201.1.2-orange)
 - [Flask](https://flask.palletsprojects.com/en/1.1.x/) - is a web framework, it provides you with tools, libraries and technologies that allow you to build a web application.
5. ![Flask-Bcrypt](https://img.shields.io/badge/Flask--Bcrypt-0.7.1-orange)
 - [Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/en/latest/) - is a Flask extension that provides bcrypt hashing utilities for your application.
6. ![Flask PyMongo](https://img.shields.io/badge/Flask--PyMongo-mongodb-blue)
 - [Flask PyMongo](https://flask-pymongo.readthedocs.io/en/latest/) - Bridges between Flask and PyMongo.
7. ![Flask Session](https://img.shields.io/badge/Flask--Session-session%20object-orange)
 - [Flask Session](https://flask.palletsprojects.com/en/1.1.x/api/#flask.session) - Flask-Session is an extension for Flask that adds support for Server-side Session to your application.
8. ![Flask WTF](https://img.shields.io/badge/Flask--WTF-0.14.3-blue)
 - [Flask WTF](https://flask-wtf.readthedocs.io/en/stable/) - Simple integration of Flask and WTForms, including CSRF, file upload, and reCAPTCHA.
9. ![Git](https://img.shields.io/badge/Git-----fast--version--control-orange)
 - [Git](https://git-scm.com/) - open source distributed version control system.
10. ![GitHub](https://img.shields.io/badge/GitHub-Git%20repository%20hosting%20service-lightgrey)
 - [GitHub](https://github.com/) - is a Web-based hosting service for version control using Git.
11. ![GitIgnore](https://img.shields.io/badge/GitIgnore-files-royalblue)
 - [GitIgnore](https://github.com/toptal/gitignore.io) - is a web service designed to help you create .gitignore files for your Git repositories.
22. ![gunicorn](https://pypi.org/project/gunicorn/)
 - [gunicorn](https://pypi.org/project/gunicorn/) - is a Python WSGI HTTP Server for UNIX. It’s a pre-fork worker model ported from Ruby’s Unicorn project. The Gunicorn server is broadly compatible with various web frameworks, simply implemented, light on server resource usage, and fairly speedy.
12. ![Heroku](https://img.shields.io/badge/Heroku-Deployment-blueviolet)
 - [Heroku](https://dashboard.heroku.com/) - lets you deploy, run and manage applications written in Ruby, Node.js, Java, Python, Clojure, Scala, Go and PHP.
13. ![HTML5](https://img.shields.io/static/v1?label=HTML&message=5&color=E34F26&logo=html5&logoColor=ffffff)
 - [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - used as the base for markup text.
14. ![JavaScript](https://img.shields.io/badge/jQuery-3.5.1-yellowgreen)
 - [JavaScript](https://www.javascript.com/) -  is a scripting or programming language that allows you to implement complex features on web pages.
14. ![jQuery](https://img.shields.io/badge/jQuery-3.5.1-yellowgreen)
 - [jQuery](https://jquery.com/) - is a fast, small, and feature-rich JavaScript library. It makes things like HTML document traversal and manipulation, event handling, animation, and Ajax much simpler with an easy-to-use API that works across a multitude of browsers.
15. ![Jinja](https://img.shields.io/badge/Jinja2-2.11.2-red)
 - [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/) - a full featured template engine for Python.
16. ![Pillow](https://img.shields.io/badge/MongoDB%20Atlas-4.4-green)
 - [Pillow](https://pillow.readthedocs.io/en/stable/) -  is the friendly PIL fork by Alex Clark and Contributors. PIL is the Python Imaging Library by Fredrik Lundh and Contributors.
18. ![PIP](https://img.shields.io/badge/PyMongo-2.3.0-green)
 - [PIP](https://pip.pypa.io/en/stable/installing/) - is the standard package manager for Python. It allows you to install and manage additional packages that are not part of the Python standard library.
17. ![Phyton](https://img.shields.io/badge/Python-3.8.3-blue)
 - [Python](https://www.python.org/downloads/release/python-383/) - is a scripting language.
21. ![psycopg2](https://pypi.org/project/psycopg2/)
 - [psycopg2](https://pypi.org/project/psycopg2/) - is the most popular PostgreSQL database adapter for the Python programming language.
19. ![Werkzeug](https://img.shields.io/badge/Werkzeug-WSGI%20-yellow)
 - [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/) - is a WSGI utility library for Python
20. ![WTforms](https://img.shields.io/badge/WTforms-0.14.3-blue)
 - [WTforms](https://pypi.org/project/WTForms/) - is  a framework agnostic library handling web forms in python.


#### Libraries
 
- [Bootstrap 4](https://getbootstrap.com/) - is a framework for building responsive, mobile-first websites.
- [FontAwesome](https://fontawesome.com/) - is a font and icon toolkit based on CSS and Less. It was used to provide icons across the website.
- [jQuery](https://jquery.com/download/) - is a lightweight, "write less, do more", JavaScript library. The purpose of jQuery is to make it much easier to use JavaScript on your website.
- [Psycopg2](https://pypi.org/project/psycopg2/) - is the most popular PostgreSQL database adapter for the Python programming language.
- [Bootsrap Select](https://developer.snapappointments.com/bootstrap-select/) - is a jQuery plugin that brings select elements into the 21st century with intuitive multiselection, searching, and much more.
##### back to [top](#table-of-contents)
 
---
## Databases Used

### Stripe API
[Stripe API](https://stripe.com/en-ie) is a payment processor, which means they support the electronic transfer of money from a customer's bank (issuing bank) into a merchant's bank (acquiring bank) as payment for goods or services bought with a credit card.
 
### PostgresSQL
[PostgresSQL](https://www.postgresql.org/) is a powerful, open source object-relational database system that uses and extends the SQL language combined with many features that safely store and scale the most complicated data workloads.
 
### SQlite3
 
[SQLite](https://www.sqlite.org/) is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. 

The SQLite file format is stable, cross-platform, and backwards compatible and the developers pledge to keep it that way through at least the year 2050. SQLite database files are commonly used as containers to transfer rich content between systems [1] [2] [3] and as a long-term archival format for data [4]. 

 
I have also created a database schema:
![Diagram of database schema](static/img/MongoDB-Schema.png)

##### back to [top](#table-of-contents)
 
---
 
## Testing
 
The project guidelines stated that a Test Driven Development (TDD) approach should be taken to developing the web application but I only manual testing was conducted during this project to fix bugs I used print() method. Below I outlined most of what I did below for documentation purposes.
I also have validated all files using online validation sites cited below and checked across different browsers and devices.
 
 
### Validators
 
#### HTML
 
- [W3C HTML Validator](https://validator.w3.org/) - `Text not allowed in elements in this context. - errors due to Jinja`
 
#### CSS
 
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - `Congratulations! No Error Found.`
 
#### PYTHON
 
- [Pep8 Online tool](http://pep8online.com/checkresult) - `minor errorsgit status`
 
#### JavaScript
 
 - [JShint](https://jshint.com/)
  - File: [main.js](static/js/main.js)
       - Metrics:
           - There are 12 functions in this file.
           - Function with the largest signature takes 2 arguments, while the median is 0.
           - Largest function has 15 statements in it, while the median is 2.
           - The most complex function has a cyclomatic complexity value of 1 while the median is 1.
 
 
### Manual Testing
I have conducted a detailed [manual testing](static/testing/manual/testing.md) to show that I have extensively tested this web application.
 
#### Testing Flask - Within my settings I had flask's debugger set to
 
`debug=True`
 
This is used for when Flask ever encounters an error the application knows to display this error in the view to give indication of what caused the app to crash.
 
I would work in small sprints where every step in my development I would ensure my app is still working as expected and where the app encounters any errors, I would debug the source until rectification was a success. Where needed I would document the error and the remediation taken in case of future occurrences.
 
Doing this meant after a while the error codes became more familiar to me. And from this debugging each error becomes less time consuming.
 
##### back to [top](#table-of-contents)
 
---
 
## Deployment

### Deploying to Heroku
 
[Body Balance](https://github.com/Camila-Ribeiro/Body-Balance_Milestone-Project) was developed  locally using **VS Code**, and all commits were pushed to [**Heroku**](https://body-balance-milestone-project.herokuapp.com/) using [**Git**](https://git-scm.com/).
 
In order to get the application ready for deployment I followed the next steps:
1. I removed all my hard-coded environment variables from app.py to protect my Database name, URI and secret-key and placed them in the env.py for development and entered it into herouku's Config Var for production.
2. On the terminal window using the command `pip3 freeze > requirements.txt` I installed `requirements.txt` file, which contains a list of items to be installed, defining the modules imported to Heroku.
3. Set up the Procfile (Remember to use a capital P in Procfile). using the command `echo web: python app.py > Procfile` - The Procfile file contains `web: python app.py` which tells Heroku to start a process called web and to run `python app.py` when it starts.
4. Created a new Heroku app
5. Created Config Var for production adding api_key, IP, PORT, MONGO_DBNAME, MONGO_URI & SECRET_KEY.
6. Set Flask's debugging to False.
7. Pushed the code to Heroku.
 
Upon successful deployment Heroku will give you the URL that is hosted on your app!
 
**IMPORTANT NOTE**:
 
- Please allow a few minutes to pass before opening your newly deployed link! Clicking this link too quickly may result in a failure to build the site, causing an Error 404 page instead.
 
Congratulations! Your project should be deployed successfully on Heroku's app! :tada:

### Local Development
To run this project locally on your own system, users can clone to their desktop by completing the following steps:
1.Go to [my GitHub repository](https://github.com/Camila-Ribeiro/Body-Balance_Milestone-Project).
2.Click on 'Code'(green button) placed beside Gitpod button.
3.Copy the clone URL for the repository in the 'Clone with HTTPs section'.
4.Open 'Git Bash' in your local IDE.
5.Change the current working directory to the location where you want the cloned directory to be made. (e.g. cd projects).
6.Type git clone, then paste the URL you copied in Step 3: git clone `https://github.com/USERNAME/REPOSITORY`
7.Press Enter to complete the process and create your local clone.
8.Create a `.env,py` file with your own credentials and import this into the `settings.py` file.
9.Install the requirements.txt file by running the below command in your CLI Terminal:
`pip3 install -r requirements.txt`.
10.Run one of the following commands in your Terminal to launch the Django project:
`python3 manage.py runserver`
11.Click the `http:// link` that loads, and the project should load. If it doesn't load when you click the link, copy and paste it into a new browser tab instead.
12.Run the following commands to migrate the database models and create a super user:
`python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser`
13.In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".
14.Set the following config vars in heroku :

![devices image](static/img/heroku_congig_vars.png)


Once the migrations are completed and the super user has been created successfully, the site should be running locally.

### Amazon Web Services(AWS) - S3

#### Media And Static Folders
In early development of the project `static` and `media` folders were pushed to GitHub. At a later stage both folders were stored on [AWS - S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html) which is a cloud-based storage service from [Amazon](https://aws.amazon.com) for the live version of the site.

To allow you to access all functionality on the site locally, ensure you have created free accounts with the following services: 

-[Stripe](https://stripe.com/)

-[AWS - S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)

#### In Gitpod you create env.py file in main directory and write in first line: import os. Use table below to copy required fields.


![devices image](static/img/env_file.png)




 
##### back to [top](#table-of-contents)
 
---
 
## Credits
 
### Content
 
- [Stipe API](https://stripe.com/) - Database payment integration
 
### Media
 

- [Unsplash](https://unsplash.com/) - Photo by Brook Lark
- [Freepik](https://freepik.com/) -
 
### Acknowledgements
 
I received inspiration for this project from Code Institute - Project Ideas
 
##### back to [top](#table-of-contents)
 
