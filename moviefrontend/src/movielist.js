import React, { useState } from 'react';
import axios from 'axios';

function MovieList() {
    const [movies, setMovies] = useState([]);
    const [query, setQuery] = useState('');
    const [error, setError] = useState(null);

    const searchMovies = async () => {
        try {
            const response = await axios.get(`https://tuw4tch-2ef1308251e7.herokuapp.com/`);
            // Ensure response.data.results is an array
            if (response.data.results && Array.isArray(response.data.results)) {
                setMovies(response.data.results);
            } else {
                setMovies([]);
                setError('No movies found.');
            }
        } catch (err) {
            console.error('Error fetching movies:', err);
            setError('Error fetching movies. Please try again later.');
        }
    };

    return (
        <div>
            <input 
                type="text" 
                value={query} 
                onChange={(e) => setQuery(e.target.value)} 
                placeholder="Search for a movie..." 
            />
            <button onClick={searchMovies}>Search</button>
            {error && <p>{error}</p>}
            <ul>
                {movies.map(movie => (
                    <li key={movie.id}>
                        {movie.poster_url && <img src={movie.poster_url} alt={movie.title}/>}
                        <h3>{movie.title}</h3>
                        <p>{movie.description}</p>
                        <p>Release Date: {movie.release_date}</p>
                        <p>Rating: {movie.rating}</p>
                        
                                
                        
                        </li>
                ))}
            </ul>
        </div>
    );
}

export default MovieList;
