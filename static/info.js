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

})