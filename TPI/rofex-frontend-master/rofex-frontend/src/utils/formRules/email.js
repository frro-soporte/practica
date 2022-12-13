// eslint-disable-next-line
const emailValid = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
const message = 'El debe ser un correo electrónico válido.';

function validate(value) {
    // Valid required with required rule
    if (!value) return true;
    return emailValid.test(value);
}

export default () => value => validate(value) || message;
