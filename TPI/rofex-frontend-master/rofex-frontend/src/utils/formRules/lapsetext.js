const message = 'Characteres invalidos.';

function validate(val) {
    // eslint-disable-next-line
    const reg = /^[A-ZÁÉÓÚÍÑ\d-_\s'()\[\]$%&=?¿<>,\.]*$/i;
    return reg.test(String(val));
}

export default () => value => validate(value) || message;
