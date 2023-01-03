<h1 align="center"> Plörrbräu </h1>
<h2 class="logo-font"> Welcome </h2>

<h4>
    This is the business website for the company Plörr GmbH, where the company will more than showcase its products with great detail.
    It will provide extensive information on the business, ingredients, and brewery.
    <br><br>
    Additionally, a great online shop is available to purchase the featured products, which can also be used without registering and has a quick checkout option.<br>
    Regular customers registering would be beneficial, as they would add to the order confirmation email, and also be able to revisit all completed order summaries on their profile page on this website.
    <br><br>
    Plörrbräu wishes all of you the best and hopes that you will have a great time on our website.
</h4>
<br><br>
<h2 align="center"><img src="https://ploerr.s3.eu-central-1.amazonaws.com/readme/top-readme.webp" height="500" width="900"></h2>

[View the live project here](https://ploerr.herokuapp.com/)

<hr>

<h2> Table of content </h2>
<h2> Table of content </h2>

- ### [Strategy](#strategy-1)
  - [Project Goals](#project-goals)
  - [User Demographic](#user-demographic)
- ### [User Stories](#user-stories-1)
- ### [Scope](#scope-1)
  - [Feature Ideas Planning](#feature-ideas-planning)
  - [Functionality Requirements](#functionality-requirements)
- ### [Structure](#structure-1)
  - [Topology Diagrams](#topology-diagrams)
  - [Database Schema and Structure](#database-schema-and-structure)
- ### [Skeleton](#skeleton-1)
  - [Wireframes](#wireframes)
  - [Design](#design)
- ### [Features](#features-1)
  - [Multi Page Elements](#multi-page-elements)
  - [Home/Index Page](#home-index-page)

- ### [Technologies Used](#technologies-used-1)
- ### [Testing](#testing-1)
- ### [Bugs, Issues, and Solutions](#bugs-issues-and-solutions-1)
- ### [Deployment & Local Development](#deployment--local-development-1)
  - [Deployment to Heroku](#deployment-to-heroku)
  - [Local Development](#local-development)
  - [Making Local Clone](#making-local-clone)
- ### [Credits](#credits-1)
  - [Code](#code)
  - [Media](#media)
  - [Resources](#resources)
- ### [Acknowledgements](#acknowledgements-1)
- ### [Copyrights](#copyrights-1)

<hr>

## Strategy
  - ### Project Goals
    * The website should offer an overview of all available products
    * The website should offer detailed information on each product
    * The website should offer detailed information on the business
    * The side is responsive and can be displayed on mobile and desktop devices
    * Provide users the option to register and create an account
    * Provide users the option to buy any listed product on the page
    * Registered users will be able to save and update their delivery information
    * Registered users will be able to review old orders
    * Provide Administrator / User designated as "staff" access to a complete CRUD functionality over products
    * To go along with the joke on beer commercials by Otto Waalkes and still present it as a serious business page<br>
    <small>("Plörr" a short version of "Plörre" means: "Dish Water", "Bräu" is german for "Brew")</small><br>
    <small>Plörrbräu <=> dish water brew</small>
    <br><br>

  - ### User Demographic
    * Anyone who is the owner of their credit card
    * Businesses in the catering trade
    * Customers interested in buying german beer and Plörrbräu
    <br><br>

## User Stories
  - ### Site User Goals - As a Site User I want to be able to
    * know how to get in contact with the brewery so that I can visit the brewery and purchase products right there to save shipping costs
    * Learn more about the brewery and ingredients so that I can have a better understanding of the product and quality
    * Easily register for an account so that I can have a personal account and be able to view my profile
    * quickly log in or log out so I can access my account information
    * have a personalized user profile so that I can view my order history and order confirmations and save my payment information
    * receive an email confirmation after registering so that I can verify that my account registration was successful
    * quickly recover my password so that I can recover access to my account
    <br><br>
  - ### Customer Goals - As a Shopper, I want to be able to:
    * easily select the quantity of a product when purchasing it so that I can ensure that I don't accidentally select the wrong product or quantity
    * adjust the number of individual products in my bag so that I can easily make changes to my purchases before checkout
    * view items in my bag to be purchased so that I can identify the total cost of my purchase and all items I will receive
    * feel my personal and payment information is safe & secure so that I can confidently provide the needed information to make a purchase
    * View an order confirmation after checkout so that I can verify that I have not made any mistakes
    * quickly enter my payment information so that I can check out quickly
    * quickly identify deals and special offers so that I can take advantage of special savings on products I'd like to buy
    * easily view the total of my purchase at any time so that I can avoid spending too much
    * View individual product details so that I can identify the price, description, ingredients, product rating, product image, and volume
    * view a list of all products so that I can select some to purchase
    * receive an email confirmation after checking out so that I can keep the confirmation on what I've purchased for my records
    * search and sort the products so that I can quickly find the product I'm looking for
    <br><br>
  - ### Store Owner Goals - As a Store Owner I want to be able to:
    * add a product so that I can add new items to my store
    * edit/update a product so that I can change product prices, descriptions, images, and other product criteria
    * delete a product so that I can remove items that are no longer for sale
    * offer a link to relevant third-party websites so that I can offer interested customers more information on our ingredients and the quality of our products
    <br><br>
  - ### Mapped User Stories to the project on GitHub:<br>
    [View the project here on GitHub](https://github.com/users/AndrosDe/projects/4)
    <br><br>
<hr>

## Scope
- ### Feature Ideas Planning
  When planning the App features and scope, I drew up an Importance Viability analysis of these features, please see below:

  | # | Feature | Importance | Viability |
  | --- | --- | --- | --- |
  | 1 | Display all products | 5 |5 |
  | 2 | Display products details  | 5 | 5 |
  | 3 | Add products to the shopping bag | 5 | 5 |
  | 4 | Select / update quantity of a products | 5 | 5 |
  | 5 | Remove a product from the shopping bag | 5 | 5 |
  | 6 | Detailed information on the upcoming costs of the shopping bag | 5 | 5 |
  | 7 | Annymos checkout possible | 4 | 5 |
  | 8 | Register, Login and Logout to Account | 5 | 5 |
  | 9 | Email confirmation are sent | 5 | 5 |
  | 10 | User Profile with default delivery information  | 4 | 3 |
  | 11 | Order history in Profile | 4 | 5 |
  | 12 | Secure Payment of Orders | 5 | 5 |
  | 13 | Message System to show important information | 4 | 4 |
  | 14 | Saving Delivery information | 4 | 4 |
  | 15 | Changing profile settings | 4 | 5 |
  | 16 | Information on Plörr | 3 | 4 |
  | 19 | Links to Third-party Websites | 2 | 2 |
  | 20 | Create, Edit, and Delete Products | 5 | 5 |
  | 22 | Search for Products | 1 | 1 |
  | 23 | Going along with the joke | 3 | 2 |

  <br>
  Based on the results of the Feature Ideas Planning, I have decided to attempt to implement most Features, except for 22 as for the current scope of products no such feature is needed. For Stores with more products "Searching and Sorting" would be necessary.
  <br><br>

- ### Functionality Requirements
  * Clean and themed presentation of the products
  * Clean and themed presentation of the products details
  * Clean and themed presentation of the shopping bag
  * Clean and themed presentation of the checkout page
  * Clean and themed presentation of the company
  * Intuitive App navigation
  * Full CRUD functionality on products for store owners
  * Use of Defensive Programming to ensure customers can review their shopping bag before checking out
  * Robust error handling provides information
  <br><br>
<hr>

## Structure
- ### Topology Diagrams
  The green elements in these diagrams illustrate the pages that are accessible to the user.<br>
  The grey elements in these diagrams are the pages not accessible to a particular user.<br>
  <summary><h3><strong>Guest User</strong></h3></summary>
  <details>
    <img src="#" name="GUEST USER JOURNEY ACROSS PLÖRR">
  </details>
  <br>

  <summary><h3><strong>Registered User</strong></h3></summary>
  <details>
    <img src="#" name="REGISTERED USER'S JOURNEY ACROSS PLÖRR">
  </details>
  <br>

  <summary><h3><strong>Administrator / Staff Memeber</strong></h3></summary>
  <details>
    <img src="#" name="STAFF MEMBER'S PERMISSION AND ACCESS ACROSS PLÖRR">
  </details>
  <br>
- ### Database Schema and Structure
  Plörr uses PostgreSQL and was created with Django+sqlparse.
  <summary><p>The current version can be seen below in the details.</p></summary>
  <details>
    <img src="#" name="POSTGRES DATABASES SCHEMA of PLÖRR">
  </details>
<hr>

## Skeleton
  - ### Wireframes
    The wireframes created for this project:
    <summary><h3><strong>Guest User</strong></h3></summary>
    <details>
      - <a href="https://ploerr.s3.eu-central-1.amazonaws.com/readme/wireframes/ploerr-index.png">Index Page</a><br>
      - <a href="https://ploerr.s3.eu-central-1.amazonaws.com/readme/wireframes/ploerr-quality.png">Quality Page</a><br>
      - <a href="https://ploerr.s3.eu-central-1.amazonaws.com/readme/wireframes/ploerr-brewery.png">Brewery Page</a><br>
      - <a href="https://ploerr.s3.eu-central-1.amazonaws.com/readme/wireframes/ploerr-imprint.png">Impressum Page</a><br>
      - <a href="https://ploerr.s3.eu-central-1.amazonaws.com/readme/wireframes/ploerr-gtc.png">AGB Page</a><br>
      - <a href="https://ploerr.s3.eu-central-1.amazonaws.com/readme/wireframes/ploerr-contact.png">Contact Page</a><br>
      - <a href="https://ploerr.s3.eu-central-1.amazonaws.com/readme/wireframes/ploerr-register.png">Register Page</a><br>
      - <a href="https://ploerr.s3.eu-central-1.amazonaws.com/readme/wireframes/ploerr-login.png">Login Page</a><br>
      - <a href="https://ploerr.s3.eu-central-1.amazonaws.com/readme/wireframes/ploerr-profile.png">Profile Page</a><br>
      - <a href="https://ploerr.s3.eu-central-1.amazonaws.com/readme/wireframes/ploerr-products.png">Product Page</a><br>
      - <a href="https://ploerr.s3.eu-central-1.amazonaws.com/readme/wireframes/ploerr-add-product.png">Edit Product Page</a><br>
      - <a href="https://ploerr.s3.eu-central-1.amazonaws.com/readme/wireframes/ploerr-updeate-product.png">Add Product Page Page</a><br>
      - <a href="https://ploerr.s3.eu-central-1.amazonaws.com/readme/wireframes/ploerr-shopping-cart.png">Bag Page</a><br>
      - <a href="https://ploerr.s3.eu-central-1.amazonaws.com/readme/wireframes/ploerr-checkout.png">Checkout Page</a><br>
      - <a href="https://ploerr.s3.eu-central-1.amazonaws.com/readme/wireframes/ploerr-checkout-success.png">Checkout Success Page</a><br>
    </details>

    During the development, the profile and product pages became overcrowded with information and features.
    Therefore these pages were changed and split up into:
    - Products and Product Details
    - Profile and Profile-Settings


  - ### Design
    [Bootstrap5  CSS](https://getbootstrap.com/docs/5.0/getting-started/introduction/) was used for styling and customized for the front-end development.
    [Bootstrap4  JS](https://getbootstrap.com/docs/4.0/getting-started/introduction/) was used for java script as the toast worked better on Bootstrap4 and was customized for the front-end development.

    - #### Typography
      I used Google Fonts to import the fonts I used across the application.

    - #### Imagery & UI
      I used a minimized home page approach and wanted the main focus of the index page to be in the background.<br>
      Which is depicting a looped video of beer being handed out to customers, giving the impression that this must beer a highly requested product.<br>
      This required a color scheme mostly of dark-background / light text, which helps to highlight any colored content on the pages and the inverted color scheme of the messages.
      
    <br><br>
<hr>

## Features
Breakdown of the features and elements implemented for the App.
The CRUD is depicted in the feature with the following color code:
  <ul>
  <span style="color: green">
  <li>
  Green = Create
  </li>
  </span>
  <li>
  White = Read
  </li>
  <span style="color: orange">
  <li>
  Orange = Update
  </li>
  </span>
  <span style="color: red">
  <li>
  Red = Delete
  </li>
  </span>
  </ul>
  <br>

- ## Multi Page Elements
    - ### Header


## Defensive Programming
Keeping the application secure and a protected profile requires the user to be logged in.
Any product creation, updating, or deletion is feature restricted to the administrator.
The payment is handled by stripe and therefore makes sure that the payment process is secure.
The user is always informed of changes via messages.

## Future Implementation
* offer more payment options
* update the model for products by splitting it into two connected models:
  * one for product: Plörr, Plörr Lau
  * one for the container: Single Can, Sixpack, 4x Sixpack, 10l-keg, 25l-keg, 50l-keg
* rating system for customers
* login via social media account
* securing order history to be only viewed by the customer that made the order
<hr>

## Technologies Used
* Languages:
    * [HTML5](https://en.wikipedia.org/wiki/HTML5) was used for the content and structure of the site.
    * [CSS3](https://en.wikipedia.org/wiki/CSS#CSS_3) was used for the styling of the site.
    * [JavaScript](https://en.wikipedia.org/wiki/JavaScript) was used for the interactivity of the site.
    * [Python](https://www.python.org/) was used for the back-end programming of the site.
<br>

* [Stripe](https://dashboard.stripe.com/) 
    * was used to enable and process the payment in the checkout app

* [Amazon Web Services S3 Bucket](https://us-east-1.console.aws.amazon.com/console/home?region=us-east-1) 
    * was used to enable users to upload images for their recipes whilst keeping the App safe and secure
  
* [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
    * Create, configure, and manage AWS services, such as Amazon Elastic Compute Cloud (Amazon EC2) and Amazon Simple Storage Service (Amazon S3).

* [Django](https://www.djangoproject.com/)
    * Django was used to create the models for the database, forms to post data into the database, the templates, and the view connecting them all.

* [Postgres](https://www.postgresql.org/)
    * Postgres was the relational database used to store user registration, login, and authentication. Postgres was also used to store products and orders.

* [pip](https://pip.pypa.io/en/stable/)
    * Pip is the package installer for Python, allowing us to install the packages we need for this site.

* [gunicorn](https://www.dnspython.org/)
    * Dnspython is a DNS toolkit for python.

* [Bootstrap 5 - CSS](https://getbootstrap.com/)
    * Bootstrap is one of the most popular front-end open-source toolkits and was used for ease of styling the pages.

* [Bootstrap 4 - JS](https://getbootstrap.com/)
    * Sadly the Bootstrap 5 JS-source toolkit is not as good as the  Bootstrap 4 counterpart when it came down to toasts.

* [Pillow](https://pypi.org/project/Pillow/)
    * Pillow adds image processing capabilities to the Python interpreter.

* [allauth](https://www.dnspython.org/)
    * Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.

* [crispy-forms](https://www.dnspython.org/)
    * control the rendering behavior of your Django forms in a very elegant and DRY way.

* [django-countries](https://www.dnspython.org/)
    * provides country choices for use with forms, flag icons static files, and a country field for models.

* [Heroku](https://devcenter.heroku.com/)
    * Heroku is where we deploy this live site. Throughout, we have ensured the version being deployed to Heroku matches the development version by checking features and screen layouts on both versions.

* [GitHub](https://github.com/)
    * GitHub is where we host our site.

* [Lunapic](https://www9.lunapic.com/editor/)
    * Lunapic was used to work with images: Background removal, scale, etc.

* [Grammarly:](https://app.grammarly.com/)
    * Grammarly was used for spell-checking.

* [Notepad++:](https://notepad-plus-plus.org/)
    * Notepad++ for keeping notes for the project.

* [WEBP Converter:](https://www.onlineconverter.com/webp)
    * WEBP Converter was used to change *.jpg files to *.webp to reduce the size.

<hr>

## Testing
### All testing undertaken for this project can be found in the [Testing Document](/TESTING.md)
<br>
<hr>

## Bugs, Issues, and Solutions
| # | Bugs, Errors, and Issues | Solutions |
| :--- | :--- | :--- |
| 1 | Purchase confirmation Email not sent | Removed the new updates to deal with the changes in Stripe in November 2022 to the webhook_handler.py code and went with the old code - My Stripe-API-keys were created in October 2022, which might be the reason why only the old code is accepted |
| 2 | Heroku deployment failed - backports.zoneinfo could not be built | Removed backports.zoneinfo==0.2.1 from requirments.txt |
| 3 | Toasts not working with Bootstrap 5 | Used Bootstrap 4 for the JS-toolkit and it worked perfectly
| 4 | CSS for the checkbox is not applied | No solution found so far - as the issue is so minor, it will be ignored

<br>
<hr>

## Deployment & Local Development

The project was deployed to [Heroku](https://www.heroku.com) using the below procedure:

### Deployment to Heroku
### 1. Create a database:
  1. **Log in to ElephantSQL.com** or create an account if required.
  1. **click** the button labeled  **Create New Instance** from the dashboard.
  1. **Set up your plan:**
      * Give your plan a **Name** (I used "poerr" for this project)
      * Select the **Tiny Turtle (Free)** plan
      * Leave the **Tags** field blank
  1. **Select Region** and then choose a data center near you.
  1. **click** the button labeled **Review** and check your details are correct and then click **Create instance**.
  1. Return to the ElephantSQL dashboard and click on the **database instance name** for this project.
  1. In the URL section, clicking the copy icon will copy the database URL to your clipboard (best to leave this tab open, as it might be of use later)

### 2. Heroku Part 1:
  1. **Log in to Heroku** or create an account if required.
  1. **click** the button labeled **New** from the dashboard in the top right corner, just below the header.
  1. From the drop-down menu **select "Create new app"**.
  1. **Enter a unique app name**. I used the same name as the GitHub repository (ploerr) for this project.
  1. Once the web portal shows the green tick to confirm the name is original **select the relevant region.** In my case, I chose Europe as I am in Germany.
  1.  When you are happy with your choice of name and that the correct region is selected, **click** on the **"Create app" button**.

  1. Then navigate to the **settings tab** and scroll down to the **"Config Vars" section**. 
  1. **Click** the button labeled **"Reveal Config Vars"** and **enter** add the following keys and values:

      | Key | Value |
      | :---: | :---: |
      | DATABASE_URL | database url from ElephantSQL |
      | SECRET_KEY | mysecretkey |
      | USE_AWS | true |
      | AWS_ACCESS_KEY_ID | mysecretawskey1
      | AWS_SECRET_ACCESS_KEY | mysecretawskey2
      | STRIPE_PUBLIC_KEY | mypublicstripekey
      | STRIPE_SECRET_KEY | mysecretstripekey
      | STRIPE_WH_SECRET | mywebhooksecretkey

  1. Leave this tab open for later. 
### 3. Project preparation in Gitpod:
  1. Open up your Gitpod tab
  1. To connect to an external database, install **dj_database_url** and **psycopg2** via the **terminal**.
  ```
    $  pip3 install dj_database_url==0.5.0 psycopg2
  ```
  3. update the **requirements.txt** file with the newly installed packages
  ```
    $  pip freeze > requirements.txt
  ```
  4. In the **settings.py** file, import dj_database_url **underneath the import for os**
  ```
    import os
    import dj_database_url
  ```
  5. In the **DATABASES** section update the code to connect to the new **ElephantSQL database**. Then save the settings.
  ```
    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.sqlite3',
    #         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #     }
    # }
     
 DATABASES = {
     'default': dj_database_url.parse('your-database-url-here')
 }
  ```
  6. Run the **showmigrations** command in the terminal
  ```
    $  python3 manage.py showmigrations
  ```
  7. Migrate the database models to the new database
  ```
    $  python3 manage.py migrate
  ```
  8. Create a superuser for the new database
  ```
    $  python3 manage.py createsuperuser
  ```
  9. To prevent exposing the **ElephantSQL database** when pushing to GitHub, delete it again from settings.py, as it will be set up using an environment variable after the first deployment.<br>
  Reconnect to the local sqlite database.

  ```
    DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
     }
    }
  ```

### 4. Heroku Part 2:
  1. Scroll back to the top of the settings page, and **navigate to the "Deploy" tab.**
  1. From the deploy tab **select Github as the deployment method**.
  1. **Confirm** you want to **connect to GitHub**.
  1. **Search** for the **repository name** and **click** the **connect** button next to the intended repository.
  1. From the bottom of the deploy page **select your preferred deployment type** by following one of the below steps:  
    * Clicking either "Enable Automatic Deploys" for automatic deployment when you push updates to Github.  
    * Select the correct branch for deployment from the drop-down menu and click the "Deploy Branch" button for manual deployment.

### Local Development
* How to Fork To fork the repository, use the following steps:
Login or signup to Github and locate the repository.
Click the Fork button in the top right corner

### Making Local Clone
1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/AndrosDe/ploerr
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/AndrosDe/ploerr
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

<hr>

## Credits
### Code
  * This project was heavily influenced by the "Boutique Ado"-Project from Code Institute / [Chris Z.](https://github.com/ckz8780).<br>
  Especially the checkout app, stripe, and java scripts, as they were very well made and exactly what I was looking for implementing into my store part of the project.<br>
  The biggest difference is, that I prefer to use more bootstrap classes and less custom css.
  * CSS Font Border - [code:](https://stackoverflow.com/questions/2570972/css-font-border)
  * Youtube implementation - [w3schools](https://www.w3schools.com/html/html_youtube.asp)
  * Responsive iFrames - [w3schools](https://www.w3schools.com/howto/howto_css_responsive_iframes.asp)
  * Google maps - [w3schools](https://www.w3schools.com/graphics/google_maps_intro.asp)
### Media
  * #### Videos
    * The main background video on the index page was Stock footage provided by <a class="link author-link-popup" target="_blank" href="https://www.videvo.net/profile/videvo">Videvo</a>, downloaded from <a class="videvo-redirect" target="_blank" href="https://www.videvo.net">videvo.net</a>
    * The middle video on the brewery page was Stock footage provided by <a class="link author-link-popup" target="_blank" href="https://www.videvo.net/profile/vidfy-Pressmaster">Pressmaster</a>, downloaded from <a class="videvo-redirect" target="_blank" href="https://www.videvo.net">videvo.net</a>

  * #### Pictures
    * All used pictures were changed/modified and are mostly only used for testing purposes
    * Beerkegs:
      * Photo by <a href="https://unsplash.com/@elevatebeer?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Elevate</a> on <a href="httpshttps://www.pexels.com/de-de/foto/stapel-zylinder-silberfass-tank-lot-1267328/">Unsplash</a>
      * Photo by <a href="https://unsplash.com/@elevatebeer?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Elevate</a> on <a href="https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
      * Image by Image by <a href="https://pixabay.com/users/hans-2/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=295568">Hans</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=295568">Pixabay</a>
    * Beercan:
      * Photo by <a href="https://unsplash.com/@steadyhandco?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Steady Hand Co.</a> on <a href="https://unsplash.com/s/photos/beer-can?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
    * Brewery:
      * Photo by <a href="https://unsplash.com/@elevatebeer?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Elevate</a> on <a href="https://www.pexels.com/de-de/foto/blauer-plastikeimer-1267361/">pexels</a>
      * Photo by cottonbro studio: <a href="https://www.pexels.com/de-de/foto/industrie-technologie-fabrik-eisen-5532668/">pexels</a>
      * Photo by cottonbro studio: <a href="https://www.pexels.com/de-de/foto/alkohol-glas-trinken-drinnen-5532994/">pexels</a>
      * The rest of the pictures allow nonprofit usage

### Resources
* The README was strongly influenced by my project [RND|Roll](https://github.com/AndrosDe/rndroll), which in turn was influenced by Joy Zadan and her awesome project [PALEO RECIPES](https://github.com/JoyZadan/paleo-recipes)

<hr>

## Acknowledgements
* Big Thank you to [Chris Z.](https://github.com/ckz8780), as the "Boutique Ado"-Project helped me with a lot of the code for this project.<br>
I especially liked the approach to the base.html, as it provides a lot of options for all other templates with the extra code blocks right from the start.
* [eRcht24](https://www.e-recht24.de) for the free (german) templates of the Imprint and GTC
* Special mention and thanks to my mentor, Dario Carrasquel, for his support and insights

<hr>

## Copyrights
&copy; 2022 Plörr by Andreas Beier