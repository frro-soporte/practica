const message = 'El campo invalido.';

function validate(decimalDigit = '1,2', value) {
    // console.log(decimalDigit);
    // Valid required with required rule
    if (!value) return true;
    const re = new RegExp(`^-?\\d+(?:[\\.,]\\d{${decimalDigit}})?$`);
    return re.test(String(value));
}

export default decimalDigit => value =>
    validate(decimalDigit, value) || message;
