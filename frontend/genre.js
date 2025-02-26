// This will run as soon as the page loads
document.addEventListener("DOMContentLoaded", () => {
    // Fetch genres from the Flask backend
    fetch("/genres")
        .then(response => response.json())  // Parse the response to JSON
        .then(data => {
            const genreSelect = document.getElementById("genre-select");

            // Clear the current options
            genreSelect.innerHTML = '<option value="" disabled selected>Select a Genre</option>';

            // Add each genre as an option in the dropdown
            data.genres.forEach(genre => {
                const option = document.createElement("option");
                option.value = genre.id;  // genre.id is the value sent to the Flask backend for movies
                option.textContent = genre.name;  // genre.name is displayed in the dropdown
                genreSelect.appendChild(option);
            });
        })
        .catch(error => console.error("Error fetching genres:", error)); // Error handling
});

// This is your existing code that runs when the 'Get Movies' button is clicked
document.getElementById("fetch-movies").addEventListener("click", () => {
    const selectedGenre = document.getElementById("genre-select").value;
    console.log("Selected genre ID:", selectedGenre); // Log the selected genre ID
    
    if (!selectedGenre) {
        alert("Please select a genre!");
        return;
    }

    fetch(`/movies/${selectedGenre}`)
        .then(response => response.json())
        .then(movies => {
            console.log(movies); // Log the movies received
            const movieList = document.getElementById("movies-list");
            movieList.innerHTML = ""; // Clear previous movies

            movies.forEach(movie => {
                const movieItem = document.createElement("div");
                movieItem.classList.add("movie");

                const movieImage = document.createElement("img");
                movieImage.src = `https://image.tmdb.org/t/p/w200${movie.poster_path}`;
                movieImage.alt = movie.title;

                const movieTitle = document.createElement("p");
                movieTitle.textContent = movie.title;

                movieItem.appendChild(movieImage);
                movieItem.appendChild(movieTitle);
                movieList.appendChild(movieItem);
            });
        })
        .catch(error => console.error("Error fetching movies:", error)); // Error handling
});
