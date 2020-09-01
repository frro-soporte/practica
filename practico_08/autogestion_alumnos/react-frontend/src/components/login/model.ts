import axios from 'axios'
import { isNil } from 'utils/checks'
import { Cookies } from 'react-cookie/lib'

export class LoginModel {
    username = ''
    password = ''
    cookies: Cookies

    constructor(cookies: Cookies) {
        this.cookies = cookies
    }

    onClickLogin = async (
        username: string,
        password: string,
        setErrorMessage: (error: string) => void,
        goToDashboard: () => void
    ): Promise<void> => {
        this.username = username
        this.password = password
        setErrorMessage('')

        if (username === '' || password === '') {
            setErrorMessage('Please complete all the fields and try again.')
            return
        }

        const maybeAuthorization = await this.tryToLogin()
        if (isNil(maybeAuthorization)) {
            setErrorMessage(
                'Something went wrong, please check your information and try again'
            )
            return
        }
        this.cookies.set('access_token', maybeAuthorization)
        return goToDashboard()
    }

    tryToLogin = async (): Promise<string> => {
        const response = axios
            .post(
                '/login',
                {
                    userName: this.username,
                    password: this.password,
                },
                {
                    headers: {
                        'Content-Type': 'application/json',
                    },
                }
            )
            .then((response) => {
                return response.data.msg.access_token
            })
            .catch(() => {
                return null
            })
        return response
    }
}
