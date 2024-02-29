console.log('hello world');

const notiBtns = [...document.getElementsByClassName('noti')];
const msgBody = document.getElementById('msg-body');

notiBtns.forEach(notiBtn => notiBtn.addEventListener('click', () =>{
    const subject = notiBtn.getAttribute('data-subject');
    const msg = notiBtn.getAttribute('data-message');
    
    msgBody.innerHTML = `
    <div id="msg-div">
        <h5 class="mt-5">${subject}</h5>
        <hr>
        <p>${msg}</p>
        <hr>
        <button id="close-btn" class="btn btn-danger">Close</button>
    </div>
    `;

    const closeBtn = document.getElementById('close-btn');
    const body = document.getElementById('msg-div');
    closeBtn.addEventListener('click', ()=>{
        body.remove();
    });

}));