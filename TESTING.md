![Website logo](/documentation/screenshots/site_logo.png)

---

# Testing

Manual testing (often called user testing) is where the site is manually tested by clicking buttons, filling out forms, and testing all the logic. Automated testing involves using scripts and a testing frameworks to test functionality. Automated testing can be quick, thorough, and allow the developer to pick up errors early on but relies on the developer asking the right questions and does not test for user experience. For this project, I have concentrated on manual testing to test the user experience and automated testing for validation of the code, accessibility testing, and site performance testing.<br>
Regression testing, to ensure that new features do not cause bugs, was not possible without custom automated testing. However, during development each feature was robustly tested when implemented, with fixes being able to be applied as and when they were encountered. Larger bugs that took some time to fix are documented at the bottom of this document. Overall, manual and automated testing were completed upon deployment of the final project to ensure that there were no bugs left in the functionality of the website. Going forward, the automated and manual testing described in this document will be completed for each affected file or feature when future features are implemented to ensure that everything works as it should.

See [README.md](/README.md) for information on project goals, user stories, security, future developments, technologies used, user feedback, credits, and acknowledgements.<br>
See [DESIGN.md](/DESIGN.md) for information on the five planes of UX design, site map, database schema, and features. <br>
See [DEV.md](/DEV.md) for an overview of the continuous integration and deployment process, how I set up my development environment, and deployment steps.

---

