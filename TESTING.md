<h1 align="center"> PLÖRR Testing Documentation </h1>

<h2 align="center"><img src="#" height="500" width="900"></h2>

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
    * a) Reviewing visitor journey through the PLÖRR-Website.<br>Visitor can access and use the following features:
        | # | Site | Feature | Expected Outcome | Result |
        | :--- | :--- | :--- | :--- |

    * b) Reviewing visitor access by manually posting the URLs in the address bar:
        | # | Site | Feature | Expected Outcome | Result |
        | :--- | :--- | :--- | :--- |

2. Test runs - Registered User access:
    User used: abeier
    
    * a) Reviewing user journey through the PLÖRR-Website.<br>Visitor can access and use the following features:
        | # | Site | Feature | Expected Outcome | Result |
        | :--- | :--- | :--- | :--- |
    
    * b) Reviewing user access by manually posting the URLs in the address bar:
        | # | Site | Feature | Expected Outcome | Result |
        | :--- | :--- | :--- | :--- |
    
2. Test runs - Administrator access:
    User used: admin

    * a) Reviewing user journey through the PLÖRR-Website.<br>Visitor can access and use the following features:
        | # | Site | Feature | Expected Outcome | Result |
        | :--- | :--- | :--- | :--- |
    
    * b) Reviewing user access by manually posting the URLs in the address bar:
        | # | Site | Feature | Expected Outcome | Result |
        | :--- | :--- | :--- | :--- |

## Validation Results
- ### HTML: W3C Markup Validator Test Results
    * [/home](#)
    * [/contact](#)
    * [/quality](#)
    * [/brewery](#)
    * [/impressum](#)
    * [/agb](#)
    * [/checkout/checkout_success](#)
    * [/checkout](#)
    * [/bag](#)
    * [/profies/profile](#)
    * [/profies/profile_settings_edit](#)
    * [/products](#)
    * [/products/product_details](#)
    * [/products/add_product](#)
    * [/products/edit_product](#)

- ### CSS: W3C CSS Validator Test Results
    * [css validation](#)<br>
    <br><br>

- ### Python: PEP8 Online Test Results
    | # | File | Error Count | Error Detail |
    | :--- | :--- | :--- | :--- |
    | 1 | # models.py |  | all right |
    | 2 | # forms.py |  | line too long|
    | 3 | # admin.py |  | all right |
    | 4 | # urls.py |  | line too long  |
    | 5 | # views.py |  | line too long |
    | 6 | # forms.py |  | line too long  |
    | 7 | # urls.py |  | line too long |
    | 8 | # views.py |  | line too long |
    | 9 | # models.py |  | all right |
    | 10 | # forms.py |  | line too long |
    | 11 | # admin.py |  | line too long |
    | 12 | # urls.py |  | line too long |
    | 13 | # views.py |  | line too long |
    | 14 | # urls.py |  | all right |
    | 15 | # settings.py |  | line too long |
    | 16 | manage.py |  | all right |

    All "line too long" either can't be fixed or would make the code unreadable.
    <br><br>

- ### Lighthouse Test Results
    The results of all pages are within 4% variation, therefore these two representatives were chosen:
    * Desktop:
        ![desktop](#)
    * Mobile:
        ![mobile](#)

<br>
<hr>
<br>

## Responsive Design Testing

<br>
<hr>
<br>

## Testing User Stories
  - ### Site User Goals - As a Site User I want to be able to
    * know how to get in contact with the brewery so that I can visit the brewery and purchase products right there to save shipping costs
    * learn more about the brewery and ingredients so that I can have a better understanding of the product and quality
    * easily register for an account so that I can have a personal account and be able to view my profile
    * quickly login or logout so I can access my personal account information
    * have a personalized user profile so that I can view my personal order history and order confirmations and save my payment information
    * receive an email confirmation after registering so that I can verify that my account registration was successful
    * quickly recover my password so that I can recover access to my account
    <br><br>
  - ### Customer Goals - As a Shopper I want to be able to:
    * easily select the quantity of a product when purchasing it so that I can ensure that I don't accidentally select the wrong product or quantity
    * adjust the quantity of individual products in my bag so that I can easily make changes to my purchases before checkout
    * view items in my bag to be purchased so that I can identify the total cost of my purchase and all items I will receive
    * feel my personal and payment information is safe & secure so that I can confidently provide the needed information to make a purchase
    * view an order confirmation after checkout so that I can verify that I have not made any mistakes
    * quickly enter my payment information so that I can checkout quickly
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