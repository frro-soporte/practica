import React, { Fragment, useCallback, useEffect, useState } from 'react'
import Select from 'react-select'
import { Style, StyleMap } from 'utils/tsTypes'
import { Cookies } from 'react-cookie/lib'
import { Layout } from 'components/app/layout'
import { TestModel } from './model'
import { TestsType, TestType } from './common'
import { SubjectModel } from '../subject/model'
import { SubjectsType, SubjectType } from '../subject/common'
import { HorizontalStack, VerticalStack } from '../../common/components/flex'
import { getValueOrDefault } from '../../utils/checks'

export const Test = (props: { cookies: Cookies }): JSX.Element => {
    const accessToken = props.cookies.get('access_token')
    const [errorMessage, setErrorMessage] = useState('')

    /*
     * TestModel
     */
    const model = new TestModel(accessToken)
    const emptyTests: TestsType = []
    const [tests, setTests] = useState(emptyTests)

    const loadTests = useCallback(async () => {
        const backendTests = await model.getTests(setErrorMessage)
        setTests(backendTests)
    }, [setTests])

    const saveTest = useCallback(
        async (
            description: string,
            date: string,
            score: string,
            setErrorMessage: (value: string) => void,
            valueSelected: string,
            cleanScreen: () => void
        ) => {
            const savedTest = await model.tryToSaveTest(
                description,
                date,
                score,
                setErrorMessage,
                valueSelected
            )
            if (savedTest.length === 0) {
                return
            }
            setTests(tests.concat(savedTest))
            cleanScreen()
        },
        [setTests, tests]
    )

    const tryToSaveTestWithEffect = (
        description: string,
        date: string,
        score: string,
        setErrorMessage: (value: string) => void,
        valueSelected: string,
        cleanScreen: () => void
    ) => {
        void saveTest(
            description,
            date,
            score,
            setErrorMessage,
            valueSelected,
            cleanScreen
        )
    }

    const changeTest = useCallback(
        async (test: TestType) => {
            const saved = await model.tryToModifyTest(test)
            if (saved) {
                const newTests = tests.map((testArray) => {
                    if (testArray.id === test.id) {
                        testArray = test
                    }
                    return testArray
                })
                setTests(newTests)
                return true
            }
            return false
        },
        [setTests, tests]
    )

    const tryToChangeTestWithEffect = async (
        test: TestType
    ): Promise<boolean> => {
        return await changeTest(test)
    }

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

    /*
     * Load the information
     */
    useEffect(() => {
        void loadTests()
        void loadSubjects()
    }, [loadTests, loadSubjects])

    /*
     * Rendering
     */
    const general: Style = {
        margin: '0',
        padding: '0',
        display: 'flex',
        gridTemplateColumns: '1fr',
        gridRow: '1fr',
        placeItems: 'center',
        alignItems: 'center',
        width: '100%',
        height: '100%',
        background: '#222',
    }

    const dropdown: Style = {
        width: '350px',
        marginTop: '50px',
        marginBottom: '50px',

    }
    const title: Style = {
        marginTop: '5%',
        textAlign: 'center',
        color: 'white',
        fontSize: '20px',
        fontFamily: 'Arial'
    }

    const [isOptionSelected, setIsOptionSelected] = useState(false)
    const [valueSelected, setValueSelected] = useState('')
    const isDropdownDisabled = subjects.length === 0
    const onOptionSelected = useCallback(
        (maybeValue: any) => {
            const value = getValueOrDefault(maybeValue, { value: '' })
            setValueSelected(value.value)
            setIsOptionSelected(value.value !== '')
        },
        [setIsOptionSelected, setValueSelected]
    )

    return (
        <Layout cookies={props.cookies}>
            <VerticalStack style={general}>
                <label style={title}>Seleccione una materia:</label>
                <Dropdown
                    style={dropdown}
                    isDisabled={isDropdownDisabled}
                    subjects={subjects}
                    onChange={onOptionSelected}
                />
                <label style={title}>{errorMessage}</label>
                <MaybeTestList
                    tests={tests}
                    accessToken={accessToken}
                    isOptionSelected={isOptionSelected}
                    valueSelected={valueSelected}
                    tryToSaveTestWithEffect={tryToSaveTestWithEffect}
                    tryToChangeTestWithEffect={tryToChangeTestWithEffect}
                />
            </VerticalStack>
        </Layout>
    )
}

const MaybeTestList = (props: {
    tests: TestsType
    accessToken: string
    isOptionSelected: boolean
    valueSelected: string
    tryToSaveTestWithEffect: (
        description: string,
        date: string,
        score: string,
        setErrorMessage: (value: string) => void,
        valueSelected: string,
        cleanScreen: () => void
    ) => void
    tryToChangeTestWithEffect: (test: TestType) => Promise<boolean>
}): JSX.Element | null => {
    if (props.isOptionSelected) {
        return (
            <TestList
                tests={props.tests}
                accessToken={props.accessToken}
                valueSelected={props.valueSelected}
                tryToSaveTestWithEffect={props.tryToSaveTestWithEffect}
                tryToChangeTestWithEffect={props.tryToChangeTestWithEffect}
            />
        )
    }
    return null
}

