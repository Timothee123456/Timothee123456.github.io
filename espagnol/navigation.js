// Function to create the menu and add it to the page
function createMenu() {
    // Create the unordered list element
    var ul = document.createElement('ul');

    // Define the menu items as an array of objects
    var menuItems = [
        {
            title: "Date",
            dropdown: true,
            items: [
                { title: "Fecha", url: "https://timothee123456.github.io/espagnol/date" },
                { title: "Día de la semana", url: "https://timothee123456.github.io/espagnol/jours-de-la-semaine" },
                { title: "Mes del año", url: "https://timothee123456.github.io/espagnol/mois" }
            ]
        },
        { title: "Mascotas", url: "https://timothee123456.github.io/espagnol/animaux/animaux" },
        { title: "Colores", url: "https://timothee123456.github.io/espagnol/couleurs" },
        { title: "Verbos", url: "https://timothee123456.github.io/espagnol/verbes" },
        { title: "La descriptión físca", url: "https://timothee123456.github.io/espagnol/description" },
        { title: "Mi familia", url: "https://timothee123456.github.io/espagnol/famille" },
        { title: "Mi casa 1", url: "https://timothee123456.github.io/espagnol/casa" },
        { title: "Mi casa 2", url: "https://timothee123456.github.io/espagnol/casa2" },
        { title: "Vehículos", url: "https://timothee123456.github.io/espagnol/vehicules" },
        { title: "Entrevisto", url: "https://timothee123456.github.io/espagnol/interview" },
        { title: "Asignaturas", url: "https://timothee123456.github.io/espagnol/matières" },
        { title: "Las vacaciones", url: "https://timothee123456.github.io/espagnol/vacances" },
        { title: "Leçons", url: "https://timothee123456.github.io/espagnol/leçons/jours-de-la-semaine", floatRight: true }
    ];

    // Get the current page title
    var currentPageTitle = document.title;

    // Loop through the menu items and create list elements
    menuItems.forEach(function(item) {
        var li = document.createElement('li');
        li.className = 'li';

        if (item.floatRight) {
            li.style.float = 'right';
        }

        if (item.dropdown) {
            var divDropdown = document.createElement('div');
            divDropdown.className = 'dropdown';

            var button = document.createElement('button');
            button.className = 'button';
            button.textContent = item.title + ' ';

            var caretIcon = document.createElement('i');
            caretIcon.className = 'fa fa-caret-down';
            button.appendChild(caretIcon);

            var divDropdownContent = document.createElement('div');
            divDropdownContent.className = 'dropdown-content';

            item.items.forEach(function(subItem) {
                var a = document.createElement('a');
                a.href = subItem.url;
                a.textContent = subItem.title;

                // Set the active class if the page title matches the subitem title
                if (currentPageTitle === subItem.title) {
                    a.className = 'active';
                }

                divDropdownContent.appendChild(a);
            });

            divDropdown.appendChild(button);
            divDropdown.appendChild(divDropdownContent);
            li.appendChild(divDropdown);
        } else {
            var a = document.createElement('a');
            a.href = item.url;
            a.textContent = item.title;

            // Set the active class if the page title matches the item title
            if (currentPageTitle === item.title) {
                a.className = 'active';
            }

            li.appendChild(a);
        }

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
