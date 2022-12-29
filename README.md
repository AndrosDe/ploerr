<h1 align="center"> Plörrbräu </h1>
<h2 class="logo-font"> Welcome </h2>

<h4>
    This is the buissness website for the company Plörr GmbH, were the company will more than showcase their products with great detail.
    It will provide extensive information on the buisness, ingridance and the berwery.
    <br><br>
    Additionally a great online shop is availbe to pruchase the featured products, which can also be used without registaring and has a quick checkout option.<br>
    For regular customers regestaring would be benifcial, as the would additonally to the order confirmation email, also be able to revisit all succefully completed order summarys on their personal profile page this website.
    <br><br>
    Plörrbräu wishes all of you the best and hopes that you will have great time on our website.
</h4>

<h2 align="center"><img src="" height="500" width="900"></h2>

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
    <br><br>
  - ### User Demographic
    <br><br>

## User Stories
  - ### 
    <br><br>
  - ### 
    <br><br>
  - ###
    <br><br>
  - ### Mapped User Stories to the project on GitHub:<br>
    [View the project here on GitHub](https://github.com/users/AndrosDe/projects/3)
    <br><br>
<hr>

## Scope
- ### Feature Ideas Planning
  When planning the App features and scope, I drew up an Importance Viability analysis of these features, please see below:

  | # | Feature | Importance | Viability |
  | --- | --- | --- | --- |

  <br>

- ### Functionality Requirements

  <br><br>
<hr>

## Structure
- ### Topology Diagrams

<hr>

## Skeleton
  - ### Wireframes
    The wireframes created for this project:

  - ### Design
    [Bootstrap5](https://getbootstrap.com/docs/5.0/getting-started/introduction/) was used and customized for the front-end development.

    - #### Typography
      I used Google Fonts to import the fonts I used across the application.

    - #### Imagery & UI

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

## Future Implementation

<hr>

## Technologies Used
* Languages:
    * [HTML5](https://en.wikipedia.org/wiki/HTML5) was used for the content and structure of the site.
    * [CSS3](https://en.wikipedia.org/wiki/CSS#CSS_3) was used for the styling of the site.
    * [JavaScript](https://en.wikipedia.org/wiki/JavaScript) was used for the interactivity of the site.
    * [Python](https://www.python.org/) was used for the back-end programming of the site.
<br>

* [Cloudinary API](https://cloudinary.com/) 
    * was used to enable users to upload images for their recipes whilst keeping the App safe and secure

* [Django](https://www.djangoproject.com/)
    * Django was used to create the models for the database, forms to post data into the database, the templates, and the view connecting them all.

* [Postgres](https://www.postgresql.org/)
    * Postgres was the relational database used to store user registration, login, and authentication. Postgres was also used to store the Categories.

* [Django Summernote](https://www.mongodb.com/)
    * MongoDB was the nonrelational database used to store less structured data such as recipes. MongoDB is where we host our NoSQL database.

* [pip](https://pip.pypa.io/en/stable/)
    * Pip is the package installer for Python, allowing us to install the packages we need for this site.

* [gunicorn](https://www.dnspython.org/)
    * Dnspython is a DNS toolkit for python.

* [Bootstrap 5](https://getbootstrap.com/)
    * Bootstrap is one of the most popular front-end open source toolkits and was used for ease of styling the Earthlings app.

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
  1. In order to connect to an external database, install **dj_database_url** and **psycopg2** via the **terminal**.
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
  Especially the checkout app, stripe and java scripts, as they were very well made and exsactly what I was looking for impementing into my store part of the project.<br>
  The biggest dirrence is, that I prever to use more bootstrap classes and less custom css.
  * CSS Font Border - [code:](https://stackoverflow.com/questions/2570972/css-font-border)
  * You tube implementation - [w3schools](https://www.w3schools.com/html/html_youtube.asp)
  * Responsive iFrames - [w3schools](https://www.w3schools.com/howto/howto_css_responsive_iframes.asp)
  * Google maps - [w3schools](https://www.w3schools.com/graphics/google_maps_intro.asp)
### Media
  * #### Videos
    * The main background video on the index page was Stock footage provided by <a class="link author-link-popup" target="_blank" href="https://www.videvo.net/profile/videvo">Videvo</a>, downloaded from <a class="videvo-redirect" target="_blank" href="https://www.videvo.net">videvo.net</a>
    * The middel video on the brewery page was Stock footage provided by <a class="link author-link-popup" target="_blank" href="https://www.videvo.net/profile/vidfy-Pressmaster">Pressmaster</a>, downloaded from <a class="videvo-redirect" target="_blank" href="https://www.videvo.net">videvo.net</a>

  * #### Pictures
    * All used pictures were changed/modified and are mostly only used for testing purpose
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
I specially liked the approachto the base.html, as it provides a lot of option for all other templates with the extra code blocks right from the start.
* Special mention and thanks to my mentor, Dario Carrasquel, for his support and insights

<hr>

## Copyrights
&copy; 2022 Plörr by Andreas Beier