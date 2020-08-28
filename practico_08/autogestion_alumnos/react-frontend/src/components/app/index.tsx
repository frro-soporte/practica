import React from 'react'
import { Switch, Route, Redirect } from 'react-router-dom'

const App = (): JSX.Element => {
    return (
        <div className="App">
            <header className="App-header">
                <a
                    className="App-link"
                    href="https://reactjs.org"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    Learn React
                </a>
            </header>
            <Switch>
                <Route exact path="/">
                    <Pepe />
                </Route>
                <Redirect to="/" />
            </Switch>
        </div>
    )
}

const Pepe = (): JSX.Element => {
    return <div>Esto es el path por defecto</div>
}

export default App
