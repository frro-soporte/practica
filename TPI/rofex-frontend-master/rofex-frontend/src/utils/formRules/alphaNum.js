const alphaNumeric = {
    // en: /^[0-9A-Z]*$/i,
    es: /^[0-9A-ZÁÉÍÑÓÚÜ]*$/i
    // pt: /^[0-9A-ZÃÁÀÂÇÉÊÍÕÓÔÚÜ]*$/i
};
const defaultMessage = 'El campo solo puede tener letras y numeros.';

export default ({ locale, message } = {}) => value =>
    alphaNumeric[locale || 'es'].test(value) || message || defaultMessage;
