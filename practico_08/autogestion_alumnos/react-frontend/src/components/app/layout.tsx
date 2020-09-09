import * as React from 'react'

import { Colors, Dimensions } from 'style'
import { JustChildren, Style, StyleMap } from 'utils/tsTypes'
import { HorizontalStack } from 'common/components/flex'
import { Navigation } from 'components/navigation'
import { Cookies } from 'react-cookie/lib'

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

function AppContent(props: JustChildren): JSX.Element {
    return (
        <RelativePositionAppContent>
            {props.children}
        </RelativePositionAppContent>
    )
}

interface LayoutState {
    isSmallScreen: boolean
}

interface LayoutProps {
    cookies: Cookies
}

export class Layout extends React.Component<LayoutProps, LayoutState> {
    constructor(props: LayoutProps) {
        super(props)
    }

    render(): JSX.Element | null {
        const props = this.props

        const styles: StyleMap = {
            container: {
                width: '100%',
                height: '100%',
            },
            innerContainer: {
                position: 'relative',
                width: '100%',
                minHeight: '100%',
                margin: 'auto',
                height: 'auto',
            },
        }
        return (
            <div style={styles.container}>
                <div style={styles.innerContainer}>
                    <HorizontalStack>
                        <Navigation cookies={props.cookies} />
                        <AppContent>{props.children}</AppContent>
                    </HorizontalStack>
                </div>
            </div>
        )
    }
}
