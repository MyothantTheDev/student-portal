const toggle = document.getElementById('header-toggle');
const nav = document.getElementById('nav-bar');
const bodypd = document.getElementById('body-pd');
const headerpd = document.getElementById('header');

const linkColor = document.querySelectorAll('.nav_link');

if (toggle && nav && bodypd && headerpd) {
    toggle.addEventListener('click', ()=>{
        nav.classList.toggle('show');
        toggle.classList.toggle('bi-x');
        bodypd.classList.toggle('body-pd');
        headerpd.classList.toggle('body-pd');
    })
}

function colorLink(){
    if (linkColor) {
        linkColor.forEach(l => l.classList.remove('active'))
        this.classList.add('active')
    }
}
linkColor.forEach(l => l.addEventListener('click', colorLink));