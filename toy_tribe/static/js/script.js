document.addEventListener("DOMContentLoaded", function() {
    // sidenav initialization
    let sidenav = document.querySelectorAll(".sidenav");
    M.Sidenav.init(sidenav);
    
    // select initialization
    let selects = document.querySelectorAll("select");
    M.FormSelect.init(selects);
    
    // modal initialization
    let modals = document.querySelectorAll('.modal');
    M.Modal.init(modals);

    // carousel initialization
    let carousels = document.querySelectorAll('.carousel');
    M.Carousel.init(carousels);

    // Label the sort select on toys.html
    // Check for the page
    if (window.location.pathname.includes('/toys')) {
        // Find the created dropdown menu
        let generatedInput = document.querySelector('.select-dropdown.dropdown-trigger');

        // If it is there, add the label
        if (generatedInput) {
            generatedInput.setAttribute('aria-labelledby', 'sort-label');
        }
    }

    // Label the toy type select on add_toy.html
    // Check for the page
    if (window.location.pathname.includes('/add_toy')) {
        // Find the created dropdown menu
        let generatedInput = document.querySelector('.select-dropdown.dropdown-trigger');

        // If it is there, add the label
        if (generatedInput) {
            generatedInput.setAttribute('aria-labelledby', 'toy-type-label');
        }
    }

    // Label the toy type select on edit_toy.html
    // Check for the page
    if (window.location.pathname.includes('/edit_toy')) {
        // Find the created dropdown menu
        let generatedInput = document.querySelector('.select-dropdown.dropdown-trigger');

        // If it is there, add the label
        if (generatedInput) {
            generatedInput.setAttribute('aria-labelledby', 'toy-type-label');
        }
    }

    // Label the review sort select on individual_toy.html
    // Check for the page
    if (window.location.pathname.includes('/toy/')) {
        // Find the created dropdown menu
        let generatedInput = document.querySelector('.select-dropdown.dropdown-trigger');

        // If it is there, add the label
        if (generatedInput) {
            generatedInput.setAttribute('aria-labelledby', 'sort-label');
        }
    }
});

