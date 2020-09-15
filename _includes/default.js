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
        try {
            document.getElementById("draft").classList.add("d-none");
            let contestLinks = document.getElementsByClassName("contest-link");
            for (var i = 0; i < contestLinks.length; i++) {
                let origLink = contestLinks[i].getAttribute("href");
                let newLink = origLink.replace("draft/contest", "contest/gamecenter");
                contestLinks[i].setAttribute("href", newLink);
            }
        }
        catch (err) {
            console.log('This is not the home page')
        }
        let links = document.getElementsByClassName("nav-link")

        for (i = 0; i < links.length; i++) {
            if (links[i].innerHTML.indexOf("Submit lineup") !== -1) {
                var contestMenuLink = links[i];
            }
        }
        // let contestMenuLink = document.getElementsByClassName("nav-link")[0]
        let origMenuLink = contestMenuLink.getAttribute("href");
        let newMenuLink = origMenuLink.replace("draft/contest", "contest/gamecenter");
        contestMenuLink.setAttribute("href", newMenuLink);
        contestMenuLink.innerHTML = "Weekly contest <i class='fas fa-football-ball'></i>"
    } else {
        try {
            document.getElementById("contest").classList.add("d-none");
        }
        catch (err) {
            console.log('Nothing to hide')
        }
    }
}

document.addEventListener('load', hideCountdown());

function hideRedZone() {
    let day = new Date().getDay();
    let links = document.getElementsByClassName("nav-item")
    if (day !== 0) {
        for (i = 0; i < links.length; i++) {
            if (links[i].innerHTML.indexOf("Red Zone") !== -1) {
                links[i].classList.add("d-none");
            }
        }
    }
}

document.addEventListener('load', hideRedZone());