## Table of contents
1. [Testing User Stories](#testing-user-stories)
2. [Manual Testing](#manual-testing)
3. [Device and Browser Testing](#device-and-browser-testing)
4. [Automated Testing](#automated-testing)
    * [Accessibility Testing](#accessibility-testing)
    * [Performance Testing](#performance-testing)
    * [HTML Validation](#html-validation)
    * [CSS Validation](#css-validation)
    * [JavaScript Validation](#javascript-validation)
    * [Python Validation](#python-validation)
5. [Bugs](#bugs)
    * [Bug 1](#bug-1)
    * [Bug 2](#bug-2)
    * [Bug 3](#bug-3)
    * [Bug 4](#bug-4)
    * [Bug 5](#bug-5)
    * [Known bugs](#known-bugs)
6. [Analytics](#analytics)

## Testing user stories 
The [user stories](/README.md#user-stories) have been a driving force for the development of this project. Here, features are assigned to the user stories to show completion. More can be seen about the individual features [here](/DESIGN.md#features). This section is designed so as to confidently say that I have successfully met all of the criteria that I set out with to create a website that the target audience of parents and cares will find usable, intuitive, and that provides a unique purpose.

**1: I want to be able to the tell the purpose of the website immediately**<br>
This requirement is met by the site logo in the header and footer, the hero image and welcome text on the home page, and the page titles.

**2: I want to be able to create an account and login**<br>
This requirement is met by the navigation links for signup and login in the header and burger menu, the signup form, and the login form. 

**3: I want a profile to be created for me when I sign up with default values**<br>
This requirement is met by the signup form which creates a user profile on submission, and the default profile page for the user.

**4: I want the site to handle my data securely**<br>
This requirement is met by alerts when entering invalid information in forms, and the profile page displaying username instead of actual name. 

**5: I want the site content to be safe and secure**<br>
This requirement is met by only allowing owners to edit or delete their profile, toys and reviews, and confirmation modals when deleting.

**6: I want to be able to see the toys in the database**<br>
This requirement is met by the toys display on the toys page, the toy cards on the toys and individual toy pages, and the open card information on the toys page.

**7: I want to be able to see clearly and intuitively the ratings of toys**<br>
This requirement is met by the star ratings showing the average rating to one decimal place on the open and closed toy cards on the toy page, and the average rating on the individual toy pages.

**8: I want to see reviews of toys**<br>
This requirement is met by showing reviews on the profile and individual toy pages, and the average rating displayed on the toys page.

**9: I want to see what other toys the reviewer liked**<br>
This requirement is met by the review content of a also liked carousel. 

**10: I want to be able to search toys**<br>
This requirement is met by the search bar on the toys page.

**11: I want to be able to navigate the website easily and intuitively**<br>
This requirement is met by the browser tab favicon and title, the site logo link in the header and footer, the site navigation links and burger menu, the back button which intuitively takes the user to the previous page, even if multiple pages could lead to it, the links to individual toys from clicking the toys on the toys page, and the more information button on the toy cards.

**12: I want to be able to log in and out of my account**<br>
This requirement is met by the login navigation link and the logout navigation link in the header and the burger menu.

**13: I want to be able to edit and update my profile**<br>
This requirement is met by edit profile page, and the edit profile form.

**14: I want to be able to see the profiles of people who leave reviews**<br>
This requirement is met by the profile pages of users, and displaying reviews on the profile pages.

**15: I want to be able to add a toy to the database if it is not already there**<br>
This requirement is met by the add toy button on the toys page, and the add toy form.

**16: I want to be able to submit my own reviews on toys**<br>
This requirement is met by the review toy button on the individual toy pages, and the review form.

**17: I want to be able to sort the toys**<br>
This requirement is met by the sort toys select box on the toys page.

**18: I want to be able to sort reviews on toy and profile pages**<br>
This requirement is met by the sort select element on the individual toy pages and the profile page.

**19: I want to be informed if I cause errors in forms**<br>
This requirement is met by error pop ups in forms, the required field hinting on forms, and the form success messages.

**20: I want to be able to change my password**<br>
This requirement is met by the link to edit a password when editing profile, and the change password form.

**21: I want to be able to delete my account if I wish**<br>
This requirement is met by the delete user button, and the confirm delete modal.

**22: I want to be able to edit toys that I create**<br>
This requirement is met by the edit toy button on the toys you create and the edit toy form.

**23: I want to be able to delete toys that I create**<br>
This requirement is met by the delete toy button and the delete toy confirmation modal.

**24: I want to be able to edit reviews that I have created**<br>
This requirement is met by the edit review button on the reviews and the edit review form.

**25: I want to be able to delete reviews that I have created**<br>
This requirement is met by the delete review button and confirm delete modal.

**26: I want to be informed if I land on a restricted or non existent page**<br>
This requirement is met by the browser tab title, the error 403 page and message, the error 404 page and message, and the error 500 page.

**27: I want to be able to navigate to the homepage if I end up on a page that does not exist**<br>
This requirement is met by the site logo link in the header and footer, the home navigation link in the header and burger menu, the link back to toys page on the 403 error page and 404 page, and the link back to the homepage on the error 500 page.

**28: I want contact information for the developer**<br>
This requirement is met by contact information in the site footer.

**29: I do not want to have to scroll to the top of the toys page when I reach the bottom**<br>
This requirement is met by the back to top button at the bottom of the toys page.

**30: I want the navigation bar to shrink down on smaller screens**<br>
This requirement is met by the burger menu for navigation links on smaller devices.


## Manual Testing

For each testing step that involved manipulation of database objects, the database was queried in PostgreSQL before and after to ensure that objects were created/edited/deleted correctly. All worked as it should.

| Feature | Action | Expected results | Passed | Comments |
| ----- | ----- | ----- | ----- | ----- |
| **base.html** | | | | |
| Navigation bar site logo | Click | Directs to home page | Y | N/A |
| Navigation bar site logo | Resize | Shrinks at screen sizes under 401px | Y | N/A |
| Footer site logo | Click | Directs to home page | Y | N/A |
| Footer site logo | Resize | Shrinks at screen sizes under 401px | Y | N/A |
| Burger menu | Resize screen | Appears under 993px screen width | Y | N/A |
| Logged out: Signup nav link | Click | Directs to signup page | Y | N/A |
| Logged out: Signup burger link | Click | Directs to signup page | Y | N/A |
| Logged out: Login nav link | Click | Directs to login page | Y | N/A |
| Logged out: Login burger link | Click | Directs to login page | Y | N/A |
| Logged in: Navbar link Home | Click | Directs to home page | Y | N/A |
| Logged in: Burger link Home | Click | Directs to home page | Y | N/A |
| Logged in: Navbar link Toys | Click | Directs to toys page | Y | N/A |
| Logged in: Burger link Toys | Click | Directs to toys page | Y | N/A |
| Logged in: Navbar link Profile | Click | Directs to user profile page | Y | N/A |
| Logged in: Burger link Profile | Click | Directs to user profile page | Y | N/A |
| Logged in: Navbar link Logout | Click | Logs out, displays message, and directs to home page | Y | N/A |
| Logged in: Burger link Logout | Click | Logs out, displays message, and directs to home page | Y | N/A |
| Footer links | Hover | Colour changes on hover | Y | N/A |
| Footer link: email | Click | Opens an email to the developer in a new window | Y | N/A |
| Footer link: LinkedIn | Click | Opens the developers LinkedIn profile in a new tab | Y | N/A |
| Footer link: GitHub | Click | Open the developers GitHub profile in a new tab | Y | N/A |
| **home.html** | | | | |
| Hero Text | Login | Displays different message if logged in | Y | N/A |
| Hero links | Hover | Colour changes | Y | N/A |
| Logged out: Signup hero image link | Click | Directs to signup page | Y | N/A |
| Logged out: Login hero image link | Click | Directs to login page | Y | N/A |
| Loggin in: Toys hero image link | Click | Directs to toys page | Y | N/A |
| Logged out: Signup/Login hero buttons | Resize | Shrink at screen sizes under 401px | Y | N/A |
| **signup.html** | | | | |
| First name field | Leave empty | Alert appears asking user to complete the field | Y | N/A |
| Last name field | Leave empty | Alert appears asking user to complete the field | Y | N/A |
| Username field | Leave empty | Alert appears asking user to complete the field | Y | N/A |
| Username field | Make a short username | Alert appears asking user to make the user name at least 3 characters | Y | N/A |
| Username field | Use special characters | Alert appears displaying invalid characters | Y | N/A |
| Email field | Leave empty | Alert appears asking user to complete the field | Y | N/A |
| Email field | Do not include "@" | Alert appears telling user to includer "@" | Y | N/A |
| Email field | End email with "@" | Alert appears telling user to complete email address | Y | N/A |
| Email field | Reuse an email address | Alert appears informing the user that the email addres is already in use | Y | N/A |
| Password field | Leave empty | Alert appears asking user to complete the field | Y | N/A |
| Password field | Make a password less than 8 characters | Alert appears informing the user to make the password at least 8 characters | Y | N/A |
| Confirm password field | Leave empty | Alert appears asking user to complete the field | Y | N/A |
| Passwords | Make them not match | Alert appears highlighting that passwords do not match | Y | N/A |
| Passwords | No capital letters, numbers, or special characters | Alert appears reminding the user of the password strength requirements | Y | N/A |
| Signup button | Add valid detail and click | Success message appears and user is redirected to login screen | Y | N/A |
| **login.html** | | | | |
| Email field | Leave empty | Alert appears asking user to complete the field | Y | N/A |
| Email field | Use less than 4 characters | Alert appears asking user to complete the field with a longer entry | Y | N/A |
| Password field | Leave empty | Alert appears asking user to complete the field | Y | N/A |
| Password field | Complete incorrectly | Alert appears informing the user that the login failed and to check their credentials | Y | N/A |
| Sign up button | Click | Directs user to the signup page | Y | N/A |
| Login button | Enter correct information and click | Success message appear and directs user to the logged in homepage | Y | N/A |
| **toys.html** | | | | |
| Toys page | Access url whilst logged out | Redirected to logged out homepage | Y | N/A |
| Search bar | Search something | Toys with matching or similar toy name, toy company, or toy type are displayed | Y | N/A |
| Sort toys: Name A-Z | Select | Displays toys in alphabetical order by toy name | Y | N/A |
| Sort toys: Name Z-A | Select | Displays toys in reverse alphabetical order by toy name | Y | N/A |
| Sort toys: Toy type A-Z | Select | Displays toys in alphabetical order by toy type | Y | N/A |
| Sort toys: Toy type Z-A | Select | Displays toys in reverse alphabetical order by toy type | Y | N/A |
| Sort toys: Company A-Z | Select | Displays toys in alphabetical order by toy company name | Y | N/A |
| Sort toys: Company Z-A | Select | Displays toys in reverse alphabetical order by toy company name | Y | N/A |
| Sort toys: Rating low to high | Select | Displays toys in order of average rating from 0-5 | Y | N/A |
| Sort toys: Rating high to low | Select | Displays toys in order of average rating from 5-0 | Y | N/A |
| Toy display area | Resize screen | Area shows rows of 4 on large screens, 3 on medium screens, 2 on small screens, and 1 on mobile | Y | Maximum width of the toy and search areas set to 2000px |
| Toy card rating | N/A | Displays "Not Reviewed Yet" if no reviews or average review to 1 decimal place | Y | N/A |
| Toy card image | Click | Directs user to correct individual toy page | Y | N/A |
| Toy card name | Click | Directs user to correct individual toy page | Y | N/A |
| Toy card ellipses | Click | Opens the toy card to review more information | Y | N/A |
| Open toy card cross | Click | Closes the toy card again | Y | N/A |
| Edit toy button | N/A | Only appears on toys that the user has created | Y | N/A |
| Delete toy button | N/A | Only appears on toys that the user has created | Y | N/A |
| Edit and delete toy button | Hover | Colours change | Y | N/A |
| Back to top button | Click | Page scrolls smoothly to the top | Y | N/A |
| Add toy button | N/A | Stays in the same spot as the page is scrolled up and down | Y | N/A |
| Add toy button | Click | Directs user to add toy page | Y | N/A |
| **add_toy.html** | | | | |
| Add toy page | Access url whilst logged out | Redirected to logged out homepage | Y | N/A |
| Back button | Click | Takes the user to the toys page, even if accessed via url | Y | N/A |
| Add toy title | Resize screen | Gets smaller on screen widths less than 900px | Y | N/A |
| Toy name field | Leave empty | Alert appears asking user to complete the field | Y | N/A |
| Company name field | Leave empty | Alert appears asking user to complete the field | Y | N/A |
| Toy type field | Leave empty | Alert appears asking user to complete the field | Y | N/A |
| Toy description field | Leave empty | Submits the form with the default value | Y | N/A |
| Toy image url field | Leave empty | Submits the form with the default value | Y | N/A |
| Add toy button | Fill out the form and click | Creates a Toy instance that appears on the toys page, shows success message, and redirects the user there | Y | N/A |
| **edit_toy.html** | | | | |
| Edit toy page | Access url whilst logged out | Directed to error 403 page, access denied | Y | N/A |
| Edit toy page | Access url whilst logged in as a user that did not create the toy | Directed to error 403 page, access denied | Y | N/A |
| Back button | Click | Takes the user to the toys page if accessed from there, or individual toy page if accessed from there | Y | N/A |
| Edit toy title | Resize screen | Gets smaller on screen widths less than 900px | Y | N/A |
| Edit toy title | N/A | Displays correct toy name | Y | N/A |
| Edit toy form | N/A | Populated with existing data | Y | N/A |
| Toy name field | Delete and leave empty | Alert appears asking user to complete the field | Y | N/A |
| Company name field | Delete and leave empty | Alert appears asking user to complete the field | Y | N/A |
| Toy description field | Leave empty | Submits the form with the default value | N | Gives an empty field. routes.py updated to give default description |
| Toy description field | Leave empty and do above fix | Submits the form with the default value | Y | N/A |
| Toy image url field | Leave empty | Submits the form with the default value | Y | N/A |
| Edit toy button | Make changes and click | Saves these changes, displays success message, and directs user to toys page if accessed from there or individual toy page if accessed from there | Y | N/A |
| **delete_toy** | | | | |
| Delete toy button | Click | Opens modal asking to confirm deletion | Y | N/A |
| Delete toy modal | N/A | Displays correct toy name | Y | N/A |
| Delete toy modal: cancel | Click | Closes the modal | Y | N/A |
| Delete toy modal: confirm | Click | Deletes the toy, directs the user to the toys page, and shows success alert | Y | N |
| Delete toy modal buttons | Hover | Colours change and words enlarge | Y | N |
| Delete toy modal | Resize screen | Text and buttons get smaller on screen widths below 601px | Y | N |
| Delete toy | Carry out deletion | Deletes all reviews associated with the toy | Y | N/A |
| Delete toy | Carry out deletion | Removes toy from all review also_liked carousels | Y | N/A |
| **individual_toy.html** | | | | |
| Individual toy page | Access url whilst logged out | Redirected to logged out home page | Y | N/A |
| Back button | Click | Directs user to toys if accessed from that page or profile if accessed from that page | Y | N/A |
| Toy name | N/A | Shows the correct toy name | Y | N/A |
| Toy image | Change screen sizes | Resizes with screen size | Y | N/A |
| Average rating | N/A | Stars and text show accurate data | Y | N/A |
| Average rating | N/A | Stays on top of image | N | Text goes behind image. Z-index and white shadow added to stand out |
| Average rating | Do above fix | Stays on top of image | Y | N/A |
| Toy information | N/A | Displays accurate information | Y | N/A |
| Add review button | N/A | Disappears if the user has a review for this toy. Reappears on review deletion | Y | N/A |
| Add review button | Click | Opens add review page | Y | N/A |
| Add review button | Hover | Colour changes and size increases | Y | N/A |
| Edit toy button | N/A | Only shows if the user is the creator of the toy | Y | N/A |
| Edit toy button | Click | Opens edit toy page | Y | N/A |
| Edit toy button | Hover | Colour changes and size increases | Y | N/A |
| Delete toy button | N/A | Only shows if the user is the creator of the toy | Y | N/A |
| Delete toy button | Hover | Colour changes and size increases | Y | N/A |
| Delete toy button | Click | Opens delete toy confirmation modal | Y | N/A |
| Add review, edit toy, delete toy buttons | Resize screen | Button size decreases below screen widths of 420px | Y | N/A |
| Delete toy modal | N/A | Displays correct toy name | Y | N/A |
| Delete toy modal: cancel | Click | Closes the modal | Y | N/A |
| Delete toy modal: confirm | Click | Deletes the toy and directs the user to the toys page | Y | N/A |
| Delete toy modal buttons | Hover | Colours change and words enlarge | Y | N/A |
| Delete toy modal | Resize screen | Text and buttons get smaller on screen widths below 601px | Y | N/A |
| Sort reviews: high to low | Select | Displays the reviews in order of highest to lowest rating | Y | N/A |
| Sort reviews: low to high | Select | Displays the reviews in order of lowest to highest rating | Y | N/A |
| Review author | N/A | Displays the username of the creator or "User Deleted" if they deleted their account | Y | N/A |
| Review author | Click | Directs the user to the author's profile page | Y | N/A |
| Review rating | N/A | Displays correct number of stars for the rating | Y | N/A |
| Also liked carousel | N/A | Shows if the review has also_liked values or does not appear if there aren't any | Y | N/A |
| Also liked carousel | Click | Cycles through the also-liked toys | Y | N/A |
| Also liked carousel | Click on toy names | Directs the user to that individual toy page | Y | N/A |
| Edit review button | N/A | Is only shown to the author of the review | Y | N/A |
| Delete review button | N/A | Is only shown to the author of the review | Y | N/A |
| Edit and delete review buttons | Hover | Colour changes and the size increases | Y | N/A |
| Edit review button | Click | Opens the edit review page | Y | N/A |
| Delete review button | Click | Opens the confirm delete review modal | Y | N/A |
| Delete review modal | N/A | Displays a message showing the correct toy name | Y | N/A |
| Delete review modal: cancel | Click | Closes the modal | Y | N/A |
| Delete review modal: confirm | Click | Deletes the review and directs the user to the toy page or profile page depending on where they accessed it from | Y | N |
| Delete review modal buttons | Hover | Colours change and words enlarge | Y | N |
| Delete review modal | Resize screen | Text and buttons get smaller on screen widths below 601px | Y | N |
| Delete review | Carry out deletion | Deletes the review and refreshes review page | Y | N/A |
| **add_review.html** | | | | |
| Add review page | Access url whilst logged out | Redirected to logged out home page | Y | N/A |
| Back button | Click | Directs the user to the individual toy page | Y | N/A |
| Add review title | N/A | Display correct toy name | Y | N/A |
| Add review title | Resize screen | Title size reduces at screen widths below 650px | Y | N/A |
| Review field | Leave empty | Alert appears asking user to complete the field | Y | N/A |
| Star rating field | Leave empty | Alert appears asking user to complete the field | Y | N/A |
| Toy type field | Leave empty | Alert appears asking user to complete the field | Y | N/A |
| Also liked field | Click | Shows a multiple select option comprised of all other toys in the database in alphabetical order | Y | N/A |
| Submit review button | Complete form and click | Submits the form, shows success alert, and directs the user to the individual toy page | Y | N/A |
| **edit_review.html** | | | | |
| Edit review page | Try to access it via url if you are not the creator or logged out | Directs the user to error 403 access denied page | Y | N/A |
| Back button | Click | Takes user to individual toy page if accessed from there or user profile if accessed from there | Y | N/A |
| Edit review form | N/A | Populated with existing data | Y | N/A |
| Review field | Try to submit with an empty field | Alert appears asking user to complete the field | Y | N/A |
| Star rating field | Set to default message and submit | Alert appears asking user to complete the field | Y | N/A |
| Submit review button | Change values and submit | Values are saved, success alert shows, and user is directed to individual toy page or profile page depending on where they accessed edit review from | Y | N/A |
| **profile.html** | | | | |
| Own Profile page (/profile) | Try to access it via url if logged out | Directs the user to the 404 page | Y | N/A |
| Other Profile page (/profile/<user_id>) | Try to access it via url if logged out | Directs the user to the logged out home page | Y | N/A |
| Flag display | N/A | If there is a flag url associated with the profile, display the country flag, otherwise display nothing | Y | N/A |
| Verified parent display | N/A | If is_parent is true for the user, display a green tick and "Verified parent" otherwise show nothing | Y | N/A |
| Flag and verified parent display | Change values | They change depending on the value in the profile instance | Y | N/A |
| Profile title | N/A | Displays the correct username for the profile | Y | N/A |
| Profile image | N/A | Displays correct image and resizes with screen size | Y | N/A |
| About me text | Have a long about me | A scroll bar appears to scroll through the content over a height of 300px | Y | N/A |
| Edit and delete profile buttons | N/A | Display for user's own profile, not for other users | Y | N/A |
| Edit and delete profile buttons | Hover | Colours change and size increases | Y | N/A |
| Edit profile button | Click | Directs to the correct edit profile page | Y | N/A |
| Delete user button | Click | Opens the confirm delete modal | Y | N/A |
| Delete user modal | N/A | Displays a warning message about the permanence of deletion | Y | N/A |
| Delete user modal: cancel | Click | Closes the modal | Y | N/A |
| Delete user modal: confirm | Click | Deletes the user account and profile, renames all review authors on the users reviews to "User Deleted", directs the user to the logged out home page and displays success message | Y | N |
| Delete user modal buttons | Hover | Colours change and words enlarge | Y | N |
| Delete user modal | Resize screen | Text and buttons get smaller on screen widths below 601px | Y | N |
| Delete review | Carry out deletion | Deletes the review, shows success alert, and refreshes review page | Y | N/A |
| User information | Resize screen | Layout changes to image on top and everything in one column on screen widths less than 600px | Y | N/A |
| Reviews title and content | N/A | Only displays if the user has submitted reviews | Y | N/A |
| Sort reviews: Newest first | Select | Displays the reviews in order of newest to oldest | Y | N/A |
| Sort reviews: Oldest first | Select | Displays the reviews in order of oldest to newest | Y | N/A |
| Sort reviews: Rating high to low | Select | Displays the reviews in order of highest to lowest rating | Y | N/A |
| Sort reviews: Rating low to high | Select | Displays the reviews in order of lowest to highest rating | Y | N/A |
| Toy name | N/A | Displays the correct toy name | Y | N/A |
| Toy name | Click | Directs the user to the correct individual toy page | Y | N/A |
| Review rating | N/A | Displays correct number of stars for the rating | Y | N/A |
| Also liked carousel | N/A | Shows if the review has also_liked values or does not appear if there aren't any | Y | N/A |
| Also liked carousel | Click | Cycles through the also-liked toys | Y | N/A |
| Also liked carousel | Click on toy names | Directs the user to that individual toy page | Y | N/A |
| Edit review button | N/A | Is only shown to the author of the review | Y | N/A |
| Delete review button | N/A | Is only shown to the author of the review | Y | N/A |
| Edit and delete review buttons | Hover | Colour changes and the size increases | Y | N/A |
| Edit review button | Click | Opens the edit review page | Y | N/A |
| Delete review button | Click | Opens the confirm delete review modal | Y | N/A |
| Delete review modal | N/A | Displays a message showing the correct toy name | Y | N/A |
| Delete review modal: cancel | Click | Closes the modal | Y | N/A |
| Delete review modal: confirm | Click | Deletes the review and directs the user to the toy page or profile page depending on where they accessed it from | Y | N |
| Delete review modal buttons | Hover | Colours change and words enlarge | Y | N |
| Delete review modal | Resize screen | Text and buttons get smaller on screen widths below 601px | Y | N |
| Delete review | Carry out deletion | Deletes the review, shows success alert, and refreshes profile page | Y | N/A |
| **edit_profile.html** | | | | |
| Edit profile page | Try to access it via url as another user or logged out | Directed to the error 403 access denied page | Y | N/A |
| Back button | Click | Directs the user back to their profile page | Y | N/A |
| Edit profile form | N/A | Populated with existing data | Y | N/A |
| About me field | Delete all and submit | The about me is populated with the default text informing other users that it is not filled out | Y | N/A |
| Parent status toggle | Click | Works well and displays/removes the verified parent display on the profile | Y | N/A |
| Country select field | Select country | Displays all countries in alphabetical order, selecting one changes the flag on the user profile | Y | N/A |
| Edit password button | Click | Directs the user to the change password page | Y | N/A |
| Save changes button | Submits the changes, updates the user profile, displays success message and directs user back to their profile page | Y | N/A |
| **change_password.html** | | | | |
| Change password page | Try to access it for another user or logged out | Directed to error 403 access denied page | Y | N/A |
| Back button | Click | Directs the user back to their edit profile page | Y | N/A |
| Change password title | Resize screen | Title size decreases at screen widths less than 420px | Y | N/A |
| Old password field | Leave empty | Alert telling users to fill in the field | Y | N/A |
| Old password field | Fill in with incorrect data | Alert shows telling the user that the old password is incorrect | Y | N/A |
| Password fields | Use two non-matching new passwords | Alert shows telling the user that the new passwords do not match | Y | N/A |
| Password fields | Use new passwords that do not have a capital letter, number, or special character | Alert shows reminding the user of the password requirements | Y | N/A |
| Change password button | Fill out form and click | Updates password, displays success message, and directs user to edit profile page | Y | N/A |
| **403.html** | | | | |
| 403 page | Try to access a url that you do not have access to | User is redirected to the error 403 access denied page | Y | N/A |
| Error message | N/A | A clear message explaining the error with a link to the home page | Y | N/A |
| Home button | Hover | Button resizes | Y | N/A |
| Home button | Click | User is directed to the home page | Y | N/A |
| **404.html** | | | | |
| 404 page | Go to a page that does not exist | User is redirected to the error 404 page not found page | Y | N/A |
| Error message | N/A | A clear message explaining the error with a link to the home page | Y | N/A |
| Home button | Hover | Button resizes | Y | N/A |
| Home button | Click | User is directed to the home page | Y | N/A |
| **500.html** | | | | |
| 500 page | N/A | User is directed to this page when there is a server error | N/A | Unable to test this with a running server but all code is correct and should work |
| Error message | N/A | A clear message explaining the error with a link to the home page | Y | N/A |
| Home button | Hover | Button resizes | Y | N/A |
| Home button | Click | User is directed to the home page | Y | N/A |

## Device and Browser Testing
I tested the responsiveness of the website using Google Chrome Devtools to simulate 17 screen sizes; ranging from large desktops to the iPhone 5/SE and am happy to report that the website appears and functions as intended across the large screen size range. Additionally the website was tested on the Google Chrome, Mozzila Firefox, Microsoft Edge, and Brave browsers and no issues were encountered. I also tested the website on my 17.5" Laptop, 14" Laptop, and smart phone, noticing that it worked well in each case.
A group of 10 of my friends and family gave feedback throughout the development of the project, this gave information that the website functions as intended on the following browsers and devices:<br>

**Browsers Used:**

| | Chrome | Firefox | Opera | Safari | Edge | Brave |
|---|---|---|---|---|---|---|
| Browser Usage | 1 | 1 | 0 | 6 | 0 | 2 |

There was no negative feedback that was browser specific. Although no users tested Opera or Edge, I have access to Edge and had already conducted browser compatability testing with it.
<br>

**Devices Used:**
| | Desktop | Tablet | iPhone | Android Phone |
| --- | --- | --- | --- | --- |
| Device usage | 0 | 3 | 5 | 2 |

There was no negative feedback that was device specific, which was great news as this covered many options of screen sizes. I had previously tested some of the devices using Chrome Dev Tools, however it was good to see that this was a suitable substitute to testing the devices themselves.
<br>


## Automated Testing

### Accessibility Testing
Accessibility was kept in mind throughout development and the best practices were kept to across the website including, but not limited to, ensuring aria-labels and alt texts were used throughout, using semantic HTML, creating easy to see colour contrasts. Where hidden text was used, it was hidden in a way that was still accessible to screen readers.
Accessibility testing was performed using the [Wave](https://wave.webaim.org/) validator to provide key information about the accessibility standard of the website. Pages that required login were beyond the purview of the [Wave](https://wave.webaim.org/) browser tool, so the Wave extension for Google Chrome was used, which can be found [here](https://wave.webaim.org/extension/).
On top of this, one of my partially sighted friends troubleshooted the website with use of their screenreader during development and provided essential feedback to achieve full accessibility, which was implemented.

**home.html**<br>
- The contrast error on the Hero text should be ignored, as the validator ignores the black shadowing of the words and assumes it is just white text on a picture background. In reality it is white text on a black shadow, making it clearly legible on the picture background. User feedback has confirmed this.
<details>
<summary>Home results</summary>
<img src="/documentation/testing/wave_home.png">
</details><br>

**signup.html**
<details>
<summary>Signup results</summary>
<img src="/documentation/testing/wave_signup.png">
</details><br>

**login.html**
<details>
<summary>Login results</summary>
<img src="/documentation/testing/wave_login.png">
</details><br>

**toys.html**<br>
- Alerts were multiplied for each toy present on the page:
    * Suspicious alt text: All checked, these are for the toy images and the ratings.
    * Possible heading: Highlighted possible headings on the delete modals but I will keep the current layout.
    * Broken same page link: Highlights the cancel buttons on the delete modals. These work as expected.
    * Redundant links: One for the Home page as it appears in the header and footer, but works as expected so will keep. The others were for the individual toy pages which lead to separate pages as intended.
<details>
<summary>Toys results</summary>
<img src="/documentation/testing/wave_toys.png">
</details><br>

**add_toy.html**<br>
Alerts:
- Redundant link: One for the Home page as it appears in the header and footer, but works as expected so will keep.
<details>
<summary>Add toy results</summary>
<img src="/documentation/testing/wave_add_toy.png">
</details><br>

**edit_toy.html**<br>
Alerts:
- Redundant link: One for the Home page as it appears in the header and footer, but works as expected so will keep..
<details>
<summary>Edit toy results</summary>
<img src="/documentation/testing/wave_edit_toy.png">
</details><br>

**individual_toy.html**<br>
Alerts
- Possible headings: The delete toy and delete modal content. Kept the way it is. One alert per also_liked review section. Kept as it is.
- Broken same page links: Confirm delete modal close buttons. They work as expected so no change here.
- Redundant link: For the Home page as it appears in the header and footer, but works as expected so will keep.
<details>
<summary>Individual toy results</summary>
<img src="/documentation/testing/wave_individual_toy.png">
</details><br>

**add_review.html**<br>
Alerts
- Redundant link: One for the Home page as it appears in the header and footer, but works as expected so will keep.
<details>
<summary>Add review results</summary>
<img src="/documentation/testing/wave_add_review.png">
</details><br>

**edit_review.html**<br>
Alerts
- Redundant link: One for the Home page as it appears in the header and footer, but works as expected so will keep.
<details>
<summary>Edit review results</summary>
<img src="/documentation/testing/wave_edit_review.png">
</details><br>

**profile.html**<br>
Alerts
- Redundant link: One for the Home page as it appears in the header and footer, but works as expected so will keep.
- Possible headings: One for each review also_liked section. Works as expected so no changes.
- Broken same page link: One for each delete confirmation modal close button. Works as expected so no changes.
<details>
<summary>Profile results</summary>
<img src="/documentation/testing/wave_profile.png">
</details><br>

**edit_profile.html**<br>
Alerts
- Redundant link: One for the Home page as it appears in the header and footer, but works as expected so will keep.
<details>
<summary>Edit Profile results</summary>
<img src="/documentation/testing/wave_edit_profile.png">
</details><br>

**change_password.html**<br>
Alerts
- Redundant link: One for the Home page as it appears in the header and footer, but works as expected so will keep.
<details>
<summary>Change password results</summary>
<img src="/documentation/testing/wave_change_password.png">
</details><br>

**403.html**<br>
Alerts
- Redundant link: One for the Home page as it appears in the header and footer, but works as expected so will keep.
<details>
<summary>Error 403 results</summary>
<img src="/documentation/testing/wave_403.png">
</details><br>

**404.html**<br>
Alerts
- Redundant link: One for the Home page as it appears in the header and footer, but works as expected so will keep.
<details>
<summary>Error 404 results</summary>
<img src="/documentation/testing/wave_404.png">
</details><br>

**500.html**<br>
Alerts
- Redundant link: Two for the Home page as it appears in the header, footer, and as a redirect link. They work as expected so will be kept.
<details>
<summary>Error 404 results</summary>
<img src="/documentation/testing/wave_500.png">
</details><br>

### Performance Testing

The performance of the webpage was tested using Lighthouse within the Google Chrome Devtools to confirm that the site was performing well, is accessible, follows best practices, and follows basic SEO (search engine optimisation) advice. 
During development, care was taking to provide the best performing website that could be provided. These efforts include:
- Image optimisation: [Cloud Convert](https://cloudconvert.com/png-to-webp) was used to convert site images to smaller file formats for faster load times. .PNG files were only used where the file size was already very small, for example the bubble text on page titles. Otherwise, .WEBP and .SVG files to reduce file sizes and optimise them for web application usage.
- Code minification: Complete code minification was avoided in this project to allow easier assessment upon submission. That being said, code has been written to meet the highest standards, repetition had been removed, and short, elegant solutions have been used wherever possible in order to reduce the code size. In future minification will be used. For example [Python Minifier](https://python-minifier.com/) reduces the size of the routes.py file from 30,136 Bytes to 10,166 Bytes highlighting a possible route for performance improvement.

The performance was tested for normal internet speed, fast 3G, and slow 3G to test the performance in a majority of scenarios and locations. This was done by setting the performance network throttling in Google Chrome Devtools. The testing was also run on Google Chrome incognito mode to avoid any complications with plugins or extensions.

**Results**: The resulting screenshots are provided in [PERFORMANCE.md](/PERFORMANCE.md) but the results are discussed here.
- The score of 96 for accessibility on the individual_toy.html and profile.html pages are for the aria-labels on the carousel images. These have been kept, as pass the accessibility criteria on the [Wave](https://wave.webaim.org/) validator and the issues picked up by Lighthouse are due to the Materialize settings for carousel items.
- The scores of 96 for best practices and 91 for SEO on the 404 page are due to the 404 error that the page shows, which indicates that it is working as expected. These were best practices issue: browser error 404 logged to console and SEO issue: Page had unsuccessful HTTP status code 404.
- All other Accessibility, Best Practices, and SEO scores were 100.
- Overall the site performs well on all 3 internet speeds, never dipping below 90 for performance.
- In future, a larger database may cause performance issues for the pages displaying toys and reviews. In this case, pages will be introduced to limit the number of toys or reviews shown at a time.

### HTML validation
The [W3C markup validation service](https://validator.w3.org/) was used to validate the HTML of each page of this website. As each page including some Jinja templating language that threw errors in the validator; the HTML was validated after deployment. Each page was accessed and the source code (CTRL+U or right click > View Page Source) was copied and pasted into the validator to validate by direct input.<br>
**Warnings**:
- toys.html showed warnings for possible misuse of aria labels on the toy review stars and the more information ellipses on the toy cards. These were investigated and as they passed accessibility criteria and are correctly picked up by screen readers with no impact to the website functionality, these warnings were eventually ignored.
- individual_toy.html showed the same warnings for possible misuse of aria labels for the toy review stars and review rating stars. The same approach as above was taken.
- profile.html showed the same warning for possible missuse of arial labels for each review rating. The same approach as above was taken.

**Errors**
- Overall there were no errors in the HTML code validation.

<br>
Screenshots of the validation results are shown here:

<details>
    <summary>Home</summary>
    <img src="/documentation/testing/html_home.png">
</details>

<details>
    <summary>Signup</summary>
    <img src="/documentation/testing/html_signup.png">
</details>

<details>
    <summary>Login</summary>
    <img src="/documentation/testing/html_login.png">
</details>

<details>
    <summary>Toys</summary>
    <img src="/documentation/testing/html_toys.png">
</details>

<details>
    <summary>Add Toy</summary>
    <img src="/documentation/testing/html_addtoy.png">
</details>

<details>
    <summary>Edit Toy</summary>
    <img src="/documentation/testing/html_edittoy.png">
</details>

<details>
    <summary>Individual Toy</summary>
    <img src="/documentation/testing/html_individualtoy.png">
</details>

<details>
    <summary>Add Review</summary>
    <img src="/documentation/testing/html_addreview.png">
</details>

<details>
    <summary>Edit Review</summary>
    <img src="/documentation/testing/html_editreview.png">
</details>

<details>
    <summary>Profile</summary>
    <img src="/documentation/testing/html_profile.png">
</details>

<details>
    <summary>Edit Profile</summary>
    <img src="/documentation/testing/html_editprofile.png">
</details>

<details>
    <summary>Change Password</summary>
    <img src="/documentation/testing/html_changepassword.png">
</details>

<details>
    <summary>Error 403</summary>
    <img src="/documentation/testing/html_403.png">
</details>

<details>
    <summary>Error 404</summary>
    <img src="/documentation/testing/html_404.png">
</details>

<details>
    <summary>Error 500</summary>
    <img src="/documentation/testing/html_500.png">
</details>

### CSS Validation
CSS validation was completed using the [W3C Jigsaw CSS validator](https://jigsaw.w3.org/css-validator/). It showed no errors in the CSS code. The 6 warnings were to do with imported style sheets that were not checked and the copied code for the star rating stylings, which were left alone to ensure correct functionality.
<details>
    <summary>CSS validation results</summary>
    <img src="/documentation/testing/css_validation.png">
</details>

### JavaScript Validation
The JavaScript code was testing using the JavaScript linter [JSLint](https://www.jslint.com/). The settings were set for browser, so that the linter recognised the "document" variable, and I added "M" to the imported variables so that the linter recognised the materialize initialisation functions. The code passed through with no errors.
<details>
    <summary>JavaScript validation results</summary>
    <img src="/documentation/testing/js_validation.png">
</details>

### Python Validation
The Python code for this project was written in strict accordance with the [PEP 8](https://peps.python.org/pep-0008/) style guide for Python code. These include using correct indentations, maximum line lengths of 79 characters, and adhering to naming conventions for variables, functions, and classes. The [Code Institue python linter](https://pep8ci.herokuapp.com/) was used to validate the written code. The only error that it reported was in my `__init__.py` file where it highlighted an import not being at the top of the page. The reason for this is because it relied on the database definition given 2 lines above it and would have caused errors in the code if it had been with the rest of the imports. All other python scripts passed with no isses. The env.py file was also linted showing no errors but the screenshot has been omitted for security issues as it contains the secret key.
<details>
    <summary>Init file results</summary>
    <img src="/documentation/testing/python_init.png">
</details>
<details>
    <summary>forms.py results</summary>
    <img src="/documentation/testing/python_forms.png">
</details>
<details>
    <summary>models.py file results</summary>
    <img src="/documentation/testing/python_models.png">
</details>
<details>
    <summary>routes.py file results</summary>
    <img src="/documentation/testing/python_routes.png">
</details>
<details>
    <summary>update_db.py file results</summary>
    <img src="/documentation/testing/python_update.png">
</details>

## Bugs

### Bug 1
**Issues:** The default values for the toy image url and description were not being added to the database upon submission of data.<br>
```py
image_url = db.Column(
    db.String(300),
    default="/static/img/default_toy.webp",
    nullable=False)
    description = db.Column(
        db.Text(),
        default="No description added yet.",
        nullable=False
    )
```

**Fix:** Default values from here on were removed from the models.py file and defined instead in the routes.py file e.g: <br>
```py
if form.validate_on_submit():
    if not form.image_url.data:
        form.image_url.data = "/static/img/default_toy.webp"
    if not form.description.data:
        form.description.data = "No description added yet."
```

### Bug 2
**Issue:** The countries in the select element in the edit profile form were not being displayed in alphabetical order, which made selecting a country difficult.
**Fix:** Sorting the variable in the routes.py file :
```py
countries = sorted(pycountry.countries, key=lambda country: country.name)
```

### Bug 3
**Issue:** When not selecting an option from a required dropdown menu, the page scrolls to top and the error flashed error message does not occur. Multiple fixes were attempted:
- Having a default set in the forms file within the SelectField does not automatically set the value on submitting the form.
- This means that checking for the value after submitting and before validation does not work e.g.:
```py 
if form.is_submitted():
    if form.rating.data == '':
        flash('Please rate the toy.')
    elif form.validate():
```
- I can have the message appear setting the form.rating.data to any of the values, but not the default.
- [This fix](https://stackoverflow.com/questions/57177597/materlialize-css-select-componenent-setting-default-value-with-javascript) on stack overflow did not work.

**Fix:** Removing the data required setting in the forms.py file fixed the issue.

### Bug 4
**Issue:** The individual toys page back button created an infinite loop with the edit toys back button after editing the toy. 

**Fix:** Added a ref on links to the page to check if it came from the profile to make the back button direct there. Otherwise it directs to the toys page.

To get around this, the referer was checked to see if it came from the profile and created a back button linked to the profile, otherwise the back button always directed back to the toys page.

```HTML
{% if referer.endswith('/profile') %}
    <a href="{{ referer }}" class="open-sans back-button" aria-label="Go back to previous page">
        <i class="fa-solid fa-backward-step"></i>
        <span>Back</span>
    </a>
    <br>
{% else %}
    <a href="{{ url_for('toys') }}" class="open-sans back-button" aria-label="Go back to previous page">
        <i class="fa-solid fa-backward-step"></i>
        <span>Back</span>
    </a>
    <br>
{% endif %}
```

### Bug 5
**Issue:** Deleted toys still appear as empty things in also_liked.

**Fix:** Added a function that combs through reviews.also_liked and remove the specific toy id. It is called during the delete_toy function and uses the reviews that have the toy id in their also liked as the arguement. 

```py
def remove_toy_from_reviews(review):
    """
    A function to remove the toy id from the also_liked list
    in the user reviews
    """
    updated_also_liked = []
    # Loop through also_liked and if they still exist, add to updated list
    for toy_id in review.also_liked:
        toy = Toy.query.filter_by(id=toy_id).first()
        if toy:
            updated_also_liked.append(toy_id)
    # Set also_liked as the updated list
    review.also_liked = updated_also_liked
```

### Known Bugs
There are no known bugs currently in the deployed website.

## Analytics
[Google Analytics](https://marketingplatform.google.com/about/analytics/) has been used to provide real time analytics about how users use my webpage. This includes how many page views, how many users scroll to the bottom of the page, indicating that content hinting is working, and how many users sign up. The data received from this will be used to inform the future updates to the webpage. This required the following code to be added to the base.html template at the bottom of the head element as directed:
```HTML
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-P76K2YLKVH"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      
      gtag('config', 'G-P76K2YLKVH', { 'anonymize_ip': true });
    </script> 
```