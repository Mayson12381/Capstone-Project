import { mount } from '@vue/test-utils'
import UserMenu from './UserMenu.vue'

// Due to transitions in component, tests dont work fully here

describe('UserMenu', () => {
  it('renders correctly', () => {
    const wrapper = mount(UserMenu)
    expect(wrapper.text()).toMatch('Open user menu')
  })
})
