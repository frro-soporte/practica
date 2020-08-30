/* Common style constants used throughout react components.
 * Mostly used to mitigate the constants duplication that inlining styles
 * would normally produce.
 * */

const InfoColors = {
    good: {
        lighter: '#A8E1DA',
        light: '#72DABC',
        base: '#00B9A1',
        dark: '#007A6A',
    },
    bad: {
        lighter: '#FFA476',
        light: '#FF9483',
        base: '#E55553',
        dark: '#B74141',
    },
    warning: {
        lighter: '#FCF0E1',
        light: '#FFDD81',
        base: '#F5B236',
        dark: '#E88C00',
    },
    neutral1: {
        light: '#C7DDE4',
        base: '#A0B8BF',
        dark: '#70878E',
    },
    neutral2: {
        light: '#8DD0EC',
        base: '#56A5C4',
        dark: '#2C6F89',
    },
    neutral3: {
        light: '#CB97CA',
        base: '#A76DB2',
        dark: '#6F477C',
    },
    white: '#FFFFFF',
} as const

function buildColorChoicesList(): string[] {
    const goodColors = InfoColors.good
    const neutral2Colors = InfoColors.neutral2
    const warningColors = InfoColors.warning
    const neutral1Colors = InfoColors.neutral1
    const neutral3Colors = InfoColors.neutral3
    const badColors = InfoColors.bad

    const colorsList = [
        goodColors,
        neutral2Colors,
        warningColors,
        neutral1Colors,
        neutral3Colors,
        badColors,
    ]

    const baseColors = colorsList.map((color) => color.base)
    const darkColors = colorsList.map((color) => color.dark)
    const lightColors = colorsList.map((color) => color.light)

    return [...baseColors, ...darkColors, ...lightColors]
}

export const Colors = {
    grey: {
        opaque: 'rgb(33,50,59)',
        a100: 'rgba(33,50,59,1)',
        a90: 'rgba(33,50,59,.9)',
        a80: 'rgba(33,50,59,.8)',
        a70: 'rgba(33,50,59,.7)',
        a60: 'rgba(33,50,59,.6)',
        a50: 'rgba(33,50,59,.5)',
        a40: 'rgba(33,50,59,.4)',
        a30: 'rgba(33,50,59,.3)',
        a20: 'rgba(33,50,59,.2)',
        a10: 'rgba(33,50,59,.1)',
    },
    info: InfoColors,
    choices: buildColorChoicesList(),
    label: {
        white: '#FFFFFF',
        dark1: '#21323B',
        dark2: '#0E4049',
        dark3: '#325c64', // used in sub-menu links
        grey1: '#7A848A',
        grey2: '#4A5860',
        grey3: '#647076', // used in file input
        blue1: '#2F7E8D',
        table1: '#4E5B63',
        logo: '#20323C',
    },
    background: {
        light1: '#FFFFFF',
        light2: '#F6F7F8',
        light3: '#F2F4F5',
        light4: '#E0E6E9',
        light5: '#F9FAFA',
        light6: '#F4FCFA',
        dark1: '#162831',
        table1: '#FFFFFF',
        table2: '#F7F8F9',
        table3: '#F4F6F6',
        table4: '#EEF1F2',
        filters: '#EBEDEE',
        filters2: '#E8EAEB',
        lightBlue1: '#DAEFF7',
        tableSelected: '#D0E4ED',
        regularCell: '#3E666D',
        selectedCell: '#F2F8FB',
        menu1: '#588691', // expanded menu entry background
        menu2: '#2E6672', // disabled menu entry background
        menu3: '#105562', // main menu background
        menu4: '#143e48', // default menu entry background
    },
    shadow: {
        light: 'rgba(0,0,0,0.12)',
        light2: 'rgba(0,0,0,0.2)',
    },
    lines: {
        line1: '#C8D5D9',
        line2: '#A4B6B9',
        border1: '#CFD7D9',
        border2: '#E4E9EA',
        border3: '#D3DDDF',
        table: '#D4DADC',
        white: '#FFFFFF',
        graphGrey: '#B6BEC2',
        underline: '#69cef5',
        darkUnderline: '#F2F4F5',
        dark1: '#21323B', // used to separate logo from entries in the menu
        active: '#00B9A1', // used in borders of active menu/sub-menu entries
        selectedCellBorder: '#0E4049',
    },
    retain: {
        paymentRecovery: {
            effectiveness: '#CAE9F1',
            switch: '#56A5C4',
        },
        churnPrevention: {
            effectiveness: '#E0D4E3',
            switch: '#A76DB2',
        },
        disabled: {
            effectiveness: '#DEE5E6',
            switch: '#E8EEF0',
        },
    },
    primary: {
        light: '#F2F4F5',
        mid: '#5D8889',
        dark1: '#162831',
        dark2: '#114E50',
        accent: '#00B9A1',
    },
} as const

const twelfthColumnMargin = 20

const fullWidth = 1280
const navWidth = 60

export const Dimensions = {
    fonts: {
        spacing1: '.75px',
        weight1: 600,
        menuSize: 16,
        menuGroupSize: 14,
    },
    width: {
        content: fullWidth - navWidth,
        nav: navWidth,
        navEntry: 36,
        full: fullWidth,
        box: 996,
        boxPadding: 28,
        modalContent: 665,
        halfWidthCard: 489,
        tableFilter: 280,
        narrowScreenThreshold: 1250,
    },
    height: {
        menu: 56,
        spacing: 46,
        chart: 370,
        smallChart: 240,
        navEntry: 36,
        navTitle: 57,
        customersTable: {
            row: 64,
            header: 46,
        },
        topBanner: 53,
        shortScreenThreshold: 700,
    },
    margins: {
        contentTop: twelfthColumnMargin,
        contentBottom: twelfthColumnMargin,
        largeContentBottom: 90,
        contentLeft: twelfthColumnMargin,
        contentRight: twelfthColumnMargin,
        cardsHorizontalSpacing: twelfthColumnMargin,
        cardsVerticalSpacing: twelfthColumnMargin,
    },
} as const

/**
 * Shared colors for different selections.
 */
export const SELECTION_COLOR_PALETTE = [
    '#484E7C',
    '#577AC3',
    '#57A4C3',
    '#59C0BB',
    '#A7DBCF',
]

export const Texts = {
    h1: {
        color: Colors.grey.a100,
        fontSize: 32,
        fontWeight: 500,
    },
    h2: {
        color: Colors.grey.a100,
        fontSize: 28,
        fontWeight: 500,
    },
    h3: {
        color: Colors.grey.a100,
        fontSize: 20,
        fontWeight: 500,
    },
    p: {
        color: Colors.grey.a70,
        fontSize: 14,
        fontWeight: 400,
    },
    label: {
        color: Colors.grey.a40,
        fontSize: 14,
        fontWeight: 500,
        letterSpacing: '0.75px',
        textTransform: 'uppercase',
    },
} as const
