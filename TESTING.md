![Website logo](/documentation/screenshots/site-logo.png)

---

# Testing

This document covers the full testing of the website. This include
- Wave accessibility validator

For overview information of this website, see [README.md](/README.md) <br>
See [DESIGN.md](/DESIGN.md) for information on the five planes of UX design, site map, database scheme, and features. <br>
For information on the development and deployment of this website, see DEV.md <br>
For information on the integrated security built into the app, see SECURITY.md <br>

---

## Table of contents
1. [Testing User Stories](#testing-user-stories)
1. [Accessibility Testing](#accessibility-testing)

## Testing user stories 
The [user stores](/README.md#user-stories) have been a driving force for the development of this project. Here, features are assigned to the user stories to show completion. More can be seen about the individual features [here](/DESIGN.md#features).

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
This requirement is met by error pop ups in forms, and the required field hinting on forms.

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


## Accessibility Testing
Accessibility was kept in mind throughout development and the best practices were kept to across the website. Where hidden text was used, it was hidden in a way that was still accessible to screen readers.
Accessibility testing was performed using the [Wave](https://wave.webaim.org/) validator to provide key information about the accessibility standard of the website. Pages that required login were beyond the purview of the [Wave](https://wave.webaim.org/) browser tool, so the Wave extension for Google Chrome was used, which can be found [here](https://wave.webaim.org/extension/).

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
