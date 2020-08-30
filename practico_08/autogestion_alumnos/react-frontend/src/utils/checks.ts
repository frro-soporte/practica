/**
 * Preconditions, based on the guava module, is comprised of utility methods for
 * runtime checks.
 * There's not a lot of knowledge in these functions, just a common way of expressing these checks
 * As an example of the intent, note that checkArgument and checkState both check a boolean
 * expression and throw if it's not met. The function name and the name of the error thrown
 * provide us more information about the intent of that call.
 *
 * https://github.com/google/guava/wiki/PreconditionsExplained
 */

/**
 * The nil type represents either a null or undefined value.
 */
export type nil = null | undefined

// Whether a value is nil (null|undefined) or not
export function isNil(ref: any): ref is nil {
    return ref === null || ref === undefined
}

// Whether a value is not nil (or not)
export function isNotNil<T>(ref: T | nil): ref is T {
    return !isNil(ref)
}

export function getValueOrDefault<T>(value: T | nil, defaultValue: T): T {
    return isNil(value) ? defaultValue : value
}
