import React, { useCallback, useState } from 'react'
import { StyleMap } from 'utils/tsTypes'
import { VerticalStack } from 'common/components/flex'

import { SignUpModel } from './model'
import {Link, Redirect, Switch, useHistory} from 'react-router-dom'

export const SignUp = (): JSX.Element => {
    const model = new SignUpModel()

    const styles: StyleMap = {
        background: {
            position: 'absolute',
            textAlign: 'center',
            verticalAlign: 'middle',
            width: '100%',
            background:
                'radial-gradient(96.69% 305.6% at 1.2% 1.81%, rgba(5, 15, 31, 0.85) 0%, #101825 44.27%, #6ba1f2 99.99%, #77a3ee 99.99%)',
            border: '1px solid #000000',
            boxSizing: 'border-box',
        },
        whiteBox: {
            position: 'relative',
            margin: '10% auto',
            width: '1000px',
            height: '1000px',
            background: '#ffffff',
            display: 'flex',
            flexDirection: 'column',
            boxShadow: '10px 10px 10px rgba(0, 0, 0, 0.25)',
        },
        userIcon: {
            borderRadius: '50%',
            marginLeft: '400px',
            marginTop: '50px',
            position: 'absolute',
            width: '200px',
            height: '200px',
            background: '#C4C4C4',
            display: 'flex',
            flexDirection: 'column',
        },
    }

    return (
        <div style={styles.background}>
            <div style={styles.whiteBox}>
                <div style={styles.userIcon} />
                <SignUpForm model={model} />
                <BottomOptions />
            </div>
        </div>
    )
}

const SignUpForm = (props: { model: SignUpModel }): JSX.Element => {
    const styles: StyleMap = {
        signUpForm: {
            marginTop: '200px',
            alignSelf: 'center',
        },
        inputForm: {
            marginTop: '75px',
            width: '300px',
            height: '50px',
            textAlign: 'center',
            color: 'rgba(0, 0, 0, 0.5)',
            fontStyle: 'normal',
            fontWeight: 'normal',
            fontSize: '35px',
            borderWidth: '4px',
            borderColor: '#b3b3b3',
            fontFamily: 'New York Medium',
        },
        signupButton: {
            marginTop: '75px',
            width: '320px',
            height: '60px',
            background: '#D22828',
            borderWidth: 'medium',
            borderColor: '#a12121',
            boxShadow: '0 4px 4px rgba(0, 0, 0, 0.25)',
            borderRadius: '22px',
            fontStyle: 'normal',
            fontWeight: 'normal',
            fontFamily: 'New York Medium',
            fontSize: '35px',
            color: '#FFFFFF',
            alignSelf: 'center',
        },
    }
    const [dni, setDni] = useState('')
    const [legajo, setLegajo] = useState('')
    const [username, setUserName] = useState('')
    const [password, setPassword] = useState('')
    const [errorMessage, setErrorMessage] = useState('')
    const history = useHistory()
    const goToLogin = useCallback(() => {
        history.push('/acc/login')
    }, [])

    return (
        <VerticalStack>
            <form style={styles.signUpForm}>
                <VerticalStack>
                    <input
                        style={styles.inputForm}
                        type="text"
                        name="dni"
                        required={true}
                        placeholder="Dni"
                        value={dni}
                        onChange={(event) => {
                            setDni(event.target.value)
                        }}
                    />
                    <input
                        style={styles.inputForm}
                        type="text"
                        name="legajo"
                        required={true}
                        placeholder="Legajo"
                        value={legajo}
                        onChange={(event) => {
                            setLegajo(event.target.value)
                        }}
                    />
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
                style={styles.signupButton}
                onClick={() =>
                    props.model.onClickSignUp(
                        dni,
                        legajo,
                        username,
                        password,
                        setErrorMessage,
                        goToLogin
                    )
                }
            >
                Sign Up
            </button>
        </VerticalStack>
    )
}

const BottomOptions = (): JSX.Element => {
    const styles: StyleMap = {
        bottomLinks: {
            width: '500px',
            alignSelf: 'center',
        },
        loginButton: {
            marginTop: '15px',
            fontStyle: 'normal',
            fontWeight: 'normal',
            fontSize: '25px',
            color: 'black',
            textDecoration: 'none',
            alignSelf: 'center',
        },
    }

    return (
        <VerticalStack style={styles.bottomLinks}>
            <Link style={styles.loginButton} to={'/acc/login'}>
                Already registered? Login
            </Link>
        </VerticalStack>
    )
}
