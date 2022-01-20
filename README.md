# Arctic Travels

## User Experience (UX)

### First-time visitor goals

1. As a first-time visitor, potential, present, or future traveler or tourist, I want to get aggregated information about the unconventional travel destinations, in this case, traveling the arctic areas in Europe. My curiosity leans over the real stories of real people excluded from marketing, promotion, or user data collecting. I want to be a part of an independent web community.

2. As a first-time visitor, I want to have easy access to the relevant information, minimum commercial ads, and meaningful content published by each registered user. Clean, simple, relatively respectful to my privacy, and adequate is precisely what I am looking for. 

3. As a first-time visitor, I want to get as much information as possible to gain confidence and personal security to travel to remote areas..

4. As a first-time contributor to the website, I want easy access to the posting form, easy registration, login, deletion, and search functionalities. 

### Returning and frequent visitor goals

1. As a returning visitor, I want to fully enjoy the complete functionality of the web and read new/updated posts, stories, and information I and others could benefit from. I want to feel the site provides me a global range of information from the Arctic, not explicitly focused on any activity. I want to think that the scope of information suits anyone searching for different ways of traveling, from mountain hiking and extreme sports to fully facilitated and accessible environments. 

2. As a returning visitor, I want to read others' posts, use them as a guidebook to the less known, explored, or described areas. 

3. As a returning/frequent visitor, I want to add new stories, tips, and suggestions empowering the site community to be a continuously evolving and independent travel hub for all intending to visit the arctic. 

4. As a returning/frequent visitor, I want to feel I can always revive my memories from spectacular travels and mutually share them with others. 

---

## Design of the site
Under the UX goals, the developer has decided not to overload the content. The Post design should feel intuitive and provide comfortable contrasts to the user. The colors chosen should reflect mysterious unknown places with hints of nature-based shades. 

### Color scheme
Main colors chosen for the site:

