// import logo from './logo.svg';
import './App.css';
import React from 'react';

const { useState, useEffect } = React;

const App = () => {
  const [title, setTitle] = useState('posts')
  const [lists, setLists] = useState([])
  
  const changeTitle = (title) => () => {setTitle(title)}
  useEffect(() => {
    fetch(`https://jsonplaceholder.typicode.com/${title}`)
    .then((res) => res.json())
    .then((json) => {setLists(json);
                    });
  }, [title])
  //console.log(json);
  
  return (
    <div className="container">
      <div className="btn-group">
        <button className="btn" onClick={changeTitle('POSTS')}>Post</button>
        <button className="btn" onClick={changeTitle('USERS')}>Users</button>
        <button className="btn" onClick={changeTitle('COMMENTS')}>Comments</button>
      </div>
      <section>
        <h2>{title}</h2>
          {lists.map((list, index) => (<pre key={list.id || index}>{JSON.stringify(list, null, 2)}</pre>
))}
      </section>
     </div>
  )
};

export default App;
