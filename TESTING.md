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
        | 5 | products | edit & delete function | fail | fail - these features are only visible to Store Owners |
        | 6 | product_details | content is visible | pass | pass |
        | 7 | product_details | quantity can be selected  | pass | pass |
        | 8 | product_details | "Add To Bag" - button adds the product with the selected quantity to the bag | pass | pass |
        | 9 | - | "Message: Success" is shown, with the bag contents visible | pass | pass |
        | 10 | - | "Message: Success" links to bag | pass | pass |
        | 11 | - | "Message: Success" links to checkout | pass | pass |
        | 12 | quality | content is visible | pass | pass - the youtube video might need a refresh of the page to start up |
        | 13 | quality | link to third-party website | pass | pass |
        | 14 | brewery | content is visible | pass | pass |
        | 15 | impressum | content is visible | pass | pass |
        | 16 | agb | content is visible | pass | pass |
        | 17 | contact | content is visible | pass | pass |
        | 18 | bag | content is visible | pass | pass - either the selected products or "bag is empty" |
        | 19 | bag | products can be removed | pass | pass |
        | 20 | bag | products quantity can be updated | pass | pass |
        | 21 | bag | bag total, weight, deposit total, shipping costs, grand total are displayed | pass | pass - they change according to the products and quantity in the bag |
        | 22 | checkout | content is visible | pass | pass |
        | 23 | checkout | order summary is visible | pass | pass |
        | 24 | checkouts | save delivery information | fail | fail -  You need to be logged in to have that feature |
        | 25 | checkout | prompted to login or create account under the delivery information| pass | pass -  not needed to complete the order |
        | 26 | checkout | enter credit card details | pass | pass |
        | 27 | checkout | complete order (with correct credit card details) | pass | pass |
        | 28 | checkout_success | content (Oder Summary)  is visible | pass | pass |
        | 29 | checkout | email confirmation is send | pass | pass |
        | 30 | login | content is visible | pass | pass |
        | 31 | password_reset | content is visible | pass | pass |
        | 32 | signup | content is visible | pass | pass |
        | 33 | - | email confirmations are sent| pass | pass |
        | 34 | - | messages are shown| pass | pass |
        | 32 | privacy policy | content is visible | pass | pass |

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
        | 9 | delete_product | access to the confirm delete page | fail | fail - redirected to login page |

        Conclusion:<br>
        As expected the visitor is prohibited from using any other feature that would require to be logged in.<br>
        The greatest downside is that everyone could look up any order summary.
        However, to do that, the order number is needed. This number is randomly generated and only known to the customer and our administrators.<br><br>
        
2. Test runs - Registered User access:
    User used: abeier
    
    * a) Reviewing user journey through the PLÖRR-Website.<br> Visitors can access and use the following features:
        | # | Site | Feature | Expected Outcome | Result |
        | :--- | :--- | :--- | :--- | :--- |
        | 1 | profile | content is visible | pass | pass |
        | 2 | profile | delivery information can be updated | pass | pass |
        | 3 | profile | "Message: Success" is displayed without the bag contents | pass | pass |
        | 4 | password_change | content is visible | pass | pass |
        | 5 | password_change | password can be changed | pass | pass |
        | 6 | profile_settings | content is visible | pass | pass |
        | 7 | profile_settings | username, name & email can be updated | pass | pass |
        | 8 | checkout | save delivery information | pass | pass |
        | 9 | checkout | save delivery information checkbox is red | pass | fail - for some reason the css is not applied |
        | 10 | logout | content is visible | pass | pass |
        | 11 | logout | able to log out from the profile | pass | pass |

        Conclusion:<br>
        In addition to all the normal visitor access logged in users have some little conveniences with their profile, where they can update delivery and personal information, as well as an overview of all previously made orders.
    
    * b) Reviewing user access by manually posting the URLs in the address bar:
        | # | Site | Feature | Expected Outcome | Result |
        | :--- | :--- | :--- | :--- | :--- |
        | 1 | add_product | content is visible | fail | fail - error message shown |
        | 2 | edit_product | content is visible | fail | fail - error message shown |
        | 3 | delete_product | product is deleted | fail | fail - error message shown |
        | 4 | delete_product | access to the confirm delete page | fail | fail - error message shown |

        Conclusion:<br>
        Trying to access restricted features will display a custom error message.<br><br>
    
3. Test runs - Administrator access:
    User used: admin

    * a) Reviewing user journey through the PLÖRR-Website.<br> Visitors can access and use the following features:
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

        Conclusion:<br>
        Store Owners have extra features to add, edit and delete products.<br>
        Deleting the product can only be done from the product details and requires confirmation.
    

## Validation Results
- ### HTML: W3C Markup Validator Test Results
    * [/home](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2F)
    * [/contact](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2Fcontact%2F)
    * [/quality](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2Fquality%2F)
    * [/brewery](https://ploerr.herokuapp.com/brewery/)
    * [/impressum](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2Fimpressum%2F)
    * [/agb](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2Fagb%2F)
    * [/checkout/checkout_success](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2Fprofile%2Forder_history%2FDA7D7DB2A8D64C90B25D91661592393E)
    * [/checkout](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2Fcheckout%2F)
    * [/bag](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2Fbag%2F)
    * [/profiles/profile](https://ploerr.herokuapp.com/profile/)
    * [/profiles/profile_settings_edit](https://ploerr.herokuapp.com/profile/settings/)
    * [/products](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2Fproducts%2F)
    * [/products/product_details](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2Fproducts%2F1%2F)
    * [/products/add_product](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2Fproducts%2Fadd%2F)
    * [/products/edit_product](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2Fproducts%2Fedit%2F1%2F)
    * [/accounts/signup/](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2Faccounts%2Fsignup%2F)
    * [/accounts/login/](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2Faccounts%2Flogin%2F)
    * [/accounts/logout/](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2Faccounts%2Flogout%2F)
    * [/password/change/](https://validator.w3.org/nu/?doc=https%3A%2F%2Fploerr.herokuapp.com%2Faccounts%2Fpassword%2Fchange%2F)
    

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
    * learn more about the brewery and ingredients so that I can have a better understanding of the product and quality
    * easily register for an account so that I can have a personal account and be able to view my profile
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
    * view an order confirmation after checkout so that I can verify that I have not made any mistakes
    * quickly enter my payment information so that I can check out quickly
    * quickly identify deals and special offers so that I can take advantage of special savings on products I'd like to buy
    * easily view the total of my purchase at any time so that I can avoid spending too much
    * view individual product details so that I can identify the price, description, ingredients, product rating, product image, and volume
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