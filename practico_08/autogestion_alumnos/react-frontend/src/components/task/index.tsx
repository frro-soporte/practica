import React, { useState, useCallback, useEffect } from 'react';
import { StyleMap, Style } from 'utils/tsTypes'
import { Cookies } from 'react-cookie/lib'
import { Layout } from 'components/app/layout'

export const Task = (props: { cookies: Cookies }): JSX.Element => {
    const general: Style = {
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
            <section style={general}>
                <TaskList />
            </section>
        </Layout>
    )
}

const TaskList = (): JSX.Element => {
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
        taskLine: {
            color: '#fff',
            fontSize: '17px',
            fontFamily: 'Arial',
            margin: '40px 0',
            display: 'block',
            cursor: 'pointer',
        },
        taskDescription: {
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

        const [styleNewTask, setStyleNewTask] = useState(styles.noInput)

        const onClick = useCallback(() => {
            setStyleNewTask(styles.inputOver)
        }, [])
    

    return (
        <div style={styles.box}>
            <h2 style={styles.subtitle} >Tareas</h2>
            <label style={styles.taskLine}>
                <input type="checkbox" name="" ></input>
                <span style={styles.taskDescription}>19/09/2020 TP Soporte</span>
            </label>
            <button onClick={onClick} style={styles.addButton}>Agregar Tarea</button> 
            <form  >
                <input style={styleNewTask} placeholder="Materia" name="subjectTask" />
                <input style={styleNewTask} placeholder="dd/mm/aa" name="dateTask" />
                <button style={styleNewTask}>Confirmar</button>
            </form> 
        </div>
    )
}
