function btnChg(color, btn) {
    btn.style.background = color;
}

function setBg() {
    header = document.getElementById('site-header');
    header.style.backgroundImage = "url('{{ page.header_image }}')";
    header.style.backgroundPosition = "{{ page.header_pos }}";
}

if ('{{ page.layout }}' === 'post' && '{{ page.header_image }}' !== 'nil') {
    document.addEventListener('load', setBg());
}

function hideCountdown() {
    var d = new Date().getDay();
    if (d > 4 || d < 2) {
        document.getElementById("draft").classList.add("d-none");
    } else {
        document.getElementById("contest").classList.add("d-none");
    }
}

if ('{{ page.title }}' === 'Home') {
    document.addEventListener('load', hideCountdown());
}

function hideRedZone() {
    var day = new Date().getDay();
    links = document.getElementsByClassName("nav-item")
    if (day !== 0) {
        links[1].classList.add("d-none");
    }
}

document.addEventListener('load', hideRedZone());