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
                    if (student_data_div.contains(event.target)) {
                        if (dropdown_div.style.visibility === 'hidden') {
                            dropdown_div.style.visibility = 'visible';
                            dropdown_div.style.display = 'block';
                            if (dropdown_icon.classList.contains('fa-chevron-down')) {
                                dropdown_icon.classList.remove('fa-chevron-down');
                                dropdown_icon.classList.add('fa-chevron-up');
                            }
                        } else {
                            dropdown_div.style.visibility = 'hidden';
                            dropdown_div.style.display = 'none';
                            if (dropdown_icon.classList.contains('fa-chevron-up')) {
                                console.log('it contains');
                                dropdown_icon.classList.remove('fa-chevron-up');
                                dropdown_icon.classList.add('fa-chevron-down');
                            }
                        }
                    }
                })
            })
    
        var library_body = document.querySelector('#library-body');
        var side_navbar = document.querySelector('#side-navbar');
        var pop_up_box = document.querySelector('.pop-up-box');
        var navbar_custom = document.querySelector('.navbar-custom'); 
        var footer = document.querySelector('#footer');  
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
                library_body.classList.add('blur');
                side_navbar.classList.add('blur');
                navbar_custom.classList.add('blur');
                footer.classList.add('blur');
                pop_up_box.classList.add('pop-up-show');
                var save_buttons = pop_up_box.querySelectorAll('.connect-button');
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
            library_body.classList.remove('blur');
            side_navbar.classList.remove('blur');
            navbar_custom.classList.remove('blur');
            footer.classList.remove('blur');
            pop_up_box.classList.remove('pop-up-show');
        })

        let screen_width = window.innerWidth;
        let remove_from_library_div = document.querySelector('.remove-from-library-div');
        let remove_from_library_link = document.querySelector('.remove-from-library-link');
        var pop_up_inner_body_row = document.querySelector('.pop-up-inner-body-row');

        if (screen_width >= 3000) {
            library_body.classList.add('px-4');

            // Adjust position of 'Remove from library' link
            remove_from_library_div.classList.remove('pe-4');
            remove_from_library_div.classList.add('pe-5');
            remove_from_library_div.classList.remove('pt-2');
            remove_from_library_div.classList.add('pt-3');
            remove_from_library_link.classList.add('me-5');

            // Add padding to pop-up with additional info
            pop_up_inner_body_row.classList.add('px-3');
            pop_up_inner_body_row.classList.add('py-2');
        };
    
        window.addEventListener('resize', () => {
            let screen_width = window.innerWidth;
            if (screen_width >= 3000) {
                // Add bigger padding to library page
                library_body.classList.add('px-4');

                // Adjust position of 'Remove from library' link
                remove_from_library_div.classList.remove('pe-4');
                remove_from_library_div.classList.add('pe-5');
                remove_from_library_div.classList.remove('pt-2');
                remove_from_library_div.classList.add('pt-3');
                remove_from_library_link.classList.add('me-5');

                // Add padding to pop-up with additional info
            pop_up_inner_body_row.classList.add('px-3');
            pop_up_inner_body_row.classList.add('py-2');

            } else {
                // Return to normal padding on library page
                library_body.classList.remove('px-4');

                // Adjust position of 'Remove from library' link
                remove_from_library_div.classList.remove('pe-5');
                remove_from_library_div.classList.add('pe-4');
                remove_from_library_div.classList.remove('pt-3');
                remove_from_library_div.classList.add('pt-2');
                remove_from_library_link.classList.remove('me-5');

                // Remove padding from pop-up with additional info
                pop_up_inner_body_row.classList.remove('px-3');
                pop_up_inner_body_row.classList.remove('py-2');
            };
        });




    // Function to apply the class based on the screen width
        function applyClassBasedOnScreenWidth() {
            var isLargeScreen = window.innerWidth > 1200;

            // Find all span elements with the class dropdown-main-text
            var dropdownMainTexts = document.querySelectorAll('.dropdown-main-text');

            // Use the variable to dynamically change the class for each span
            //dropdownMainTexts.forEach(function (mainText) {
                //mainText.className = isLargeScreen ? 'text-style-ro-24b' : 'text-style-ro-20b';
                //mainText.classList.toggle('text-style-ro-24b', isLargeScreen);
                //mainText.classList.toggle('text-style-ro-20b', !isLargeScreen);
            //});
        }

        var save_buttons = document.querySelectorAll('.connect-button');
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
                  status: 'connected',
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
                    const savedItem = document.getElementById('saved-item');
                    if (savedItem){
                        savedItem.textContent = "SAVED | " + data['saved'];
                    }

                    const connectedItem = document.getElementById('connected-item');
                    if (connectedItem){
                        connectedItem.textContent = "|  CONNECTED | " + data['connected'];
                    }
                    if (statusElement) {
                        statusElement.textContent = `Connected`; // Replace with the appropriate property from the response
                    }
                    // Update the UI if needed
                  })
                  .catch(error => {
                    // Handle any errors
                    console.error(error);
                  });
            })
        })

})