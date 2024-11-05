// Function to create the menu and add it to the page
function createMenu() {
    // Create the unordered list element
    var ul = document.createElement('ul');

    // Define the menu items as an array of objects
    var menuItems = [
        {
            title: "Forces et interactions",
            dropdown: true,
            items: [
                { title: "1", url: "https://timothee123456.github.io/eval/physique/2/schema1" },
                { title: "2", url: "https://timothee123456.github.io/eval/physique/2/schema2" },
                { title: "3", url: "https://timothee123456.github.io/eval/physique/2/schema3" }
            ]
        },
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
            if (removeHyphen(currentPageTitle) === item.title) {
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


function removePrefix(str) {
    const prefix = "Physique - ";
    if (str.startsWith(prefix)) {
        return str.substring(prefix.length);
    } else {
        return str; // Or handle the case where the prefix isn't there
    }
}

// Run the createMenu function when the page loads
window.onload = createMenu;
