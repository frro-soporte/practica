const message = 'Characteres invalidos.';

function validate(val) {
    const reg = /^[A-ZÁÉÓÚÍÑ\d-_\s'()º]*$/i;

    return reg.test(String(val));
}

export default () => value => validate(value) || message;
