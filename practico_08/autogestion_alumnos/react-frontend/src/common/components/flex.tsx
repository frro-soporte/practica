import * as React from 'react'
import { MaybeVisible, Style } from 'utils/tsTypes'

type StackProps = React.DetailedHTMLProps<
    React.HTMLAttributes<HTMLDivElement>,
    HTMLDivElement
>

export function VerticalStack(props: StackProps): JSX.Element {
    const { style: divStyle, children, ...divProps } = props

    const style: Style = {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'stretch',
        ...divStyle,
    }

    return (
        <div style={style} {...divProps}>
            {children}
        </div>
    )
}

export function Space(): JSX.Element {
    const style: Style = {
        flex: 1,
    }

    return <div style={style} />
}

interface HorizontalGapProps {
    width: number
}

/**
 * This adds some horizontal space. Usually more flexible than using padding.
 */
export function HorizontalGap(props: HorizontalGapProps): JSX.Element {
    const style: Style = { width: props.width }

    return <div style={style} />
}

export function MaybeHorizontalGap(
    props: MaybeVisible<HorizontalGapProps>
): JSX.Element | null {
    if (!props.isVisible) {
        return null
    }

    return <HorizontalGap width={props.width} />
}

/**
 * This adds some vertical space. Usually more flexible than using padding.
 */
export function VerticalGap(props: { height: number }): JSX.Element {
    const style: Style = {
        height: props.height,
    }

    return <div style={style} />
}

export function HorizontalStack(props: StackProps): JSX.Element {
    const { style: divStyle, children, ...divProps } = props

    const style: Style = {
        display: 'flex',
        flexDirection: 'row',
        alignItems: 'stretch',
        justifyContent: 'space-between',
        ...divStyle,
    }

    return (
        <div style={style} {...divProps}>
            {children}
        </div>
    )
}

export function HorizontalCentered(props: StackProps): JSX.Element {
    const { style: divStyle, children, ...divProps } = props

    const style: Style = {
        justifyContent: 'center',
        alignItems: 'center',
        ...divStyle,
    }

    return (
        <HorizontalStack style={style} {...divProps}>
            {children}
        </HorizontalStack>
    )
}
