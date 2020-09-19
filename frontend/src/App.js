import React from 'react';
import './App.css';
import {useState, useEffect} from 'react';


function App() {

  const [recipes, setRecipes] = useState(null);

  useEffect(() => {
    fetchRecipes()
  
  }, []);

  async function fetchRecipes() {
    const response = await fetch("http://localhost:8000/api/recipe/");
    const jsonData = await response.json();
    const hsldhj = JSON.stringify(jsonData);
    console.log(hsldhj);
    setRecipes(hsldhj);
  }
  return (
    <div>
        {recipes}
    </div>
  );
}

export default App;
