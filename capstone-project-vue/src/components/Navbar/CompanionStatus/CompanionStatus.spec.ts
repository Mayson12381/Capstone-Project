import { mount } from '@vue/test-utils'
import CompanionStatus from './CompanionStatus.vue'

describe('CompanionStatus', () => {
  it('renders offline status on default', () => {
    const wrapper = mount(CompanionStatus, {})
    expect(wrapper.text()).toMatch('Companion Offline')
  })

  it('renders offline status on default', () => {
    const status = 'online'
    const wrapper = mount(CompanionStatus, {
      props: { status },
    })
    expect(wrapper.text()).toMatch('Companion Online')
  })
})
