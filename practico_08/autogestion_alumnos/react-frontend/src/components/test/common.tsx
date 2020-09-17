export type TestsType = TestType[]

export interface TestType {
    id: string
    description: string
    subjectId: string
    date?: string
    score?: string
}
