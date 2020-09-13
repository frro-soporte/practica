import React from 'react'
import { StyleMap, Style } from 'utils/tsTypes'
import { Cookies } from 'react-cookie/lib'
import { Layout } from 'components/app/layout'

export const Test = (props: { cookies: Cookies }): JSX.Element => {
    const style: Style = {
        margin: '0',
        padding: '0',
        display: 'grid',
        gridTemplateColumns: '1fr',
        gridRow: '1fr',
        placeItems: 'center',
        alignItems: 'center',
        width: '100%',
        height: '100%',
        background: '#222',
    }

    return (
        <Layout cookies={props.cookies}>
            <section style={style}>
                <TestList />
            </section>
        </Layout>
    )
}

const TestList = (): JSX.Element => {
    const styles: StyleMap = {
        box: {
            padding: '40px 75px 10px 30px',
            position: 'relative',
            background: '#333',
            borderTop: '50px solid white',
            width: '350px',
        },
        subtitle: {
            color: '#fff',
            fontSize: '30px',
            padding: '1px 0',
            marginLeft: '20px',
            borderBottom: '4px solid #fff',
            textAlign: 'center',
            marginTop: '0px',
        },
        testLine: {
            color: '#fff',
            fontSize: '17px',
            fontFamily: 'Arial',
            margin: '40px 0',
            display: 'block',
            cursor: 'pointer',
        },
        testDescription: {
            position: 'relative',
            left: '20px',
            transition: '0.6s',
    return (
        <div style={styles.box}>
            <h2 style={styles.subtitle} >Examenes</h2>
            <label style={styles.testLine}>
                <input type="checkbox" name="" ></input>
                <span style={styles.testDescription}>19/09/2020 Parcial Soporte</span>
            </label>
        </div>
    )
}
