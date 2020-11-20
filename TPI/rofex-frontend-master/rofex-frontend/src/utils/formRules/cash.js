const cashValid = /^([1-9]{1}\d*|0)([,.]\d{1,2})?$/;
// const message = "El campo solo puede un moto valido.";
const message = 'Monto no valido.';

function validate(value) {
    // Valid required with required rule
    if (!value) return true;
    return cashValid.test(String(value));
}

export default () => value => validate(value) || message;
