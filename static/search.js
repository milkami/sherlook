function getCookie(name) {
  const cookieValue = document.cookie.split(';')
    .map(cookie => cookie.split('='))
    .find(([cookieName]) => cookieName.trim() === name);

  if (cookieValue) {
    return cookieValue[1];
  }

  return null;
}

document.addEventListener('DOMContentLoaded', function() {
    var all_data = document.querySelectorAll('.all-data');
    console.log(all_data);
    
    all_data.forEach(function(each_row) {
      each_row.addEventListener('click', event => {
        const dropdown_icon = each_row.querySelector('.dropdown-icon');
        const student_data_div = each_row.querySelector('.student-data-div');
        console.log(event.target);
        const dropdown_div = each_row.querySelector('.dropdown-div');

        // if (event.target === dropdown_icon) 
        if (student_data_div.contains(event.target)){
          console.log(student_data_div);
          if (dropdown_div.style.visibility === 'hidden') {
            dropdown_div.style.visibility = 'visible';
            dropdown_div.style.display = 'block';
            dropdown_div.style.opacity = '0';
            dropdown_div.style.height = '0';
            if (dropdown_icon.classList.contains('fa-chevron-down')) {
              dropdown_icon.classList.remove('fa-chevron-down');
              dropdown_icon.classList.add('fa-chevron-up');
            }

            // Delay before applying the transition
            setTimeout(() => {
              dropdown_div.style.transition = 'opacity 1.5s ease, height 1.5s ease';
              dropdown_div.style.opacity = '1';
              dropdown_div.style.height = 'auto';
            }, 10);
          } else {
            dropdown_div.style.transition = 'opacity 3.5s ease, height 3.5s ease';
            dropdown_div.style.opacity = '0';
            dropdown_div.style.height = '0px';

            // Delay before hiding the element
            setTimeout(() => {
              dropdown_div.style.display = 'none';
              dropdown_div.style.visibility = 'hidden';
            }, 115);

            if (dropdown_icon.classList.contains('fa-chevron-up')) {
              console.log('it contains');
              dropdown_icon.classList.remove('fa-chevron-up');
              dropdown_icon.classList.add('fa-chevron-down');
            }
          }
        }
      });
    });
   

    // var all_data = document.querySelectorAll('.all-data');
    //     console.log(all_data);
    //     all_data.forEach(function(each_row) {
    //     each_row.addEventListener('click', event => {
    //         const dropdown_icon = each_row.querySelector('.dropdown-icon');
    //         console.log(event.target);
    //         const dropdown_div = each_row.querySelector('.dropdown-div');
    //             if (event.target === dropdown_icon) {
    //                 if (dropdown_div.style.visibility === 'hidden') {
    //                     dropdown_div.style.visibility = 'visible';
    //                     dropdown_div.style.display = 'block';
    //                 } else {
    //                     dropdown_div.style.visibility = 'hidden';
    //                     dropdown_div.style.display = 'none';
    //                 }   
    //             }
    //         })
    // })

    var search_body = document.querySelector('#search-body');
    var side_navbar = document.querySelector('#side-navbar');
    var footer = document.querySelector('#footer');
    var pop_up_box = document.querySelector('.pop-up-box');
    var navbar_custom = document.querySelector('.navbar-custom'); 
    // var pop_up_position = document.querySelector('#pop-up-position');
    // var pop_up_nationality = document.querySelector('#pop-up-nationality');
    // var pop_up_specialization = document.querySelector('#pop-up-specialization');
    // var pop_up_age = document.querySelector('#pop-up-age');

    var detailed_experience_buttons = document.querySelectorAll('.detailed-experience');
    console.log(detailed_experience_buttons);
    detailed_experience_buttons.forEach(function(btn) {
        btn.addEventListener('click', event =>{
            console.log(event.target);
            console.log(event.target.dataset.studentid);
    //         const button = event.target;
    //         const button_div = button.parentNode;
    //         const student_div = button_div.parentNode;
    //         const position = student_div.querySelector('#position').textContent;
    //         const nationality = student_div.querySelector('#nationality').textContent;
    //         const specialization = student_div.querySelector('#specialization').textContent;
    //         const age = student_div.querySelector('#age').textContent;
    //         console.log(position);
    //         pop_up_position.innerHTML = position;
    //         pop_up_nationality.innerHTML = nationality;
    //         pop_up_specialization.innerHTML = specialization;
    //         pop_up_age.innerHTML = age;
            search_body.classList.add('blur');
            side_navbar.classList.add('blur');
            navbar_custom.classList.add('blur');
            footer.classList.add('blur');
            pop_up_box.classList.add('pop-up-show');
            var save_buttons = pop_up_box.querySelectorAll('.save-button');
            console.log(event.target.dataset.studentid.toString())
            save_buttons[0].setAttribute('data-student-id', event.target.dataset.studentid.toString());
            console.log(save_buttons)
        })
        // const button = btn.target;
        // console.log(button);
        // document.querySelector('#search-body').classList.add('blur');
        // document.querySelector('.pop-up-box').classList.add('pop-up-show');
    })
    document.querySelector('.overlay').addEventListener('click', () => {
        search_body.classList.remove('blur');
        side_navbar.classList.remove('blur');
        navbar_custom.classList.remove('blur');
        footer.classList.remove('blur');
        pop_up_box.classList.remove('pop-up-show');
    })

    var save_buttons = document.querySelectorAll('.save-button');
    save_buttons.forEach(function(btn) {
        btn.addEventListener('click', event =>{
            console.log(event.target);
            const studentId = btn.dataset.studentId;
            console.log(`Clicked on student with ID: ${studentId}`);
            const csrftoken = getCookie('csrftoken');
            console.log(csrftoken )

            const updateData = {
              // Define the data you want to update
              // For example, name or any other fields
              status: 'saved',
            };

            fetch(`/update_order/${studentId}/`, {
              method: 'PUT', // Or 'POST' based on your needs
              headers: {
                  'Content-Type': 'application/json',
                  'X-CSRFToken': csrftoken, // Include the CSRF token
              },
              body: JSON.stringify(updateData),
            })
              .then(response => response.json())
              .then(data => {
                // Handle any response from the server
                console.log(data);
                const statusElement = document.querySelector(`[data-student-status-id="${studentId}"]`);
                if (statusElement) {
                    statusElement.textContent = `Saved`; // Replace with the appropriate property from the response
                }
                // Update the UI if needed
              })
              .catch(error => {
                // Handle any errors
                console.error(error);
              });
        })
    })


    var search_buttons = document.querySelectorAll('#search');
    search_buttons.forEach(function(btn) {
        btn.addEventListener('click', event =>{
            console.log(event.target);
            var selectedPosition = document.getElementById("selected-position").innerText;
            if (selectedPosition === 'E.g. Mechanical Eng.'){
                selectedPosition = ''
            }
            console.log(selectedPosition);
            var selectedSpecialization = document.getElementById("selected-specialization").innerText;
            if (selectedSpecialization === 'E.g. Aerodynamics'){
                selectedSpecialization = ''
            }
            console.log(selectedSpecialization);
            var selectedCountry = document.getElementById("selected-country").innerText;
            if (selectedCountry === 'E.g. Germany'){
                selectedCountry = ''
            }
            console.log(selectedCountry);

            var url = '/search/?position=' + encodeURIComponent(selectedPosition) + '&specialization=' + encodeURIComponent(selectedSpecialization) + '&country=' + encodeURIComponent(selectedCountry);

            // Redirect to the generated URL
            window.location.href = url;
        })
    })

    var experience_buttons = document.querySelectorAll('#experience');
    console.log(experience_buttons)
    experience_buttons.forEach(function(btn) {
        btn.addEventListener('click', event =>{
            console.log(event.target);
            var selectedPosition = document.getElementById("selected-position").innerText;
            if (selectedPosition === 'E.g. Mechanical Eng.'){
                selectedPosition = ''
            }
            console.log(selectedPosition);
            var selectedSpecialization = document.getElementById("selected-specialization").innerText;
            if (selectedSpecialization === 'E.g. Aerodynamics'){
                selectedSpecialization = ''
            }
            console.log(selectedSpecialization);
            var selectedCountry = document.getElementById("selected-country").innerText;
            if (selectedCountry === 'E.g. Germany'){
                selectedCountry = ''
            }
            console.log(selectedCountry);

            var url = '/search/?position=' + encodeURIComponent(selectedPosition) + '&specialization=' + encodeURIComponent(selectedSpecialization) + '&country=' + encodeURIComponent(selectedCountry) + '&experience=True';

            // Redirect to the generated URL
            window.location.href = url;
        })
    })

    document.getElementById('expand-button').addEventListener('click', function() {
        var container = document.querySelector('.light-pink-box');
        var country_rating_row = document.querySelector('.country-rating-row');
        var search_row = document.querySelector('.search-row');
        var expand_button_up_div = document.querySelector('.expand-button-up-div');
        var expand_button_down_div = document.querySelector('.expand-button-down-div');
        container.style.height = 'auto';
        country_rating_row.style.display = 'block';
        country_rating_row.style.visibility = 'visible';
        search_row.style.display = 'block';
        search_row.style.visibility = 'visible';
        expand_button_up_div.style.display = 'block';
        expand_button_up_div.style.visibility = 'visible';
        expand_button_down_div.style.display = 'none';
        expand_button_down_div.style.visibility = 'hidden';
        expand_button_down_div.style.height = 0;
        // this.style.display = 'none';
    });

    document.getElementById('expand-button-up').addEventListener('click', function() {
        var container = document.querySelector('.light-pink-box');
        var country_rating_row = document.querySelector('.country-rating-row');
        var search_row = document.querySelector('.search-row');
        var expand_button_up_div = document.querySelector('.expand-button-up-div');
        var expand_button_down_div = document.querySelector('.expand-button-down-div');
        container.style.height = '200px';
        country_rating_row.style.display = 'none';
        country_rating_row.style.visibility = 'hidden';
        search_row.style.display = 'none';
        search_row.style.visibility = 'hidden';
        expand_button_up_div.style.display = 'none';
        expand_button_up_div.style.visibility = 'hidden';
        expand_button_down_div.style.display = 'block';
        expand_button_down_div.style.visibility = 'visible';
        expand_button_down_div.style.height = auto;
        // this.style.display = 'none';
    });



})