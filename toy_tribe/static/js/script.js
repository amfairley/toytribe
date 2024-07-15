document.addEventListener("DOMContentLoaded", function() {
    // sidenav initialization
    let sidenav = document.querySelectorAll(".sidenav");
    M.Sidenav.init(sidenav);
    
    // select initialization
    let selects = document.querySelectorAll("select");
    M.FormSelect.init(selects);

    // carousel initialization
    let carousels = document.querySelectorAll('.carousel');
    M.Carousel.init(carousels);
});

