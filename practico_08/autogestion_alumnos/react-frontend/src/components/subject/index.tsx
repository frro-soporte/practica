import React, { useState, useCallback, useEffect } from 'react';
import { StyleMap, Style } from 'utils/tsTypes'
import { Cookies } from 'react-cookie/lib'
import { Layout } from 'components/app/layout'
import { SubjectModel } from './model'
import { SubjectsType, SubjectType } from './common'
import { HorizontalStack, VerticalStack } from '../../common/components/flex'
import { getValueOrDefault } from '../../utils/checks'

export const Subject = (props: { cookies: Cookies }): JSX.Element => {
    const accessToken = props.cookies.get('access_token')
    const [errorMessage, setErrorMessage] = useState('')

    /*
     * SubjectModel
     */
    const subjectModel = new SubjectModel(accessToken)
    const emptySubjects: SubjectsType = []
    const [subjects, setSubjects] = useState(emptySubjects)

    const loadSubjects = useCallback(async () => {
        const backendSubjects = await subjectModel.getSubjects(setErrorMessage)
        setSubjects(backendSubjects)
    }, [setSubjects])



    const saveSubject = useCallback(
        async (
            name: string,
            division: string,
            condition: string,
            theoryDDHHHH: string,
            practiceDDHHHH: string,
            score: string,
            theoryProfessor: string,
            practiceProfessor: string,
            setErrorMessage: (value: string) => void,
            cleanScreen: () => void
        ) => {
            const savedSubject: SubjectsType = await subjectModel.tryToSaveSubject(
                name,
                division,
                condition,
                theoryDDHHHH,
                practiceDDHHHH,
                score,
                theoryProfessor,
                practiceProfessor,
                setErrorMessage,
            )
            if (savedSubject.length === 0) {
                return
            }
            setSubjects(subjects.concat(savedSubject))
            cleanScreen()
            
        },
        [setSubjects, subjects]
    )


    /*
     * Load the information
     */
    useEffect(() => {
        void loadSubjects()
    }, [loadSubjects])


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
                <SubjectList 
                    accessToken={accessToken}
                    subjects={subjects}
                    tryToSaveSubject={saveSubject}     
                />
            </section>
        </Layout>
    )
}

const SubjectList = (props: {
    subjects: SubjectsType
    accessToken: string
    tryToSaveSubject: (
        name: string,
        division: string,
        condition: string,
        theoryDDHHHH: string,
        practiceDDHHHH: string,
        score: string,
        theoryProfessor: string,
        practiceProfessor: string,
        setErrorMessage: (value: string) => void,
        cleanScreen: () => void
    ) => void
}): JSX.Element => {
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

        const [isAddSubjectClicked, setIsAddSubjectClicked] = useState(false)

        const onClick = useCallback(() => {
            setIsAddSubjectClicked(true)
        }, [setIsAddSubjectClicked])
        
         const subjectsSelected = props.subjects

        const subjectRow = subjectsSelected.map((subject) => {
            return (
                <tr>
                    <th style={styles.cells}>{subject.name}</th><th>{subject.theoryProfessor}</th><th>{subject.practiceProfessor}</th><th>{subject.division}</th><th>{subject.condition}</th><th>{subject.score}</th>
                </tr>
            )
        })

        return (
            <div style={styles.box}>
            <h2 style={styles.title}>Materias</h2>
            <table style={styles.table}>
                <thead style={styles.tableTitle}>
                    <tr>
                        <th style={styles.cells}>Nombre</th><th>Profesor Teoria</th><th>Profesor Practica</th><th>Division</th><th>Condicion</th><th>Score</th>
                    </tr>
                </thead>
                {subjectRow}
            </table>
            <button onClick={onClick} style={styles.addButton}>
                Agregar Materia
            </button>
            <MaybeSubjectForm
                isAddSubjectClicked={isAddSubjectClicked}
                onCancel={() => setIsAddSubjectClicked(false)}
                tryToSaveSubject={props.tryToSaveSubject}
            />
        </div>
        )
    }
interface MaybeSubjectFormProps {
        isAddSubjectClicked: boolean
        onCancel: () => void
        tryToSaveSubject: (
            name: string,
            division: string,
            condition: string,
            theoryDDHHHH: string,
            practiceDDHHHH: string,
            score: string,
            theoryProfessor: string,
            practiceProfessor: string,
            setErrorMessage: (value: string) => void,
            cleanScreen: () => void
        ) => void
    }
