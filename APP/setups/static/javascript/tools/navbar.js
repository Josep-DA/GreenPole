let header = document.querySelector("header");

let lastScrollY = window.scrollY

window.addEventListener("scroll", () => {

    if (lastScrollY + 100 < window.scrollY) {
        header.style = "position:relative;bottom:20em";
        lastScrollY = window.scrollY;
    } else if (lastScrollY - 100 > window.scrollY) {
        header.style = header.style = "bottom:10em"
        lastScrollY = window.scrollY
    }

    if (window.scrollY < 100) {
        header.style = header.style = "bottom:10em"
    }
})

