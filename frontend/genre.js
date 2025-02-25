// URL of the Flask backend

then((movies) => {
    movieList.innerHTML = ""; // clear previous movies
    movies.forEach((movie) => {
        const movieItem = document.createElement("div");
        movieItem.classList.add("movie");

        const movieImage = document.createElement("img");
        movieImage.src = 'https://image.tmdb.org/t/p/w200${movie.poster_path}';
        movieImage.alt = movie.title;

        const movieTitle = document.createElement("p");
        movieTitle.textContent = movie.title;

        movieItem.appendChild(movieImage);
        movieItem.appendChild(movieTitle);
        movieItem.appendChild(movieItem);
    })
});