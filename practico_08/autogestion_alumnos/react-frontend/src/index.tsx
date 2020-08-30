import React from 'react'
import ReactDOM from 'react-dom'
import { BrowserRouter as Router } from 'react-router-dom'
import './index.css'
import { RoutesApp } from './routes'

ReactDOM.render(
    <Router>
        <RoutesApp />
    </Router>,
    document.getElementById('root')
)
