import React from 'react'
import { Route, Redirect, Switch } from 'react-router-dom'
import { Login } from './components/login'
import { SignUp } from './components/signUp'
import { Layout } from './components/app/layout'
import { Cookies, withCookies } from 'react-cookie/lib'
import { isNotNil } from './utils/checks'

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

export const App = (props: { cookies: Cookies }): JSX.Element => {
    const accessToken = props.cookies.get('access_token')
    const isAuthenticated = isNotNil(accessToken)
    if (isAuthenticated) {
        return (
            <Switch>
                <Route exact path="/app">
                    <Redirect to={'/app/dashboard'} push={true} />
                </Route>
                <Route exact path="/">
                    <Redirect to={'/app/dashboard'} push={true} />
                </Route>
                <Route
                    path={'/app/dashboard'}
                    render={() => <DashboardLoader cookies={props.cookies} />}
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
    const isAuthenticated = isNotNil(accessToken)
    if (isAuthenticated) {
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

const DashboardLoader = (props: { cookies: Cookies }): JSX.Element => {
    return <Layout>Log Out</Layout>
}

const PasswordReset = (): JSX.Element => {
    return <h1>passwordreset</h1>
}

export default withCookies(RoutesApp)
