import * as React from 'react'

import { Colors, Dimensions } from 'style'
import { JustChildren, Style, StyleMap } from 'utils/tsTypes'
import { HorizontalStack } from 'common/components/flex'
import { Navigation } from 'navigation'

class ScrollContainer extends React.Component<JustChildren> {
    private htmlRef: HTMLElement | null
    constructor(props: JustChildren) {
        super(props)
        this.htmlRef = null
    }

    setHTMLRef(ref: HTMLElement | null): void {
        this.htmlRef = ref
    }

    render(): JSX.Element {
        const style: Style = {
            width: '100%',
            height: '100%',
            overflowY: 'scroll',
        }

        return (
            <div ref={(ref) => this.setHTMLRef(ref)} style={style}>
                {this.props.children}
            </div>
        )
    }
}

function AbsolutePositionAppContent(props: JustChildren): JSX.Element {
    const style: Style = {
        backgroundColor: Colors.background.light3,
        display: 'block',
        position: 'absolute',
        top: 0,
        left: Dimensions.width.nav,
        width: Dimensions.width.content,
        minHeight: '100%',
        height: 'auto',
        boxShadow: '5px 0 20px -15px',
    }
    return <div style={style}>{props.children}</div>
}

function RelativePositionAppContent(props: JustChildren): JSX.Element {
    const style: Style = {
        backgroundColor: Colors.background.light3,
        display: 'block',
        position: 'relative',
        width: Dimensions.width.content + Dimensions.width.nav,
        minHeight: '100%',
        height: 'auto',
        boxShadow: '5px 0 20px -15px',
    }
    return <div style={style}>{props.children}</div>
}

interface AppContentProps extends JustChildren {
    isSmallScreen: boolean
}

function AppContent(props: AppContentProps): JSX.Element {
    if (props.isSmallScreen) {
        return (
            <RelativePositionAppContent>
                {props.children}
            </RelativePositionAppContent>
        )
    }
    return (
        <AbsolutePositionAppContent>
            {props.children}
        </AbsolutePositionAppContent>
    )
}

interface LayoutState {
    isSmallScreen: boolean
}

export class Layout extends React.Component<any, LayoutState> {
    private match: MediaQueryList

    constructor(props: any) {
        super(props)
        this.match = window.matchMedia(
            `(max-height:${Dimensions.height.shortScreenThreshold}px)`
        )
        this.state = {
            isSmallScreen: this.match.matches,
        }
    }

    componentDidMount(): void {
        this.match.addListener(this.setWidthScreen)
    }

    componentWillUnmount(): void {
        this.match.removeListener(this.setWidthScreen)
    }

    setWidthScreen = (e: MediaQueryListEvent): void => {
        this.setState({ isSmallScreen: e.matches })
    }

    render(): JSX.Element | null {
        const props = this.props
        const isSmallScreen = this.state.isSmallScreen

        const styles: StyleMap = {
            container: {
                width: '100%',
                height: '100%',
            },
            innerContainer: {
                position: 'relative',
                width: Dimensions.width.full,
                minHeight: '100%',
                margin: 'auto',
                height: 'auto',
            },
        }
        return (
            <div style={styles.container}>
                <ScrollContainer>
                    <div style={styles.innerContainer}>
                        <HorizontalStack>
                            <Navigation isSmallScreen={isSmallScreen} />
                            <AppContent isSmallScreen={isSmallScreen}>
                                {props.children}
                            </AppContent>
                        </HorizontalStack>
                    </div>
                </ScrollContainer>
            </div>
        )
    }
}
