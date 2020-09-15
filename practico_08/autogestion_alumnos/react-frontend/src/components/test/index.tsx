import React, { useState, useCallback, useEffect } from 'react';
import { StyleMap, Style } from 'utils/tsTypes'
import { Cookies } from 'react-cookie/lib'
import { Layout } from 'components/app/layout'

export const Test = (props: { cookies: Cookies }): JSX.Element => {
    const general: Style = {
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
            <section style={general}>
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
            borderRadius: '25px',
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
            },
        noInput: {
            display: 'none',
        
        },
        inputOver:{
            height: '25px',
            width: '200px',
            borderWidth: 'small',
            borderColor: '#b3b3b3',
            boxShadow: '0 1px 1px rgba(0, 0, 0, 0.25)',
            fontSize: '14px',
            marginTop: '2%',
            marginBottom: '4%',
            borderRadius: '5px',
            display: 'flex',
        },
        addButton: {
            height: '30px',
            background: '#e91e63',
            borderWidth: 'small',
            borderColor: '#b3b3b3',
            boxShadow: '0 1px 1px rgba(0, 0, 0, 0.25)',
            color: 'white',
            fontSize: '14px',
            marginTop: '2%',
            marginBottom: '4%',
            float: 'right',
            borderRadius: '5px',
            cursor: 'pointer',
             }
            }

            const [styleNewTest, setStyleNewTest] = useState(styles.noInput)

            const onClick = useCallback(() => {
                setStyleNewTest(styles.inputOver)
            }, [])
        

    return (
        <div style={styles.box}>
            <h2 style={styles.subtitle} >Examenes</h2>
            <label style={styles.testLine}>
                <input type="checkbox" name="" ></input>
                <span style={styles.testDescription}>19/09/2020 Parcial Soporte</span>
            </label>
             <button onClick={onClick} style={styles.addButton}>Agregar Examen</button>
             <form  >
                <input style={styleNewTest} placeholder="Materia" name="subjectTest" />
                <input style={styleNewTest} placeholder="dd/mm/aa" name="dateTest" />
                <button style={styleNewTest}>Confirmar</button>
            </form> 
        </div>
    )
}
