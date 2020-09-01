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

        const response = await this.tryToLogin()

        if (response.status === 'ok') {
            this.cookies.set('access_token', response.msg.access_token)
            return goToDashboard()
        }
        if (response.msg === '') {
            setErrorMessage('Something went wrong, please try again')
            return
        }
        setErrorMessage(response.msg)
        return
    }

    tryToLogin = async (): Promise<{ msg: any; status: string }> => {
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
                return {
                    status: response.data.status,
                    msg: response.data.msg || response.data.data,
                }
            })
            .catch(() => {
                return {
                    status: 'error',
                    msg: '',
                }
            })
        return response
    }
}
