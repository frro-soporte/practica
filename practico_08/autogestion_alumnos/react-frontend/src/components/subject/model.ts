import axios from 'axios'
import { SubjectType, SubjectsType } from './common'
import { processTasks } from '../task/model'
import { processTests } from 'components/test/model'

export {}

export class SubjectModel {
    constructor(private accessToken: string) {}

    getSubjects = async (
        setErrorMessage: (error: string) => void
    ): Promise<SubjectsType> => {
        const response = await this.tryToGetSubjects()

        if (response.status === 'ok') {
            const subjects = response.msg.subjects
            return this.parseSubjects(subjects)
        }
        if (response.msg === '') {
            setErrorMessage('Something went wrong, please try again')
            return []
        }
        return []
    }

    tryToGetSubjects = async (): Promise<{ msg: any; status: string }> => {
        const response = axios
            .get('/subjects', {
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

    getSubjectById = async (
        setErrorMessage: (error: string) => void,
        id: string
    ): Promise<SubjectType | null> => {
        const response = await this.tryToGetSubject(id)

        if (response.status === 'ok') {
            const subject = response.msg.subject as SubjectType
            return subject
        }
        if (response.msg === '') {
            setErrorMessage('Something went wrong, please try again')
            return null
        }
        return null
    }

    tryToGetSubject = async (
        id: string
    ): Promise<{ msg: any; status: string }> => {
        const response = axios
            .post(
                '/getsubject',
                {
                    id: id,
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

    parseSubjects = (subjectsBackend: any): SubjectType[] => {
        if (Array.isArray(subjectsBackend)) {
            return subjectsBackend.map((subject: any) => {
                return {
                    id: subject.id,
                    name: subject.name,
                    division: subject.division,
                    condition: subject.condition,
                    theoryDDHHHH: subject.theory_ddhhhh,
                    practiceDDHHHH: subject.practice_ddhhhh,
                    score: subject.score,
                    theoryProfessor: subject.theory_professor,
                    practiceProfessor: subject.practice_professor,
                    exams: processTests(subject.exams),
                    tasks: processTasks(subject.tasks),
                }
            })
        }
        return [
            {
                id: subjectsBackend.id,
                name: subjectsBackend.name,
                division: subjectsBackend.division,
                condition: subjectsBackend.condition,
                theoryDDHHHH: subjectsBackend.theory_ddhhhh,
                practiceDDHHHH: subjectsBackend.practice_ddhhhh,
                score: subjectsBackend.score,
                theoryProfessor: subjectsBackend.theory_professor,
                practiceProfessor: subjectsBackend.practice_professor,
                exams: processTests(subjectsBackend.exams),
                tasks: processTasks(subjectsBackend.tasks),
            },
        ]
    }

    tryToSaveSubject = async (
        name: string,
        division: string,
        condition: string,
        theoryDDHHHH: string,
        practiceDDHHHH: string,
        score: string,
        theoryProfessor: string,
        practiceProfessor: string,
        setErrorMessage: (value: string) => void
    ): Promise<SubjectsType> => {
        const response = await this.saveSubject(
            name,
            division,
            condition,
            theoryDDHHHH,
            practiceDDHHHH,
            score,
            theoryProfessor,
            practiceProfessor
        )

        if (response.status === 'ok') {
            const subject = response.msg
            return this.parseSubjects(subject)
        }
        if (response.msg === '') {
            setErrorMessage('Something went wrong, please try again')
            return []
        }
        setErrorMessage(response.msg)
        return []
    }

    saveSubject = async (
        name: string,
        division: string,
        condition: string,
        theoryDDHHHH: string,
        practiceDDHHHH: string,
        score: string,
        theoryProfessor: string,
        practiceProfessor: string
    ): Promise<{ msg: any; status: string }> => {
        const response = axios
            .post(
                '/subject',
                {
                    name: name,
                    division: division,
                    condition: condition,
                    theoryddhhhh: theoryDDHHHH,
                    practiceddhhhh: practiceDDHHHH,
                    score: score,
                    theory_professor: theoryProfessor,
                    practice_professor: practiceProfessor,
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
                    msg: response.data.subject || response.data.msg,
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
