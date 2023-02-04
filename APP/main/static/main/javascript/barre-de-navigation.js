let header = document.querySelector("header");

let lastScrollY = window.scrollY

window.addEventListener("scroll", () => {

    if (lastScrollY + 200 < window.scrollY) {
        header.style = "position:relative;bottom:12em";
        lastScrollY = window.scrollY;
    } else if (lastScrollY - 200 > window.scrollY) {
        header.style = header.style = "bottom:6em"
        lastScrollY = window.scrollY
    }

    if (window.scrollY < 200) {
        header.style = header.style = "bottom:6em"
    }
})

