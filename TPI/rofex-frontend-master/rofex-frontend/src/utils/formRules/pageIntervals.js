const message = 'Secuencia de paginas incorrecta.';

function validate(value, countPage = 1) {
    if (!value) return 'Campo requerido.';

    // Valida que tenga números y guiones y coma
    const { length } = countPage.toString();
    const validRegExp = new RegExp(`^(?:[,-]?[0-9]{1,${length}})*$`).test(
        value
    );
    if (!validRegExp) return 'Formato invalido.';
    // Valida que todo los numero sean menores al anterior y al total de hojas
    const valid = value
        .replace(/-/g, ',') // 1,2,4,7,10-20,22,25-30 => "1,2,4,7,10,20,23,25,30"
        .split(',') // 1,2,4,7,10,20,22,25,30 => [1,2,4,7,10,20,23,25,30]
        .map(ele => parseInt(ele, 10))
        .reduce((acc, ele) => {
            if (acc === false || ele <= 0 || ele > countPage) return false;
            return acc <= ele ? ele : false;
        }, 0);
    return valid && valid <= countPage;
}

// export default (value, { params = [], message = message }) =>
//   validate(value, ...params) || message;
export default countPage => value => validate(value, countPage) || message;
