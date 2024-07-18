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
Accessibility testing was performed using the [Wave](https://wave.webaim.org/) validator to provide key information about the accessibility standard of the website.

- home.html:
    * The contrast error on the Hero text should be ignored, as the validator ignores the black shadowing of the words and assumes it is just white text on a picture background. In reality it is white text on a black shadow, making it clearly legibile on the picture background. User feedback has confirmed this.