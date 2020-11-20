const message = 'Las contraseñas tienen que coincidir.';

function validate(password, value) {
    // Valid required with required rule
    return value ? password === value : true;
}

export default password => value => validate(password, value) || message;
