<h1 align="center"> PLÖRR Testing Documentation </h1>
<h2 align="center"><img src="https://ploerr.s3.eu-central-1.amazonaws.com/readme/top-readme.webp" height="500" width="900"></h2>

<hr>
<br>

<h2> Table of content </h2>

- ### [MANUAL TESTING](#manual-testing-1)
- ### [Validation Results](#validation-results-1)
- ### [Responsive Design Testing](#responsive-design-testing-1)
- ### [Testing User Stories](#testing-user-stories-1)

<br>
<hr>
<br>

## MANUAL TESTING
Preliminary Setup:
Created: 
* User: Superuser - admin
* User: abeier
* Products: Plörr - Singel Can, Plörr Lau - Singel Can, Plörr - Sixpack, Plörr Lau - Sixpack, Plörr - 4x Sixpack, Plörr Lau - 4x Sixpack, Plörr - 10l-Keg, Plörr Lau - 10l-Keg, Plörr - 25l-Keg, Plörr Lau - 25l-Keg, Plörr - 50l-Keg, Plörr Lau - 50l-Keg
* Test Order: 90B44FA42CD14B198D96D141553E943E, CCB08426FED9446286DEF94A5A8B04DB, 770176D77BA04048A2285888CC5896D3
<br> This will serve as test content in the following tests.

1. Test runs - Visitor access:
    * a) Reviewing visitor journey through the PLÖRR-Website.<br> Visitors can access and use the following features:
        | # | Site | Feature | Expected Outcome | Result |
        | :--- | :--- | :--- | :--- | :--- |
        | 1 | index | content is visible | pass | pass |
        | 2 | index | Navigation links | pass | pass |
        | 3 | products | content is visible | pass | pass |
        | 4 | products | link to product details | pass | pass |
        | 5 | products | filter products by category | pass | pass |
        | 6 | products | edit & delete function | fail | fail - these features are only visible to Store Owners |
        | 7 | product_details | content is visible | pass | pass |
        | 8 | product_details | quantity can be selected  | pass | pass |
        | 9 | product_details | "Add To Bag" - button adds the product with the selected quantity to the bag | pass | pass |
        | 10 | - | "Message: Success" is shown, with the bag contents visible | pass | pass |
        | 11 | - | "Message: Success" links to bag | pass | pass |
        | 12 | - | "Message: Success" links to checkout | pass | pass |
        | 13 | quality | content is visible | pass | pass - the youtube video might need a refresh of the page to start up |
        | 14 | quality | link to third-party website | pass | pass |
        | 15 | brewery | content is visible | pass | pass |
        | 16 | impressum | content is visible | pass | pass |
        | 17 | agb | content is visible | pass | pass |
        | 18 | contact | content is visible | pass | pass |
        | 19 | bag | content is visible | pass | pass - either the selected products or "bag is empty" |
        | 20 | bag | products can be removed | pass | pass |
        | 21 | bag | products quantity can be updated | pass | pass |
        | 22 | bag | bag total, weight, deposit total, shipping costs, grand total are displayed | pass | pass - they change according to the products and quantity in the bag |
        | 23 | checkout | content is visible | pass | pass |
        | 24 | checkout | order summary is visible | pass | pass |
        | 25 | checkouts | save delivery information | fail | fail -  You need to be logged in to have that feature |
        | 26 | checkout | prompted to login or create account under the delivery information| pass | pass -  not needed to complete the order |
        | 27 | checkout | enter credit card details | pass | pass |
        | 28 | checkout | complete order (with correct credit card details) | pass | pass |
        | 29 | checkout_success | content (Oder Summary)  is visible | pass | pass |
        | 30 | checkout | email confirmation is send | pass | pass |
        | 31 | login | content is visible | pass | pass |
        | 32 | password_reset | content is visible | pass | pass |
        | 33 | signup | content is visible | pass | pass |
        | 34 | - | email confirmations are sent| pass | pass |
        | 35 | - | messages are shown| pass | pass |
        | 36 | privacy policy | content is visible | pass | pass |

        Conclusion:<br>
        The visitor has exactly as much access to the Plörr-Website and Online Shop as intended.
        All information on the business and the product are visible and purchases can be done anonymously.

    * b) Reviewing visitor access by manually posting the URLs in the address bar:
        | # | Site | Feature | Expected Outcome | Result |
        | :--- | :--- | :--- | :--- | :--- |
        | 1 | 404 | Custom Error-Page | pass | pass - if a site is not available the error page is displayed |
        | 2 | profile | content is visible | fail | fail - redirected to login page |
        | 3 | password_change | content is visible | fail | fail - redirected to login page |
        | 4 | profile_settings | content is visible | fail | fail - redirected to login page |
        | 5 | add_product | content is visible | fail | fail - redirected to login page |
        | 6 | edit_product | content is visible | fail | fail - redirected to login page |
        | 7 | delete_product | product is deleted | fail | fail - redirected to login page |
        | 8 | order_history | content is visible | pass | pass - sadly that is true for all orders |
        | 9 | containers | access to the containers page | fail | fail - redirected to login page |
        | 10 | add_containers | access to the add containers page | fail | fail - redirected to login page |
        | 11 | edit_containers | access to the edit containers page | fail | fail - redirected to login page |
        | 12 | delete_containers | access to the delete containers page | fail | fail - redirected to login page |
        | 13 | description | access to the product description page | fail | fail - redirected to login page |
        | 14 | add_description | access to the add product description page | fail | fail - redirected to login page |
        | 15 | edit_description|access to the edit product description page | fail | fail - redirected to login page |
        | 16 | delete_description | access to the delete product description page | fail | fail - redirected to login page |
        | 17 | productmanagement | access to the product management page | fail | fail - redirected to login page |
        | 18 | add_product_review | access to the add product review page | fail | fail - redirected to login page |
        | 19 | edit_product_review | access to the edit product review page | fail | fail - redirected to login page |

        Conclusion:<br>
        As expected the visitor is prohibited from using any other feature that would require to be logged in.<br>
        The greatest downside is that everyone could look up any order summary.
        However, to do that, the order number is needed. This number is randomly generated and only known to the customer and our administrators.<br><br>
        
