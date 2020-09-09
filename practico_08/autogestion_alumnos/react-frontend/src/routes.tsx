import React from 'react'
import { Route, Redirect, Switch } from 'react-router-dom'
import { Login } from './components/login'
import { SignUp } from './components/signUp'
import { Cookies, withCookies } from 'react-cookie/lib'
import { isNotNil } from './utils/checks'
import { Dashboard } from './components/dashboard'
import { Task } from 'components/task'
import { Test } from 'components/test'

interface RoutesAppProps {
    cookies: Cookies
}

class RoutesApp extends React.Component<RoutesAppProps> {
    render(): JSX.Element {
        return (
            <Switch>
                <Route exact path="/">
                    <Redirect to={'/app'} push={true} />
                </Route>
                <Route
                    path="/app"
                    render={() => <App cookies={this.props.cookies} />}
                />
                <Route
                    path="/acc"
                    render={() => <Acc cookies={this.props.cookies} />}
                />
            </Switch>
        )
    }
}

const App = (props: { cookies: Cookies }): JSX.Element => {
    const accessToken = props.cookies.get('access_token')
    console.log(accessToken)
    if (accessToken && isNotNil(accessToken)) {
        return (
            <Switch>
                <Route exact path="/app">
                    <Redirect to={'/app/dashboard'} push={true} />
                </Route>
                <Route
                    path={'/app/dashboard'}
                    render={() => <Dashboard cookies={props.cookies} />}
                />
                <Route
                    path={'/app/task'}
                    render={() => <Task cookies={props.cookies} />}
                />
                <Route
                    path={'/app/calendar'}
                    render={() => <Dashboard cookies={props.cookies} />}
                />
                <Route
                    path={'/app/subject'}
                    render={() => <Dashboard cookies={props.cookies} />}
                />
                <Route
                    path={'/app/test'}
                    render={() => <Test cookies={props.cookies} />}
                />
            </Switch>
        )
    }
    return (
        <Switch>
            <Redirect to={'/acc'} push={true} />
        </Switch>
    )
}

const Acc = (props: { cookies: Cookies }): JSX.Element => {
    const accessToken = props.cookies.get('access_token')
    console.log(props.cookies.get('access_token'))
    if (accessToken && isNotNil(accessToken)) {
        return (
            <Switch>
                <Redirect to={'/app'} push={true} />
            </Switch>
        )
    } else
        return (
            <Switch>
                <Route exact path="/acc">
                    <Redirect to={'/acc/login'} push={true} />
                </Route>
                <Route
                    path="/acc/login"
                    render={() => <Login cookies={props.cookies} />}
                />
                <Route path="/acc/signup" render={() => <SignUp />} />
                <Route path="/acc/password-reset" component={PasswordReset} />
            </Switch>
        )
}

const PasswordReset = (): JSX.Element => {
    return <h1>passwordreset</h1>
}

export default withCookies(RoutesApp)
