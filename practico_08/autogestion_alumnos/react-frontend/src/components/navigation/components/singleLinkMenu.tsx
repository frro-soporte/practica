import React from 'react'

import { Style } from '../../../utils/tsTypes'
import { TriggerIcon } from './menuEntry'
import { Link } from 'react-router-dom'

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
        width: 28,
        height: 28,
        marginBottom: 2,
        display: 'block',
        outline: 'none',
    }
    return (
        <Link to={'/app/dashboard/'} style={logo}>
            <svg /*logo*/ />
        </Link>
    )
}
