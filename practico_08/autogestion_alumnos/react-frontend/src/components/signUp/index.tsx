import React from 'react'
import { StyleMap } from 'utils/tsTypes'
import { VerticalStack } from 'common/components/flex'

export const signUp = (): JSX.Element => {
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
        },
        loginButton: {
            marginTop: '15px',
            fontStyle: 'normal',
            fontWeight: 'normal',
            fontSize: '25px',
            color: 'black',
            textDecoration: 'none',
        },
        bottomLinks: {
            width: '500px',
            alignSelf: 'center',
        },
    }

    return (
        <div style={styles.background}>
            <div style={styles.whiteBox}>
                <div style={styles.userIcon} />
                <form style={styles.signUpForm} action="#" method="post">
                    <VerticalStack>
                        <input
                            style={styles.inputForm}
                            type="text"
                            name="dni"
                            required={true}
                            placeholder="Dni"
                        />
                        <input
                            style={styles.inputForm}
                            type="text"
                            name="legajo"
                            required={true}
                            placeholder="Legajo"
                        />
                        <input
                            style={styles.inputForm}
                            type="text"
                            name="userName"
                            required={true}
                            placeholder="Username"
                        />
                        <input
                            style={styles.inputForm}
                            type="password"
                            name="password"
                            required={true}
                            placeholder="Password"
                        />
                        <input
                            style={styles.signupButton}
                            type="submit"
                            value="SignUp"
                        />
                    </VerticalStack>
                </form>
                <VerticalStack style={styles.bottomLinks}>
                    <a style={styles.loginButton} href="/acc/login">
                        Already registered? Login
                    </a>
                </VerticalStack>
            </div>
        </div>
    )
}
