import React, { useCallback, useState } from 'react'
import { StyleMap, Style } from 'utils/tsTypes'
import { Cookies } from 'react-cookie/lib'
import {Redirect, Switch, useHistory} from 'react-router-dom'
import { Layout } from 'components/app/layout'
import calendar from 'common/img/calendar-logo.png'
import task from 'common/img/task-logo.png'
import test from 'common/img/test-logo.png'
import subject from 'common/img/subject-logo.png'

export const Dashboard = (props: { cookies: Cookies }): JSX.Element => {
    const style: Style = {
        background: '#222',
        display: 'flex',
        position: 'absolute',
        textAlign: 'center',
        verticalAlign: 'middle',
        width: '100%',
        height: '100%',
        overflowY: 'hidden',
        alignContent: 'center',
    }

    if (!props.cookies.get('access_token')) {
        return (
            <Switch>
                <Redirect to={'/app'} push={true} />
            </Switch>
        )
    }

    return (
        <Layout cookies={props.cookies}>
            <section style={style}>
                <Calendar />
                <Task />
                <Test />
                <Subject />
            </section>
        </Layout>
    )
}

const Calendar = (): JSX.Element => {
    const menu = {
        name: 'Calendario ',
        description: 'Seleccionar calendario con fechas importantes',
        foto: calendar,
    }
    return (
        <Menu
            name={menu.name}
            description={menu.description}
            foto={menu.foto}
            toWhere={'calendar'}
        />
    )
}
const Task = (): JSX.Element => {
    const menu = {
        name: 'Tareas ',
        description: 'Seleccionar lista con las proximas tareas',
        foto: task,
    }
    return (
        <Menu
            name={menu.name}
            description={menu.description}
            foto={menu.foto}
            toWhere={'task'}
        />
    )
}
const Test = (): JSX.Element => {
    const menu = {
        name: 'Examenes ',
        description: 'Seleccionar lista con los proximos examenes',
        foto: test,
    }
    return (
        <Menu
            name={menu.name}
            description={menu.description}
            foto={menu.foto}
            toWhere={'test'}
        />
    )
}
const Subject = (): JSX.Element => {
    const menu = {
        name: 'Materias ',
        description: 'Seleccionar lista con las materias',
        foto: subject,
    }
    return (
        <Menu
            name={menu.name}
            description={menu.description}
            foto={menu.foto}
            toWhere={'subject'}
        />
    )
}
interface MenuProps {
    name: string
    description: string
    foto: string
    toWhere: string
}

const Menu = (props: MenuProps): JSX.Element => {
    const styles: StyleMap = {
        item: {
            background: '#333',
            padding: '20px',
            display: 'grid',
            transition: '0.8s',
            height: '220px',
            width: '210px',
            marginTop: '180px',
            marginLeft: '35px',
            marginRight: '35px',
            borderRadius: '45px',
            cursor: 'pointer',
        },
        itemOver: {
            background: '#e91e63',
            transform: 'translateY(20px)',
            padding: '20px',
            display: 'grid',
            transition: '0.8s',
            height: '220px',
            width: '210px',
            marginTop: '180px',
            marginLeft: '35px',
            marginRight: '35px',
            cursor: 'pointer',
            borderRadius: '45px',
        },
        text: {
            color: '#fff',
            textAlign: 'center',
            fontSize: '22px',
            marginTop: '0px',
        },
        img: {
            display: 'block',
            margin: ' auto',
            maxWidth: '110px',
            marginBottom: '10px',
        },
        description: {
            color: '#fff',
            textAlign: 'center',
            fontSize: '17px',
            marginBottom: '25px',
            marginTop: '0px',
        },
    }

    const history = useHistory()
    const [styleMenu, setStyleMenu] = useState(styles.item)

    const onMouseOver = useCallback(() => {
        setStyleMenu(styles.itemOver)
    }, [])

    const onMouseOut = useCallback(() => {
        setStyleMenu(styles.item)
    }, [])

    const onClick = useCallback(() => {
        history.push(`/app/${props.toWhere}`)
    }, [])

    return (
        <div
            style={styleMenu}
            onMouseOver={onMouseOver}
            onMouseOut={onMouseOut}
            onClick={onClick}
        >
            <img style={styles.img} src={props.foto} alt={props.name} />
            <h1 style={styles.text}>{props.name}</h1>
            <p style={styles.description}>{props.description}</p>
        </div>
    )
}
