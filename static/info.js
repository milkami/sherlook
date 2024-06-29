document.addEventListener('DOMContentLoaded', function() {
    var info_search = document.querySelector('#info-search');
    var library_button = document.querySelector('#library-button');

    // library_button.addEventListener('click', event => {
    //     info_search.style.visibility = 'hidden';
    // });

    // window.addEventListener('resize', function() {
    //     var element = document.getElementById('info-images-div');
    //     console.log(element);
    //     if (window.innerWidth > 1600) {
    //         element.classList.remove('px-3');
    //     } else {
    //         element.classList.add('px-3');
    //     }
    // });
    var library_button = document.querySelector('#go-to-library');

    if (document.body.contains(library_button)) {
        library_button.addEventListener('click', event => {
            var currentURL = window.location.href;
            var url = currentURL + "?library=True";

            window.location.href = url; // Redirect to the modified URL
        });
    };

    var info_body = document.querySelector('#info-body');
    var info_search_div_one = document.querySelector('.info-search-div-one');
    var info_search_div_two = document.querySelector('.info-search-div-two');
    var filter_search_categories_div = document.querySelector('.filter-search-categories-div');
    var info_search_div_six = document.querySelector('.info-search-div-six');
    var info_library_div_two = document.querySelector('.info-library-div-two');
    var info_library_text_box = document.querySelector('.info-library-text-box');
    let screen_width = window.innerWidth;


    if (screen_width >= 3000) {
        info_body.classList.remove('px-4');
        info_body.classList.add('px-5');

        // Size adjustment of 'How to use search 1' div
        if (document.body.contains(info_search_div_one)) {
            info_search_div_one.classList.remove('col-10');
            info_search_div_one.classList.add('col-9');
        };

        // Size adjustment of 'How to use search 2' div
        if (document.body.contains(info_search_div_two)) {
            info_search_div_two.classList.add('ms-5');
            info_search_div_two.classList.add('ps-5');
        };

        // Size adjustment of 'Filter search categories' div in 'How to use search 5' div
        if (document.body.contains(filter_search_categories_div)) {
            filter_search_categories_div.classList.remove('pb-2');
            filter_search_categories_div.classList.add('pb-4');
        };

        // Size adjustment of 'How to use search 6' div
        if (document.body.contains(info_search_div_six)) {
            info_search_div_six.classList.remove('col-10');
            info_search_div_six.classList.add('col-9');
        };

        // Size adjustment of 'How to use library 2' div
        if (document.body.contains(info_library_div_two)) {
            info_library_div_two.classList.remove('col-10');
            info_library_div_two.classList.add('col-9');
        };

        // Size adjustment of text box inside 'How to use library 2' div
        if (document.body.contains(info_library_text_box)) {
            info_library_text_box.classList.remove('px-md-2');
            info_library_text_box.classList.remove('px-xl-4');
            info_library_text_box.classList.add('px-5');
        };

    };
    
    window.addEventListener('resize', () => {
      let screen_width = window.innerWidth;

      if (screen_width >= 3000) {
        // Add bigger padding to info page
        info_body.classList.remove('px-4');
        info_body.classList.add('px-5');

        // Size adjustment of 'How to use search 1' div
        if (document.body.contains(info_search_div_one)) {
            info_search_div_one.classList.remove('col-10');
            info_search_div_one.classList.add('col-9');
        };

        // Size adjustment of 'How to use search 2' div
        if (document.body.contains(info_search_div_two)) {
            info_search_div_two.classList.add('ms-5');
            info_search_div_two.classList.add('ps-5');
        };

        // Size adjustment of 'Filter search categories' div in 'How to use search 5' div
        if (document.body.contains(filter_search_categories_div)) {
            filter_search_categories_div.classList.remove('pb-2');
            filter_search_categories_div.classList.add('pb-4');
        };

        // Size adjustment of 'How to use search 6' div
        if (document.body.contains(info_search_div_six)) {
            info_search_div_six.classList.remove('col-10');
            info_search_div_six.classList.add('col-9');
        };

        // Size adjustment of 'How to use library 2' div
        if (document.body.contains(info_library_div_two)) {
            info_library_div_two.classList.remove('col-10');
            info_library_div_two.classList.add('col-9');
        };

        // Size adjustment of text box inside 'How to use library 2' div
        if (document.body.contains(info_library_text_box)) {
            info_library_text_box.classList.remove('px-md-2');
            info_library_text_box.classList.remove('px-xl-4');
            info_library_text_box.classList.add('px-5');
        };

      } else {
        // Return to normal padding on info page
        info_body.classList.remove('px-5');
        info_body.classList.add('px-4');

        // Size adjustment of 'How to use search 1' div
        if (document.body.contains(info_search_div_one)) {
            info_search_div_one.classList.remove('col-9');
            info_search_div_one.classList.add('col-10');
        };

        // Size adjustment of 'How to use search 2' div
        if (document.body.contains(info_search_div_two)) {
            info_search_div_two.classList.remove('ms-5');
            info_search_div_two.classList.remove('ps-5');
        };

        // Size adjustment of 'Filter search categories' div in 'How to use search 5' div
        if (document.body.contains(filter_search_categories_div)) {
            filter_search_categories_div.classList.remove('pb-4');
            filter_search_categories_div.classList.add('pb-2');
        };

        // Size adjustment of 'How to use search 6' div
        if (document.body.contains(info_search_div_six)) {
            info_search_div_six.classList.remove('col-9');
            info_search_div_six.classList.add('col-10');
        };

        // Size adjustment of 'How to use library 2' div
        if (document.body.contains(info_library_div_two)) {
            info_library_div_two.classList.remove('col-9');
            info_library_div_two.classList.add('col-10');
        };

        // Size adjustment of text box inside 'How to use library 2' div
        if (document.body.contains(info_library_text_box)) {
            info_library_text_box.classList.remove('px-5');
            info_library_text_box.classList.add('px-md-2');
            info_library_text_box.classList.add('px-xl-4');
        };
      };
    });


})