import React from 'react';
import './App.css';
import MovieList from './movielist';

function App() {
    return (
        <div className="App">
            <header className="App-header">
                <h1>TUW4TCH - Movie recommendation</h1>
                <MovieList />
            </header>
        </div>
    );
}

export default App;