2. Test runs - Registered User access:
    User used: abeier
    
    * a) Reviewing user journey through the PLÖRR-Website.<br> User can access and use the following features:
        | # | Site | Feature | Expected Outcome | Result |
        | :--- | :--- | :--- | :--- | :--- |
        | 1 | profile | content is visible | pass | pass |
        | 2 | profile | delivery information can be updated | pass | pass |
        | 3 | profile | "Message: Success" is displayed without the bag contents | pass | pass |
        | 4 | profile | rate product feature visible | pass | pass |
        | 5 | profile | list of rated products, once the user rated a product | pass | pass |
        | 6 | profile | edit / delete product rating visible | pass | pass |
        | 7 | add_profile_review | able to rate a product | pass | pass |
        | 8 | edit_profile_review | edit exsitng rating | pass | pass |
        | 9 | delete_profile_review | # | pass | pass |
        | 10 | password_change | content is visible | pass | pass |
        | 11 | password_change | password can be changed | pass | pass |
        | 12 | profile_settings | content is visible | pass | pass |
        | 13 | profile_settings | username, name & email can be updated | pass | pass |
        | 14 | checkout | save delivery information | pass | pass |
        | 15 | checkout | save delivery information checkbox is red | pass | fail - for some reason the css is not applied |
        | 16 | logout | content is visible | pass | pass |
        | 17 | logout | able to log out from the profile | pass | pass |

        Conclusion:<br>
        In addition to all the normal visitor access logged in users have some little conveniences with their profile, where they can update delivery and personal information, as well as an overview of all previously made orders.
    
    * b) Reviewing user access by manually posting the URLs in the address bar:
        | # | Site | Feature | Expected Outcome | Result |
        | :--- | :--- | :--- | :--- | :--- |
        | 1 | add_product | content is visible | fail | fail - error message shown |
        | 2 | edit_product | content is visible | fail | fail - error message shown |
        | 3 | delete_product | product is deleted | fail | fail - error message shown |
        | 4 | delete_product | access to the confirm delete page | fail | fail - error message shown |
        | 5 | containers | access to the containers page | fail | fail - error message shown |
        | 6 | add_containers | access to the add containers page | fail | fail - error message shown |
        | 7 | edit_containers | access to the edit containers page | fail | fail - error message shown |
        | 8 | delete_containers | access to the delete containers page | fail | fail - error message shown |
        | 9 | description | access to the product description page | fail | fail - error message shown |
        | 10 | add_description | access to the add product description page | fail | fail - error message shown |
        | 11 | edit_description|access to the edit product description page | fail | fail - error message shown |
        | 12 | delete_description | access to the delete product description page | fail | fail - error message shown |
        | 13 | productmanagement | access to the product management page | fail | fail - error message shown |
        | 14 | add_product_review | access to the add product review page | fail | fail - error message shown |
        | 15 | edit_product_review | access to the edit product review page | fail | fail - error message shown |

        Conclusion:<br>
        Trying to access restricted features will display a custom error message.<br><br>
    
