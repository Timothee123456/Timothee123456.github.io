// Array of list items and their URLs
const pages = [
  { title: "Día de la semana", url: "https://timothee123456.github.io/espagnol/jours-de-la-semaine"},
  { title: "Mes del año", url: "https://timothee123456.github.io/espagnol/mois" },
  { title: "Las estaciones", url: "https://timothee123456.github.io/espagnol/saisons/saisons" },
  // Add more pages here as needed
];

// Create a new unordered list element
const ul = document.createElement('ul');


// Loop through the items and create list elements with links
items.forEach(item => {
    const li = document.createElement('li');
    li.className = 'list-item';
    
    const a = document.createElement('a');
    a.textContent = item.text;
    a.href = item.url;
    
    li.appendChild(a);
    ul.appendChild(li);
        });

// Append the unordered list to the container
document.getElementById('list-container').appendChild(ul);
