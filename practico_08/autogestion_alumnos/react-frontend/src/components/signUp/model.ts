import axios from 'axios'

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

        if (response.status === 'ok') {
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
