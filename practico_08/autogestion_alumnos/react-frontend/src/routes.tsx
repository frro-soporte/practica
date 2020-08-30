import React from 'react'
import { Route, Redirect, Switch } from 'react-router-dom'
import { login } from './components/login'
import { signUp } from './components/signUp'
import { Layout } from './components/app/layout'

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

const isAuthenticated = false

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
                <Route path="/acc/login" component={login} />
                <Route path="/acc/signup" component={signUp} />
                <Route path="/acc/password-reset" component={PasswordReset} />
            </Switch>
        )
}

const DashboardLoader = (): JSX.Element => {
    return <Layout>Log Out</Layout>
}

const PasswordReset = (): JSX.Element => {
    return <h1>passwordreset</h1>
}
