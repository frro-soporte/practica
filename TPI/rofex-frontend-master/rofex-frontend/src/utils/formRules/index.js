// https://github.com/logaretm/vee-validate/tree/master/src/rules
// https://vuetifyjs.com/en/components/forms#validation-with-submit-clear
// https://github.com/validatorjs/validator.js
// import isLength from "validator/lib/isLength";

import alpha_num from './alphaNum';
import alpha_spaces from './alphaSpaces';
import alpha_spaces_num_lodash from './alphaSpacesNumLodash';
import cash from './cash';
import email from './email';
import lapsetext from './lapsetext';
import numeric from './numeric';
import decimal from './decimal';
import page_intervals from './pageIntervals';
import password from './password';
import password_equal from './passwordEqual';
// import phone_number from "./phoneNumber";
import required from './required';
import required_if from './requiredIf';
import cuit_cuil from './cuitCuil';
import latitude_longitude from './latitudeLongitude';
import { between, max, min } from './lengthRules';

export default {
    alpha_num,
    alpha_spaces,
    alpha_spaces_num_lodash,
    between,
    cash,
    cuit_cuil,
    email,
    decimal,
    lapsetext,
    max,
    min,
    numeric,
    page_intervals,
    password,
    // phone_number,
    password_equal,
    required,
    required_if,
    latitude_longitude
};
