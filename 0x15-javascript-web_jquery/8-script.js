const $Uri = $('https://swapi-api.alx-tools.com/api/films/?format=json');
const $movieList = $('ul#list_movies');

$.get($Uri, function (response) {
  const movies = response.results;

  for (const movie of movies) {
    const listItem = $('<li></li>');
    listItem.text(movie.title);
    $movieList.append(listItem);
  }
});
