![Website logo]()

---

# Toy Tribe

*An online community for rating, reviewing, and recommending children's toys. Insightful feedback from parents and guardians*

This full stack review website for children's toys was born from my wife and I's experience with finding the right toys for our child when he was young, resulting in toys that were rarely touched if ever, and not enough of the toys that were stimulating and engaging. Every child is different and we attempt to overcome that difficulty when recommending toys by providing recommendations based on what your child already enjoys. The target audience are parents, carers, primary school teachers, and others with first-hand experience of how children have responded to their toys.

![A mock-up image of the website]()

[Click here to access the site]()

---

## Table of Contents
1. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
    2. [Site Owner Goals](#site-owner-goals)
    3. [Developer Goals](#developer-goals)
2. [User Stories](#user-stories)
    1. [First Time Visitor Goals](#first-time-visitor-goals)
    2. [Returning Visitor Goals](#returning-visitor-goals)
    3. [Frequent Visitor Goals](#frequent-visitor-goals)
3. [Five Planes of UX](#five-planes-of-ux)
    1. [Strategy](#strategy)
        - [Viability and Feasibility](#viability-and-feasibility)
    2. [Scope](#scope)
        - [Back-end](#back-end)
        - [Front-end](#front-end)
    3. [Structure](#structure)
        - [base.html](#basehtml)
        - [signup.html](#signuphtml)
        - [login.html](#loginhtml)
        - [lost_password.html](#lost_passwordhtml)
        - [toys.html](#toyshtml)
        - [add_toy.html](#add_toyhtml)
        - [toy.html](#toyhtml)
        - [edit_toy.html](#edit_toyhtml)
        - [add_review.html](#add_reviewhtml)
        - [edit_review.html](#edit_reviewhtml)
        - [user_profile.html](#user_profilehtml)
        - [edit_user.html](#edit_userhtml)
        - [edit_password.html](#edit_passwordhtml)
        - [404.html](#404html)
        - [Information Architecture](#information-architecture)
        - [Interactive Experience](#interactive-experience)

## Project Goals

### User Goals
A website that is easy to navigate.
A website that will display well on different devices.
Positive and immediate feedback from the site such as on hover or on click JavaScript animations to ensure a good user experience.
Contact information of the developer.
Ability to create an account and log in and out.
Ability to create, read, update and delete personal reviews for toys.
Ability to see other people's reviews for toys.
Have my own public profile that I can add an about-me section to and show my reviews.
Ability to see other people's profiles.
Have toy recommendations based on which other toys children like.
Have my data and information stored securely.

### Site Owner Goals
Provide a community website for parents and others to share their honest reviews of children's toys.
Have potential for amazon affiliate links to be used to direct users to buy toys that they find match their needs.
A website that is responsive and works well on mobiles as well as desktops.
A website that is safe for users to sign up to and that their data is handled securely.

### Developer Goals
A well designed website that catches the attention of the users.
A responsive website where the functionality is not impacted by screen size.
Easy navigation that is intuitive and responsive.
A website designed with accessibility in mind.
A back end that will handle user details, toy details, and review details.
Full CRUD (Create, Read, Update, Delete) functionality for the user.
Defensive programming to prevent the user accidentally deleting their reviews, toys, or profile.
A finished product that will proudly be displayed within the developer's portfolio.

## User Stories

### First Time Visitor Goals
1. As a First Time Visitor, I want to be able to the tell the purpose of the website immediately, so that I can decide whether I want to use the website.
2. As a First Time Visitor, I want to be able to navigate the website easily and intuitively, so that I can find the content that I need.
3. As a First Time Visitor, I want to be able to make an account, so that I can access the website and add my own reviews.
4. As a First Time Visitor, I want to set up my profile, so that other users can understand the person behind my reviews.
5. As a First Time Visitor, I want to create information on toys, so that I can review the toy and let others review it.
6. As a First Time Visitor, I want to create reviews for toys, so that I can help the community.
7. As a First Time Visitor, I want to see other user's reviews, so that I am informed about toys that I might want to purchase.

### Returning Visitor Goals
8. As a Returning Visitor, I want to be able to log in and out of my account, so that on shared devices someone else cannot access my account.
9. As a Returning Visitor, I want to be able to update my toys and reviews, so that any changes or extra information can be added to help the community.
10. As a Returning Visitor, I want to be able to delete my toys and reviews, so that irrelevant content can be removed.
11. As a Returning Visitor, I want to be able to see other user's profiles, so I can understand the person behind their reviews.
12. As a Returning Visitor, I want to be able to search for a toy, so that I can read or make reviews about it.

### Frequent Visitor Goals
13. As a Frequent Visitor, I want to be able to navigate to the homepage if I end up on a page that does not exist, so that I am not stuck on a non existent page.
14. As a Frequent Visitor, I want to be able to contact the developer or team that runs the website, so that I can ask for help or collaborate with them.
15. As a Frequent Visitor, I want to be able to access the site on different devices and screen sizes, so that I can use the website on the go or at home.
16. As a Frequent Visitor, I want to be able to delete my profile if I want, so that my data is not stored longer than I wish it to be.
17. As a Frequent Visitor, I want to be able to easily recover my password in case I forget it, so that I can recover access to my account
18. As a Frequent Visitor, I want to be able to change my password, so that I know my account is kept secure.

## Five Planes of UX

### Strategy

- **What value does the project provide?** This project provides a website for an online community of parents and carers to share honest reviews and experiences with children's toys as a way to inform other parents and carers before they buy the toys. On top of that, it also provides context for the review in the form of sharing what other toys the child likes. For example a child that likes toy cars and trucks may rate a doll low, or a child that likes footballs and frisbees may rate a trampoline highly.
- **What are the business needs?** The business needs are to provide an intuitive, pleasant looking, and accessible website to entice more users to join and add their own data to the database. In future, affiliate links may be used to link users to buying products, which will provide income to the business.
- **Who is the target audience?** There are two target audiences for this web application. Firstly, anyone who is looking to buy a child a toy, be it parents, relatives, guardians etc who would like clear honest feedback on which toy would be suitable. Secondly, those with children who can lend their expertise and experience in their reviews and recommendations on toys.
- **What are the user requirements and expectations?** The users can make their own profile in order to read and submit reviews of their own. They also expect to be able to Create, Read, Update, and Delete their own profile, toy data, and reviews whenever they want. It is expected that they can search toys to read reviews and also see other user's profiles.

#### Viability and Feasibility
Followed is an analysis of the above user and business needs ranked from 1 (least important/viable) to 5 (most important/viable):
|   Task |   Importance | Viability/Feasibility |
| --------- | ------------- | ----------------- |
| Easy to navigate | 5 | 5 |
| Responsive | 5 | 5 |
| Immediate feedback to the user | 5 | 5 |
| Accessible | 5 | 5 |
| Store information securely | 5 | 3 |
| Informative and welcoming home screen | 5 | 5 |
| 404 page with link to homepage | 5 | 5 |
| Contact details for the developer | 3 | 5 |
| Create a user profile and log in / log out functionality| 5 | 3 |
| Recover password functionality | 4 | 3 |
| Change password functionality | 4 | 3 |
| About-me section in public profile | 3 | 4 |
| Full CRUD functionality for the user profile | 5 | 4 |
| Full CRUD functionality for the user's own reviews | 5 | 4 |
| Full CRUD functionality for the user's own toys | 5 | 4 |
| Defensive programming to stop accidental deletion of information | 5 | 4 |
| View other user's reviews and toys | 5 | 5 |
| Search toys | 4 | 3 |
| See other people's profiles | 4 | 3 |

Overall, the above listed features to include in the site are all important and viable. Viability is ranked lower for those that I do not know how to implement yet but every effort will be made to get these into the finished product.

### Scope

#### Back-end
Multiple tables within a database are required for this project. These models are:
- **User** table that keeps track of the user's name, email, and password for created users.
- **Toy** table that keeps track of the toy name, company, type, and image url for created toys.
- **Review** table that keeps track of the review, rating, the user that left the review, the toy being reviewed, and similar toys children liked for created reviews.
- **Profile** table that keeps track the about me section, country, whether they are a parent, created toys, and created reviews for the user.

#### Front-end
The website will utilise template inheritance that allows for less code to be written and quicker load times for a better user experience.
**Templates**
- base.html: This will be the base template that the others call from to ensure a cohesive structure across the website. Present here will be:
    - The header with the brand logo and title and the navigation links. Whilst logged out the navigation links will be replaced with buttons for login / sign up. When logged in the navigation bar will offer links to the user's own profile, and to view toys.
    - The footer with site name, logo, and contact information.
- login.html: This will open a form allowing the user to login to the website.
- signup.html: This will open a form allowing the user to sign up to the website.
- lost_password.html: This will open a form allowing the user to reset their password.
- toys.html: This will act as the website homepage. If the user is not logged in it will display a welcome message to the website and some text and a link for the user to either login or sign up. When logged in it will display all the toys currently reviewed on the website. Clicking on a toy will take the user to the individual toy page.
- add_toy.html: This will open a form in which the user can fill out details of a toy and submit it to be shown in the toys.html page.
- toy.html: The page for an individual toy showing information on the toy and allowing users to upload, edit, or delete their own reviews.
- edit_toy.html: This will open a form in which the user that created a toy can edit the details.
- add_review.html: This will open a form in which the user can enter and submit a review for the toy.
- edit_review.html: This will open a form in which the user can amend their own review.
- user_profile.html: This page will show the public information of the user.
- edit_user.html: This will open a form to allow the user to edit their own user profile.
- edit_password.html: This will open a form to allow the user to change their password.

### Structure

#### base.html
- Being the base template that the other templates will build from, this will have a navigation bar and a footer.
- The navigation bar will meet the requirement for intuitive and responsive navigation. It will consist of the brand logo, website title and navigation links. When logged out the navigation links will be sign up and login. When logged in the navigation links will be the Toys page, the user's profile, and a link to log out.
- The footer will have the site logo, site name, copywrite information, and contact information for the developer. This meets the requirement for providing contact details for the developer.

#### signup.html
- This page will consist of a sign up form for the user to submit data and create their own account on the website. This will meet the requirement for allowing users to create accounts. It also meets some of the requirement for full CRUD functionality of the user profile.
- It will have labels and input areas for: first name, last name, email address and desired password. 
- There will be a submit button for the user to submit their details.

#### login.html
- This page will consist of the login form to allow the user to log into their account and access the website. This meets the requirement for allowing users to login to the website.
- There will be labels and input areas for the user's email address and password.
- There will be a submit button for the user to submit their details and login.
- There will be a link to open lost_password.html for users who have forgotten their password. This meets the requirement for password recovery.

#### lost_password.html
- This will open the form allowing the user to recover their password.
- The form will consist of a label and input for the user's email address and the password will be sent to the user via email. This meets the requirement for password recover.

#### toys.html
- This will serve as the homepage for the website.
- When logged out the user will be met with a welcome message on top of a hero image with some descriptive text about the website and a prompt for the user to either sign up or login to continue. This meets the requirement for a welcoming and informative home screen.
- When logged in the user will be met with a page title and a responsive grid of toys beneath a search bar. This meets the requirements to view toys and to search toys.
- The last entry in the grid will be an option for the user to add a toy if it is not already in the list. This meets the requirement for adding toys.

#### add_toy.html
- This will open the form to allow the user to add a toy to the database. This meets part of the requirement for full CRUD functionality for the user's toys.
- There will be labels and input areas for toy name, company, type, and image url.
- There will be a submit button that will add the toy to the database when clicked.

#### toy.html
- This page will display the information along with reviews of a specific toy.
- The creator of the toy will be able to edit or delete the toy. This meets the requirement for full CRUD functionality for the user's toys.
- An average rating of the toy will be displayed.
- The reviews will say who reviewed them and have links to their profiles. This meets the requirement for seeing other user's profiles.

#### edit_toy.html
- This opens a form for the user who created the toy to edit the information and update the database. This meets the requirement for full CRUD functionality.
- There will be labels and input sections for each of the columns in the toy table and a submit button to commit the changes.

#### add_review.html
- This will open a form to submit a review for the toy. This meets part of the requirement for full CRUD functionality on a user's own reviews.
- A form will appear with labels and input sections for each of the columns in the review table and a submit button to add the review to the database.

#### edit_review.html
- This will open a form to allow the user to edit their own review for the toy. This meets part of the requirement for full CRUD functionality on a user's own reviews.
- A form will appear with labels and input sections for each of the columns in the review table and a submit button to update the review in the database.

#### user_profile.html
- This page will show the public user information. This meets the requirement for users to see each others profiles and an about-me section on the profile.
- There will be buttons to edit or delete the user's own profile. This meets the requirement for full CRUD functionality of a user's own profile.
- There will also be a button to change the user's password, meeting the requirements for full CRUD functionality of a user's own profile and the ability to change your password.

#### edit_user.html
- This will open a form for the user to update their profile details including adding an about-me section. This meets the requirements of having an about-me section and full CRUD functionality for the user's own profile.
- There will be a label and input section for each column in the user table excluding email and password. 

#### edit_password.html
- This will open a form for the user to change their password. This meets the requirements of being able to change your password and having full CRUD functionality of a user's own profile.

#### 404.html
- This page will serve the purpose of indicating that the user has made a wrong turn somewhere. This meets the requirement for having a 404 page.
- There will be a description telling the user the error and a link back to the homepage.

#### Information Architecture
**Front-end**: Site map <br>
Below is a proposed site map of the website showing links and redirections.
![Toy tribe site map](/documentation/five_planes_of_ux/site_map.png)

**Back-end**: Entity-relationship-diagram (ERD) <br>
Below is a proposed ERD for the tables to be modelled for the database.
![Toy tribe entity relationship diagram](/documentation/five_planes_of_ux/entity_relationship_diagram.png)

#### Interactive Experience
- Clickable links will have animated effects on hover or click, providing clear feedback to the user.
- All external links will open in a new tab. 
- Content hinting will be used where possible to influence the user to scroll down and uncover new content on the pages.