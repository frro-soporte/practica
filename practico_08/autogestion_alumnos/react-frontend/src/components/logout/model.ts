import axios from 'axios'
import { Cookies } from 'react-cookie/lib'

export class LogoutModel {
    cookies: Cookies

    constructor(cookies: Cookies) {
        this.cookies = cookies
    }

    onClickLogout = async (goToLogin: () => void): Promise<void> => {
        const response = await this.tryToLogout()

        if (response.status === 'ok') {
            this.cookies.remove('access_token', {
                path: '/',
            })
            return goToLogin()
        }
        return
    }

    tryToLogout = async (): Promise<{ status: string }> => {
        const token = this.cookies.get('access_token') as string
        const response = await axios
            .delete('/logout', {
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Bearer ${token}`,
                },
            })
            .then((response) => {
                return {
                    status: response.data.status,
                }
            })
            .catch(() => {
                return {
                    status: 'error',
                }
            })
        return response
    }
}
