import axios from 'axios'
import { TasksType, TaskType } from './common'

export class TaskModel {
    constructor(private accessToken: string) {}

    getTasks = async (
        setErrorMessage: (error: string) => void
    ): Promise<TasksType> => {
        const response = await this.tryToGetTasks()

        if (response.status === 'ok') {
            const tasks = response.msg.tasks
            return processTasks(tasks)
        }
        if (response.msg === '') {
            setErrorMessage('Something went wrong, please try again')
            return []
        }
        return []
    }

    tryToGetTasks = async (): Promise<{ msg: any; status: string }> => {
        const response = axios
            .get('/tasks', {
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

    tryToSaveTask = async (
        description: string,
        isDone: boolean,
        date: string,
        score: string,
        setErrorMessage: (value: string) => void,
        valueSelected: string
    ): Promise<TasksType> => {
        const response = await this.saveTask(
            description,
            isDone,
            date,
            score,
            valueSelected
        )

        if (response.status === 'ok') {
            const task = response.msg
            return processTasks(task)
        }
        if (response.msg === '') {
            setErrorMessage('Something went wrong, please try again')
            return []
        }
        setErrorMessage(response.msg)
        return []
    }

    saveTask = async (
        description: string,
        isDone: boolean,
        date: string,
        score: string,
        valueSelected: string
    ): Promise<{ msg: any; status: string }> => {
        const response = axios
            .post(
                '/task',
                {
                    description: description,
                    isDone: isDone,
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
                    msg: response.data.task || response.data.msg,
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

    tryToModifyTask = async (task: TaskType): Promise<boolean> => {
        const response = await this.changeTask(task)

        return response.status === 'ok'
    }

    changeTask = async (
        task: TaskType
    ): Promise<{ msg: any; status: string }> => {
        const response = axios
            .put(
                '/task',
                {
                    id: task.id,
                    description: task.description,
                    isDone: task.isDone,
                    date: task.date,
                    score: task.score,
                    subjectId: task.subjectId,
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

export const processTasks = (tasks: any): TasksType => {
    if (Array.isArray(tasks)) {
        return tasks.map((task: any) => {
            const isDone = task.is_done === 'true' || task.is_done === 'True'
            return {
                date: task.date,
                description: task.description,
                id: task.id,
                isDone: isDone,
                score: task.score,
                subjectId: task.subject_id,
            }
        })
    }
    const isDone = tasks.is_done === 'true' || tasks.is_done === 'True'
    return [
        {
            date: tasks.date,
            description: tasks.description,
            id: tasks.id,
            isDone: isDone,
            score: tasks.score,
            subjectId: tasks.subject_id,
        },
    ]
}
