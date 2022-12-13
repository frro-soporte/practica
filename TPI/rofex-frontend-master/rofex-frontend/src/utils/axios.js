import axios from 'axios';
import store from '../store/index';
import router from '../router/index';
//
// XXX  Cambiar desde .env.local o .env.production
const BASE_URL = process.env.VUE_APP_SERVER_API
    ? process.env.VUE_APP_SERVER_API
    : 'http://localhost:3000';

// axios defaults
// axios.defaults.timeout = 10000;
axios.defaults.baseURL = BASE_URL;
// axios.defaults.headers.post["X-Requested-With"] = "XMLHttpRequest";
axios.defaults.headers.post['Cache-Control'] = 'no-cache';
axios.defaults.headers.post['Content-Type'] = 'application/json';
// axios.defaults.headers.get["Content-Type"] = "application/x-www-form-urlencoded";
// axios.defaults.headers.get["Content-Type"] = "text/plain";
// axios.defaults.headers.common["Access-Control-Request-Headers"] = null;
// axios.defaults.headers.common["Access-Control-Request-Method"] = null;

// Add a request interceptor
axios.interceptors.request.use(
    function (config) {
        // Do something before request is sent
        if (store.state.token) {
            // `Bearer ${store.state.token}`;
            config.headers.authorization = store.state.token;
        }
        return config;
    },
    function (error) {
        // Do something with request error
        return Promise.reject(error);
    }
);

// Add a response interceptor
axios.interceptors.response.use(
    function (response) {
        // Do something with response data
        if (process.env.NODE_ENV === 'development') {
            console.info(
                '[INFO] -- axios -->',
                response.config.url,
                '\n',
                response
            );
        }
        const data =
            typeof response.data.data !== 'undefined'
                ? response.data.data
                : response.data
                ? response.data
                : {};
        const error = response.data.errors || null;
        const message = response.data.message || '';
        response.data = {
            data,
            error,
            message
        };
        const totalItems = response.headers['x-total-count'];
        if (typeof totalItems !== 'undefined') {
            response.data._totalItems = parseInt(totalItems, 10);
        }
        return response;
    },
    // https://github.com/axios/axios#handling-errors
    function ({ response }) {
        if (process.env.NODE_ENV === 'development') {
            console.error(
                '[ERROR] -- axios --> ',
                response.config.url,
                '\n',
                response
            );
        }
        // Do something with response error
        if (response) {
            const data =
                typeof response.data.data !== 'undefined'
                    ? response.data.data
                    : response.data
                    ? response.data
                    : {};
            const error =
                response.data.name === 'MongoError'
                    ? 'Error al guardar en mongoDB'
                    : response.data.errors || null;
            const { message } = response.data;

            switch (response.status) {
                case 401:
                case 403:
                    store.dispatch('auth/signOut');
                    router.replace('login');
                    break;
                default:
                    response.error = error;
                    response.message = message;
                    response.data = data;
                    break;
            }
        }
        return Promise.reject(response);
    }
);

export default axios;
