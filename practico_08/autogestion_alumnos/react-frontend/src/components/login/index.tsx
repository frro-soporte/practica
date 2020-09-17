import React, { useCallback, useState } from 'react'
import { StyleMap } from 'utils/tsTypes'
import { VerticalStack } from 'common/components/flex'
import { LoginModel } from 'components/login/model'
import { Cookies } from 'react-cookie/lib'
import { Link, useHistory} from 'react-router-dom'

export const Login = (props: { cookies: Cookies }): JSX.Element => {
    const model = new LoginModel(props.cookies)

    const styles: StyleMap = {
        background: {
            position: 'absolute',
            textAlign: 'center',
            verticalAlign: 'middle',
            width: '100%',
            background: '#2B2F32',
            border: '1px solid #000000',
            boxSizing: 'border-box',
        },
        whiteBox: {
            position: 'relative',
            margin: '5% auto',
            width: '450px',
            height: '500px',
            background: '#ffffff',
            display: 'flex',
            flexDirection: 'column',
            boxShadow: '10px 10px 10px rgba(0, 0, 0, 0.25)',
            borderRadius: '45px'
        },
        userIcon: {
            borderRadius: '50%',
            alignSelf: 'center',
            marginTop: '30px',
            position: 'absolute',
            width: '100px',
            height: '100px',
            background: '#C4C4C4',
            display: 'flex',
            flexDirection: 'column',
        },
    }

    return (
        <div style={styles.background}>
            <div style={styles.whiteBox}>
                <div style={styles.userIcon} />
                <LoginForm model={model} />
                <BottomOptions />
            </div>
        </div>
    )
}

const LoginForm = (props: { model: LoginModel }): JSX.Element => {
    const styles: StyleMap = {
        loginForm: {
            marginTop: '100px',
            alignSelf: 'center',
        },
        inputForm: {
            marginTop: '55px',
            width: '280px',
            height: '25px',
            textAlign: 'center',
            color: 'rgba(0, 0, 0, 0.5)',
            fontStyle: 'normal',
            fontWeight: 'normal',
            fontSize: '25px',
            borderWidth: '2px',
            borderColor: '#b3b3b3',
            fontFamily: 'New York Medium',
        },
        loginButton: {
            marginTop: '40px',
            width: '320px',
            height: '42px',
            background: '#e91e63',
            borderWidth: 'medium',
            borderColor: '#b3b3b3',
            boxShadow: '0 4px 4px rgba(0, 0, 0, 0.25)',
            borderRadius: '22px',
            fontStyle: 'normal',
            fontWeight: 'normal',
            fontFamily: 'New York Medium',
            fontSize: '30px',
            color: '#FFFFFF',
            cursor: 'pointer'
        },
    }

    const [username, setUserName] = useState('')
    const [password, setPassword] = useState('')
    const [errorMessage, setErrorMessage] = useState('')
    const history = useHistory()
    const goToDashboard = useCallback(() => {
        history.push('/app/dashboard')
    }, [])

    return (
        <VerticalStack style={{ alignSelf: 'center' }}>
            <form style={styles.loginForm}>
                <VerticalStack>
                    <input
                        style={styles.inputForm}
                        type="text"
                        name="userName"
                        required={true}
                        placeholder="Username"
                        value={username}
                        onChange={(event) => {
                            setUserName(event.target.value)
                        }}
                    />
                    <input
                        style={styles.inputForm}
                        type="password"
                        name="password"
                        required={true}
                        placeholder="Password"
                        value={password}
                        onChange={(event) => {
                            setPassword(event.target.value)
                        }}
                    />
                    {errorMessage}
                </VerticalStack>
            </form>
            <button
                style={styles.loginButton}
                onClick={() =>
                    props.model.onClickLogin(
                        username,
                        password,
                        setErrorMessage,
                        goToDashboard
                    )
                }
            >
                Log In
            </button>
        </VerticalStack>
    )
}

const BottomOptions = (): JSX.Element => {
    const styles: StyleMap = {
        signUp: {
            marginTop: '35px',
            fontStyle: 'normal',
            fontWeight: 'normal',
            fontSize: '18px',
            color: 'black',
            textDecoration: 'none',
        },
        lostYourPassword: {
            marginTop: '15px',
            fontStyle: 'normal',
            fontWeight: 'normal',
            fontSize: '20px',
            color: 'black',
            textDecoration: 'none',
        },
        bottomLinks: {
            width: '500px',
            alignSelf: 'center',
        },
    }
    return (
        <VerticalStack style={styles.bottomLinks}>
            <Link style={styles.signUp} to={'/acc/signup'}>
                Sign Up
            </Link>
            <Link style={styles.lostYourPassword} to={'/'}>
                Lost your password?
            </Link>
        </VerticalStack>
    )
}
