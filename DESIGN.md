![Website logo](/documentation/screenshots/site_logo.png)

---

# Design

See [README.md](/README.md) for information on project goals, user stories, security, future developments, technologies used, user feedback, credits, and acknowledgements.<br>
See [TESTING.md](/TESTING.md) for information on the manual and automated testing of the site, bugs encountered, and website analytics. <br>
See [DEV.md](/DEV.md) for an overview of the continuous integration and deployment process, how I set up my development environment, and deployment steps.

---

## Table of Contents
1. [Five Planes of UX](#five-planes-of-ux)
    1. [Strategy](#strategy)
        * [Viability and Feasibility](#viability-and-feasibility)
    2. [Scope](#scope)
        * [Back End](#back-end)
        * [Font End](#front-end)
    3. [Structure](#structure)
        * [base.html](#basehtml)
        * [home.html](#homehtml)
        * [signup.html](#signuphtml)
        * [login.html](#loginhtml)
        * [toys.html](#toyshtml)
        * [add_toy.html](#add_toyhtml)
        * [edit_toy.html](#edit_toyhtml)
        * [individual_toy.html](#individual_toyhtml)
        * [add_review.html](#add_reviewhtml)
        * [edit_review.html](#edit_reviewhtml)
        * [profile.html](#profilehtml)
        * [edit_profile.html](#edit_profilehtml)
        * [change_password.html](#change_passwordhtml)
        * [403.html](#403html)
        * [404.html](#404html)
        * [500.html](#500html)
        * [Information Architecture](#information-architecture)
        * [Interactive Experience](#interactive-experience)
    4. [Skeleton](#skeleton)
        * [Wireframes](#wireframes)
    5. [Surface](#surface)
        * [Colour Scheme](#colour-scheme)
        * [Typography](#typography)
        * [Images](#images)
2. [Features](#features)

## Five Planes of UX
Here I outline the design process of the website, ensuring that I meet accessibility guidelines, follow the principles of UX design, and create a website that meets the purpose of being a fun and intuitive online community for reviewing and recommending children's toys through user interactions.

### Strategy

- **What value does the project provide?** This project provides a website for an online community of parents and carers to share honest reviews and experiences with children's toys as a way to inform other parents and carers before they buy the toys. On top of that, it also provides context for the review in the form of sharing what other toys the child likes. For example a child that likes toy cars and trucks may rate a doll low, or a child that likes footballs and frisbees may rate a trampoline highly.
- **What are the business needs?** The business needs are to provide an intuitive, pleasant looking, and accessible website to entice more users to join and add their own data to the database. In future, affiliate links may be used to link users to buying products, which will provide income to the business.
- **Who is the target audience?** There are two target audiences for this web application. Firstly, anyone who is looking to buy a child a toy, be it parents, relatives, guardians etc who would like clear honest feedback on which toy would be suitable. Secondly, those with children who can lend their expertise and experience in their reviews and recommendations on toys.
- **What are the user requirements and expectations?** The users can make their own profile in order to read and submit reviews of their own. They also expect to be able to Create, Read, Update, and Delete their own profile, toy data, and reviews whenever they want. It is expected that they can search toys to read reviews and also see other user's profiles.

#### Viability and Feasibility
Followed is an analysis of the user stories and above user and business needs ranked from 1 (least important/viable) to 5 (most important/viable):
|   Task |   Importance | Viability/Feasibility |
| --------- | ------------- | ----------------- |
| Clear home screen conveying purpose | 4 | 5 |
| Easy and intuitive navigation | 5 | 5 |
| Immediate feedback to the user | 5 | 5 |
| Responsive | 4 | 4 |
| Accessible | 5 | 4 |
| Login/Logout functionality | 5 | 5 |
| Full CRUD functionality: user account | 4 | 4 |
| Full CRUD functionality: toys | 4 | 4 |
| Full CRUD functionality: reviews | 4 | 4 |
| Robust site and data security | 5 | 4 |
| Robust defensive programming | 5 | 4 |
| Toys display page | 5 | 5 |
| Search toys functionality | 4 | 3 |
| Sort toys functionality | 4 | 3 |
| Display clear ratings | 4 | 4 |
| Scroll to top button | 3 | 3 |
| Individual toy pages showing reviews | 5 | 5 |
| Sort reviews functionality | 4 | 3 |
| Also liked functionality in reviews | 4 | 3 |
| See public profiles | 4 | 5 |
| Have contact information for the developer | 3 | 5 |
| 404 error page | 5 | 5 |
| 403 error page | 4 | 4 |
| 500 error page | 5 | 4 |

Overall, the above listed features to include in the site are all important and viable. Viability is ranked lower for those that I do not know how to implement yet but every effort will be made to get these into the finished product.

### Scope

#### Back-end
Multiple tables within a relational database are required for this project. These models are:
- **Users** table that keeps track of the users. It will consist of ID, first name, last name, username, email, password.
- **Profile** table that handles the public profile data. It will consist of ID, user id, about me, country, parenthood, profile image.
- **Toy** table that keeps track of the toys. It will consist of ID, author id, type of toy, toy name, company name, approval status, image, description, affiliate link, date of creation.
- **ToyType**: table that lists all the options for toy type. It will consist of an ID and type of toy.
- **Review** table that keeps track of the reviews. It will consist of ID, author id, toy id, the review, rating, also liked, date of creation.

#### Front-end
The website will utilise template inheritance that allows for less code to be written and quicker load times for a better user experience.

**Templates**
- base.html: This will be the base template that the others call from to ensure a cohesive structure across the website. Present here will be:
    - The header with the brand logo and title and the navigation links. Whilst logged out the navigation links will be replaced with buttons for login / sign up. When logged in the navigation bar will offer links to the user's own profile, and to view toys.
    - The footer with site name, logo, and contact information.
- home.html: This will be the website homepage. It will welcome the user with different messages if they are logged in or logged out. It will provide the user the opportunity to login or sign up if they are logged out or allow them to access the rest of the site if they are logged in.
- login.html: This will open a form allowing the user to login to the website.
- signup.html: This will open a form allowing the user to sign up to the website.
- toys.html: This will display all the toys currently reviewed on the website. Clicking on a toy will take the user to the individual toy page.
- add_toy.html: This will open a form in which the user can fill out details of a toy and submit it to be shown in the toys.html page.
- edit_toy.html: This will open a form in which the user can edit the details of a toy that they created.
- individual_toy.html: The page for an individual toy showing information on the toy and allowing users to upload, edit, or delete their own reviews.
- add_review.html: This will open a form in which the user can enter and submit a review for the toy.
- edit_review.html: This will open a form in which the user can amend their own review.
- profile.html: This page will show the public information of the user.
- edit_profile.html: This will open a form to allow the user to edit their own user profile.
- change_password.html: This will open a form in which the user can change their password.
- 403.html: A 403 error page with an explanation and link for the user to click.
- 404.html: A 404 error page with an explanation and link for the user to click.
- 500.html: A 500 error page with an explanation and link for the user to click.


### Structure

#### base.html
- Being the base template that the other templates will build from, this will have a navigation bar and a footer.
- The navigation bar will meet the requirement for intuitive and responsive navigation. It will consist of the brand logo, website title and navigation links. When logged out the navigation links will be sign up and login. When logged in the navigation links will be the Toys page, the user's profile, and a link to log out.
- The footer will have the site logo, site name, copywrite information, and contact information for the developer. This meets the requirement for providing contact details for the developer.

#### home.html
- This will provide a welcoming message and prompts for a user to their login/signup or explore the site. This meets the requirement for an informative and welcoming message.

#### signup.html
- This page will consist of a sign up form for the user to submit data and create their own account on the website. This will meet the requirement for allowing users to create accounts. It also meets some of the requirement for full CRUD functionality of the user profile.
- It will have labels and input areas for: first name, last name, username, email address and desired password. 
- There will be a submit button for the user to submit their details.

#### login.html
- This page will consist of the login form to allow the user to log into their account and access the website. This meets the requirement for allowing users to login to the website.
- There will be labels and input areas for the user's email address and password.
- Email address is chosen over username, as these are easier for the user to remember.
- There will be a submit button for the user to submit their details and login.

#### toys.html
- It will consist of a page title and a responsive grid of toys beneath a search bar and a sort menu. This meets the requirements to view toys and to search and order toys.
- Each toy object with have the image, name, rating, company, and toy description.
- There will be an option to add a toy, fulfilling the requirement for creating a toy object.
- At the bottom of the list, there will be a button to allow the user to go back to the top, for better user experience.

#### add_toy.html
- This will open the form to allow the user to add a toy to the database. This meets part of the requirement for full CRUD functionality for the user's toys.
- There will be labels and input areas for toy name, company, type, and image url.
- There will be a submit button that will add the toy to the database when clicked.

#### edit_toy.html
- This opens a form for the user who created the toy to edit the information and update the database. This meets the requirement for full CRUD functionality.
- There will be labels and input sections for each of the columns in the toy table and a submit button to commit the changes.

#### individual_toy.html
- This page will display the information along with reviews of a specific toy.
- The creator of the toy will be able to edit or delete the toy. This meets the requirement for full CRUD functionality for the user's toys.
- An average rating of the toy will be displayed.
- The reviews will say who reviewed them and have links to their profiles. This meets the requirement for seeing other user's profiles.
- The reviews will have the function to be sorted.

#### add_review.html
- This will open a form to submit a review for the toy. This meets part of the requirement for full CRUD functionality on a user's own reviews.
- A form will appear with labels and input sections for each of the columns in the review table and a submit button to add the review to the database.

#### edit_review.html
- This will open a form to allow the user to edit their own review for the toy. This meets part of the requirement for full CRUD functionality on a user's own reviews.
- A form will appear with labels and input sections for each of the columns in the review table and a submit button to update the review in the database.

#### profile.html
- This page will show the public user information. This meets the requirement for users to see each others profiles and an about-me section on the profile.
- There will be buttons to edit or delete the user's own profile. This meets the requirement for full CRUD functionality of a user's own profile.
- There will also be a button to change the user's password, meeting the requirements for full CRUD functionality of a user's own profile and the ability to change your password.
- Reviews submitted by this user will be displayed and will be able to be sorted.

#### edit_profile.html
- This will open a form for the user to update their profile details including adding an about-me section. This meets the requirements of having an about-me section and full CRUD functionality for the user's own profile.. 

#### change_password.html
- This will open a form for the user to change their password. This meets the requirements of being able to change your password and having full CRUD functionality of a user's own profile.

#### 403.html
- This page will serve the purpose of indicating that the user is trying to access something that they do not have access to. This meets the requirement for having a 403 page.
- There will be a description telling the user the error and a link back to the homepage.

#### 404.html
- This page will serve the purpose of indicating that the user has made a wrong turn somewhere. This meets the requirement for having a 404 page.
- There will be a description telling the user the error and a link back to the homepage.

#### 500.html
- This page will serve the purpose of indicating to the user that there is an error on the server end. This meets the requirement for having a 500 page.
- There will be a description telling the user the error and a link back to the homepage.

#### Information Architecture
**Front-end**: Site map <br>
Below is a proposed site map of the website showing links and redirections.
![Toy tribe site map](/documentation/design/site_map.png)<br>
The key points are:
- The navbar will display links to signup and login when the user is logged out
- The navbar will display links to home, toys, user profile, and log out when the user is logged in.
- The navbar and footer logos will be a link to the homepage
- The footer will have external links to the developer's GitHub, LinkedIn, and email
- The signup page will divert the user to the logged in page when successfully signed up
- The login page will have a link to the signup page for those without a user account yet
- The homepage will provide a link to the main toys page
- The toys page will link to individual toy pages, as well as providing the functionality of adding a toy, or editing a toy
- The individual toy page will allow users to edit the toy, delete the toy, add/edit/delete reviews. Upon deletion of the toy the users are redirected to the toys page.
- The profile page will display the user information, allowing the user to edit or delete their profile. Deletion will divert the user to the logged out home page.
- The edit profile page will provide a link to change the password, which directs the user back to the profile when changed
- Editing the reviews or toys will always divert the user back to their previous page upon completion
- Trying to access the edit page for a toy, review, or user you do not own will divert the user to the error 403 access denied page

**Back-end**: Entity-relationship-diagram (ERD) <br>
Below is a proposed ERD for the tables to be modelled for the database that is relevant to the webite purpose and contains relationships between tables.
![Toy tribe entity relationship diagram](/documentation/design/entity_relationship_diagram.png)<br>
**Explanation**
- The relational database will consist of 5 linked tables.
- The user table will house information on the user and will not use any foreign keys. It will autoincrement, giving each user a unique ID. This gives the potential functionality for users to create, edit, and delete their user account including changing password, meeting user stories 2, 12, 20, and 21.
- The toy type table will list various types of toys with incremental ids. Allowing users to search through toys based on their type, meeting user stories 10 and 17.
- The toy table will house the toy data. It will use the user_id as a foreign key in order to identify the creator of the toy. This creates a one to many relationship between users and toys, as one user may create many toys. It is linked in a way that if a user is deleted, the toy will remain in the database. The table also has a foreign key of the toy_type_id. This provides a one to one relationship, as a toy will only be able to have one toy type. This allows for functionality of the user to create, edit, delete, and search toys, meeting the requirements for user stories 6, 7, 10, 15, 17, 22, and 23. It also houses approved data, which is set to true by default but in future updates allows toy submission and editing to be approved before appearing on the site.
- The review table will house the review data. It will have the user_id as a foreign key in order to identify the author of the review. This creates a one to many relationship between users and reviews, as one user may create multiple reviews. The table also has the foreign key of toy_id to identify which toy the review is for. This creates a one to many relationship between toys and reviews, as even though only one user may create a review for a specific toy, that toy can have multiple reviews from different users. It is linked in a way that deletion of a user will not delete the review, but deletion of a toy will delete all associated reviews. The also_liked data of a review houses a list of integers that relate to toy_ids that the reviewer also liked. Instead of setting up a many to many relationship in the schema, reading the also_liked data and assigning associated toys will be handled with python code. This allows users the functionality of creating, editing, and deleting reviews, assigning ratings to toys, and sorting the reviews. This meets the requirements for user stories 7, 8, 9, 16, 18, 24 and 25.
- The profile table will house the public profile data about the user. It will have user_id as a foreign key to assign the profile to the correct user. This is a one to one relationship, as a user is only allowed one profile. It is linked in a way that deletion of the user will also delete the profile associated with them. Housing this data gives the potential functionality to edit their user profile and see other user profiles, providing the requirements for user stories 3, 13, and 14. 


#### Interactive Experience
- Clickable links will have animated effects on hover or click, providing clear feedback to the user.
- All external links will open in a new tab. 
- Content hinting will be used where possible to influence the user to scroll down and uncover new content on the pages.

### Skeleton

[Balsamiq Wireframes](https://balsamiq.com/) was used during this section to create wireframes.

#### Wireframes

[Desktop Wireframes](/documentation/design/desktop_wireframes.png)
<br>

[Mobile Wireframes](/documentation/design/mobile_wireframes.png)

### Surface

#### Colour scheme

**NOTE: FOR ACCESSIBILITY AND CONTRAST REASONS; D93B58 WAS REPLACED WITH A SHADE 10% DARKER: #D02847 ACROSS THE SITE**<br>

The colour scheme started as primary colours; red, blue, and yellow. However the blue tended to not show up well on the the other colours and was dropped. In favour of a gold colour to show up nicely on the muted yellow background. A calm red was used so as to not be to harsh on the eyes and throughout the site, all black and white colours were replaced with an off-black and off white.
The background was designed using [BGJar](https://bgjar.com/) and curvy loops and squiggles were employed to give a fun, childish appearance to the site.

The star ratings are coloured white and yellow and were the default colours used. The code and functionality was taken from [Fred Genkin](https://codepen.io/FredGenkin/pen/eaXYGV).

![Colour Scheme](/documentation/design/colour_scheme.png)

| Muted Yellow #FFF3D3| Yellow #F6D36A | Gold #8A6D1E | Red #D02847 | Off-White #F5F5F5 | Off-Black #333A3F |
| ------------------- | -------------------- | ------------ | ----------- | ----------------  | ----------------- |
| Background colour | Edit profile slider | Brand logo | Brand title | Homepage hero text | Back buttons |
| Navigation background | Review outline and shadow | | Burger menu | Homepage buttons | Navigation links |
| Burger menu background | Review name divider | | Burger menu links | Profile buttons | Developer links |
| Footer background | Delete modal divider | | Footer logo | Toy card reveal text | Homepage buttons |
| Homepage buttons: hover | | | Developer links: hover | Add toy text | Signup form icons |
| Signup button | | | Homepage buttons: hover | Back to top link | Signup form text |
| Login buttons | | | Homepage message | Individual toy information | Login form labels |
| Profile buttons: hover | | | Form error messages | Individual toy buttons | Profile text |
| Edit profile button | | | Signup button | Delete modal button hover | Profile buttons |
| Change password button | | | Login buttons | | Edit profile text |
| No reviews background | | | Profile buttons: hover | | Change password text |
| Toys button | | | Edit profile slider | | Toy card title |
| Add toy textarea | | | Edit profile button | | Toy rating border |
| Select background | | | Change password button | | No reviews text |
| Add toy button | | | Toy card links | | Toys button |
| Edit toy description area | | | Toy rating background | | Back to top border |
| Edit toy button | | | Toys button hover | | Add toy text |
| Toy information column borders | | | Toy card reveal background | | Select text hover |
| Toy button hover | | | Add toy icon | | Edit toy text |
| Review backgrounds | | | Select text | | Individual toy text |
| Liked toy link | | | Add toy button | | Individual toy buttons |
| Add review textarea | | | Form required * | | Add review text |
| Add review button | | | Edit toy button | | Edit review text |
| Edit review textarea | | | Individual toy information | | Delete modal text |
| Edit review button | | | Toy button hover | | Delete modal button hover |
| Delete modal buttons | | | Toy review title | | Sort select text |
| Delete modal background | | | Carousel divider | | |
| Modal overlay | | | Review dividers | | |
| Toy search text | | | Add review button | | |
| Error page button | | | Edit review button | | |
| | | | Delete modal confirmation | | |
| | | | Delete modal buttons | | |
| | | | Delete modal border | | |
| | | | Toy search button | | |
| | | | Error page text | | |
| | | | Error page button | | |

**Other colours used:**
- Green #008000: Verified parent tag on profile and background for success messages.

#### Typography

I wanted the typefaces used on this website to get across the fun nature of the subject matter whilst remaining legible and clear for the user. [Google Fonts](https://fonts.google.com/) was used to provide the free fonts in this project. Here are the fonts that I decided on:

**[Dangrek](https://fonts.google.com/specimen/Dangrek)**<br>
![Dangrek](/documentation/design/typeface_dangrek.png)<br>
Dangrek is a balloon-like Khmer font that is legible and fun. It was used for headings and the site logo. As a sans serif font, the backup fonts used were Arial, Helvitica, and sans-serif.

**[Playfair Display](https://fonts.google.com/specimen/Playfair+Display)**<br>
![Playfair Display](/documentation/design/typeface_playfair.png)<br>
Playfair Display is an stylish font with a modern flair. It is clear to read and gives a sense of importance, so is used for some of the page titles in my project. As a serif font, the backup fonts were Times New Roman, Times, and serif.

**[Open Sans](https://fonts.google.com/specimen/Open+Sans)**<br>
![Open Sans](/documentation/design/typeface_open_sans.png)<br>
Open sans as a user friendly, very legible appearance, and it pairs nicely with Playfair Display. It is used in navigation links and button text to give it some obvious difference from the site text. As a sans-serif font, the backup fonts were Arial, Helvetica, and sans-serif.

**[Roboto](https://fonts.google.com/specimen/Roboto)**<br>
![Roboto](/documentation/design/typeface_roboto.png)<br>
Roboto is the most popular google font with high legibility and nice curves. It is used for the bulk text of the website to be easy on user's eyes and not cause strain when reading longer reviews. As a sans serif font, the backup fonts were Arial, Helvetica, and sans-serif.

#### Images
- The icons used across the site were from [Font Awesome](https://fontawesome.com/).
- The site logo image used was from [Clipart Max](https://www.clipartmax.com/) and edited in microsoft paint to make the site logo and default toy images. The same logo was used to create the [Favicon](https://favicon.io/) for the browser tab.
- The site logo and some site headings were created used [InkPX wordart generator](https://inkpx.com/word-art-generator).
- The hero image on the homepage was retrieved from [Pixabay](https://pixabay.com/photos/building-business-design-display-1867350/) from a user named Pexels and is free to use.
- The default profile image was taken from [Pexels](https://www.pexels.com/photo/brown-teddy-bear-on-brown-wooden-bench-outside-207891/) and was free to use.

## Features

| **Browser Tab** |
|-------- |
| **Page:** All |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/browser_tab.png"></details> |
| **Details:** A favicon appears in the browser tab showing the webstie logo for immediate recognition by the user. Each page has the page title appear in the form of "Toy Tribe > Page Title" to allow the user to see just from the browser tab, the current page. |
| **User stories covered:** 11, 26|

| **Site Logo: Header** |
|-------- |
| **Page:** base.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/site_logo_header.png"></details> |
| **Details:** A site logo that is uniform across the site to provide. When clicked it directs the user to the homepage. |
| **User stories covered:** 1, 11, 27|

| **Navigation bar: Logged out** |
|-------- |
| **Page:** base.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/nav_bar_logged_out.png"></details> |
| **Details:** Links for login and signup that appear if the user is not logged in. |
| **User stories covered:** 2, 11, 12 |

| **Navigation bar: Logged in** |
|-------- |
| **Page:** base.html|
| <details><summary>Feature Image</summary><img src="/documentation/design/features/nav_bar_logged_in.png"></details> |
| **Details:** Links for home, toys, profile, and logout that appear if the user is logged in. |
| **User stories covered:** 11, 12, 27 |

| **Burger menu** |
|-------- |
| **Page:** base.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/burger_menu.png"></details> |
| **Details:** On smaller screen sizes the navigation links are replaced with a burger icon which is instantly recognisable as a minimised navigation menu. When clicked it shows links for signup and login if the user is logged out or links for home, toys, profile, and logout if the user is logged in. |
| **User stories covered:** 2, 11, 12, 27, 30|

| **Site Footer** |
|-------- |
| **Page:** base.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/footer.png"></details> |
| **Details:** A site footer that contains a logo that links back to the homepage and contact information for the website developer. |
| **User stories covered:** 1, 11, 27, 28|

| **Hero Image** |
|-------- |
| **Page:** home.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/hero_image.png"></details> |
| **Details:** A hero image of toys to welcome users to the website and give them an idea of the purpose of the website. It contains a welcome message, which reads "Welcome to Toy Tribe!" if logged out or "Welcome back to Toy Tribe!" if logged in. When logged out there are links for signup and login, and when logged in there is a link to the toys page. |
| **User stories covered:** 1, 11 |

| **Welcome Message** |
|-------- |
| **Page:** home.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/welcome_message.png"></details> |
| **Details:** A welcome message on the home page clearly lays out the purpose and content of the website as well as highlighting the solution that it can provide the user, making them more likely to join. |
| **User stories covered:** 1 |

| **Signup title** |
|-------- |
| **Page:** signup.html|
| <details><summary>Feature Image</summary><img src="/documentation/design/features/signup_title.png"></details> |
| **Details:** A title conveying the purpose of the page to the user. |
| **User stories covered:** 1|

| **Signup form** |
|-------- |
| **Page:** signup.html|
| <details><summary>Feature Image</summary><img src="/documentation/design/features/signup_form.png"></details> |
| **Details:** This form allows users to enter their details to create an account with the website. Font awesome icons appear next to the labels to help the user identify the fields at a glance. |
| **User stories covered:** 2, 3|

| **Signup alerts** |
|-------- |
| **Page:** signup.html|
| <details><summary>Feature Image</summary><img src="/documentation/design/features/signup_alert.png"></details> |
| **Details:** If the form is submitted with invalid data, an alert appears at the relevent input to alert the user. These alerts are; "Please fill in this field" for any empty fields,"Please lengthen this text to 3 characters or more (you are currently using x characters)" for username, "Please include an @ in the email address" for email, and "Please lengthen this text to 8 characters or more (you are currently using x characters)" for password. |
| **User stories covered:** 4, 19| 

| **User exists alert** |
|-------- |
| **Page:** signup.html|
| <details><summary>Feature Image</summary><img src="/documentation/design/features/user_exists.png"></details> |
| **Details:** Provides the user with an alert if they use an email address already linked with an account. |
| **User stories covered:** 4, 19|

| **Signup password alerts** |
|-------- |
| **Page:** signup.html|
| <details><summary>Feature Image</summary><img src="/documentation/design/features/signup_password_alert.png"></details> |
| **Details:** If the strength of the password does not meet the written requirements, this alert appears informing the user. |
| **User stories covered:** 4, 19|

| **Signup submit button** |
|-------- |
| **Page:** signup.html|
| <details><summary>Feature Image</summary><img src="/documentation/design/features/signup_submit_button.png"></details> |
| **Details:** A button that submits the form details, allowing the user to signup to the website. |
| **User stories covered:** 2|

| **Form Success Alert** |
| ------ | 
| **Page:** signup.html, login.html, add_toy.html, edit_toy.html, add_review.html, edit_review.html, edit_profile.html, change_password.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/form_success.png"></details> |
| **Details:** On successful submission of any form, a Materialize toast pops up informing the user that the submission was successful and alerting them that they will be redirected. |
| **User stories covered:** 19 |

| **Login title** |
|-------- |
| **Page:** login.html|
| <details><summary>Feature Image</summary><img src="/documentation/design/features/login_title.png"></details> |
| **Details:** A title for the login page informing the user of the page purpose. |
| **User stories covered:** 1|

| **Login form** |
|-------- |
| **Page:** login.html|
| <details><summary>Feature Image</summary><img src="/documentation/design/features/login_form.png"></details> |
| **Details:** A login form allowing the user to input information and gain access to the rest of the website. |
| **User stories covered:** 2|

| **Login button** |
|-------- |
| **Page:** login.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/login_button.png"></details> |
| **Details:** A login button that submits the user entered data and provides access to the rest of the website. |
| **User stories covered:** 2|

| **Signup button** |
|-------- |
| **Page:** login.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/signup_button_login.png"></details> |
| **Details:** A signup button to direct the user if they do not already have an account. |
| **User stories covered:** 2 |

| **Login alert** |
|-------- |
| **Page:** login.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/login_alert.png"></details> |
| **Details:** Alerts showing the user if they failed to meet requirements for the data entry. "Please fill in the field" if the fields are empty and "Please lengthen this text to 4 characters or more" for the email. |
| **User stories covered:** 4, 19 |

| **Login failed** |
|-------- |
| **Page:** login.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/login_failed.png"></details> |
| **Details:** An alert showing the user that the details that they entered did not match any in the database. |
| **User stories covered:** 4, 19 |

| **Profile display** |
|-------- |
| **Page:** profile.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/profile_display.png"></details> |
| **Details:** The profile display shows visiting users your country in the form of a flag, whether you are a parent, your username, description and profile image. The default profile image is a teddy bear and the default about me is "I am yet to fill this out". The username is displayed instead of first and last names to keep the user information secure. |
| **User stories covered:** 3, 4, 14 |  

| **Edit profile button** |
|-------- |
| **Page:** profile.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/edit_profile.png"></details> |
| **Details:** A button allowing the owner of the profile to edit it. When hovered, the font colour changes to yellow and the background colour changes to red showing it is clickable. |
| **User stories covered:** 5, 11, 13 |

| **Delete user button** |
|-------- |
| **Page:** profile.html|
| <details><summary>Feature Image</summary><img src="/documentation/design/features/delete_user.png"></details> |
| **Details:** A delete user button allowing the user to delete their own account if they so wish. When hovered, the font colour changes to yellow and the background colour changes to red showing it is clickable. |
| **User stories covered:** 5, 21|

| **Confirm delete modal** |
|-------- |
| **Page:** profile.html|
| <details><summary>Feature Image</summary><img src="/documentation/design/features/confirm_user_delete_modal.png"></details> |
| **Details:** This modal appears when the delete user button is clicked. It fades out the rest of the page so the modal stands out and gets the user's attention. The cancel button cancels the deletion and closes the modal, whereas the confirm button deletes the user account and redirects the user to the logged out homepage. Both buttons have hover effects to imply their use. |
| **User stories covered:** 5, 21 |

| **Reviews title** |
|-------- |
| **Page:** profile.html individual_toy.html|
| <details><summary>Feature Image</summary><img src="/documentation/design/features/profile_reviews_title.png"></details> |
| **Details:** A heading that appears on the profile if the user has submitted and reviews and preceeds the reviews themselves or if the toy has reviews on the individual toy pages. |
| **User stories covered:** 1 |

| **Sort reviews** |
|-------- |
| **Page:** profile.html, individual_toy.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/profile_sort_reviews.png"></details> |
| **Details:** A select box allowing the user to order the reviews by date submitted or review rating on the profiles or by rating on the toy pages. It refreshes the page to reorder the reviews but puts the user at this point in the page so they do not have to scroll back here. |
| **User stories covered:** 18 |

| **Reviews** |
|-------- |
| **Page:** profile.html, individual_toy.html|
| <details><summary>Feature Image</summary><img src="/documentation/design/features/profile_review.png"></details> |
| **Details:** A display box for the reviews. It includes a link to the toy reviewed (on profile) or username of the reviewer (on toy), the rating, the review description, and toys the reviewer also liked. If the user is the author of the review, it also provides links to edit and delete their review.|
| **User stories covered:** 8, 9, 13, 14 |

| **Also liked carousel** |
|-------- |
| **Page:** profile.html, individual_toy.html|
| <details><summary>Feature Image</summary><img src="/documentation/design/features/also_liked_carousel.png"></details> |
| **Details:** A display carousel for the also liked data. The user can scroll through toys that the reviewe also liked. If they created the toy, the edit and delete toy buttons appear for them. Toys that are deleted are removed globally from the also-liked data. The toy name on each page of the carousel acts as a link to the individual toy page.|
| **User stories covered:** 9 |

| **Delete review button** |
|-------- |
| **Page:** profile.html, individual_toy.html|
| <details><summary>Feature Image</summary><img src="/documentation/design/features/delete_review_button.png"></details> |
| **Details:** The delete review button allows the review author to remove their review from the database. On hover the button gets larger, changes colour, and the cursor changes to a pointer, indicating functionality. On click it opens the delete review modal. |
| **User stories covered:** 25 |

| **Delete review modal** |
|-------- |
| **Page:** profile.html, individual_toy.html|
| <details><summary>Feature Image</summary><img src="/documentation/design/features/delete_review_modal.png"></details> |
| **Details:**  This modal appears when the delete review button is clicked. It fades out the rest of the page so the modal stands out and gets the user's attention. The cancel button cancels the deletion and closes the modal, whereas the confirm button deletes the review and redirects the user to toy page if clicked from their or profile page if clicked from there. Both buttons have hover effects to imply their use. |
| **User stories covered:** 25 |

| **Back button** |
|-------- |
| **Page:** edit_profile.html, individual_toy.html, edit_toy.html, add_review.html, edit_review.html, change_password.html|
| <details><summary>Feature Image</summary><img src="/documentation/design/features/back_button.png"></details> |
| **Details:** A button taking the user to the previous page. It works by taking the the previous page, so if you were to get to individual_toy.html from toys.html, back will take you to toys.html. But if you managed to get to individual_toy.html from the reviews in the user profile, back will take you to the user profile. Code is provided to stop an infinite loop e.g. edit_toy.html <--> individual_toy.html. |
| **User stories covered:** 11 |

| **Edit profile title** |
|-------- |
| **Page:** edit_profile.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/edit_profile_title.png"></details> |
| **Details:** A title showing the user the purpose of the page. It is not in the bubble script to highlight its functionality rather than a display page. |
| **User stories covered:** 1 |

| **Edit profile form** |
|-------- |
| **Page:** edit_profile.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/edit_profile_form.png"></details> |
| **Details:** The form takes in general information to be displayed on the user's profile and updates it when submitted. The buttons have the cursor change to a pointer when hovering, indicating their functionality. |
| **User stories covered:** 13 |

| **Parent toggle** |
|-------- |
| **Page:** edit_profile.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/parent_toggle.png"></details> |
| **Details:** This toggle allows the user to select whether or not they are a parent, displaying the verified parent icon on their public profile page. |
| **User stories covered:** 13|

| **Edit password button** |
|-------- |
| **Page:** edit_profile.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/edit_password_button.png"></details> |
| **Details:** Redirects the user to change_password.html where they can update their password. |
| **User stories covered:** 20 |

| **Change password title** |
|-------- |
| **Page:** change_password.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/change_password_title.png"></details> |
| **Details:** A title showing the purpose of the page to the user. A short message displaying the password requirements to the user for a good user experience. |
| **User stories covered:** 1 |

| **Change password form** |
|-------- |
| **Page:** change_password.html|
| <details><summary>Feature Image</summary><img src="/documentation/design/features/change_password_form.png"></details> |
| **Details:** A form gathering information from the user to change their password. The submit button changes the cursor to a pointer on hover to show functionality. |
| **User stories covered:** 20 |

| **Change password errors** |
|-------- |
| **Page:** change_password.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/change_password_errors.png"></details> |
| **Details:** Errors display alerting the user to try a different password that matches the password requirements. |
| **User stories covered:** 19 |

| **Change password alert** |
|-------- |
| **Page:** change_password.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/change_password_alert.png"></details> |
| **Details:** Alerts that appear if the user has not entered information to allow the user to accurately complete the form. Displays "Please fill this field." on empty fields and specifies a password length of 8 characters or more for the new password. |
| **User stories covered:** 19 |

| **Toys title** |
|-------- |
| **Page:** toys.html|
| <details><summary>Feature Image</summary><img src="/documentation/design/features/toys_title.png"></details> |
| **Details:** A title for the toys page keeping the theme and font. |
| **User stories covered:** 1 |

| **Search toys** |
|-------- |
| **Page:** toys.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/search_toys.png"></details> |
| **Details:** A search bar for the toys page. It searches through toy name, company name, and toy type to return similar results. The "search" button activates the search based on user input and the text boldens when hovered indicating the functionality. The below toy display is only filled with those that match the search criteria when submitted. |
| **User stories covered:** 10 |

| **Sort toys** |
|-------- |
| **Page:** toys.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/sort_toys.png"></details> |
| **Details:** A sort toys functionality to order the toys in the toy display section alphabetically by name, toy company, or toy type or by their average rating, all ascending or descending. Clicking an option refreshes the page and repopulates the toy display with the toys in the chosen order. |
| **User stories covered:** 17 |

| **Toys display** |
|-------- |
| **Page:** toys.html|
| <details><summary>Feature Image</summary><img src="/documentation/design/features/toys_display.png"></details> |
| **Details:** The display area shows all of the toys in the database or those searched for.|
| **User stories covered:** 6 |

| **Toy card: closed** |
|-------- |
| **Page:** toys.html|
| <details><summary>Feature Image</summary><img src="/documentation/design/features/toy_card_closed.png"></details> |
| **Details:** Displays the individual toy details to the user. Shows the average rating, toy image and toy name. If the user created the toy it also allows them to edit and delete the toy. The card image and toy name act as hyperlinks to the individual toy page, whilst the three ellipses (...) allow the user to open the card for more information. |
| **User stories covered:** 6, 7, 11 |

| **Toy card: open** |
|-------- |
| **Page:** toys.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/toy_card_open.png"></details> |
| **Details:** The open toy card reveals more information: the name of the company that made the toy and the type of toy. The name of the toy still functions as a link to the individual toy page and the X in the top right closes the card again. The average rating and the edit/delete toy buttons are still available to the user when the card is open. |
| **User stories covered:** 6, 7, 11 |

| **Average rating** |
|-------- |
| **Page:** toys.html, individual_toy.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/average_rating.png"></details> |
| **Details:** The average rating of a toy from its reviews is displayed in the universal star system and displays numbers from 1-5 to one decimal place. This is updated whenever a review is added, deleted, or edited. It allows a user to garner how good a toy is at a glance. If there a no reviews, the star rating is replaced with the text "Not Reviewed Yet". |
| **User stories covered:** 7 |

| **Edit toy button** |
|-------- |
| **Page:** toys.html, individual_toy.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/edit_toy_button.png"></details> |
| **Details:** This button appears on the toys that the logged in user created. When hovered, the colours invert and the cursor becomes a pointer to show functionality. It takes the user to the edit_toy.html page for that specific toy. |
| **User stories covered:** 5, 22 |

| **Delete toy button** |
|-------- |
| **Page:** toys.html, individual_toy.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/delete_toy_button.png"></details> |
| **Details:** This button appears on the toys that the logged in user created. When hovered, the colours invert and the cursor becomes a pointer to show functionality. It opens the delete toy confirmation modal when clicked. |
| **User stories covered:** 5, 23 |

| **Delete toy modal** |
|-------- |
| **Page:** toys.html, individual_toy.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/delete_toy_modal.png"></details> |
| **Details:** This modal appears when the delete toy button is clicked. It fades out the rest of the page so the modal stands out and gets the user's attention. The modal description lists the toy that will be deleted on confirmation by the user. The cancel button cancels the deletion and closes the modal, whereas the confirm button deletes the toy and redirects the user to the toys page. Both buttons have hover effects to imply their use. |
| **User stories covered:** 5, 23 |

| **Back to top** |
|-------- |
| **Page:** toys.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/back_to_top.png"></details> |
| **Details:** This button appears as the last section of the toys display. Hovering turns the cursor into a pointer, indicating functionality. Clicking it smoothly scrolls the screen to the top of the page for a good user experience. |
| **User stories covered:** 5, 29 |

| **Add toy** |
|-------- |
| **Page:** toys.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/add_toy.png"></details> |
| **Details:** This add toy button floats on the bottom right hand corner of the page and is always on top and available to the user. On hover, the cursor changes to a pointer to indicate functionality. On click, it directs the user to the add toy form. |
| **User stories covered:** 15 |

| **Add toy title** |
|-------- |
| **Page:** add_toy.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/add_toy_title.png"></details> |
| **Details:** The title for the add toy form in keeping with the site style. Tells the user what page they are on. |
| **User stories covered:** 1 |

| **Add toy form** |
|-------- |
| **Page:** add_toy.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/add_toy_form.png"></details> |
| **Details:** The form letting a user add a toy. Required fields are highlighted. Unrequired forms have a default value set if they are submitted empty. The usual alert pop up occurs if a required field is left empty. |
| **User stories covered:** 15, 19 |

| **Required field** |
|-------- |
| **Page:** add_toy.html, add_review.html, edit_review.html|
| <details><summary>Feature Image</summary><img src="/documentation/design/features/required_field.png"></details> |
| **Details:** Required fields are marked with a red asterix, which leads to a comment below the form indicating to the user that these form sections must be completed. |
| **User stories covered:** 19 |

| **Edit toy title** |
|-------- |
| **Page:** edit_toy.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/edit_toy_title.png"></details> |
| **Details:** The title for the edit toy form in keeping with the site style and then the toy name clearly shown. Tells the user what page they are on. |
| **User stories covered:** 1 |

| **Edit toy form** |
|-------- |
| **Page:** edit_toy.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/edit_toy_form.png"></details> |
| **Details:** This form allows users to update a toy that they have created. It is prepopulated with the existing details and the usual alert popups occur when required fields are left blank. |
| **User stories covered:** 19, 22 |

| **Toy name** |
|-------- |
| **Page:** individual_toy.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/individual_toy_name.png"></details> |
| **Details:** The title for the tou page that the user is on. |
| **User stories covered:** 1 |

| **Individual toy description** |
|-------- |
| **Page:** individual_toy.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/individual_toy_card.png"></details> |
| **Details:** This card shows the toy image, rating, and then a table of the name, company name, type, and description. Below this there is a button to add a review if the user has not already and the edit and delete toy buttons available to the toy creator. |
| **User stories covered:** 5, 6, 7 |

| **Review toy button** |
|-------- |
| **Page:** individual_toy.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/review_toy_button.png"></details> |
| **Details:** This button only appears if the user has not already submitted a review, making it one review per person and making it harder to manipulate ratings. When hovered, the colour changes, it gets larger, and the cursor becomes a pointer, indicating functionality. When clicked it takes the user to the add review form. |
| **User stories covered:** 5, 16 |

| **Add review title** |
|-------- |
| **Page:** add_review.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/add_review_title.png"></details> |
| **Details:** The title on the add review form showing the purpose of the form and display the toy name that is being reviewed. |
| **User stories covered:** 1 |

| **Add review form** |
|-------- |
| **Page:** add_review.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/add_review_form.png"></details> |
| **Details:** The add review form collects user data. It gives feedback if sections are left black and highlights required sections. The submit review button causes the mouse to become a pointer on hover, indicating functionality. |
| **User stories covered:** 16, 19 |

| **Edit review title** |
|-------- |
| **Page:** edit_review.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/edit_review_title.png"></details> |
| **Details:** The edit review title is in keeping with the site style and informs the user of the page purpose. |
| **User stories covered:** 1 |

| **Edit review form** |
|-------- |
| **Page:** edit_review.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/edit_review_form.png"></details> |
| **Details:** The edit review form is prepopulated with the existing details. The usual error pop ups occur for empty fields. The submit review button causes the mouse to become a pointer on hover, indicating functionality. |
| **User stories covered:** 24 |

| **Error 403 page** |
|-------- |
| **Page:** 403.html |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/error_403.png"></details> |
| **Details:** This page is displayed when a user tries to access something that they do not have access to. Such as accessing the url of editing a profile, password, toy, or review that is not theirs or try to add a second review for a toy. The large no access icon portrays the purpose of the error, which is confirmed with the title "403- Access Denied". A message to redirect the user and a link for the toys page allows the user to exit the error page. On hover the button enlarges, showing functionality. |
| **User stories covered:**  1, 26, 27 |

| **Error 404 page** |
|-------- |
| **Page:** Page that does not exist. |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/error_404.png"></details> |
| **Details:** This page is displayed when a user accesses a page that does not exist. The large question mark icon portrays the purpose of the error, which is confirmed with the title "404- Page not found". A message to redirect the user and a link for the toy page allows the user to exit the error page. On hover the button enlarges, showing functionality. |
| **User stories covered:**  1, 26, 27 |

| **Error 500 page** |
|-------- |
| **Page:** Server Error |
| <details><summary>Feature Image</summary><img src="/documentation/design/features/error_500.png"></details> |
| **Details:** This page is displayed when there is a server error to inform the user that the error is not on their end. The large server icon portrays the purpose of the error, which is confirmed with the title "500- Internal Server Error". A message to redirect the user and a link for the home page allows the user to exit the error page. On hover the button enlarges, showing functionality. |
| **User stories covered:**  1, 26, 27 |