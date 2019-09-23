function btnChg(color, btn) {
    btn.style.background = color;
}

function setBg() {
    if ('{{ page.header_image }}' !== '') {
        let header = document.getElementById('site-header');
        header.style.backgroundImage = "url('{{ page.header_image }}')";
        header.style.backgroundPosition = "{{ page.header_pos }}";
    }
}

if ('{{ page.layout }}' === 'post' && '{{ page.header_image }}' !== 'nil') {
    document.addEventListener('load', setBg());
}

function hideCountdown() {
    var d = new Date().getDay();
    if (d > 4 || d < 2) {
        document.getElementById("draft").classList.add("d-none");
        let contestLinks = document.getElementsByClassName("contest-link");
        for (var i = 0; i < contestLinks.length; i++) {
            let origLink = contestLinks[i].getAttribute("href")
            let newLink = origLink.replace("draft/contest", "contest/gamecenter");
            contestLinks[i].setAttribute("href", newLink);
        }
        let contestMenuLink = document.getElementsByClassName("nav-link")[0]
        let origMenuLink = contestMenuLink.getAttribute("href");
        let newMenuLink = origMenuLink.replace("draft/contest", "contest/gamecenter");
        contestMenuLink.setAttribute("href", newMenuLink);
    } else {
        document.getElementById("contest").classList.add("d-none");
    }
}

if ('{{ page.title }}' === 'Home') {
    document.addEventListener('load', hideCountdown());
}

function hideRedZone() {
    let day = new Date().getDay();
    let links = document.getElementsByClassName("nav-item")
    if (day !== 0) {
        links[1].classList.add("d-none");
    }
}

document.addEventListener('load', hideRedZone());