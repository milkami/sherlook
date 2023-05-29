document.addEventListener('DOMContentLoaded', function() {
    console.log('bla');

    var search_body = document.querySelector('#search-body');
    var pop_up_box = document.querySelector('.pop-up-box');
    var pop_up_position = document.querySelector('#pop-up-position');
    var pop_up_nationality = document.querySelector('#pop-up-nationality');
    var pop_up_specialization = document.querySelector('#pop-up-specialization');
    var pop_up_age = document.querySelector('#pop-up-age');

    var connect_buttons = document.querySelectorAll('.connect-button');
    console.log(connect_buttons);
    connect_buttons.forEach(function(btn) {
        btn.addEventListener('click', event =>{
            console.log(event.target);
            const button = event.target;
            const button_div = button.parentNode;
            const student_div = button_div.parentNode;
            const position = student_div.querySelector('#position').textContent;
            const nationality = student_div.querySelector('#nationality').textContent;
            const specialization = student_div.querySelector('#specialization').textContent;
            const age = student_div.querySelector('#age').textContent;
            console.log(position);
            pop_up_position.innerHTML = position;
            pop_up_nationality.innerHTML = nationality;
            pop_up_specialization.innerHTML = specialization;
            pop_up_age.innerHTML = age;
            search_body.classList.add('blur');
            pop_up_box.classList.add('pop-up-show');
        })
        // const button = btn.target;
        // console.log(button);
        // document.querySelector('#search-body').classList.add('blur');
        // document.querySelector('.pop-up-box').classList.add('pop-up-show');
    })
    document.querySelector('.overlay').addEventListener('click', () => {
        document.querySelector('#search-body').classList.remove('blur');
        document.querySelector('.pop-up-box').classList.remove('pop-up-show');
    })

})