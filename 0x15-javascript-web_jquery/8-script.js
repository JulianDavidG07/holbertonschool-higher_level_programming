// Javascript script that fetches and lists all movies title by using this URL: https://swapi.co/api/films/?format=json

$.getJSON('https://swapi.co/api/films/?format=json', function (json) {
  for (const i in json.results) {
    $('UL#list_movies').append(`<li>${json.results[i].title}</li>`);
  }
});
