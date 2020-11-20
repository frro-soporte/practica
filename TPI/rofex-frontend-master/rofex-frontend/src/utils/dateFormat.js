import format from 'date-fns/format';
import es from 'date-fns/locale/es';

export default function (value, formatStr = 'PP') {
    const date = typeof value === 'string' ? new Date(value) : value;
    return format(date, formatStr, { locale: es });
}
