fetch("https://swapi-api.hbtn.io/api/films/?format=json")
  .then(response => response.json())
  .then(data => {
    const list_movies = document.getElementById('list_movies')
    
    data.results.forEach(film => {
        const li = document.createElement('li')
        li.textContent = film.title
        list_movies.appendChild(li)
        
    });
  });

