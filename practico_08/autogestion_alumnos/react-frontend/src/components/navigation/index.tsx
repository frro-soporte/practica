import * as React from 'react'

import { JustChildren, Style } from '../../utils/tsTypes'
import { Colors, Dimensions } from '../../style'
import { VerticalStack } from '../../common/components/flex'
import { EntrySeparator } from './components/menuEntry'
import {DashboardMenu} from "./components/singleLinkMenu";

function StaticPositionMainContainer(props: JustChildren): JSX.Element {
    const style: Style = {
        background: Colors.background.menu3,
        color: Colors.primary.light,
        height: '100%',
        width: Dimensions.width.nav,
        flex: `0 0 ${Dimensions.width.nav}px`,
    }
    return <VerticalStack style={style}>{props.children}</VerticalStack>
}

function FixedPositionMainContainer(props: JustChildren): JSX.Element {
    const style: Style = {
        background: Colors.background.menu3,
        color: Colors.primary.light,
        position: 'fixed',
        top: 0,
        bottom: 0,
        width: Dimensions.width.nav,
        flex: `0 0 ${Dimensions.width.nav}px`,
    }
    return <VerticalStack style={style}>{props.children}</VerticalStack>
}

type ContainerProps = JustChildren & ScreenSizeProps

interface ScreenSizeProps {
    isSmallScreen: boolean
}

function MainContainer(props: ContainerProps): JSX.Element {
    if (props.isSmallScreen) {
        return (
            <StaticPositionMainContainer>
                {props.children}
            </StaticPositionMainContainer>
        )
    }
    return (
        <FixedPositionMainContainer>
            {props.children}
        </FixedPositionMainContainer>
    )
}

function AbsolutePositionNavContainer(props: JustChildren): JSX.Element {
    const style: Style = {
        display: 'block',
        position: 'absolute',
        top: 0,
        left: 0,
        width: Dimensions.width.nav,
        minHeight: '100%',
        zIndex: 100,
    }
    return <div style={style}>{props.children}</div>
}

function StaticPositionNavContainer(props: JustChildren): JSX.Element {
    const style: Style = {
        display: 'block',
        width: Dimensions.width.nav,
        minHeight: 690,
    }
    return <div style={style}>{props.children}</div>
}

function NavigationContainer(props: ContainerProps): JSX.Element {
    if (props.isSmallScreen) {
        return (
            <StaticPositionNavContainer>
                {props.children}
            </StaticPositionNavContainer>
        )
    }
    return (
        <AbsolutePositionNavContainer>
            {props.children}
        </AbsolutePositionNavContainer>
    )
}

function TopContainer(props: JustChildren): JSX.Element {
    const style: Style = {
        borderBottom: `1px solid ${Colors.lines.dark1}`,
    }
    return <VerticalStack style={style}>{props.children}</VerticalStack>
}

function MiddleContainer(props: ContainerProps): JSX.Element {
    const flex = props.isSmallScreen ? undefined : 'auto'
    const style: Style = {
        flex,
    }
    return <VerticalStack style={style}>{props.children}</VerticalStack>
}

function BottomContainer(props: ContainerProps): JSX.Element {
    const justifyContent = props.isSmallScreen ? 'flex-start' : 'flex-end'
    const style: Style = {
        justifyContent,
    }
    return <VerticalStack style={style}>{props.children}</VerticalStack>
}

/**
 * Navigation bar
 */

export function Navigation(props: ScreenSizeProps): JSX.Element {
    const isSmallScreen = props.isSmallScreen
    return (
        <NavigationContainer isSmallScreen={isSmallScreen}>
            <MainContainer isSmallScreen={isSmallScreen}>
                <TopContainer>
                    <EntrySeparator style={{ flexBasis: 12 }} />
                    <DashboardMenu />
                    <EntrySeparator style={{ flexBasis: 10 }} />
                </TopContainer>
                <MiddleContainer isSmallScreen={isSmallScreen}>
                    <EntrySeparator />
                    {/*<Otros menues />*/}
                    <EntrySeparator />
                </MiddleContainer>
                <BottomContainer isSmallScreen={isSmallScreen}>
                    {/*<LogOut />*/}
                    <EntrySeparator />
                </BottomContainer>
            </MainContainer>
        </NavigationContainer>
    )
}