3. Test runs - Administrator access:
    User used: shop-admin

    * a) Reviewing user journey through the PLÖRR-Website.<br> Shop-admin can access and use the following features:
        | # | Site | Feature | Expected Outcome | Result |
        | :--- | :--- | :--- | :--- | :--- |
        | 1 | add_product | link is shown in the navigation bar | pass | pass |
        | 2 | add_product | content is visible | pass | pass |
        | 3 | add_product | new product is added | pass | pass |
        | 4 | edit_product | link is shown in products and produc_details | pass | pass |
        | 5 | edit_product | content is visible | pass | pass |
        | 6 | edit_product | product is updated | pass | pass |
        | 7 | delete_product | link is shown in produc_details | pass | pass |
        | 8 | delete_product | product is deleted | pass | pass |
        | 9 | delete_product | access to the confirm delete page | pass | pass |
        | 10 | containers | access to the containers page | pass | pass |
        | 11 | add_containers | access to the add containers page | pass | pass |
        | 12 | edit_containers | access to the edit containers page | pass | pass |
        | 13 | delete_containers | access to the delete containers page | pass | pass |
        | 14 | description | access to the product description page | pass | pass |
        | 15 | add_description | access to the add product description page | pass | pass |
        | 16 | edit_description|access to the edit product description page | pass | pass |
        | 17 | delete_description | access to the delete product description page | pass | pass |
        | 18 | productmanagement | access to the product management page | pass | pass |
        | 19 | add_product_review | access to the add product review page | pass | pass |
        | 20 | edit_product_review | access to the edit product review page | pass | pass |

        Conclusion:<br>
        Store Owners have extra features to add, edit and delete products, containers, product-description.<br>
        Deleting the product, container, and product-description requires confirmation. Containers and product-description will remove all associated products.


