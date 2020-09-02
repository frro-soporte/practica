import axios from 'axios'
import {withCookies} from "react-cookie/lib";
import {withRouter} from "react-router";

export class SignUpModel {
    dni = ''
    legajo = ''
    username = ''
    password = ''

    onClickSignUp = async (
        dni: string,
        legajo: string,
        username: string,
        password: string,
        setErrorMessage: (error: string) => void,
        goToLogin: () => void
    ): Promise<void> => {
        this.dni = dni
        this.legajo = legajo
        this.username = username
        this.password = password
        setErrorMessage('')

        if (dni === '' || legajo === '' || username === '' || password === '') {
            setErrorMessage('Please complete all the fields and try again.')
            return
        }

        const response = await this.tryToSignUp()

        console.log(response)
        if (response.status === 'ok') {
            console.log('adentro del if status')
            return goToLogin()
        }
        if (response.msg === '') {
            setErrorMessage('Something went wrong, please try again')
            return
        }
        setErrorMessage(response.msg)
        return
    }

    tryToSignUp = async (): Promise<{ msg: any; status: string }> => {
        const response = axios
            .post(
                '/sign_up',
                {
                    userName: this.username,
                    password: this.password,
                    legajo: this.legajo,
                    dni: this.dni,
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
                    msg: response.data.msg || '',
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
