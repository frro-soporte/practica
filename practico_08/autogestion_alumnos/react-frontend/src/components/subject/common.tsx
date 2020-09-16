import { TasksType } from '../task/common'

export type SubjectsType = [] | SubjectType[]
export interface SubjectType {
    id: string
    name: string
    division: string
    condition: string
    theoryDDHHHH?: string
    practiceDDHHHH?: string
    score?: string
    theoryProfessor?: string
    practiceProfessor?: string
    exams: any[] //TODO: type this!!!
    tasks: TasksType[]
}