## Validation Results
- ### HTML: W3C Markup Validator Test Results
    * [/home](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2F)
    * [/contact](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2Fcontact%2F)
    * [/quality](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2Fquality%2F)
    * [/brewery](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2Fbrewery%2F)
    * [/impressum](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2Fimpressum%2F)
    * [/agb](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2Fagb%2F)
    * [/checkout/checkout_success](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2Fprofile%2Forder_history%2FDA7D7DB2A8D64C90B25D91661592393E)
    * [/checkout](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2Fcheckout%2F)
    * [/bag](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2Fbag%2F)
    * [/profiles/profile](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2Fprofile%2F)
    * [/profiles/profile_settings_edit](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2Fprofile%2Fsettings%2F)
    * [/products](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2Fproducts%2F)
    * [/products/product_details](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2Fproducts%2F1%2F)
    * [/products/add_product](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2Fproducts%2Fadd%2F)
    * [/products/edit_product](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2Fproducts%2Fedit%2F1%2F)
    * [/accounts/signup/](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2Faccounts%2Fsignup%2F)
    * [/accounts/login/](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2Faccounts%2Flogin%2F)
    * [/accounts/logout/](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2Faccounts%2Flogout%2F)
    * [/password/change/](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2Faccounts%2Fpassword%2Fchange%2F)
    * [/privacypolicy/](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2Fprivacypolicy%2F)
    * [/management/](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2Fproducts%2Fmanagement%2F)
    * [/management/descriptions/](https://ploerr.herokuapp.com/products/management/descriptions/)
    * [/management/containers/](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2Fproducts%2Fmanagement%2Fcontainers%2F)
    * [/management/add/description/](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2Fproducts%2Fadd%2Fcontainer%2F)
    * [/management/edit/description/](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2Fproducts%2Fedit%2Fcontainer%2F10%2F)
    * [/management/delete/description/](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2Fproducts%2Fconfirm%2Fdelete%2Fcontainer%2F10%2F)
    * [/management/add/container/](https://ploerr.herokuapp.com/products/add/description/)
    * [/management/edit/container/](https://ploerr.herokuapp.com/products/edit/description/4/)
    * [/management/delete/container/](https://ploerr.herokuapp.com/products/confirm/delete/description/4/)
    * [/products/category/](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2Fproducts%2Fcategory%2F1%2F)
    * [/add/review/](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2Fproducts%2Fadd%2Freview%2F6%2F)
    * [/edit/review/](https://ploerr.herokuapp.com/products/edit/review/1/2)
    

- ### CSS: W3C CSS Validator Test Results
    * [css validation](https://ploerr.s3.eu-central-1.amazonaws.com/readme/testing/ploerr-w3c-css-validation.png)<br>
    <br><br>

- ### Python: PEP8 Online Test Results
    | # | File | Error Count | Error Detail |
    | :--- | :--- | :--- | :--- |
    | 1 | checkout/apps.py | 1 | 'checkout.signals' imported but unused |
    | 2 | checkout/webhook_handler.py | 2 | line too long |
    | 3 | checkout/webhooks.py | 1 | line too long |
    | 4 | products/widgets.py | 1 | line too long |
    | 5 | ploerr/settings.py | 5 | line too long |

    All "line too long" either can't be fixed or would make the code unreadable.
    Checkout/apps.py needs 'checkout.signals', since the checkout app has a signal.py file.
    <br><br>

- ### Lighthouse Test Results
    The results of all pages variate within 2% for desktop and 7% for mobile, therefore these two representatives were chosen:
    * Desktop:
        ![desktop](https://ploerr.s3.eu-central-1.amazonaws.com/readme/testing/lighthouse-desktop-ploerr-index.png)
    * Mobile:
        ![mobile](https://ploerr.s3.eu-central-1.amazonaws.com/readme/testing/lighthouse-mobile-ploerr-index.png)
        The biggest issue for mobile is bootstrap css, bootstrap js, and stripe js.
<br>
<hr>
<br>

## Responsive Design Testing
* The responsiveness was tested via [screenfly](https://bluetree.ai/screenfly/?u=https%3A//ploerr.herokuapp.com/&a=19&b=10).<br>
The Website is responsive up to 320px width without any issues.<br>
Below 300px width, the navigation bar will stag on each other.<br>
This could be fixed with a smaller font but was deemed unnecessary as the smallest mobile dives are at 320px width.
<br>

* Examples:
    * [Chromebook Pixel 1280x850](https://ploerr.s3.eu-central-1.amazonaws.com/readme/testing/Chromebook-Pixel-1280x850.webp)
    * [iPad Mini 768x1024](https://ploerr.s3.eu-central-1.amazonaws.com/readme/testing/iPad-Mini-768x1024.webp)
    * [Samsung Galaxy Note 5 480x853](https://ploerr.s3.eu-central-1.amazonaws.com/readme/testing/SamsungGalaxyNote5-480x853.webp)
    * [iPhone 5 320x568](https://ploerr.s3.eu-central-1.amazonaws.com/readme/testing/iPhone5-320x568.webp)
<hr>
<br>

## Testing User Stories
  - ### Site User Goals - As a Site User I want to be able to
    * know how to get in contact with the brewery so that I can visit the brewery and purchase products right there to save shipping costs
        - Contact Information is available in contact.html and imprint.html
        - A Google Map with a custom marker for Plörr and directions is in contact.html<br>
        ![contact](https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-contact-1.webp)
    * learn more about the brewery and ingredients so that I can have a better understanding of the product and quality
        - the brewery page is dedicated to information on the history of the company and the brewing process<br>
        ![Brewery](https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-brewery-1.webp)
        - the quality page is dedicated to information on the ingredients<br>
        ![Quality](https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-quality-1.webp)
    * easily register for an account so that I can have a personal account and be able to view my profile
        - by using django-allauth quick and secure registration is possible by using the account dropdown menu <br>
        ![Account](https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-header-nav-account-2.webp)
    * quickly log in or log out so I can access my account information
        - by using django-allauth quick and secure login and logout is possible from using the account dropdown menu <br>
        ![Account](https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-header-nav-account-2.webp)<br>
        ![Account](https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-header-nav-account-3.webp)
    * have a personalized user profile so that I can view my order history and order confirmations and save my payment information
        - the profile app was created and has the option to save payment information, update the function for profile settings and the order history<br>
        ![Profile](https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-profile-1.webp)
    * receive an email confirmation after registering so that I can verify that my account registration was successful
        - by using django-allauth and setting up the email connection, registration confirmation emails are sent and working as intended
    * quickly recover my password so that I can recover access to my account
        - by using django-allauth the option to reset your password is on the login page
        - the option to change the password is in the personal profile
    <br><br>
  - ### Customer Goals - As a Shopper, I want to be able to:
    * easily select the quantity of a product when purchasing it so that I can ensure that I don't accidentally select the wrong product or quantity
        - to add a product to the shopping cart, one has to be on the product detail page
        - a quantity selector is on the product detail page<br>
        ![Product Detail](https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-products-details.webp)<br>
        ![Product Detail](https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-products-quantity.webp)<br>
        ![Product Detail](https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-products-details-addtobag.webp)<br>
    * adjust the number of individual products in my bag so that I can easily make changes to my purchases before checkout
        - the option to adjust the quantity or remove items from the shopping card is in the bag.html<br>
        ![Bag](https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-shopping-cart-1.webp)
    * view items in my bag to be purchased so that I can identify the total cost of my purchase and all items I will receive
        - in bag.html all items that have been added to the shopping cart are listed and the costs are calculated<br>
        ![Bag](https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-shopping-cart-1.webp)<br>
        ![Bag](https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-shopping-cart-2.webp)
    * feel my personal and payment information is safe & secure so that I can confidently provide the needed information to make a purchase
        - the payment process is done by the stripe API, which provides a safe and secure checkout and payment
        <br>
        ![checkout](https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-checkout-2.webp)
    * view an order confirmation after checkout so that I can verify that I have not made any mistakes
        - after a successful order the checkout.html will forward every customer to an order summary<br>
        ![checkout success](https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-checkout-success-1.webp)
    * quickly enter my payment information so that I can check out quickly
        - to purchase in the online shop, login is optional and orders can be made anonymously
    * quickly identify deals and special offers so that I can take advantage of special savings on products I'd like to buy
        - the newsletter option will inform customers about new deals
        - new promotions are displayed on the homepage
    * easily view the total of my purchase at any time so that I can avoid spending too much
        - the total of the order is visible on the header by the card symbol
        <br>
        ![Account](https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-header-nav-account-3.webp)
        - a summary of the shopping bag is shown per message with every change in the shopping cart content
        <br>
        ![Message](https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-messages-2.webp)
    * view individual product details so that I can identify the price, description, ingredients, product rating, product image, and volume
        - all information on the product is listed on the product-details page<br>
        ![Product Detail](https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-products-details.webp)
    * view a list of all products so that I can select some to purchase
        - the overview of all products ist on products.html<br>
        ![Products](https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-products.webp)
    * receive an email confirmation after checking out so that I can keep the confirmation on what I've purchased for my records
        - an order confirmation email with a small order summary is sent by email after a successful checkout
    * search and sort the products so that I can quickly find the product I'm looking for
        - all products are listed on products.html
        - a search or sort function is not implemented as there are too few products to make that function necessary
        - it is under future implementation if more products are added
    <br><br>
  - ### Store Owner Goals - As a Store Owner I want to be able to:
    * add a product so that I can add new items to my store
        - adding a product can be done with: Product Management in the Account dropdown menu, if the user is set as "staff"<br>
        ![Account](https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-header-nav-account.webp)
    * edit/update a product so that I can change product prices, descriptions, images, and other product criteria
        - updating products can be done the products.html and profuct_details.html
        <br>
        ![products](https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-products-admin.webp)
        <br>
        ![Product details](https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-products-details-admin.webp)
    * delete a product so that I can remove items that are no longer for sale
        - deleting products can be done the products.html and profuct_details.html
        <br>
        ![products](https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-products-admin.webp)
        <br>
        ![Product details](https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-products-details-admin.webp)
    * offer a link to relevant third-party websites so that I can offer interested customers more information on our ingredients and the quality of our products
        - link to local farmers has been added to quality.html<br>
        ![Quality](https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-quality-link.webp)
        - link to Facebook business is on the footer and therefore on every page
        <br>
        ![Footer](https://ploerr.s3.eu-central-1.amazonaws.com/readme/features/ploerr-footer-nav.webp)
    <br><br>