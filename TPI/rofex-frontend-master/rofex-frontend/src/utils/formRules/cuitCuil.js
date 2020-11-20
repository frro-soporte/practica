const regexp = /^(?:20|23|24|27|30|33|34)(?:\D)?[0-9]{8}(?:\D)?[0-9]$/;
const message = 'Cuil o cuit invalido';

function validate(value) {
    // Valid required with required rule
    if (!value) return true;

    const validRegExp = regexp.test(value);
    if (!validRegExp) return false;

    const sCUIT = value.replace(/[-//]/g, '');

    const aMult = '5432765432'.split('');
    if (sCUIT.length === 11) {
        const aCUIT = sCUIT.split('');
        let iResult = 0;
        for (let i = 0; i <= 9; i++) {
            iResult += aCUIT[i] * aMult[i];
        }
        iResult %= 11;
        iResult = 11 - iResult;
        if (iResult === 11) iResult = 0;
        if (iResult === 10) iResult = 9;
        return iResult === aCUIT[10];
    }
    return false;
}

export default () => value => validate(value) || message;
