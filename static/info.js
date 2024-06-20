document.addEventListener('DOMContentLoaded', function() {
    var info_search = document.querySelector('#info-search');
    var library_button = document.querySelector('#library-button');

    library_button.addEventListener('click', event => {
        info_search.style.visibility = 'hidden';
    });

    window.addEventListener('resize', function() {
        var element = document.getElementById('info-images-div');
        console.log(element);
        if (window.innerWidth > 1600) {
            element.classList.remove('px-3');
        } else {
            element.classList.add('px-3');
        }
    });
    var library_button = document.querySelector('#go-to-library');

    library_button.addEventListener('click', event => {
        var currentURL = window.location.href;
        var url = currentURL + "?library=True";

        window.location.href = url; // Redirect to the modified URL
    });

    var info_body = document.querySelector('#info-body');
    var info_search_div = document.querySelector('.info-search-6-div');
    let screen_width = window.innerWidth;

      if (screen_width >= 3000) {
        info_body.classList.remove('px-4');
        info_body.classList.add('px-5');

        info_search_div.classList.remove('col-10');
        info_search_div.classList.add('col-9');
      };
    
    window.addEventListener('resize', () => {
      let screen_width = window.innerWidth;
      if (screen_width >= 3000) {
        // Add bigger padding to info page
        info_body.classList.remove('px-4');
        info_body.classList.add('px-5');

        // Change size of one of info div's
        info_search_div.classList.remove('col-10');
        info_search_div.classList.add('col-9');

      } else {
        // Return to normal padding on info page
        info_body.classList.remove('px-5');
        info_body.classList.add('px-4');

        // Change size of one of info div's
        info_search_div.classList.remove('col-9');
        info_search_div.classList.add('col-10');
      };
    });


})