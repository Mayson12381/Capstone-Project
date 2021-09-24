import { mount } from '@vue/test-utils'
import Tabs from './Tabs.vue'

describe('Tabs', () => {
  it('renders offline status on default', () => {
    const navigationItems = ['Nav1', 'Nav2']
    const currentRoute = 'Nav1'
    const wrapper = mount(Tabs, {
      props: { navigationItems, currentRoute },
    })
    expect(wrapper.text()).toContain(navigationItems[0])
    expect(wrapper.text()).toContain(navigationItems[1])
  })

  it('renders highlighted tab', () => {
    const navigationItems = ['Nav1', 'Nav2']
    const currentRoute = 'Nav1'
    const wrapper = mount(Tabs, {
      props: { navigationItems, currentRoute },
    })
    expect(wrapper.find('[data-test="active-tab"]').exists()).toBe(true)
  })

  it('renders empty navigation items on default', () => {
    const wrapper = mount(Tabs)
    expect(wrapper.text()).toBe('')
  })
})
