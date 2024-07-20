![Website logo](/documentation/screenshots/site_logo.png)

---

# Toy Tribe

*An online community for rating, reviewing, and recommending children's toys. Insightful feedback from parents and guardians*

This full stack review website for children's toys was born from my wife and I's experience with finding the right toys for our child when he was young, resulting in toys that were rarely touched, and not enough of the toys that were stimulating and engaging. Every child is different and we attempt to overcome the difficulty of recommending toys by providing recommendations based on what your child already enjoys. The target audience are parents, carers, primary school teachers, and others with first-hand experience of how children have responded to their toys.

![A mock-up image of the website](/documentation/screenshots/site_mockup.png)

[Click here to access the site](https://toytribe-78734704f44d.herokuapp.com/)

For information on the development and deployment of this website, see DEV.md <br>
See [DESIGN.md](/DESIGN.md) for information on the five planes of UX design, site map, database scheme, and features. <br>
For information on the integrated security built into the app, see SECURITY.md <br>
See [TESTING.md](/TESTING.md) for information on the testing of the site <br>
For information on the testing procedure, see TESTING.md

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
3. [Security](#security)
    1. [Defensive Programming](#defensive-programming)
    2. [Future Security Implementations](#future-security-implementations)
4. [Future Development](#future-development)
5. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks](#frameworks)
    3. [Libraries and Packages](#libraries-and-packages)
    3. [Tools](#tools)
6. [Credits](#credits)
7. [Acknowledgements](#acknowledgements)

## Project Goals

### User Goals
A website that is easy to navigate.
A website that will display well on different devices.
Positive and immediate feedback from the site such as on hover or on click JavaScript animations to ensure a good user experience.
Contact information of the developer.
Able to create an account to log in and out.
A public profile page that displays information about me and my reviews.
Full CRUD (Create Read Update Delete) functionality on my user account.
Full CRUD (Create Read Update Delete) functionality on toys that I add to the database.
Full CRUD (Create Read Update Delete) functionality on reviews that I leave.
Security in place to stop others updating or deleting my account, created toys, or created reviews.
Ability to see other people's reviews for toys.
Ability to see other people's public profiles.
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
Full CRUD (Create, Read, Update, Delete) functionality for the user on their account, created toys, and created reviews.
Defensive programming to ensure a pleasant user experience.
A finished product that will proudly be displayed within the developer's portfolio.

## User Stories

### First Time Visitor Goals
1. As a First Time Visitor, I want to be able to the tell the purpose of the website immediately, so that I can decide whether I want to use the website.
2. As a First Time Visitor, I want to be able to create an account and login, so that I can access the website see the content.
3. As a First Time Visitor, I want a profile to be created for me when I sign up with default values, so that I can access the site quickly and edit them later if I choose to.
4. As a First Time Visitor, I want the site to handle my data securely, so that I am confident nothing bad would happen if I were to signup.
5. As a First Time Visitor, I want the site content to be safe and secure, so that I am not open to any malicious activities.
6. As a First Time Visitor, I want to be able to see the toys in the database, so as to browse for toys that might interest my child.
7. As a First Time Visitor, I want to be able to see clearly and intuitively the ratings of toys, so that I can see if they are a good fit for my child.
8. As a First Time Visitor, I want to see reviews of toys, so that I can see the context behind their review.
9. As a First Time Visitor, I want to see what other toys the reviewer liked, so that I can see if my child might agree with their review.
10. As a First Time Visitor, I want to be able to search toys, so as to find ones that I am looking for quicker.
11. As a First Time Visitor, I want to be able to navigate the website easily and intuitively, so that I can find the content that I need.

### Returning Visitor Goals
12. As a Returning Visitor, I want to be able to log in and out of my account, so that on shared devices someone else cannot access my account.
13. As a Returning Visitor, I want to be able to edit and update my profile, so that my data stays up to date and other users can see information about me.
14. As a Returning Visitor, I want to be able to see the profiles of people who leave reviews, so as to provide further context to their review.
15. As a Returning Visitor, I want to be able to add a toy to the database if it is not already there, so as to allow myself and others to review it.
16. As a Returning Visitor, I want to be able to submit my own reviews on toys, so as to inform other users of my experience.
17. As a Returning Visitor, I want to be able to sort the toys, so that I can find toys that interest me.
18. As a Returning Visitor, I want to be able to sort reviews on toy and profile pages, so as to see different views.
19. As a Returning Visitor, I want to be informed if I cause errors in forms, so that I am not clueless as to what went wrong.

### Frequent Visitor Goals
20. As a Frequent Visitor, I want to be able to change my password, so as to keep my account secure over time.
21. As a Frequent Visitor, I want to be able to delete my account if I wish, so as to retain agency over my information. 
22. As a Frequent Visitor, I want to be able to edit toys that I create, so as to keep information current or correct mistakes.
23. As a Frequent Visitor, I want to be able to delete toys that I create, so I may remove it if it is a duplicate.
24. As a Frequent Visitor, I want to be able to edit reviews that I have created, so as to keep them accurate or update them.
25. As a Frequent Visitor, I want to be able to delete reviews that I have created, so that I can remove irrelevant content.
26. As a Frequent Visitor, I want to be informed if I land on a restricted or non existent page, so that I can refrain from doing that again.
27. As a Frequent Visitor, I want to be able to navigate to the homepage if I end up on a page that does not exist, so that I am not stuck on a non existent page.
28. As a Frequent Visitor, I want contact information for the developer, so that I can ask questions or propose a collaboration.
29. As a Frequent Visitor, I do not want to have to scroll to the top of the toys page when I reach the bottom, as it is a bad user experience.
30. As a Frequent Visitor, I want the navigation bar to shrink down on smaller screens, so that it does not take up a lot of my screen space.

## Security
Security concerns were considered throughout the development of this project and the implementation of the following security protocols were made:
- **.gitignore file**: This was used to hide the env.py file so as to not publicly upload any secret keys to GitHub.
- **403 error handling**: Only the creator of the user profile, toy, or review can edit and delete them. Trying to maliciously access this function without being the creator diverts the user to the error 403 access denied page.
- **Password strength**: The password requirement for user accounts are at least 1 capital letter, 1 special character, 1 number and over 8 characters long, providing users with strong passwords by default.
- **Password storage**: When the user or creates their password, it is not saved as it is in the database. It is salted with an 8 byte string to precede the password. This ensures that any 2 exact passwords are different before the hashing. The hashing is done using Password-Based Key Derivation Function 2 (PBKDF2) with Secure Hash Algorithm 256-bit (SHA-256) and the result is stored as the user password. This makes it computationally expensive to crack passwords, providing robust security. This is a one-way hash, making it impossible to reverse engineer the user password from the stored value.
- **Usernames**: Originally first and last names were displayed on user reviews and user profiles, but this was changed to require users to create usernames. This allows users to feel that their personal information is not being shared without their consent.
- **External links**: All external links open in a new tab and have the attribute `rel="noopener"` which removes the threat of [Tabnabbing](https://en.wikipedia.org/wiki/Tabnabbing).
- **Cross-Site-Request-Forgery Protection**: WTFroms provides CSRF protection by generating a hidden field in each form containing a unique, secret token. When a form is submitted, the server uses this value to ensure that the submitted data is from my website and not from a malicious third party. This is achieved in the code with `{{ form.hidden_tag() }}` being present as the first thing in any form on this website.
- **Database storage**: The database information is stored and maintained in a secure PostgreSQL database that can be only accessed with a secret key. To ensure that the data is kept securely, [binascii](https://docs.python.org/3/library/binascii.html) was used to generate a 24-byte random key converted into hexadecimal code using `secret_key=binascii.hexlify(os.urandom(24)).decode('utf-8)` which gave a 48 character string that was used for my secret key.
- **Cross-Site Scripting (XSS) Defence**: To avoid the user providing malicious information into forms such as scripts; Flask-WTF is used to create the forms, which is a secure framework that automatically escapes user input, preventing any entered scripts from running.

### Defensive Programming
Along with security measures, defensive programming was implemented throughout to ensure a good user experience. Examples of these are:
- There is a modal pop up to confirm any deletion, adding security against accidental deletion
- Creating or changing a password requires a password confirmation, preventing the user from creating a typo in their password and effectively locking themselves out of their user account
- Error messages appear in forms to inform the user of the issues
- Required fields are highlighted in forms so that a user does not try and submit without providing necessary data
- The input of toy name and company name are sanitised, meaning that users are not frustrated by simple grammatical errors
- Only 1 review per toy per person is allowed to prevent malicious manipulation of the toy rating system

### Future Security Implementations
Security risk are ever present so future updates will provide the extra security features:
- Admin approval of verified parent, image uploads, toy creation etc to ensure the site remains user friendly
- Profiles will have the option to allow information to be public or private. This will be achieved with an extra column in the Profile table for private/not private. One feature of this will be to remove the automatic hyperlink on the review author to the user profile if set to private.
- Email verification to ensure that sign ups are real
- A requirement to change password every year, to ensure the safety of user accounts.

## Future Development
Listed here are features that will be introduced in future updates to provide a better user experience:
- Success message for adding/editing/deleting things
- Select country default on profile

- Functionality to vote on specific review
- Pages for toys and reviews so performance does not suffer with a large dataset
- Image upload function for toy images
- Image upload function for profile image
- Multiple default profile images to pic from
- Enable multiple selection for toy types
- Carousel displaying toys created on profile page
- Favourite toys list on profile that is automatically added to reviews and replaces also_liked
- Automatically login when you sign up
- Display affiliate links for purchasing toys
- Update database model for date_created and date_edited on all tables for enhanced querying capabilities

The current database schema has been developed to be future proof in the following ways:
- Amazon affiliate link column is already in the Toy table
- Improved querying capabilities with index=True on emails in the Users model

## Technologies Used

### Languages

- [HTML](https://en.wikipedia.org/wiki/HTML)
    - Markup language used for website structure
- [CSS](https://en.wikipedia.org/wiki/CSS)
    - Used for styling the elements on the webpage
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    - Used for dynamic functionality on the website
- [Python](https://www.python.org/)
    - Used for server side scripting and backend development
- [SQL](https://en.wikipedia.org/wiki/SQL)
    - Used for maintenance and querying of database throughout to confirm correct functionality

### Database Management System

- [PostgreSQL](https://www.postgresql.org/)
    - An object relational database management system used to get, store and update my database

### Frameworks
- [Materialize](https://materializecss.com/)
    - A CSS and JavaScript library used for functionality and styling within this project. 
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
    - A flexible python microframework providing me the basis to get my web application running, providing URL routing, Jinja2 templating, form templating, and Web Server Gateway Interface compliance.

### Libraries and packages
- [Pip](https://pypi.org/project/pip/)
    - The package installer for python used to install packages and libraries 
- [Jinja2](https://palletsprojects.com/p/jinja/)
    - A template engine for python allowing template inheritance and injection of python variables and control structures into HTML pages.
- [SQLAlchemy](https://www.sqlalchemy.org/)
    - An object relational mapper, allowing the full power and flexibility of SQL as pythonic code.
- [Psycopg2](https://pypi.org/project/psycopg2/)
    - A PostgreSQL database adaptor for python, granting me database connection and querying capabilities.
- [WTForms](https://wtforms.readthedocs.io/en/3.1.x/)
    - A form validation and rendering library used for producing forms for my website.
- [Werkzeug](https://werkzeug.palletsprojects.com/en/3.0.x/)
    - A WSGI web application library. Used in my project for security and hashing user passwords.
- [pycountry](https://pypi.org/project/pycountry/)
    - A library of country information used to display country flags on the user profiles.
- [binascii](https://docs.python.org/3/library/binascii.html)
    - Used to convert data and provide a secure secret key for my website to connect to my database with.

### Tools
- [Visual Studio Code](https://code.visualstudio.com/)
    * This is my IDE of choice for writing my HTML, CSS, JavaScript, and Python code for this project
- [Git](https://git-scm.com/)
	* Used for version control
- [GitHub](https://github.com/)
	* Used to store the code in a repository
- [Heroku](https://www.heroku.com/)
    - A cloud platform as a service (PaaS) where I hosted my deployed project and can manage my database through.
- [Python minifier](https://python-minifier.com/)
    - Used to provide an example of minified code to implemented after assessment.
- [BGJar](https://bgjar.com/)
    - Used to provide the colourful background for the website.
- [InkPX wordart generator](https://inkpx.com/word-art-generator)
    - Used to create wordart for the site logo and page titles.
- [ClipArtMax](https://www.clipartmax.com/)
    - Used to provide the site logo image.
- [Balsamiq Wireframes](https://balsamiq.com/)
    - Used to create wireframes for the project.
- [LucidChart](https://www.lucidchart.com/pages/?)
    - Used to create the site map and database schema.
- [Multi Mock-up](https://techsini.com/multi-mockup/index.php)
    - Used to create mock-up images of the site for README.md.
- [Google Fonts](https://fonts.google.com/)
    - Used to supply typefaces for the website.
- [Font Awesome](https://fontawesome.com/)
    - Used throughout for decorative icons.
- [Favicon](https://favicon.io/)
	- Used to add the site logo to the browser tab.
- [Cloud Convert](https://cloudconvert.com/png-to-webp)
    - Used for image optimisation to convert from .png to .webp format.
- [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)
    - Used for testing the webpage during development and testing the performance using Lighthouse.
- [W3C HTML Validation Service](https://validator.w3.org/)
    - Used to validate the HTML code.
- [W3C Jigsaw CSS Validation Service](https://jigsaw.w3.org/css-validator/)
    - Used to validate the CSS code.
- [JSHint](https://jshint.com/)
    - Used to validate JavaScript code.
- [Wave Web Accessibility Evaluation Tool](https://wave.webaim.org/)
    - Used to validate the accessibility of the web page.
- [Code Institute Python Linter](https://pep8ci.herokuapp.com/)
    - Used to validate Python code against PEP8 standards.

## Credits
- The styling and functionality of the star ratings from [Fred Genkin](https://codepen.io/FredGenkin/pen/eaXYGV)
- The hero image on the homepage was retrieved from [Pixabay](https://pixabay.com/photos/building-business-design-display-1867350/) from a user named Pexels and is free to use.
- The default profile image was taken from [Pexels](https://www.pexels.com/photo/brown-teddy-bear-on-brown-wooden-bench-outside-207891/) and was free to use.

## Acknowledgements
- 