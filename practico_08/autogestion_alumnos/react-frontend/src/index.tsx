import React from 'react'
import ReactDOM from 'react-dom'
import { BrowserRouter as Router } from 'react-router-dom'
import './index.css'
import { CookiesProvider } from 'react-cookie/lib'
import RoutesApp from './routes'

ReactDOM.render(
    <CookiesProvider>
        <Router>
            <RoutesApp />
        </Router>
    </CookiesProvider>,
    document.getElementById('root')
)
