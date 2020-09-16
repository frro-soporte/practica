import React from 'react'

import { Style } from 'utils/tsTypes'
import { TriggerIcon } from './menuEntry'
import { Link } from 'react-router-dom'
import calendar from 'common/img/calendar-logo.png'
import task from 'common/img/task-logo.png'
import test from 'common/img/test-logo.png'
import subject from 'common/img/subject-logo.png'
import dashboard from 'common/img/home-logo.png'
import logout from 'common/img/logout-logo.png'
import { Logout } from '../../logout'
import { Cookies } from 'react-cookie/lib'
import Tooltip from '@material-ui/core/Tooltip'

interface SingleLinkMenuProps {
    routeName: string
    icon: string
}

export function SingleLinkMenu(props: SingleLinkMenuProps): JSX.Element {
    const style: Style = {
        outline: 'none',
    }
    const path = props.routeName
    return (
        <Link to={path} style={style}>
            <TriggerIcon icon={props.icon} />
        </Link>
    )
}

export function DashboardMenu(): JSX.Element {
    const logo = {
        maxWidth: '40px',
        maxHeight: '40px',
        marginBottom: 2,
        display: 'block',
        outline: 'none',
        cursor: 'pointer',
        alignSelf: 'center',
    }
    return (
        <Tooltip title="Dashboard" placement="right">
            <Link to={'/app/dashboard/'} style={logo}>
                <img src={dashboard} style={logo} />
            </Link>
        </Tooltip>
    )
}

export function TaskMenu(): JSX.Element {
    const logo = {
        maxWidth: '40px',
        maxHeight: '40px',
        marginBottom: 2,
        display: 'block',
        outline: 'none',
        cursor: 'pointer',
        alignSelf: 'center',
        marginTop: '10px',
    }
    return (
        <Tooltip title="Task" placement="right">
            <Link to={'/app/task/'} style={logo}>
                <img src={task} style={logo} />
            </Link>
        </Tooltip>
    )
}

export function SubjectMenu(): JSX.Element {
    const logo = {
        maxWidth: '40px',
        maxHeight: '40px',
        marginBottom: '30px',
        display: 'block',
        outline: 'none',
        cursor: 'pointer',
        alignSelf: 'center',
        marginTop: '10px',
    }
    return (
        <Tooltip title="Subject" placement="right">
            <Link to={'/app/subject/'} style={logo}>
                <img src={subject} style={logo} />
            </Link>
        </Tooltip>
    )
}

export function TestMenu(): JSX.Element {
    const logo = {
        maxWidth: '40px',
        maxHeight: '40px',
        marginBottom: 2,
        display: 'block',
        outline: 'none',
        cursor: 'pointer',
        alignSelf: 'center',
        marginTop: '10px',
    }
    return (
        <Tooltip title="Exam" placement="right">
            <Link to={'/app/test/'} style={logo}>
                <img src={test} style={logo} />
            </Link>
        </Tooltip>
    )
}

export function CalendarMenu(): JSX.Element {
    const logo = {
        maxWidth: '40px',
        maxHeight: '40px',
        marginBottom: 2,
        display: 'block',
        outline: 'none',
        cursor: 'pointer',
        alignSelf: 'center',
        marginTop: '10px',
    }
    return (
        <Tooltip title="Calendar" placement="right">
            <Link to={'/app/calendar/'} style={logo}>
                <img src={calendar} style={logo} />
            </Link>
        </Tooltip>
    )
}

export function LogoutMenu(props: { cookies: Cookies }): JSX.Element {
    const logo = {
        maxWidth: '40px',
        maxHeight: '40px',
        marginBottom: 2,
        display: 'block',
        outline: 'none',
        cursor: 'pointer',
        alignSelf: 'center',
    }
    return (
        <Logout cookies={props.cookies} style={logo}>
            <Tooltip title="LogOut" placement="right">
                <img src={logout} style={logo} />
            </Tooltip>
        </Logout>
    )
}
