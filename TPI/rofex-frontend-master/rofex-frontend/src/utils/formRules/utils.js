export const isNullOrUndefined = value => {
    return value === null || value === undefined;
};

export const isEmptyArray = arr => {
    return Array.isArray(arr) && arr.length === 0;
};
