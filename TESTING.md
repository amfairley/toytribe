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

## Accessibility Testing
Accessibility was kept in mind throughout development and the best practices were kept to across the website. Where hidden text was used, it was hidden in a way that was still accessible to screen readers.
Accessibility testing was performed using the [Wave](https://wave.webaim.org/) validator to provide key information about the accessibility standard of the website. Pages that required login were beyond the perview of the [Wave](https://wave.webaim.org/) browser tool, so the Wave extension for Google Chrome was used, which can be found [here](https://wave.webaim.org/extension/).

**home.html**:
- The contrast error on the Hero text should be ignored, as the validator ignores the black shadowing of the words and assumes it is just white text on a picture background. In reality it is white text on a black shadow, making it clearly legibile on the picture background. User feedback has confirmed this.
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

**toys.html**
- Alerts were multipled for each toy present on the page:
    * Suspicious alt text: All checked, these are for the toy images and the ratings.
    * Possible heading: Highlighted possible headings on the delete modals but I will keep the current layout.
    * Broken same page link: Highlights the cancel buttons on the delete modals. These work as expected.
    * Redundant links: One for the Home page as it appears in the header and footer, but works as expected so will keep. The others were for the individual toy pages which lead to separate pages as indended.
<details>
<summary>Toys results</summary>
<img src="/documentation/testing/wave_toys.png">
</details><br>

**add_toy.html**
Alerts:
- Redundant link: One for the Home page as it appears in the header and footer, but works as expected so will keep.
<details>
<summary>Add toy results</summary>
<img src="/documentation/testing/wave_add_toy.png">
</details><br>

**edit_toy.html**
Alerts:
- Redundant link: One for the Home page as it appears in the header and footer, but works as expected so will keep..
<details>
<summary>Edit toy results</summary>
<img src="/documentation/testing/wave_edit_toy.png">
</details><br>

**individual_toy.html**
Alerts
- Possible headings: The delete toy and delete modal content. Kept the way it is. One alert per also_liked review section. Kept as it is.
- Broken same page links: Confirm delete modal close buttons. They work as expected so no change here.
- Redundant link: For the Home page as it appears in the header and footer, but works as expected so will keep.
<details>
<summary>Individual toy results</summary>
<img src="/documentation/testing/wave_individual_toy.png">
</details><br>

**add_review.html**
Alerts
- Redundant link: One for the Home page as it appears in the header and footer, but works as expected so will keep.
<details>
<summary>Add review results</summary>
<img src="/documentation/testing/wave_add_review.png">
</details><br>

**edit_review.html**
Alerts
- Redundant link: One for the Home page as it appears in the header and footer, but works as expected so will keep.
<details>
<summary>Edit review results</summary>
<img src="/documentation/testing/wave_edit_review.png">
</details><br>

**profile.html**
Alerts
- Redundant link: One for the Home page as it appears in the header and footer, but works as expected so will keep.
- Possible headings: One for each review also_liked section. Works as expected so no changes.
- Broken same page link: One for each delete confirmation modal close button. Works as expected so no changes.
<details>
<summary>Profile results</summary>
<img src="/documentation/testing/wave_profile.png">
</details><br>

**edit_profile.html**
Alerts
- Redundant link: One for the Home page as it appears in the header and footer, but works as expected so will keep.
<details>
<summary>Edit Profile results</summary>
<img src="/documentation/testing/wave_edit_profile.png">
</details><br>

**change_password.html**
Alerts
- Redundant link: One for the Home page as it appears in the header and footer, but works as expected so will keep.
<details>
<summary>Change password results</summary>
<img src="/documentation/testing/wave_change_password.png">
</details><br>

**403.html**
Alerts
- Redundant link: One for the Home page as it appears in the header and footer, but works as expected so will keep.
<details>
<summary>Error 403 results</summary>
<img src="/documentation/testing/wave_403.png">
</details><br>

**404.html**
Alerts
- Redundant link: One for the Home page as it appears in the header and footer, but works as expected so will keep.
<details>
<summary>Error 404 results</summary>
<img src="/documentation/testing/wave_404.png">
</details><br>

**500.html**
Alerts
- Redundant link: Two for the Home page as it appears in the header, footer, and as a redirect link. They work as expected so will be kept.
<details>
<summary>Error 404 results</summary>
<img src="/documentation/testing/wave_500.png">
</details><br>




Hidden labels still accessible to screen readers