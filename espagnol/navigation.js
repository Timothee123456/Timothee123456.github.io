// menu.js

// Function to create the menu and add it to the page
function createMenu() {
    // Create the unordered list element
    var ul = document.createElement('ul');

    // Define the menu items as an array of objects
    var menuItems = [
        { title: "Día de la semana", url: "timothee123456.github.io/espagnol/jours-de-la-semaine" },
        { title: "Mes del año", url: "https://timothee123456.github.io/espagnol/mois" },
        { title: "Las estaciones", url: "https://timothee123456.github.io/espagnol/saisons/saisons" },
        { title: "Mascotas", url: "https://timothee123456.github.io/espagnol/animaux/animaux" },
        { title: "Colores", url: "https://timothee123456.github.io/espagnol/couleurs" },
        { title: "Verbos", url: "https://timothee123456.github.io/espagnol/verbes" },
        { title: "La descriptión físca", url: "https://timothee123456.github.io/espagnol/description" },
        { title: "Mi familia", url: "https://timothee123456.github.io/espagnol/famille" },
        { title: "Mi casa 1", url: "https://timothee123456.github.io/espagnol/casa" },
        { title: "Mi casa 2", url: "https://timothee123456.github.io/espagnol/casa2" },
        { title: "Vehículos", url: "https://timothee123456.github.io/espagnol/vehicules" },
        { title: "Horas", url: "https://timothee123456.github.io/espagnol/heures" },
        { title: "Entrevisto", url: "https://timothee123456.github.io/espagnol/interview" },
        { title: "Asignaturas", url: "https://timothee123456.github.io/espagnol/matières" },
        { title: "Leçons", url: "https://timothee123456.github.io/espagnol/leçons/jours-de-la-semaine", floatRight: true }
    ];

    // Get the current page URL
    var currentUrl = window.location.href;

    // Loop through the menu items and create list elements
    menuItems.forEach(function(item) {
        var li = document.createElement('li');
        li.className = 'li';

        if (item.floatRight) {
            li.style.float = 'right';
        }

        var a = document.createElement('a');
        a.href = item.url;
        a.textContent = item.title;

        // Set the active class if the URL matches the current page
        if (document.title === item.title) {
            a.className = 'active';
        }

        li.appendChild(a);
        ul.appendChild(li);
    });

    // Find the div with the ID 'menuContainer' and append the ul to it
    var menuContainer = document.getElementById('menuContainer');
    if (menuContainer) {
        menuContainer.appendChild(ul);
    }
}

// Run the createMenu function when the page loads
window.onload = createMenu;
