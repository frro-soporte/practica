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
            background: '#2B2F32',
            border: '1px solid #000000',
            boxSizing: 'border-box',
        },
        whiteBox: {
            position: 'relative',
            margin: '5% auto',
            width: '450px',
            height: '550px',
            background: '#ffffff',
            display: 'flex',
            flexDirection: 'column',
            boxShadow: '10px 10px 10px rgba(0, 0, 0, 0.25)',
            borderRadius: '45px'
        },
        userIcon: {
            borderRadius: '50%',
            alignSelf: 'center',
            marginTop: '25px',
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
                <SignUpForm model={model} />
                <BottomOptions />
            </div>
        </div>
    )
}

const SignUpForm = (props: { model: SignUpModel }): JSX.Element => {
    const styles: StyleMap = {
        signUpForm: {
            marginTop: '100px',
            alignSelf: 'center',
        },
        inputForm: {
            marginTop: '45px',
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
        signupButton: {
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
            cursor: 'pointer',
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
            fontSize: '18px',
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
