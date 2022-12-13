import {
    parsePhoneNumberFromString,
    getCountryCallingCode
} from 'libphonenumber-js';

const message = 'El número no parece ser válido';

function validate(value) {
    const number = /^\+/.test(value) ? value : `+${value}`;
    const phoneNumber = parsePhoneNumberFromString(number) || {};
    // return phoneNumber.isPossible && phoneNumber.isPossible();
    return phoneNumber.isValid && phoneNumber.isValid();
}

export default function (county = 'AR') {
    const countyCode = getCountryCallingCode(county);
    return function (value) {
        const phoneNumber = countyCode + value;
        // Valid only number, not if field is required
        if (!value) return true;
        return (/^\+?\d+$/.test(value) && validate(phoneNumber)) || message;
    };
}
