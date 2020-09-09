import React, { useCallback } from 'react'
import { Cookies } from 'react-cookie/lib'
import { useHistory } from 'react-router-dom'
import { LogoutModel } from 'components/logout/model'
import { JustChildren, Style } from '../../utils/tsTypes'

interface LogoutProps extends JustChildren {
    cookies: Cookies
    style: Style
}

export const Logout = (props: LogoutProps): JSX.Element => {
    const model = new LogoutModel(props.cookies)
    const history = useHistory()
    const goToLogin = useCallback(() => {
        history.push('/acc/login')
    }, [])
    return (
        <div onClick={() => model.onClickLogout(goToLogin)} style={props.style}>
            {props.children}
        </div>
    )
}
