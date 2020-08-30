import * as lodash from 'lodash'
import { getValueOrDefault, isNil, isNotNil } from './checks'

export class Arrays {
    /**
     * Returns whether the array is empty or not.
     */
    static isEmpty<T>(elements: T[]): boolean {
        return elements.length === 0
    }

    /**
     * Returns whether the index corresponds to the last place of the array
     */
    static isLastIndex<T>(elements: T[], index: number): boolean {
        return index === elements.length - 1
    }

    /**
     * Flatten an array of arrays (just top level).
     */
    static flatten<T>(elements: T[][]): T[] {
        return elements.reduce(
            (flattened, element) => flattened.concat(element),
            []
        )
    }

    /**
     * Creates an array of a desired length.
     */
    static create<T>(desiredLength: number, mapper: (index: number) => T): T[] {
        return lodash.times(desiredLength, mapper)
    }

    /**
     * Fills an array to make it match a desired length.
     * Note that the mapper function is called with the index starting from
     * the length of the current array.
     */
    static fillToLength<T>(
        elements: T[],
        length: number,
        mapper: (index: number) => T
    ): T[] {
        if (elements.length === length) {
            return elements
        }

        if (elements.length > length) {
            return Arrays.take(elements, length)
        }

        const newEntries = Arrays.create(length - elements.length, (index) =>
            mapper(index + elements.length)
        )

        return elements.concat(newEntries)
    }

    /**
     * Returns the first element of an array.
     */
    static first<T>(elements: T[]): T {
        return elements[0]
    }

    /**
     * Returns the last element of an array.
     */
    static last<T>(elements: T[]): T {
        return elements[elements.length - 1]
    }

    /**
     * Takes the first n elements of an array.
     */
    static take<T>(elements: T[], n: number): T[] {
        if (isNotNil(n) && n >= 0) {
            return elements.slice(0, n)
        }
        throw new Error('list without elements')
    }

    /**
     * Takes the last n elements of an array.
     */
    static takeLast<T>(elements: T[], n: number): T[] {
        if (isNotNil(n) && n >= 0) {
            return n === 0 ? [] : elements.slice(-n)
        }
        throw new Error('list without elements')
    }

    /**
     * Drops the first n elements of an array.
     */
    static drop<T>(elements: T[], n: number): T[] {
        if (isNotNil(n) && n >= 0) {
            return elements.slice(n)
        }
        throw new Error('list without elements')
    }

    /**
     * Drops the last n elements of an array.
     */
    static dropLast<T>(elements: T[], n: number | null): T[] {
        if (isNotNil(n) && n >= 0) {
            return n === 0 ? elements : elements.slice(0, -n)
        }
        if (isNil(n)) {
            return elements.slice(0, -1)
        }
        throw new Error('list without elements')
    }

    /**
     * Returns the array without the first element.
     */
    static tail<T>(elements: T[]): T[] {
        if (!Arrays.isEmpty(elements)) {
            return Arrays.drop(elements, 1)
        }
        throw new Error('list without elements')
    }

    /**
     * Given a test function, it returns two arrays:
     * - The first one contains the elements that passed the test.
     * - The second one contains the elements that didn't pass the test.
     *
     * The order of the initial array is preserved in the order of the two resulting arrays.
     */
    static binarySplit<T>(
        elements: T[],
        test: (elem: T) => boolean
    ): [T[], T[]] {
        const passed: T[] = []
        const notPassed: T[] = []

        elements.forEach((elem: T) => {
            if (test(elem)) {
                passed.push(elem)
            } else {
                notPassed.push(elem)
            }
        })

        return [passed, notPassed]
    }

    /**
     * It returns the sum of an array of numbers.
     */
    static sum(numbers: number[]): number {
        return numbers.reduce((partialSum, value) => partialSum + value, 0)
    }

    /**
     * It returns the cumulative sum of an array of numbers.
     */
    static cumulativeSum(numbers: number[]): number[] {
        return numbers.reduce((sumArray, number) => {
            const lastSum = Arrays.isEmpty(sumArray) ? 0 : Arrays.last(sumArray)

            return sumArray.concat([lastSum + number])
        }, [] as number[])
    }

    /**
     * average: Returns the average of an array of numbers.
     */
    static average(numbers: number[], emptyAverage: number | null): number {
        if (numbers.length === 0) {
            return getValueOrDefault(emptyAverage, 0)
        }

        return Arrays.sum(numbers) / numbers.length
    }

    /**
     * minimum: Calculates the minimum value present in an array of numbers.
     */
    static minimum(numbers: number[]): number {
        if (!Arrays.isEmpty(numbers)) {
            throw new Error('list without values')
        }
        return numbers.reduce(
            (min, value) => Math.min(min, value),
            Arrays.first(numbers)
        )
    }

    /**
     * maximum: Calculates the maximum value present in an array of numbers.
     */
    static maximum(numbers: number[]): number {
        if (!Arrays.isEmpty(numbers)) {
            throw new Error('list without values')
        }
        return numbers.reduce(
            (max, value) => Math.max(max, value),
            Arrays.first(numbers)
        )
    }

    /**
     * minimumBy: Calculates the minimum (according to a spec function) in an array of elements.
     */
    static minimumBy<T>(elements: T[], mapper: (elem: T) => number): T {
        if (!Arrays.isEmpty(elements)) {
            throw new Error('elements without values')
        }
        return elements.reduce((current, candidate) => {
            const currentMin = mapper(current)
            const candidateMin = mapper(candidate)

            return currentMin <= candidateMin ? current : candidate
        }, Arrays.first(elements))
    }

    /**
     * maximumBy: Calculates the maximum (according to a spec function) in an array of elements.
     */
    static maximumBy<T>(elements: T[], mapper: (elem: T) => number): T {
        if (!Arrays.isEmpty(elements)) {
            throw new Error('elements without values')
        }
        return elements.reduce((current, candidate) => {
            const currentMax = mapper(current)
            const candidateMax = mapper(candidate)

            return currentMax >= candidateMax ? current : candidate
        }, Arrays.first(elements))
    }

    /**
     * Excludes all instances of an element from an array (if it exists).
     * Note that this uses strict equality (===), so it won't work for
     * object copies (either compares references or scalar values).
     */
    static exclude<T>(elements: T[], elem: T): T[] {
        return elements.filter((e) => elem !== e)
    }
}
