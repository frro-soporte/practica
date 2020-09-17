import axios from 'axios'
import { TestsType, TestType } from './common'

export class TestModel {
    constructor(private accessToken: string) {}

    getTests = async (
        setErrorMessage: (error: string) => void
    ): Promise<TestsType> => {
        const response = await this.tryToGetTests()

        if (response.status === 'ok') {
            const tests = response.msg.exams
            return processTests(tests)
        }
        if (response.msg === '') {
            setErrorMessage('Something went wrong, please try again')
            return []
        }
        return []
    }

    tryToGetTests = async (): Promise<{ msg: any; status: string }> => {
        const response = axios
            .get('/exams', {
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Bearer ${this.accessToken}`,
                },
            })
            .then((response) => {
                return {
                    status: response.data.status,
                    msg: response.data.msg || response.data.data,
                }
            })
            .catch(() => {
                return {
                    status: 'error',
                    msg: '',
                }
            })
        return await response
    }

    tryToSaveTest = async (
        description: string,
        date: string,
        score: string,
        setErrorMessage: (value: string) => void,
        valueSelected: string
    ): Promise<TestsType> => {
        const response = await this.saveTest(
            description,
            date,
            score,
            valueSelected
        )

        if (response.status === 'ok') {
            const test = response.msg
            return processTests(test)
        }
        if (response.msg === '') {
            setErrorMessage('Something went wrong, please try again')
            return []
        }
        setErrorMessage(response.msg)
        return []
    }

    saveTest = async (
        description: string,
        date: string,
        score: string,
        valueSelected: string
    ): Promise<{ msg: any; status: string }> => {
        const response = axios
            .post(
                '/exam',
                {
                    description: description,
                    date: date,
                    score: score,
                    subjectId: valueSelected,
                },
                {
                    headers: {
                        'Content-Type': 'application/json',
                        Authorization: `Bearer ${this.accessToken}`,
                    },
                }
            )
            .then((response) => {
                return {
                    status: response.data.status,
                    msg: response.data.exam || response.data.msg,
                }
            })
            .catch(() => {
                return {
                    status: 'error',
                    msg: '',
                }
            })
        return await response
    }

    tryToModifyTest = async (test: TestType): Promise<boolean> => {
        const response = await this.changeTest(test)

        return response.status === 'ok'
    }

    changeTest = async (
        test: TestType
    ): Promise<{ msg: any; status: string }> => {
        const response = axios
            .put(
                '/exam',
                {
                    id: test.id,
                    description: test.description,
                    date: test.date,
                    score: test.score,
                    subjectId: test.subjectId,
                },
                {
                    headers: {
                        'Content-Type': 'application/json',
                        Authorization: `Bearer ${this.accessToken}`,
                    },
                }
            )
            .then((response) => {
                return {
                    status: response.data.status,
                    msg: response.data,
                }
            })
            .catch(() => {
                return {
                    status: 'error',
                    msg: '',
                }
            })
        return await response
    }
}

export const processTests = (tests: any): TestsType => {
    console.log(tests)
    if (Array.isArray(tests)) {
        return tests.map((test: any) => {
            return {
                date: test.date,
                description: test.description,
                id: test.id,
                score: test.score,
                subjectId: test.subject_id,
            }
        })
    }
    return [
        {
            date: tests.date,
            description: tests.description,
            id: tests.id,
            score: tests.score,
            subjectId: tests.subject_id,
        },
    ]
}
