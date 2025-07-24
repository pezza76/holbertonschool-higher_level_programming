fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
.then(response => response.json()) // convert json data to something like a python dict
.then(data => document.getElementById('character').textContent = data.name);