const TestList = (props: {
    tests: TestsType
    accessToken: string
    valueSelected: string
    tryToSaveTestWithEffect: (
        description: string,
        date: string,
        score: string,
        setErrorMessage: (value: string) => void,
        valueSelected: string,
        cleanScreen: () => void
    ) => void
    tryToChangeTestWithEffect: (test: TestType) => Promise<boolean>
}): JSX.Element => {
    const styles: StyleMap = {
        box: {
            padding: '40px 40px 10px 30px',
            position: 'relative',
            background: '#333',
            borderTop: '50px solid white',
            width: '350px',
            borderRadius: '25px',
            marginBottom: '25px'
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
            borderRadius: '5px',
            cursor: 'pointer',
            textAlign: 'center',
            width: '100%',
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
    }
    const [isAddTestClicked, setIsAddTestClicked] = useState(false)

    const onClick = useCallback(() => {
        setIsAddTestClicked(true)
    }, [setIsAddTestClicked])

    const onModify = (test: TestType): Promise<boolean> =>
        props.tryToChangeTestWithEffect(test)

    const testsSelected = props.tests.filter(
        (test) => test.subjectId === props.valueSelected
    )

    const testsRow = testsSelected.map((test) => {
        return (
            <label key={test.id} style={styles.testLine}>
                <span style={styles.testDescription}>
                    {test.description}
                    {'  '}
                    {test.date}
                    {'   '}
                    {test.score}
                </span>
            </label>
        )
    })

    return (
        <div style={styles.box}>
            <h2 style={styles.subtitle}>Examenes</h2>
            {testsRow}
            <div onClick={onClick} style={styles.addButton}>
                Agregar Examen
            </div>
            <MaybeTestForm
                isAddTestClicked={isAddTestClicked}
                onCancel={() => setIsAddTestClicked(false)}
                valueSelected={props.valueSelected}
                tryToSaveTestWithEffect={props.tryToSaveTestWithEffect}
            />
        </div>
    )
}

interface MaybeTestFormProps {
    valueSelected: string
    isAddTestClicked: boolean
    onCancel: () => void
    tryToSaveTestWithEffect: (
        description: string,
        date: string,
        score: string,
        setErrorMessage: (value: string) => void,
        valueSelected: string,
        cleanScreen: () => void
    ) => void
}

const MaybeTestForm = (props: MaybeTestFormProps): JSX.Element | null => {
    const [errorMessage, setErrorMessage] = useState('')
    const [description, setDescription] = useState('')
    const [date, setDate] = useState('')
    const [score, setScore] = useState('')

    const onCancel = (): void => {
        setErrorMessage('')
        setDescription('')
        setDate('')
        setScore('')
        props.onCancel()
    }

    const onConfirm = (): void => {
        if (description === '') {
            setErrorMessage('Titulo de examen vacio')
            return
        }
        props.tryToSaveTestWithEffect(
            description,
            date,
            score,
            setErrorMessage,
            props.valueSelected,
            onCancel
        )
        return
    }

    if (!props.isAddTestClicked) {
        return null
    }
    const styles: StyleMap = {
        input: {
            height: '25px',
            width: '100%',
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
            padding: '5px',
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
            padding: '5px',
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
                placeholder="Titulo examen*"
                name="description"
                value={description}
                onChange={(event) => {
                    setDescription(event.target.value)
                }}
            />
            <input
                style={styles.input}
                placeholder="DD/MM/AA"
                name="date"
                value={date} // TODO: please parse the data using: https://momentjs.com/docs/#/parsing/ IN EVERY PLACE THAT WE SHOW IT
                onChange={(event) => {
                    setDate(event.target.value)
                }}
            />
            <input
                style={styles.input}
                placeholder="Score"
                name="score"
                value={score}
                onChange={(event) => {
                    setScore(event.target.value)
                }}
            />
            {errorMessage}
            <HorizontalStack>
                <div style={styles.confirm} onClick={onConfirm}>
                    Confirmar
                </div>
                <div style={styles.cancel} onClick={onCancel}>
                    Cancelar
                </div>
            </HorizontalStack>
        </VerticalStack>
    )
}

interface DropdownProps {
    isDisabled: boolean
    subjects: SubjectType[]
    style: Style
    onChange: (value: any) => void
}

const Dropdown = (props: DropdownProps): JSX.Element => {
    const options = props.subjects.map((subject: SubjectType) => {
        return {
            label: subject.name,
            value: subject.id,
        }
    })
    return (
        <div style={props.style}>
            <Fragment>
                <Select
                    className="basic-single"
                    classNamePrefix="select"
                    isDisabled={false}
                    isClearable={true}
                    isSearchable={true}
                    name="Subjects"
                    options={options}
                    onChange={props.onChange}
                />
            </Fragment>
        </div>
    )
}
