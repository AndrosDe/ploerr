<h1 align="center"> 𝔓𝔩ö𝔯𝔯𝔟𝔯ä𝔲 </h1>
<h2 class="logo-font"> Welcome </h2>

<h4>
    This is the business website for the company 𝔓𝔩ö𝔯𝔯 GmbH, where the company will more than showcase its products with great detail.
    It will provide extensive information on the business, ingredients, and brewery.
    <br><br>
    Additionally, a great online shop is available to purchase the featured products, which can also be used without registering and has a quick checkout option.<br>
    Regular customers registering would be beneficial, as they would add to the order confirmation email, and also be able to revisit all completed order summaries on their profile page on this website.
    <br><br>
    𝔓𝔩ö𝔯𝔯𝔟𝔯ä𝔲 wishes all of you the best and hopes that you will have a great time on our website.
</h4>
<br><br>
<h2 align="center"><img src="https://ploerr.s3.eu-central-1.amazonaws.com/readme/top-readme.webp" height="500" width="900"></h2>

[View the live project here](https://ploerr.herokuapp.com/)

<hr>

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
  - [Home/Index Page](#homeindex)
  - [Quality](#quality)
  - [Brewery](#brewery)
  - [Contact](#contact)
  - [Imprint](#imprint)
  - [Private Policy](#privacy-policy)
  - [GTC](#gtc)
  - [Products](#products)
  - [Product Details](#product-details)
  - [Bag](#bag)
  - [Checkout](#checkout)
  - [Checkout Success](#checkout-success)
  - [Register](#register)
  - [Login](#login)
  - [Reset Password](#reset-password)
  - [Profile](#profile)
  - [Profile Settings](#profile-settings)
  - [Change Password](#change-password)
  - [Product Mangement](#product-mangement)
  - [Edit Product](#edit-product)
  - [Delete Product](#delete-product)
- ### [Defensive Programming](#defensive-programming-1)
- ### [SEO-Dokumentation](#seo-dokumentation-1)
- ### [Future Implementation](#future-implementation-1)
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
    <img src="https://ploerr.s3.eu-central-1.amazonaws.com/readme/topology-diagram/ploerr-authorisation-visitor.webp" name="GUEST USER JOURNEY ACROSS PLÖRR">
  </details>
  <br>

  <summary><h3><strong>Registered User</strong></h3></summary>
  <details>
    <img src="https://ploerr.s3.eu-central-1.amazonaws.com/readme/topology-diagram/ploerr-authorisation-user.webp" name="REGISTERED USER'S JOURNEY ACROSS PLÖRR">
  </details>
  <br>

  <summary><h3><strong>Administrator / Staff Memeber</strong></h3></summary>
  <details>
    <img src="https://ploerr.s3.eu-central-1.amazonaws.com/readme/topology-diagram/ploerr-authorisation-admin.webp" name="STAFF MEMBER'S PERMISSION AND ACCESS ACROSS PLÖRR">
  </details>
  <br>
- ### Database Schema and Structure
  Plörr uses PostgreSQL and was created with Django+sqlparse.
  <summary><p>The current version can be seen below in the details.</p></summary>
  <details>
    <img src="https://ploerr.s3.eu-central-1.amazonaws.com/readme/database-schema/ploerr-database.webp" name="POSTGRES DATABASES SCHEMA of PLÖRR">
  </details>
<hr>

## Skeleton
  - ### Wireframes
    The wireframes created for this project:
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

    Last-minute additions were:
    - the private policy page, which is a wireframe copy of the Imprint Page
    - a custom 404-Error-Page with just standard wireframe from the base with centered text in the content block
    - the confirm deletion page, which is a wireframe copy of the Product Detail Page.


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
      ![Header of 𝔓𝔩ö𝔯𝔯](https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-header-nav.webp)
      <details>
      <summary><strong>General Features of the Header</strong></summary>
        <ul>
          <li>
          Logo
          </li>
        </ul>
        <br>
        Navigation to:
        <ul>
          <li>
          Home (Link is in the Logo)
          </li>
          <li>
          Registration
          </li>
          <li>
          Login
          </li>
          <details>
          <summary>Image</summary>
          <img src="https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-header-nav-account-2.webp" name="navigation dropdown">
          </details>
          <li>
          Shopping Bag
          </li>
          <li>
          Products
          </li>
          <li>
          Quality
          </li>
          <li>
          Brewery
          </li>
        </ul>
      </details>
      <br>
      <details>
      <summary><strong>Features of the Header for authenticated users </strong></summary>
        Navigation to:
        <ul>
          <li>
          Profile
          </li>
          <li>
          Logout
          </li>
          <details>
          <summary>Image</summary>
          <img src="https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-header-nav-account-3.webp" name="navigation links for user">
          </details>
        </ul>
      </details>
      <br>
      <details>
      <summary><strong>Features of the Header for Shop Owners </strong></summary>
        Navigation to:
        <ul>
          <li>
          Product Management
          </li>
          <details>
          <summary>Image</summary>
          <img src="https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-header-nav-account.webp" name="navigation links for shop owners">
          </details>
        </ul>
      </details>
      <br>

    - ### Footer
      ![Footer of 𝔓𝔩ö𝔯𝔯](https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-footer-nav.webp)
      <details>
        <summary>Link to Facebook Business Page</summary>
      </details>
      <details>
        <summary>Subscription to Newsletter</summary>
      </details>
      <details>
        <summary>Nagigation to:</summary>
        <ul>
          <li>
            Contact
          </li>
          <li>
            Imprint
          </li>
          <li>
            Privacy Policy
          </li>
          <li>
            GTC
          </li>
        </ul>
      </details>
      <br>

    - ### Messages
      <details>
      <summary>4 Types of messages:</summary>
      <ul>
        <details>
          <summary>Success</summary>
          <img src="https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-messages.webp" name="Message">
        </details>
        <details>
          <summary>Info</summary>
        </details>
        <details>
          <summary>Warining</summary>
        </details>
        <details>
          <summary>Error</summary>
        </details>
      </ul>
      </details>
      
      <details>
      <summary>If one or more products have been placed in the bag, it will show a content overview of the bag with:</summary>
      <ul>
          <li>
            the total amount of items in your bag
          </li>
          <li>
            list of the products with image, name, and quantity 
          </li>
          <li>
            price, deposit total, shipping costs, grand total
          </li>
          <li>
            link to the shopping bag
          </li>
          <li>
            link to the checkout page
          </li>
          <details>
          <summary>Image</summary>
          <img src="https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-messages-2.webp" name="Message with bag contents">
          </details>
      </ul>
      </details>
  <br>
- ## Home/Index
  <details>
    <summary>Background video in a loop of "beer being handed out to customers"</summary>
  </details>
  <details>
    <summary>A friendly greeting</summary>
  </details>
  <details>
    <summary>Promotion of new products</summary>
  </details>
  <details>
    <summary>Image</summary>
    <img src="https://ploerr.s3.eu-central-1.amazonaws.com/readme/testing/Chromebook-Pixel-1280x850.webp" name="Index Page of Plörr">
  </details>
  <br>
- ## Quality
  <details>
    <summary>Detailed information on the ingredients of Plörrbräu</summary>
  </details>
  <details>
    <summary>Image</summary>
    <img src="https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-quality-1.webp" name="Quality Page of Plörr">
  </details>
  <br>
  <details>
    <summary>External link to local farmers</summary>
  </details>
  <details>
    <summary>Image</summary>
    <img src="https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-quality-link.webp" name="Link and video of local farmers">
  </details>
  <br>
- ## Brewery
  <details>
    <summary>Detailed information on the History of the Plörrbräu and the brewing process</summary>
  </details>
  <details>
    <summary>Image</summary>
    <img src="https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-brewery-1.webp" name="Brewery Page of Plörr">
  </details>
  <br>
- ## Contact
  <details>
    <summary>Google Map with a custom marker for the 𝕻𝖑𝖔𝖗𝖗 GmbH</summary>
  </details>
  <details>
    <summary>Directions</summary>
  </details>
  <details>
    <summary>Email, Fax, and Phone contact information</summary>
  </details>
  <details>
  <details>
  <summary>Image</summary>
  <img src="https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-contact-1.webp" name="Contact Page of Plörr">
  </details>
  <br>
- ## Imprint
  <details>
    <summary>The Imprint page with all the required information on the 𝕻𝖑𝖔𝖗𝖗 GmbH</summary>
  </details>
  <details>
    <summary>Image</summary>
    <img src="https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-imprint-1.webp" name="Imprint Page of Plörr">
  </details>
  <br>
- ## Privacy Policy
  <details>
    <summary>Overview of the Privacy Policy</summary>
  </details>
  <details>
    <summary>Image</summary>
    <img src="https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-private-policy.webp" name="Privacy Policy Page of Plörr">
  </details>
  <br>
- ## GTC
  <details>
    <summary>Overview of the General Terms and Conditions</summary>
  </details>
  <details>
    <summary>Image</summary>
    <img src="https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-gtc-1.webp" name="GTC Page of Plörr">
  </details>
  <br>
- ## Products
  <details>
    <summary>Overview of all products with image, price, and product rating</summary>
  </details>
    <details>
    <summary>Link to the products details</summary>
  </details> 
  <details>
    <summary>Image</summary>
    <img src="https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-products.webp" name="Product Overview of Plörr">
  </details>
  <br>
- ## <span style="color: orange">Product Details</span>
  <span style="color: orange"><details></span>
  <summary>Detailed information about a product</summary>
    <ul>
      <li>
      Name
      </li>
      <li>
      Image
      </li>
      <li>
      Description
      </li>
      <li>
      Price
      </li>
      <li>
      Volumen
      </li>
      <li>
      Deposit
      </li>
      and a lot more...<br>
      <details>
      <summary>Image</summary>
      <img src="https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-products-details.webp" name="Product Details">
      </details>
    </ul>
  </details>
  <span style="color: orange"><details></span>
    <summary>Option to set the quantity</summary>
    <span style="color: orange">
    <ul>
      <details>
      <summary>Image</summary>
      <img src="https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-products-quantity.webp" name="Quantity selector">
      </details>
    </ul>
    </span>
  </details>
  <span style="color: orange"><details></span>
    <summary>Add to Bag - Feature</summary>
    <span style="color: orange">
    <ul>
      <details>
      <summary>Image</summary>
      <img src="https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-products-details-addtobag.webp" name="Add to Bag">
      </details>
    </ul>
    </span>
  </details>
  <br>
- ## <span style="color: orange">Bag</span>
  <details>
  <summary>List of the bags content with</summary>
    <ul>
    <li>
    image
    </li>
    <li>
    Name
    </li>
    <li>
    Volume
    </li>
    <li>
    Price
    </li>
    <li>
    Deposit
    </li>
    <li>
    Subtotal
    </li>
    <li>
    Subtotal - Deposit
    </li>
      <details>
      <summary>Image</summary>
      <img src="https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-shopping-cart-1.webp" name="Shopping Bag Page of Plörr">
      </details>
    </ul>
  </details>
  <span style="color: orange"><details></span>
    <summary>Option to set the quantity</summary>
    <span style="color: orange">
    <ul>
      <details>
      <summary>Image</summary>
      <img src="https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-products-quantity.webp" name="Checkout Success Page of Plörr">
      </details>
    </ul>
    </span>
  </details>
  <span style="color: red"><details></span>
    <summary>Remove item from the Bag</summary>
    <span style="color: red">
    <ul>
      <details>
      <summary>Image</summary>
      <img src="https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-shopping-cart-1.webp" name="Checkout Success Page of Plörr">
      </details>
    </ul>
    </span>
  </details>
  <br>
- ## <span style="color: orange">Checkout</span>
  <details>
    <summary>Summary of the order</summary>
  </details>
  <details>
    <summary><span style="color: orange">Checkout Form with Billing and Delivery Information</span></summary>
    <ul>
      This can be prefilled for logged-in Users if they have added this information to the Profile page.
    </ul>
  </details>
  <details>
    <summary><span style="color: orange">Option to safe DeliveryInformation to Profile for logged in Users</span></summary>
  </details>
  <details>
    <summary>Secure Payment Form for Credit Cards</summary>
  </details>
  <details>
    <summary>Adjust Bag Option, which takes the user back to the bag</summary>
  </details>
  <details>
    <summary><span style="color: green">Complete Order Option</span></summary>
      <ul>
        This will create the order.
      </ul>
      <ul>
        This will send a confirmation email for this order.
      </ul>
  </details>
  <details>
    <summary>Image 1</summary>
    <img src="https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-checkout-1.webp" name="Checkout Page of Plörr">
  </details>
  <details>
    <summary>Image 2</summary>
    <img src="https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-checkout-2.webpp" name="Checkout Page of Plörr">
  </details>
  <br>
- ## Checkout Success
  <details>
    <summary>Summary of the order</summary>
  </details>
  <details>
    <summary>Image</summary>
    <img src="https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-checkout-success-1.webp" name="Checkout Success Page of Plörr">
  </details>
  <br>
- ## Register
  <details>
    <summary>creates a new account</summary>
  </details>
  <details>
    <summary>error messages are in a different color</summary>
  </details>
  <details>
    <summary>offers a link to the login page</summary>
  </details>
  <details>
    <summary>will send a confirmation email with a confirmation link</summary>
  </details>
  <br>
- ## Login
  <details>
  <summary>General Features of Login</summary>
  <ul>
    <li>
      offers a link to the registration page
    </li>
    <li>
      offers a link to the password reset page
    </li>
  </ul>
  </details>
  <details>
  <summary>Features of Login for authenticated users</summary>
  <ul>
    <li>
      log into the user account
    </li>
  </ul>
  </details>
  <br>
- ## Reset Password
  <details>
  <summary>will send an email with a link to reset the password</summary>
  </details>
  <br>
- ## Profile
  <details>
  <summary>Features for authenticated users</summary>
    <ul>
      <li>
      Section 1
        <ul>
          <li>
            User Details:
            <ul>
              <li>
                Username
              </li>
              <li>
                Name
              </li>
              <li>
                Email
              </li>
            </ul>
          </li>
          <li>
            Link to Profile Settings
          </li>
          <li>
            Link to Change Password (update password)
          </li>
        </ul>
      </li>
      <br>
      <li>
      Section 2 - Default Delivery Form:
        <ul>
          <li>
            Display any previously saved data of:
            <ul>
              <li> 
                Phone Number
              </li>
              <li>
                Postal Code
              </li>
              <li>
                Town or City
              </li>
              <li>
                Street Address 1
              </li>
              <li>
                Street Address 2
              </li>
              <li>
                County, State, or Locality
              </li>
              <li>
                Country
              </li>
            </ul>
          </li>
          <span style="color: orange">
            <li>
              Update Data in Delivery Form.
            </li>
          </span>
        </ul>
      </li>
      <br>
      <li>
      Section 3 - Order history:
        <ul>
          <li>
            Displaying all previously made orders
          </li>
          <li>
            Links to the order summary of checkout success for these specific orders
          </li>
        </ul>
      </li>
    </ul>
    
    <details>
    <summary>Image</summary>
      <img src="https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-profile-1.webp" name="Profile Page of Plörr">
    </details>
  </details>
  <br>
- ## <span style="color: orange">Profile Settings</span>
  <details>
    <summary><span style="color: orange">Features for authenticated users:</span></summary>
    <span style="color: orange">
    Edit Function for:
    <ul>
      <li>
        Username
      </li>
      <li>
        First Name
      </li>
      <li>
        Last Name
      </li>
      <li>
        Email
      </li>
    </ul>
    </span>
  </details>
  <br>
- ## <span style="color: orange">Change Password</span>
  <details>
    <summary><span style="color: orange">Features for authenticated users:</span></summary>
    <span style="color: orange">
    <ul>
      Update Password        
    </ul>
    </span>
  </details>
  <br>
- ## <span style="color: green">Product Mangement</span>
  <details>
  <summary><span style="color: green">Features for Shop Owners:</span></summary>
    <span style="color: green">
    <ul>
      Add a new Product<br>
      <details>
      <summary>Image</summary>
      <img src="https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-header-nav-account.webp" name="Product Management of Plörr">
      </details>
    </ul>
    </span>
  </details>
  <br>
- ## <span style="color: orange">Edit Product</span>
  <details>
  <summary><span style="color: orange">Features for Shop Owners:</span></summary>
    <span style="color: orange">
    <ul>
      Update a Product<br>
      <details>
      <summary>Image 1</summary>
      <img src="https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-products-admin.webp" name="Edit Product in Products">
      </details>
      <details>
      <summary>Image 2</summary>
      <img src="https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-products-details-admin.webp" name="Edit Product in Product Details">
      </details>
    </ul>
    </span>
  </details>
  <br>
- ## <span style="color: red">Delete Product</span>
  <span style="color: red"><details></span>
  <summary><span style="color: red">Features for Shop Owners</span></summary>
    <span style="color: red">
    <ul>
      Delete a Product<br>
      <details>
      <summary>Image 1</summary>
      <img src="https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-products-details-admin.webp" name="Delete Product in Product Details">
      </details>
      <details>
      <summary>Image 2</summary>
      <img src="https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-products-admin.webp" name="Delete Product in Products">
      </details>
    </ul>
    </span>
  </details>

## Defensive Programming
To keep the application secure and the profile/profile information protected requires the user to be logged in if they want to save delivery information. Users have only access to their profile and delivery information.<br>
The user is always informed of changes via messages. A custom 404-Error Page was created.<br>
Stripe handles the payment and makes sure that the payment process is secure.<br>
Any product creation, updating, or deletion is feature restricted to the administrator. All deletions of products require a confirmation.<br><br>
To access an order-summary the  order number is required.<br>The order number is randomly created and only given to the customer of that purchase. A security breach outside this app/website (for example: customers email account was compromised, etc.) is required  to have any effect.

## SEO-Dokumentation
- ### Advertising Strategy
    As the website is about a brewery, beer, and spirits dealer there are a lot of options for commercial placements, like TV & Radio Commercials, sponsoring sports teams, banners, flyers, and so on.<br>
    However, the 𝔓𝔩ö𝔯𝔯 GmbH is a smaller company and therefore has to rely on more cost-efficient commercial placements.<br><br>
    The best options for that social media interactions and newsletters:<br>
    Therefore a Facebook business page has been created and is connected to the website.
    <details>
      <summary>Image</summary>
      <img src="https://ploerr.s3.eu-central-1.amazonaws.com/readme/facebook-page.webp" name="Facebook Business Page">
    </details>
    <br>
    Right next to the Facebook link on the website is the option to subscribe to a newsletter via MailChimp.
    <details>
      <summary>Image</summary>
      <img src="https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-footer-nav.webp" name="Facebook and Newsletter">
    </details>
    <br>

- ### Website Planning
  Before the website was created keywords and keyphrases were brainstormed:
  1.  A list of words associated with beer/brewery by using a [Thesaurus](https://www.thesaurus.com/):
      - beer -> ale, brew, brewage, refreshment
      - brewery -> brewhouse
  <br><br>
  2.  As the product is supposed to be "cheap" better wording was needed.<br>
    In the end, it was the consensus that the product was to be marked as:
      - inexpensive brew/ale/beer
  <br><br>
  3.  As mentioned in the [Project Goals](#project-goals):
    Plörrbräu <small>(-> Dishwaterbrew)</small> is based on a joke by Otto Waalkes and makes fun of beer commercials.
    The joke 𝔓𝔩ö𝔯𝔯𝔟𝔯ä𝔲 was presented in two variances:
      - normal 𝔓𝔩ö𝔯𝔯
      - 𝔓𝔩ö𝔯𝔯 Lau <small>(-> half-hearted, lukewarm)</small>
    The challenge is to go along with the joke and still be a serious business website and promote the product.<br>
    Therefore normal 𝔓𝔩ö𝔯𝔯 will be promoted as high carbonated, sparkling and 𝔓𝔩ö𝔯𝔯 Lau as low carbonated, smooth brew
  <br><br>
  4.  Health and untreated products are a big concern for most customers nowadays. For that reason the products will be promoted as:
      - being naturally carbonated
      - having no exogen food additive 290
      - being made with local natural reserve water and from local ingredients
  <br><br>
  5.  To find keywords with a good volume and low competition rate [wordtraker](https://www.wordtracker.com/) was used and yielded the following additional keywords:
      - brewing company
      - craft beer near me
      - german beers
  <br><br>
  6.  This led to the creation of the final keywords list:
      - brewing company
      - beer near me
      - german beer
      - brewhouse
      - inexpensive brew/ale/beer
      - smooth brew
      - sparkling brew
      - beer from local ingredients
      - local natural reserve water
      - traditional german beer brewing
      - traditional brew
  <br><br>
- ### Implementing Keywords into Website:
  By taking inspiration from the brewing company [Pott's](https://www.potts.de/) it was decided to give visitors of the website a lot of information about the company, the ingredients, the brewing process, and the products themselves.<br>
  This way it was possible to insinuate that the products must be of high quality without stating it anywhere on the website. It does the opposite, but in a context that makes it appear to be something good.
  <br><br>
    As the index page is styled to have the [backgound as the main stage](https://usersnap.com/blog/background-webdesign/), the content has to be diverted to other pages. This led to the creation of:
  <ul>
    <li>
      quality.html
    </li>
    <li>
      brewery.html
    </li>
      This was a great opportunity to insert certain keywords into these pages as part of their content without looking out of place, like putting "beer from local ingredients", "local natural reserve water" into the quality.html, and "traditional german beer brewing" into brewery.html.<br>
      These pages add a lot of value, as a site user find out more information on the company and the product.
  </ul>
  <br>
    To give the appearance of a serious business page, the following pages were added to the footer in an extra navigation bar at the bottom of the page:
  <ul>
    <li>
      contact.html
    </li>
    <li>
      imprint.html
    </li>
    <li>
      privacypolicy.html
    </li>
    <li>
      GTC.html
    </li>
    While being mostly dry text pages, they display all needed information policywise and open the door for business-to-business deals.
    In the contact.html the keyword "beer near me" was able to be implemented into the meta description, as it does make sense content-wise.
  </ul>
  <br>
    Another great place to use the meta description was the products.html, as it allowed to insert the keyword "inexpensive ale & beer" in a kind of stealthy but still appropriate way.
  <br><br>
- ### Pictures, Videos, and external sources:
  One of the biggest successes is the index page with the video of "beer being handed out to customers" running in a loop.<br>It is supposed to subtly encourage a desire to get a beer or a drink and according to our website testers, it seems to work quite well.
  <br><br>
  The video and pictures in brewery.html also underline the professional tone of the website, helping to build trust in the company and insinuate a high-quality product.
  <br><br>
  As finding external resources for a brewing company is challenging, but the quality.html opened up a great opportunity to link to [local framers](https://www.magdochjeder.de/) and display a youtube video from them, that fits the content of the page. This is helping to make the company appear more open, friendly, and less corporate.

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
  * Mailchimp PopUp on Click -[Rahman Zeb](https://rahmanzeb.com/how-to-make-mailchimps-popup-window-appear-with-click-only/)
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