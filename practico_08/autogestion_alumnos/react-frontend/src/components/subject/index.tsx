import React, { useState, useCallback, useEffect } from 'react';
import { StyleMap, Style } from 'utils/tsTypes'
import { Cookies } from 'react-cookie/lib'
import { Layout } from 'components/app/layout'

export const Subject = (props: { cookies: Cookies }): JSX.Element => {
    const general: Style = {
        display: 'grid',
        gridTemplateColumns: '1fr',
        gridRow: '1fr',
        placeItems: 'center',
        alignItems: 'center',
        height: '100%',
        background: '#222',
        fontFamily: 'Arial',
        }

    return (
        <Layout cookies={props.cookies}>
            <section style={general}>
                <SubjectList />
            </section>
        </Layout>
    )
}

const SubjectList = (): JSX.Element => {
    const styles: StyleMap = {
        box: {
            padding: '35px',
            position: 'relative',
            background:  '#333',
            borderTop: '50px solid white',
            width: '60%',
            height: 'auto',
            paddingBottom: '60px',
            borderRadius: '25px',
        },
        title: {
            color: '#fff',
            fontSize: '30px',
            padding: '10px 0',
            borderBottom: '4px solid #fff',
            textAlign: 'center',
        },
        table: {
            color: 'black',
            fontSize: '13px',
            textAlign: 'left',
            width: '100%',
            backgroundColor: 'white',
            borderCollapse: 'collapse',
            
        },
        cells: {
            padding: '15px',
        },
        tableTitle: {
            color: 'white',
            backgroundColor: '#666',
            borderBottom: '5px solid #222',
         },
         noInput: {
            display: 'none',
        
        },
        inputOver:{
            height: '25px',
            width: '300px',
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
            marginTop: '4%',
            float: 'right',
            borderRadius: '5px',
            cursor: 'pointer',
         }
}

        const [styleNewSubject, setStyleNewSubject] = useState(styles.noInput)

        const onClick = useCallback(() => {
            setStyleNewSubject(styles.inputOver)
        }, [])


    return (
        <div style={styles.box}>
        <h2 style={styles.title}>Materias</h2>
        <table style={styles.table}>
            <thead style={styles.tableTitle}>
                <tr>
                    <th style={styles.cells}>Nombre</th><th>Profesor Teoria</th><th>Profesor Practica</th><th>Division</th><th>Condicion</th><th>Score</th>
                </tr>
            </thead>
            <tr>
                <td style={styles.cells}>Sopor</td><td>Profesor</td><td>Comision</td><td>Horario</td><td>Condicion</td>
            </tr>
            <tr>
                <td style={styles.cells}>Nombre</td><td>Profesor</td><td>Comision</td><td>Horario</td><td>Condicion</td>
            </tr>
            <tr>
                <td style={styles.cells}>Nombre</td><td>Profesor</td><td>Comision</td><td>Horario</td><td>Condicion</td>
            </tr>
            <tr>
                <td style={styles.cells}>Nombre</td><td>Profesor</td><td>Comision</td><td>Horario</td><td>Condicion</td>
            </tr>
        </table>
        <button onClick={onClick}  style={styles.addButton}>Nueva Materia</button>
        <form  >
            <input style={styleNewSubject} placeholder="Materia" name="subjectName" />
            <input style={styleNewSubject} placeholder="Profesor Teoria" name="theory_professor" />
            <input style={styleNewSubject} placeholder="Profesor Practica" name="practice" />
            <input style={styleNewSubject} placeholder="Division" name="division" />
            <input style={styleNewSubject} placeholder="Condicion" name="condition" />
            <button style={styleNewSubject}>Confirmar</button>
        </form> 
    </div>
    )
}
