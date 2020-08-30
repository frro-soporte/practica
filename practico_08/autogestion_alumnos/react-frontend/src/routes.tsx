import React from 'react'
import { Route, Redirect, Switch } from 'react-router-dom'

export class RoutesApp extends React.Component {
    render(): JSX.Element {
        return (
            <Switch>
                <Route exact path="/">
                    <Redirect to={'app'} />
                </Route>
                <Route path="/app" component={App} />
                <Route path="/acc" component={Acc} />
            </Switch>
        )
    }
}

const isAuthenticated = true

const App = (): JSX.Element => {
    if (isAuthenticated) {
        return (
            <Switch>
                <Route exact path="/app">
                    <Redirect to={'/app/dashboard'} />
                </Route>
                <Route path={'/app/dashboard'} component={DashboardLoader} />
            </Switch>
        )
    }
    return (
        <Switch>
            <Redirect to={'/acc'} />
        </Switch>
    )
}

const Acc = (): JSX.Element => {
    if (isAuthenticated) {
        return (
            <Switch>
                <Redirect to={'/app'} />
            </Switch>
        )
    } else
        return (
            <Switch>
                <Route exact path="/acc">
                    <Redirect to={'/acc/login'} />
                </Route>
                <Route path="/acc/login" component={Login} />
                <Route path="/acc/signup" component={Signup} />
                <Route path="/acc/password-reset" component={PasswordReset} />
            </Switch>
        )
}

const DashboardLoader = (): JSX.Element => {
    return <button>Log Out</button>
}

const Login = (): JSX.Element => {
    return <button>Login</button>
}

const Signup = (): JSX.Element => {
    return <h1>signup</h1>
}

const PasswordReset = (): JSX.Element => {
    return <h1>passwordreset</h1>
}
