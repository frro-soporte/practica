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
        <Link to={'/app/dashboard/'} style={logo}>
            <img src={dashboard} style={logo}/>
        </Link>
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
        marginTop: '10px'

    }
    return (
        <Link to={'/app/task/'} style={logo}>
            <img src={task} style={logo}/>
        </Link>
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
        marginTop: '10px'

    }
    return (
        <Link to={'/app/subject/'} style={logo}>
            <img src={subject} style={logo}/>
        </Link>
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
        marginTop: '10px'

    }
    return (
        <Link to={'/app/test/'} style={logo}>
            <img src={test} style={logo}/>
        </Link>
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
        marginTop: '10px'

    }
    return (
        <Link to={'/app/calendar/'} style={logo}>
            <img src={calendar} style={logo}/>
        </Link>
    )
}

export function LogoutMenu(): JSX.Element {
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
        <Link to={'/app/logout/'} style={logo}>
            <img src={logout} style={logo}/>
        </Link>
    )
}