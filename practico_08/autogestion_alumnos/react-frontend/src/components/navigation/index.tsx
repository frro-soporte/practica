import * as React from 'react'

import { JustChildren, Style } from 'utils/tsTypes'
import { Colors, Dimensions } from 'style'
import { VerticalStack } from 'common/components/flex'
import { EntrySeparator } from './components/menuEntry'
import {
    DashboardMenu,
    CalendarMenu,
    TaskMenu,
    TestMenu,
    SubjectMenu,
    LogoutMenu,
} from './components/singleLinkMenu'
import { Cookies } from 'react-cookie/lib'

function StaticPositionMainContainer(props: JustChildren): JSX.Element {
    const style: Style = {
        background: '#333',
        color: Colors.primary.light,
        height: '100%',
        width: Dimensions.width.nav,
        flex: `0 0 ${Dimensions.width.nav}px`,
    }
    return <VerticalStack style={style}>{props.children}</VerticalStack>
}

function MainContainer(props: JustChildren): JSX.Element {
    return (
        <StaticPositionMainContainer>
            {props.children}
        </StaticPositionMainContainer>
    )
}

function StaticPositionNavContainer(props: JustChildren): JSX.Element {
    const style: Style = {
        display: 'block',
        width: Dimensions.width.nav,
        minHeight: 690,
        border: `3px solid #000000`,
    }
    return <div style={style}>{props.children}</div>
}

function NavigationContainer(props: JustChildren): JSX.Element {
    return (
        <StaticPositionNavContainer>
            {props.children}
        </StaticPositionNavContainer>
    )
}

function TopContainer(props: JustChildren): JSX.Element {
    const style: Style = {
        borderBottom: `3px solid #000000`,
    }
    return <VerticalStack style={style}>{props.children}</VerticalStack>
}

function MiddleContainer(props: JustChildren): JSX.Element {
    return <VerticalStack>{props.children}</VerticalStack>
}

function BottomContainer(props: JustChildren): JSX.Element {
    const justifyContent = 'flex-start'
    const style: Style = {
        justifyContent,
        borderTop: `3px solid #000000`,
    }
    return <VerticalStack style={style}>{props.children}</VerticalStack>
}

/**
 * Navigation bar
 */

export function Navigation(props: { cookies: Cookies }): JSX.Element {
    return (
        <NavigationContainer>
            <MainContainer>
                <TopContainer>
                    <EntrySeparator style={{ flexBasis: 12 }} />
                    <DashboardMenu />
                    <EntrySeparator style={{ flexBasis: 10 }} />
                </TopContainer>
                <MiddleContainer>
                    <EntrySeparator />
                    <CalendarMenu />
                    <EntrySeparator />
                    <TaskMenu />
                    <EntrySeparator />
                    <TestMenu />
                    <EntrySeparator />
                    <SubjectMenu />
                    <EntrySeparator />
                </MiddleContainer>
                <BottomContainer>
                    <EntrySeparator style={{ flexBasis: 10 }} />
                    <LogoutMenu cookies={props.cookies} />
                    <EntrySeparator style={{ flexBasis: 12 }} />
                </BottomContainer>
            </MainContainer>
        </NavigationContainer>
    )
}
