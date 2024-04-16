var pages = [
  { title: "Mascotas", url: "https://timothee123456.github.io/espagnol/a" },
  { title: "Mes del año", url: "https://timothee123456.github.io/espagnol/aaa" },
  { title: "Las estaciones", url: "https://timothee123456.github.io/espagnol/aa" },
  // Add more pages here as needed
];

var navigationMenu = document.getElementById("navigation-menu");
for (var i = 0; i < pages.length; i++) {
  var page = pages[i];
  var listItem = document.createElement("li");
  var link = document.createElement("a");
  link.href = page.url;
  link.textContent = page.title;

  // Add the "active" class to the current page's link
  if (window.location.pathname === page.url) {
    link.classList.add("active");
  }

  listItem.appendChild(link);
  navigationMenu.appendChild(listItem);
}
