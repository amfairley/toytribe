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
- change_password.html: This will open a form in which the user can change their password.
- profile.html: This page will show the public information of the user.
- edit_profile.html: This will open a form to allow the user to edit their own user profile.
- edit_password.html: This will open a form to allow the user to change their password.
- 403.html: A 403 error page with an explanation and link for the user to click.
- 404.html: A 404 error page with an explanation and link for the user to click.
- 500.html: A 500 error page with an explanation and link for the user to click.
