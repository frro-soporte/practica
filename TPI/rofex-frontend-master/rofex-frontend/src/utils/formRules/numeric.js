const message = 'El campo solo puede tener numero.';

function validate(value) {
    // Valid required with required rule
    if (typeof value !== 'number' && !value) return true;
    return /^[0-9]+$/.test(String(value));
}

export default () => value => validate(value) || message;
