const message = 'Al menos 6 caracteres, combinando letras y números.';

function validate(value) {
    // Valid required with required rule
    if (!value) return true;

    // generic password: upper-case, lower-case, number/special character, and min 8 characters
    const passwordValid = /^((?=.*\d)(?=.*[a-záéóúíñ])(?=.*[A-ZÁÉÓÚÍÑ])?(.*[@#$%!&?¡¿!])?.{6,30})$/;
    // const passwordValid = /^((?=.*\d)(?=.*[a-záéóúíñ])(?=.*[A-ZÁÉÓÚÍÑ])(.*[@#$%!&?¡¿!])?.{8,30})$/;
    return passwordValid.test(value);
}

export default () => value => validate(value) || message;
