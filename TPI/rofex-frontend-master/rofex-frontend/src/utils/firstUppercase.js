export default value => {
    if (!value || typeof value !== 'string') return '';
    return value[0].toUpperCase() + value.substr(1);
};
