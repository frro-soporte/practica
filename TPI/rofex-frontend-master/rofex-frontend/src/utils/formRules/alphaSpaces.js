const alphaSpaces = {
    // en: /^[A-Z\s]*$/i,
    es: /^[A-ZÁÉÍÑÓÚÜ\s]*$/i
    // pt: /^[A-ZÃÁÀÂÇÉÊÍÕÓÔÚÜ\s]*$/i
};

const message = 'El campo solo puede tener letras.';

export default (locale = 'es') => value =>
    alphaSpaces[locale].test(value) || message;
