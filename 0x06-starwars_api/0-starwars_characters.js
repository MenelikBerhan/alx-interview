#!/usr/bin/node
const request = require('request');

async function asyncRequest (url) {
  // Returns a promise that resolves with a json parsed response body
  return new Promise((resolve, reject) => {
    request.get(url, (_, resp, body) => {
      if (resp.statusCode === 200) resolve(JSON.parse(body));
      else reject(new Error(`HTTP error: ${resp.statusCode}: ${resp.statusMessage}`));
    });
  });
}

/*
Using the Star wars API, prints all characters of a Star Wars movie with given id (process.argv[2]).
Displays one character name per line in the same order as the “characters” list in the /films/ endpoint.
*/
function getCharactersList (filmId) {
  asyncRequest(`https://swapi-api.alx-tools.com/api/films/${filmId}/`)
    .then((film) => film.characters)
    .then(async (charactersUrlList) => {
      for (const characterUrl of charactersUrlList) {
        // `asyncRequest` returns a promise which is awaited to preserve sequence in `charactersUrlList`
        const character = await asyncRequest(characterUrl);
        console.log(character.name);
      }
    })
    .catch((error) => { console.error(error.message); });
}

const filmId = parseInt(process.argv[2]);
if (isNaN(filmId)) console.error('Usage: ./0-starwars_characters.js <integer>');
else getCharactersList(filmId);

/*
Optionally it can be implemented using `fetch` which is an async form of request
function usingFetch (filmId) {
  fetch(`https://swapi-api.alx-tools.com/api/films/${filmId}/`)
    .then((resp) => resp.json()) // return film as json (Promise)
    .then((film) => film.characters) // return list of characters url
    .then(async (charactersUrlList) => {
      for (const characterUrl of charactersUrlList) {
        // fetch() & json() both return a promise which are awaited so that
        //  character names are printed in same order as in `charactersUrlList`
        const character = await (await fetch(characterUrl)).json();
        console.log(character.name);
      }
    })
    .catch((reason) => { console.log(reason); });
}
usingFetch(3);
*/
