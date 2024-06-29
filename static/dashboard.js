document.addEventListener('DOMContentLoaded', function() {
    var dashboard_container = document.querySelector('.dashboard-container');
    var dashboard_line = document.querySelector('.dashboard-line');
    let screen_width = window.innerWidth;

    if (screen_width <= 1300) {
        dashboard_container.classList.remove('p-5');
        dashboard_container.classList.add('p-4');

        // dashboard_line.classList.remove('px-5');
        // dashboard_line.classList.add('px-1');
    };

    window.addEventListener('resize', () => {
        let screen_width = window.innerWidth;

        if (screen_width <= 1300) {
            dashboard_container.classList.remove('p-5');
            dashboard_container.classList.add('p-4');

            // dashboard_line.classList.remove('px-5');
            // dashboard_line.classList.add('px-1');
        } else {
            dashboard_container.classList.remove('p-4');
            dashboard_container.classList.add('p-5');

            // dashboard_line.classList.remove('px-1');
            // dashboard_line.classList.add('px-5');
        };
    });
});