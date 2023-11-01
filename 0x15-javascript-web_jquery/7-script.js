const $Uri = $('https://swapi-api.alx-tools.com/api/people/5/?format=json');
const $divcharacter = $('div##character');

$.get($Uri, function (response) {
  $divcharacter.text(response.name);
});
