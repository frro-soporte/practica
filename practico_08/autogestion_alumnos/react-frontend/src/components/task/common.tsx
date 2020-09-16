export type TasksType = TaskType[]

export interface TaskType {
    id: string
    description: string
    isDone: boolean
    date?: string
    score?: string
    subjectId: string
}