- ![#333](https://via.placeholder.com/15/333/000000?text=+) `#333`
- ![#555](https://via.placeholder.com/15/555/000000?text=+) `#555`
- ![#000000](https://via.placeholder.com/15/000000/000000?text=+) `#000000`
- ![#ffffff](https://via.placeholder.com/15/ffffff/000000?text=+) `#ffffff`
- ![#334a2b](https://via.placeholder.com/15/334a2b/000000?text=+) `#334a2b`
- ![#990a0a](https://via.placeholder.com/15/990a0a/000000?text=+) `#990a0a`
- ![#340e0e](https://via.placeholder.com/15/340e0e/000000?text=+) `#340e0e`
- ![#99a0f3](https://via.placeholder.com/15/99a0f3/000000?text=+) `#99a0f3`
- ![#f7ba69](https://via.placeholder.com/15/f7ba69/000000?text=+) `#f7ba69`
- ![#e8f0fe](https://via.placeholder.com/15/e8f0fe/000000?text=+) `#e8f0fe`
- ![#616161](https://via.placeholder.com/15/616161/000000?text=+) `#616161`
- ![#0b1a36](https://via.placeholder.com/15/0b1a36/000000?text=+) `#0b1a36`
- ![#009b15](https://via.placeholder.com/15/009b15/000000?text=+) `#009b15`
- ![#eceff1](https://via.placeholder.com/15/eceff1/000000?text=+) `#eceff1`
- ![#949494](https://via.placeholder.com/15/949494/000000?text=+) `#949494`
- ![#8f8f8f](https://via.placeholder.com/15/8f8f8f/000000?text=+) `#8f8f8f`
- ![#4caf50](https://via.placeholder.com/15/4caf50/000000?text=+) `#4caf50`
- ![#f44336](https://via.placeholder.com/15/f44336/000000?text=+) `#f44336`
- ![#945b06ee](https://via.placeholder.com/15/945b06ee/000000?text=+) `#945b06ee`

#### Typography
- Main font from google fonts _Josefin Sans_ , fallback font _Sans Serif_.


#### Imagery
- Except for the main background image, all images are inserted by registered users via a direct input link to the external image in post form. Each image is responsive and toggles to the whole screen width on click.


![FeatureMockup](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/static/images/readme/mockup.jpg)

---

## Features
The main structure of the site is divided into three parts:
1. __Navbar__
    - Navbar and footer are designed and subsequently customized with Materialize CSS component library. Both are linked to the base template file using Flask web framework functionalities to unify its appearance for all additional customized template files. The base.html file wires the central template navigation functionality within the other navbar links and provides the site's element visibility conditional criteria for unregistered, registered, and admin users by using Jinja templating for elements in the navbar menu. 
    - Each link is wired with url_for function to the app.py app.route decorators to provide programmed specific functionalities to the templates.
    - Navbar is fully responsive throughout wide range of devices. 
    
2. __Main content section__
    - This section is fully customized in accordance with the goal of each navbar link using Python(Flask) to provide special functionality for each of them. 
    - The main section also holds the functionality for flash messages defined in app.py file for specific templates and custom made scrollTop button.
    - Background image is the same throughout the site.
    
3.  __Footer__
    - Footer is unified for all users(new/logged in/admin) and provides links to the social media using cloudflare library hover effects linked with CDN in head element of the base template. Footer is fully responsive throughout wide range of devices.
    - Due to the simplicity of the footer, it is not being mentioned in another sections of the readme.md file.
    ![footer](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/static/images/readme/footer.jpg)


### New visitor
#### Landing Page
##### Navbar
- Unlogged/new visitor is provided with Logo link and links for Home, Posts, Log in and Register. 
![Navbar_unlogged](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/static/images/readme/navbarunlogged.jpg)

##### Home
- New visitor will see Welcome Title of the site and "Start" button linking him to the registration form. Background image is the same throughout the site. 
![Home_unlogged](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/static/images/readme/homeunlogged.jpg)

#### Post Page
- Unlogged/new visitors are provided with the functionality to view/search the posts. No other functionality is accessible.
Search functionality indexing allows to search within the title text and summary text(Set in MongoDB database)
Posts consist of Materializecss library collapsible component and its required JS functions provided on materializecss.com and present in script.js file. Collapsible has its header with title, date, category, summary, image, and image title. Materialize image classes provide toggle functionality to zoom each post image. The collapsible body triggers by clicking on the collapsible header. For better user experience, a hover effect over the collapsible header was implemented to make it evident that the header is clickable. The collapsible body provides main body text, username, and email(not required). No email option offers the user privacy if chosen. It doesn't interfere with possible user restrictions in case of explicitly inappropriate content, as the post is related to the username in the MongoDB database. Jinja templating provides iterating through the database and returning paginated posts with date descending criteria. 
![Posts_search](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/static/images/readme/postssearch.jpg)
![Posts_unlogged](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/static/images/readme/postsunlogged.jpg)

#### Log In Form
- The form provides straight-through login functionality with required Username and Password input fields. 
- The registration link is suggested to the new visitor under the login form. 
![Login_form](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/static/images/readme/loginform.jpg)

#### Registration Form
- The form provides easy registration with Username, Password, and Password confirmation all required and with validation requirement functionality embedded in form input fields in register.html file. The rule checkbox offers a toggle window with information about the site's rules. 
- The Log in link is suggested to the registered visitor under the login form.
![Register_form](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/static/images/readme/registerform.jpg)



### Logged-In User
#### Landing Page
##### Navbar
- Logged-in user is provided with Logo link and links for Home, Posts, Profile, Add Post and Log out.
![Navbar_logged](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/static/images/readme/navbarlogged.jpg)

##### Home
- Logged-in user can see Welcome Title of the site and "Start" button linking him to the registration form invisible as it loses its logic. Background image is the same throughout the site. 
![Home_logged](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/static/images/readme/homelogged.jpg)

##### Post Page
- Logged in user is provided with the functionality to view/search/edit/delete the posts.
- In addition to the posts page's unlogged visitor functionality, the right side of the collapsible header contains Edit/Delete buttons to the session(logged in) user's posts providing a fast and easy way to edit or delete existing posts.
![Posts_logged](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/static/images/readme/postlogged.jpg)

###### Delete button 
- defensive programming solved with a confirmation toggle window. 
- The user is informed about the confirmed deletion with a flash message in the upper part of the page.
![post_delete_toggle](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/static/images/readme/postdeletetoggle.jpg)
![post_delete_confirm](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/static/images/readme/postdeleteconfirm.jpg)

###### Edit button
- redirects the user into edit_post.html template with input fields/textareas correctly prefilled with actual saved data ready for editing. All fields required with validation specificity embedded in edit_post.html template except for email, as explained before. The form offers edit/cancel buttons. After edit button confirmation, the post data get updated in the database and consequently on the posts.html. 
- Cancel button redirects back to posts.html template. 
- The user is informed about the confirmed edit(update) with a flash message in the upper part of the page.
![post_edit](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/static/images/readme/postedit.jpg)
![post_edit_confirm](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/static/images/readme/posteditconfirm.jpg)

##### Profile Page
- Profile page offers the same functionality as Posts page, except the posts rendered are explicitly posted by a session(logged in) user. _"active user"'s profile_ is printed above the post's preview. 
![profileuser](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/static/images/readme/profileuser.jpg)

##### Log Out Nav Link
- Log out link redirects user into login.html template as stated in /logout app.py router decorator and provides a flash message informing the user about being logged out. 
- The navbar switches into the primary content offer functionality for the new visitor/unlogged user as stated in the base.html conditioning for login.html template.  
![user_loggedout](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/static/images/readme/userloggedout.jpg)

### Logged-In Admin User
#### Landing Page
##### Navbar
- Logged-in Admin user is provided with Logo link and links for Home, Posts, Profile, Add Post, Log out and extended for Manage Categories link. The if criteria stated in base.html nav links.
- At this point of the development, the Admin has equal rights as any other user except the Manage Categories functionality not available to any other user. 
![Navbar_logged](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/static/images/readme/navbaradmin.jpg)

##### Manage Categories Page
- Manage Categories allow Admin to add/modify and delete records in MongoDB categories collection. 
- The defense programming for deleting/editingcategories principally is identical to the posts deleting/editing. Add/Edit categories buttons are linked to their templates where the modification is specified and after confirmation executed in the database through app.py route decorators and their functions. After the confirmation Manage Categories template re-renders with a Flah message confirming deleting/editing. 
![Manage_categories](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/static/images/readme/managecategories.jpg)

###### Add Category
![Add_category](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/static/images/readme/addcategory.jpg)
![Addcatconfirm](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/static/images/readme/addcatconfirm.jpg)

###### Edit Category
![Edit_category](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/static/images/readme/editcat.jpg)
![Editcatconfirm](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/static/images/readme/editcatconfirm.jpg)

###### Delete Category
![Deletecattoggle](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/static/images/readme/deletecattoggle.jpg)
![Deleteconfirmed](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/static/images/readme/deletecatconfirm.jpg)

### Features left to implement
* Comments, Likes functionality to comments for each user. 
* Extension of Admin rights to delete any post, restrict user, delete a user account.
* Social media communities linked to Arctic Travels. 
* Change username and password functionality.

## Main technologies used
* HTML5
* CSS3
* JavaScript
* Python
* Flask
* Pprintpp
* [Balsamiq](https://balsamiq.com/)
* [Font Awsome](https://fontawesome.com/)
* [Heroku](https://heroku.com/)
* [Github](https://github.com/)
* [Gitpod](https://www.gitpod.io/)
* [Imgur](https://imgur.com/)
* [JQuery API](https://api.jquery.com/)
* [Materializecss 1.0.0.](https://materializecss.com/)
* [MongoDB](https://www.mongodb.com/)
* [Pymongo](https://pymongo.readthedocs.io/en/stable/)
* [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/)

## Testing

### Visual testing
* Google Devtools and its Toggle device toolbar with (responsive rule, grid blocks and given default mobile devices), lighthouse
* Heroku deployed [travel-post](https://travel-post.herokuapp.com/) on smartphone Samsung Galaxy Xcover Pro, laptop HP ProBook x360 11 G3 EE, and Dell screen res. 1920 x 1080px.
* Browsers used for testing - Google Chrome, Microsoft Edge.

### Google Devtools Lighthouse - testing

#
#
# give a report
#
#


### Base template testing
- wiring funcitonalities providing unified interface for Nav bar, Footer, Flash messages and CrollTop button work correctly on all pages of the site

### Home page testing
* __Start button__ visibility works following the development intentions
    - hidden for logged-in users
    - visible for unlogged users/new visitors

### Posts page testing
* __Posts rendering__
    - posts render, and all data are iterated fully from MongoDB without any issues
    - posts sorted from the newest to the oldest
    - minor issue between pagination a iteration of data from MongoDB described in section of __Bugs and debugging__ in readme.md.
    - hover effect over posts works correctly
    - click on the collapsible header correctly renders the collapsible body
    - accessibility of the externally linked images is fixed by injecting the image_title MongoDB record field added by the user into the alt attribute while adding the post and image_title input is required
    - edit/delete buttons render correctly to a session user, hidden to another user or unlogged visitor and links the user into the appropriate template for editing or functionality for deleting of the post
    - delete defensive programming toggle window works correctly
    - flash messages work correctly 
    - posts' image onclick zooming works correctly
    search functionality set by Python interpreter in IDE command-line by creating indexing using MongoDB within "title_text" field and "summary" field in posts collection works correctly
    - if search result doesn't exist if conditioning sorting the result by the length, which in this case is <= 0 triggers else statement with heading informing the user that nothing was found - the functionality works correctly
    - minor issue in searching of fragments of words described section __Bugs and debugging__ in readme.md
    
    
### Profile page testing
- the profile provides injected profile session username by Jinja capitalized in h3 heading at the top of the page under Navbar
- posts are sorted by the date as in the posts page, profile user(author), and all functionalities for edit/delete posts work accordingly

### Add post page testing
- all inputs work correctly as stated in the code
- input validation criteria set in html code input attributes and script.js work correctly without any issue and validate the input data correctly
- email input is not required and renders without an error in the templates if not included
- flash message after insertion of new post and redirection to a post page work correctly

### Register form functionality testing
- works correctly and after succesful registration redirects the user into profile page
- validation works correctly including the flash messages for not matching passwords and existing user
- checkbox toggle window with rules works correctly including the "rules" window close button and check validation
- link to login form provided under the form, linked correctly

### Log In form functionality testing
- works correctly and after succesful logging redirects the user into posts page
- validation of incorrect password/username works correctly together with the flash message about incorrect password and/or username
- link to register form provided under the form, linked correctly

### Log Out functionality testing
- works correctly and deletes session coockies from the browser
- redirects to login form

### Manage Categories page testing
- the template page is visible only to the user with the username Admin/admin as stated in the base.html template navbar conditioning
- all CRUD functionalities and related forms for manage categories page work correctly, including the flash messages after confirmation of add/edit/delete button and redirects back into the manage categories template 

### Validator testing

#### HTML [W3C validator](https://validator.w3.org/) using direct input.
- [base.html](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/templates/base.html)
    * No major errors were returned.
    * Errors reported related with Flask Jinja templating syntax having no negative impact on functionality of html markup.
        


- [add_category.html](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/templates/add_category.html)
- [add_post.html](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/templates/add_post.html)
- [categories.html](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/templates/categories.html)
- [edit_categories.html](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/templates/edit_category.html)
- [edit_post.html](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/templates/edit_post.html)
- [home.html](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/templates/home.html)
- [login.html](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/templates/login.html)
- [posts.html](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/templates/posts.html)
- [profile.html](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/templates/profile.html)
- [register.html](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/templates/register.html)
    * No major errors were returned.
    * Errors reported related with Flask Jinja templating syntax having no negative impact on functionality of html markup.
    * Missing lang attribute is part of the base.html template extention



#### CSS [W3C validator](https://jigsaw.w3.org/css-validator/)
- Validation of the site URI deployed on Github [Travel Post](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/static/css/style.css)
    * No errors were returned in the direct input css code.
    * Errors related to external libraries.



#### JSHint [validator](https://jshint.com/)
- Validation of JS files
[script.js](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/static/js/script.js)
    - No major issues found.



#### PEP8 [validator](http://pep8online.com/)
- Validation of JS files
[app.py](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/app.py)
    - No issues detected.

### Responsive Design:
* Materializecss grid applied in HTML markup
* 4 media queries specifying minor adjustments

### Wireframes
- Links to wireframes below show the basic structure of each page on a mobile devices, tablet, and laptop.

1. [Wireframe Admin](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/static/images/wireframes/loggedadmin.png)
2. [Wireframe User](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/static/images/wireframes/loggeduser.png)
3. [Wireframe New Visitor](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/static/images/wireframes/newvisitor.png)
4. [Wireframe Post Concept](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/static/images/wireframes/postconcept.png)

### Bugs and Debugging
#### Bugs
- A commonly known bug with very low resolution, ca <200px, causes the float of the content to the left and creates a gap on the right side of the screen.
- Warning generated by validator while testing HTML code about structural heading outline were intended.
- Error while validating HTML caused by Flask templating - causing no issue to functionality of the app
- Array rendering in the app, fixed with help of tutor by adding appending '\n' behind the iterated items in Jinja template.
- Date sorting didn't take the month and year after the day as a criteria(DD.MM.YYYY). Solved by restructuring the date to YYYY.MM.DD.
- searching functionality has an issue with searching parts of the text, it returns the result only if the whole word exist. Example:
    - searching a word "ice" returns no result though the word "icehole" exist
- pagination functionality works fine except the collection from MongoDB is paginated first and then sorted by a date on each page. Correct functionality should be to sort the collection the collection first and then paginate. I haven't found the solution for this issue yet. 
- console in google dev tools reports textarea element not found and refers to materialzeccs javascript library
    - so far no functional issues with textarea used in the project were detected

### Testing User Stories from User Experience (UX) Section
#### First-time visitor goals

1. As a first-time visitor, potential, present, or future traveler or tourist, I want to get aggregated information about the unconventional travel destinations, in this case, traveling the arctic areas in Europe. My curiosity leans over the real stories of real people excluded from marketing, promotion, or user data collecting. I want to be a part of an independent web community.
    - The user is provided with the possibility to get registered without inserting any sensitive personal information and become a member of the community.
    - User's privacy is maintained by self-chosen username and only optional email insertion while adding a post
    - Data collection of email is only voluntary and the exclusion of email has no impact to use the site fully.

2. As a first-time visitor, I want to have easy access to the relevant information, minimum commercial ads, and meaningful content published by each registered user. Clean, simple, relatively respectful to my privacy, and adequate is precisely what I am looking for. 
    - The user is provided relevant data with zero ads, search functionality, privacy, and safety that Admin user regularly checks the environment for inappropriate content defined in rules each user has to accept during the registration.

3. As a first-time visitor, I want to get as much information as possible to gain confidence and personal security to travel to remote areas..
    - The users are content creators; therefore, the relevance and scope of information solely rely on community members' contribution to the site. 

4. As a first-time contributor to the website, I want easy access to the posting form, easy registration, login, deletion, and search functionalities. 
    - The focus is to prevent users from going through any unnecessary action to use the CRUD functionality of the web fully.

#### Returning and frequent visitor goals

1. As a returning visitor, I want to fully enjoy the complete functionality of the web and read new/updated posts, stories, and information I and others could benefit from. I want to feel the site provides me a global range of information from the Arctic, not explicitly focused on any activity. I want to think that the scope of information suits anyone searching for different ways of traveling, from mountain hiking and extreme sports to fully facilitated and accessible environments. 
    - The user is allowed to include any post related to the Arctic. If the category isn't fitting the user's needs, it might be additionally and promptly added by Admin.
    - Category others offers users to categorize their post in none of the options fits their needs.
    - Users may contact the Admin via e-mail included in the site's footer. 
    - Quality and range of the content rely on the users' contribution.

2. As a returning visitor, I want to read others' posts, use them as a guidebook to the less known, explored, or described areas. 
    - All posts are visible to all even unregistered users
    - Guidance, quality and range of the content rely on the users' contribution.

3. As a returning/frequent visitor, I want to add new stories, tips, and suggestions empowering the site community to be a continuously evolving and independent travel hub for all intending to visit the arctic. 
    - All users have unlimited and free access to add the content

4. As a returning/frequent visitor, I want to feel I can always revive my memories from spectacular travels and mutually share them with others.
    - The intention is not to delete any older post, so even the oldest ones will be always available to the user.


## Deployment
### GitHub Pages
- The site was deployed to GitHub pages. The steps to deploy are as follows:
1. Log in to GitHub and locate the [GitHub Repository](https://github.com/JakubKocerha/Travel-Post-MS3)
2. At the top of the Repository (not top of page), navigate to the _Settings_ button.
3. Scroll down the Settings page until you locate the _GitHub Pages_ Section.
4. Under _Source_, click the dropdown called _None_ and select _Master Branch_ and press _Save_. 
5. Once the _Master branch_ has been selected, the page will be automatically refreshed with a detailed ribbon including a link to the site to indicate the successful deployment. 

- The link to the repository can be found [here](https://github.com/JakubKocerha/Travel-Post-MS3)

### Forking the GitHub Repository
- By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...
1. Log in to GitHub and locate the [GitHub Repository](https://github.com/JakubKocerha/Travel-Post-MS3)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/JakubKocerha/Travel-Post-MS3)
2. Above the list of files, click "Code".
3. To clone the repository using HTTPS, navigate to "HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `Spoon-Knife`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

### Heroku
1. Create requirements.txt file updated with all dependencies created and push the file into your repository
2. Create correctly defined Procfile linking to the python app file in the repository push the file into your repository
    - avoid of empty line which might cause issues running the app on Heroku
3. Create a new app
    - Log in to Heroku account.
    - Click on New, then click on Create new app.
    - Insert name of new Heroku app. It must be unique and using dash(-) instead of spaces
    - Click on Create app
4.  Connect the app to GitHub
    - Click on Deploy in Heroku app.
    - Choose Deploy method Github.
    - Search the repository you want to connect and click Connect.
5. Set environment variables
    - Make sure all env variables are set correctly in env.py in your workspace file and add the env.py file into .gitignore
    - In Heroku app navigate to Settings
    - Click on Reveal Config Vars
    - Fill in the inputs with env.py variable parameters without quotation marks
6. Navigate into Deploy section of your Heroku app
    - click on Enable Automatic Deployment and after click on Deploy branch
7. After the deployment is processed, you’ll see the message “Your app is successfully deployed”

8. Live link can be found [here](https://travel-post.herokuapp.com/)

