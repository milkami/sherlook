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
                    console.log(event.target);
                    const dropdown_div = each_row.querySelector('.dropdown-div');
                    if (event.target === dropdown_icon) {
                        if (dropdown_div.style.visibility === 'hidden') {
                            dropdown_div.style.visibility = 'visible';
                            dropdown_div.style.display = 'block';
                        } else {
                            dropdown_div.style.visibility = 'hidden';
                            dropdown_div.style.display = 'none';
                        }
                    }
                })
            })


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

        // var remove_buttons = document.querySelectorAll('.remove-button');
        // remove_buttons.forEach(function(btn) {
        //     btn.addEventListener('click', event =>{
        //         console.log(event.target);
        //         const studentId = btn.dataset.studentId;
        //         console.log(`Clicked on student with ID: ${studentId}`);
        //         const csrftoken = getCookie('csrftoken');
        //         console.log(csrftoken )
        //
        //         const updateData = {
        //           // Define the data you want to update
        //           // For example, name or any other fields
        //           status: 'removed',
        //         };
        //
        //         fetch(`/update_order/${studentId}/`, {
        //           method: 'PUT', // Or 'POST' based on your needs
        //           headers: {
        //               'Content-Type': 'application/json',
        //               'X-CSRFToken': csrftoken, // Include the CSRF token
        //           },
        //           body: JSON.stringify(updateData),
        //         })
        //           .then(response => response.json())
        //           .then(data => {
        //             // Handle any response from the server
        //             console.log(data);
        //             const statusElement = document.querySelector(`[data-student-status-id="${studentId}"]`);
        //             const savedItem = document.getElementById('saved-item');
        //             if (savedItem){
        //                 savedItem.textContent = "SAVED | " + data['saved'];
        //             }
        //
        //             const connectedItem = document.getElementById('connected-item');
        //             if (connectedItem){
        //                 connectedItem.textContent = "|  CONNECTED | " + data['connected'];
        //             }
        //             if (statusElement) {
        //                 statusElement.textContent = `Connected`; // Replace with the appropriate property from the response
        //             }
        //             // Update the UI if needed
        //           })
        //           .catch(error => {
        //             // Handle any errors
        //             console.error(error);
        //           });
        //     })
        // })
})