// Javascript script that fetches and replaces the name of this URL: https://swapi.co/api/people/5/?format=json

$.getJSON('https://swapi.co/api/people/5/?format=json', function(json) {
  $('DIV#character').text(json.name);
});
