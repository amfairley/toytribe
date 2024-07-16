![Website logo](/documentation/screenshots/site-logo.png)

---

# Design

**This document covers the five stages of UX design that went into this project, along with the database design, and the final features provided.**

For overview information of this website, see README.md <br>
For information on the five planes of UX design details, see DESIGN.md <br>
For information on the integrated security built into the app, see SECURITY.md <br>
For information on the testing procedure, see TESTING.md

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

## Five Planes of UX

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
![Toy tribe site map](/documentation/design/site_map.png)

**Back-end**: Entity-relationship-diagram (ERD) <br>
Below is a proposed ERD for the tables to be modelled for the database.
![Toy tribe entity relationship diagram](/documentation/design/entity_relationship_diagram.png)

#### Interactive Experience
- Clickable links will have animated effects on hover or click, providing clear feedback to the user.
- All external links will open in a new tab. 
- Content hinting will be used where possible to influence the user to scroll down and uncover new content on the pages.

### Skeleton

[Balsamiq Wireframes](https://balsamiq.com/) was used during this section to create wireframes.

#### Wireframes

[Desktop Wireframes](/documentation/design/desktop_wireframes.png)