const MaybeSubjectForm = (props: MaybeSubjectFormProps): JSX.Element | null => {
        const [errorMessage, setErrorMessage] = useState('')
        const [name, setName] = useState('')
        const [division, setDivision] = useState('')
        const [condition, setCondition] = useState('')
        const [score, setScore] = useState('')
        const [theoryDDHHHH, setTheoryDDHHHH] = useState('')
        const [practiceDDHHHH, setPracticeDDHHHH] = useState('')
        const [practiceProfessor, setPracticeProfessor] = useState('')
        const [theoryProfessor, setTheoryProfessor] = useState('')

        const onCancel = (): void => {
            setErrorMessage('')
            setName('')
            setDivision('')
            setCondition('')
            setScore('')
            setTheoryDDHHHH('')
            setPracticeDDHHHH('')
            setPracticeProfessor('')
            setTheoryProfessor('')
            props.onCancel()
        }
    
        const onConfirm = (): void => {
            if ((name === '')||(division === '')) {
                setErrorMessage('Nombre o division vacios')
                return
            }
            props.tryToSaveSubject(
                name,
                division,
                condition,
                theoryDDHHHH,
                practiceDDHHHH,
                score,
                theoryProfessor,
                practiceProfessor,
                setErrorMessage,
                onCancel
            )
            return
        }
    
        if (!props.isAddSubjectClicked) {
            return null
        }
        const styles: StyleMap = {
            input: {
                height: '25px',
                width: '80%',
                borderWidth: 'small',
                borderColor: '#b3b3b3',
                boxShadow: '0 1px 1px rgba(0, 0, 0, 0.25)',
                fontSize: '14px',
                marginTop: '2%',
                marginBottom: '4%',
                borderRadius: '5px',
                display: 'flex',
            },
            confirm: {
                height: '30px',
                background: '#75cb64',
                borderWidth: 'small',
                borderColor: '#b3b3b3',
                boxShadow: '0 1px 1px rgba(0, 0, 0, 0.25)',
                color: 'white',
                fontSize: '14px',
                marginTop: '2%',
                marginBottom: '4%',
                borderRadius: '5px',
                cursor: 'pointer',
                textAlign: 'center',
                width: '100%',
            },
            cancel: {
                height: '30px',
                background: '#cb6464',
                borderWidth: 'small',
                borderColor: '#b3b3b3',
                boxShadow: '0 1px 1px rgba(0, 0, 0, 0.25)',
                color: 'white',
                fontSize: '14px',
                marginTop: '2%',
                marginBottom: '4%',
                borderRadius: '5px',
                cursor: 'pointer',
                textAlign: 'center',
                width: '100%',
            },
        }
    
        return (
            <VerticalStack style={{ marginTop: '50px' }}>
                <input
                    style={styles.input}
                    placeholder="Nombre Materia*"
                    name="name"
                    value={name}
                    onChange={(event) => {
                        setName(event.target.value)
                    }}
                />
                <HorizontalStack style={{ color: 'white', alignSelf: 'start' }}>
                    <input
                        style={styles.input}
                        placeholder="Division*"
                        name="division"
                        value={division}
                        onChange={(event) => {
                            setDivision(event.target.value)
                        }}
                    />
                </HorizontalStack>
                    <input
                        style={styles.input}
                        placeholder="Hora de practica"
                        name="practiceDDHHHH"
                        value={practiceDDHHHH}
                        onChange={(event) => {
                            setPracticeDDHHHH(event.target.value)
                        }}
                    />
                    <input
                        style={styles.input}
                        placeholder="Hora de teoria"
                        name="theoryDDHHHH"
                        value={theoryDDHHHH}
                        onChange={(event) => {
                            setTheoryDDHHHH(event.target.value)
                        }}
                    />
                    <input
                        style={styles.input}
                        placeholder="Profesor de practica"
                        name="practiceProfessor"
                        value={practiceProfessor}
                        onChange={(event) => {
                            setPracticeProfessor(event.target.value)
                        }}
                    />
                    <input
                        style={styles.input}
                        placeholder="Profesor de teoria"
                        name="theoryProfessor"
                        value={theoryProfessor}
                        onChange={(event) => {
                            setTheoryProfessor(event.target.value)
                        }}
                    />
                    <input
                        style={styles.input}
                        placeholder="Condicion"
                        name="condition"
                        value={condition}
                        onChange={(event) => {
                            setCondition(event.target.value)
                        }}
                    />
                {errorMessage}
                <HorizontalStack>
                    <button style={styles.confirm} onClick={onConfirm}>
                        Confirmar
                    </button>
                    <button style={styles.cancel} onClick={onCancel}>
                        Cancelar
                    </button>
                </HorizontalStack>
            </VerticalStack>
        )
    }