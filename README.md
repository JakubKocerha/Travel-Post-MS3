# Arctic Travels

## User Experience (UX)

---

### First-time visitor goals

1. As a first-time visitor, potential, present, or future traveler or tourist, I want to get aggregated information about the unconventional travel destinations, in this case, traveling the arctic areas in Europe. My curiosity leans over the real stories of real people excluded from marketing, promotion, or user data collecting. I want to be a part of an independent web community.

2. As a first-time visitor, I want to have easy access to the relevant information, minimum commercial ads, and meaningful content published by each registered user. Clean, simple, relatively respectful to my privacy, and adequate is precisely what I am looking for. 

3. As a first-time visitor, I want to get as much information as possible to gain confidence and personal security to travel to remote areas..

4. As a first-time contributor to the website, I want easy access to the posting form, easy registration, login, deletion, and search functionalities. 

---

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


![FeatureMockup](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/static/images/Readme/mockup.jpg)

## Features
The main structure of the site is divided into three parts:
1. __Navbar__
    - Navbar and footer are designed and subsequently customized with Materialize CSS component library. Both are linked to the base template file using Flask web framework functionalities to unify its appearance for all additional customized template files. The base.html file wires the central template navigation functionality within the other navbar links and provides the site's element visibility conditional criteria for unregistered, registered, and admin users by using Jinja templating for elements in the navbar menu. 
    - Each link is wired with url_for function to the app.py app.route decorators to provide programmed specific functionalities to the templates.
    - Navbar is fully responsive throughout wide range of devices. 
    
2. __Main content section__
    - This section is fully customized in accordance with the goal of each navbar link using Python(Flask) to provide special functionality for each of them. 
    - The main section also holds the functionality for flash messages defined in app.py file for specific templates and custom made back-to-top button.
    - Background image is the same throughout the site.
    
3.  __Footer__
    - Footer is unified for all users(new/logged in/admin) and provides links to the social media using cloudflare library hover effects linked with CDN in head element of the base template. Footer is fully responsive throughout wide range of devices.
    - Due to the simplicity of the footer, it is not being mentioned in another sections of the readme.md file.
    ![footer](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/static/images/Readme/footer.jpg)


### New visitor
#### Landing Page
##### Navbar
- Unlogged/new visitor is provided with Logo link and links for Home, Posts, Log in and Register. 
![Navbar unlogged](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/static/images/Readme/navbarunlogged.jpg)

##### Home
- New visitor will see Welcome Title of the site and "Start" button linking him to the registration form. Background image is the same throughout the site. 
![Home unlogged](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/static/images/Readme/homeunlogged.jpg)

#### Post Page
- Unlogged/new visitors are provided with the functionality to view/search the posts. No other functionality is accessible.
Posts consist of Materializecss library collapsible component and its required JS functions provided on materializecss.com and present in script.js file. Collapsible has its header with title, date, category, summary, image, and image title. Materialize image classes provide toggle functionality to zoom each post image. The collapsible body triggers by clicking on the collapsible header. For better user experience, a hover effect over the collapsible header was implemented to make it evident that the header is clickable. The collapsible body provides main body text, username, and email(not required). No email option offers the user privacy if chosen. It doesn't interfere with possible user restrictions in case of explicitly inappropriate content, as the post is related to the username in the MongoDB database. Jinja templating provides iterating through the database and returning paginated posts with date descending criteria. 
![Posts_search](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/static/images/Readme/postssearch.jpg)
![Posts_unlogged](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/static/images/Readme/postsunlogged.jpg)

#### Log In Form
- The form provides straight-through login functionality with required Username and Password input fields. 
- The registration link is suggested to the new visitor under the login form. 
![Login_form](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/static/images/Readme/loginform.jpg)

#### Registration Form
- The form provides easy registration with Username, Password, and Password confirmation all required and with validation requirement functionality embedded in form input fields in register.html file. The rule checkbox offers a toggle window with information about the site's rules. 
- The Log in link is suggested to the registered visitor under the login form.
![Register_form](https://github.com/JakubKocerha/Travel-Post-MS3/blob/main/static/images/Readme/registerform.jpg)



### Logged in user
#### Landing Page
##### Navbar
- Logged in user is provided with Logo link and links for Home, Posts, Profile, Add Post and Log out.
![Navbar logged](https://github.com/JakubKocerha/JakubKocerha-milestonep2-rare-tropical-plants/blob/main/readme-media/landingp.jpg)

##### Home
- Logged in user can see Welcome Title of the site and "Start" button linking him to the registration form invisible as it loses its logic. Background image is the same throughout the site. 
![Home logged](https://github.com/JakubKocerha/JakubKocerha-milestonep2-rare-tropical-plants/blob/main/readme-media/landingp.jpg)

#### Post Page
- Logged in user is provided with the functionality to view/search/edit/delete the posts.
- In addition to the posts page's unlogged visitor functionality, the right side of the collapsible header contains Edit/Delete buttons to the session(logged in) user's posts providing a fast and easy way to edit or delete existing posts.
![Posts_logged](https://github.com/JakubKocerha/JakubKocerha-milestonep2-rare-tropical-plants/blob/main/readme-media/landingp.jpg)

    ##### Delete button 
    - defensive programming solved with a confirmation toggle window. 
    - The user is informed about the confirmed deletion with a flash message in the upper part of the page.
![post_delete_toggle](https://github.com/JakubKocerha/JakubKocerha-milestonep2-rare-tropical-plants/blob/main/readme-media/landingp.jpg)
![post_delete_confirm](https://github.com/JakubKocerha/JakubKocerha-milestonep2-rare-tropical-plants/blob/main/readme-media/landingp.jpg)

    ##### Edit button
    - redirects the user into edit_post.html template with input fields/textareas correctly prefilled with actual saved data ready for editing. All fields required with validation specificity embedded in edit_post.html template except for email, as explained before. The form offers edit/cancel buttons. After edit button confirmation, the post data get updated in the database and consequently on the posts.html. 
    - Cancel button redirects back to posts.html template. 
    - The user is informed about the confirmed edit(update) with a flash message in the upper part of the page.
![post_edit](https://github.com/JakubKocerha/JakubKocerha-milestonep2-rare-tropical-plants/blob/main/readme-media/landingp.jpg)
![post_edit_confirm](https://github.com/JakubKocerha/JakubKocerha-milestonep2-rare-tropical-plants/blob/main/readme-media/landingp.jpg)

##### Profile Page
- Profile page offers the same functionality as Posts page, except the posts rendered are explicitly posted by a session(logged in) user. _"active user"'s profile_ is printed above the post's preview. 
![profileuser](https://github.com/JakubKocerha/JakubKocerha-milestonep2-rare-tropical-plants/blob/main/readme-media/landingp.jpg)




![posts_logged](https://github.com/JakubKocerha/JakubKocerha-milestonep2-rare-tropical-plants/blob/main/readme-media/landingp.jpg)
![Posts_logged_delete_toggle](https://github.com/JakubKocerha/JakubKocerha-milestonep2-rare-tropical-plants/blob/main/readme-media/landingp.jpg)







- Logged in Admin user is provided with Logo link and links for Home, Posts, Profile, Add Post, Manage Categories and Log out.
![Navbar admin](https://github.com/JakubKocerha/JakubKocerha-milestonep2-rare-tropical-plants/blob/main/readme-media/landingp.jpg)


