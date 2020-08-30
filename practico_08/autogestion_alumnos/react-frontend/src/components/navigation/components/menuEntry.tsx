import * as React from 'react'
import { Colors, Dimensions } from '../../../style'
import { Style, StyleMap } from '../../../utils/tsTypes'
import { getValueOrDefault, isNil } from '../../../utils/checks'
import { HorizontalStack } from '../../../common/components/flex'
import { noop } from '../../../utils/utils'

interface EntryToolTipProps {
    tooltip: React.ReactNode
}

function EntryTooltip(props: EntryToolTipProps): JSX.Element {
    const styles: StyleMap = {
        container: {
            position: 'absolute',
            top: -Dimensions.height.navEntry,
            left: Dimensions.width.nav,
            zIndex: 1000,
            height: Dimensions.height.navEntry,
            whiteSpace: 'nowrap',
            background: Colors.background.menu3,
            borderRadius: 2,
            boxShadow: `0 8px 18px 0 ${Colors.shadow.light2}`,
            fontWeight: 600,
            textAlign: 'center',
            fontSize: 14,
            lineHeight: `${Dimensions.height.navEntry}px`,
            padding: '0 16px',
        },
        triangle: {
            border: 'none',
            backgroundColor: Colors.background.menu3,
        },
    }
    return (
        <div style={styles.container}>
            {/*<TooltipTriangle*/}
            {/*    direction={TRIANGLE_DIR.LEFT}*/}
            {/*    edgePixels={8}*/}
            {/*    borderOffsetPixels={0}*/}
            {/*    triangleStyle={styles.triangle}*/}
            {/*/>*/}
            {props.tooltip}
        </div>
    )
}

interface EntryBorderProps {
    isHighlighted?: boolean
}

function EntryBorder(props: EntryBorderProps): JSX.Element {
    const background = props.isHighlighted ? Colors.lines.active : undefined
    const style: Style = {
        background,
        width: 3,
    }
    return <div style={style} />
}

/**
 * Gap between MenuEntries
 */
interface EntrySeparatorProps {
    style?: Style
}
export function EntrySeparator(props: EntrySeparatorProps): JSX.Element {
    const style: Style = {
        minHeight: 5,
        flexBasis: 21,
        ...props.style,
    }
    return <div style={style} />
}

/**
 * Outer frame for composing menu entries.
 * It includes the behavior of showing a tooltip when the mouse is hovering and
 * a left-border that is visible when the menu is active
 */

interface MenuEntryProps {
    children: React.ReactNode
    tooltip: React.ReactNode
    tooltipEnabled?: boolean
    style?: Style
    isActive?: boolean
    isDisabled?: boolean
}

export function MenuEntry(props: MenuEntryProps): JSX.Element {
    const tooltipEnabled = getValueOrDefault(props.tooltipEnabled, false)
    const styles: StyleMap = {
        stack: {
            alignSelf: 'stretch',
            userSelect: 'none',
            flex: 'none',
            ...props.style,
        },
        disabledTrigger: {
            cursor: 'default',
        },
    }
    const triggerStyle = props.isDisabled ? styles.disabledTrigger : null
    const tooltip = <EntryTooltip tooltip={props.tooltip} />
    return (
        <HorizontalStack style={styles.stack}>
            <EntryBorder isHighlighted={props.isActive} />
            {/*<OnHoverTooltip*/}
            {/*    tooltip={tooltip}*/}
            {/*    closeTrigger={TOOLTIP_CLOSE_TRIGGER.CONTAINER_CLICK}*/}
            {/*    tooltipEnabled={tooltipEnabled}*/}
            {/*    style={triggerStyle}*/}
            {/*    showDelayMs={0}*/}
            {/*    hideDelayMs={0}*/}
            {/*>*/}
            {props.children}
            {/*</OnHoverTooltip>*/}
            <EntryBorder />
        </HorizontalStack>
    )
}

/**
 * Button-alike container for composing menu dropdowns and single-link menus
 */

interface MenuTriggerProps {
    children: React.ReactNode
    isActive?: boolean
    isExpanded?: boolean
    isDisabled?: boolean
    onClick?(): void
}

export class MenuTrigger extends React.Component<MenuTriggerProps> {
    constructor(props: MenuTriggerProps) {
        super(props)
    }

    render(): JSX.Element {
        const onClick =
            this.props.isDisabled || isNil(this.props.onClick)
                ? noop
                : this.props.onClick
        const background = this.getBackground(
            this.props.isActive,
            this.props.isExpanded,
            this.props.isDisabled
        )
        const style: Style = {
            width: Dimensions.width.navEntry,
            height: Dimensions.height.navEntry,
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            borderRadius: 2,
            background,
            position: 'relative',
        }
        return (
            <div style={style} onClick={onClick}>
                {this.props.children}
            </div>
        )
    }

    private getBackground(
        isActive?: boolean,
        isExpanded?: boolean,
        isDisabled?: boolean
    ): string {
        if (isDisabled) {
            return Colors.background.menu2
        }
        if (isActive) {
            return Colors.background.light1
        }
        if (isExpanded) {
            return Colors.background.menu1
        }
        return Colors.background.menu4
    }
}

/**
 * Icon component to be used inside MenuTriggers
 */
interface TriggerIconProps {
    // icon: Icons
    style?: Style
    isActive?: boolean
    isExpanded?: boolean
    isDisabled?: boolean
}

export class TriggerIcon extends React.Component<TriggerIconProps> {
    constructor(props: TriggerIconProps) {
        super(props)
    }

    render(): JSX.Element {
        const triggerIconStyle = this.getTriggerIconStyle(
            this.props.isActive,
            this.props.isExpanded,
            this.props.isDisabled
        )
        const style: Style = {
            fontSize: 22,
            ...triggerIconStyle,
            ...this.props.style,
        }
        // return <Icon icon={this.props.icon} style={style} />
        return <a>I</a>
    }

    private getTriggerIconStyle(
        isActive?: boolean,
        isExpanded?: boolean,
        isDisabled?: boolean
    ): Style {
        if (isDisabled) {
            return {
                color: Colors.primary.light,
                opacity: 0.25,
            }
        }
        if (isActive) {
            return {
                color: Colors.background.menu3,
                opacity: 1,
            }
        }
        if (isExpanded) {
            return {
                color: Colors.background.light1,
                opacity: 1,
            }
        }
        return {
            color: Colors.primary.light,
            opacity: 0.5,
        }
    }
}
