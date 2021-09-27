import { shallowMount } from '@vue/test-utils'
import BaseButton from './BaseButton.vue'

describe('BaseButton', () => {
  it('renders title prop', () => {
    const title = 'TestTitle'
    const wrapper = shallowMount(BaseButton, {
      props: { title },
    })
    expect(wrapper.text()).toMatch(title)
  })

  it('has primary class on default', () => {
    const title = 'TestTitle'
    const wrapper = shallowMount(BaseButton, {
      props: { title },
    })
    expect(wrapper.props('variant')).toBe('primary')
  })

  it('has secondary class on prop', () => {
    const title = 'TestTitle'
    const variant = 'secondary'
    const wrapper = shallowMount(BaseButton, {
      props: { title, variant },
    })
    expect(wrapper.props('variant')).toBe('secondary')
  })

  it('emits click event on click', () => {
    const title = 'TestTitle'
    const wrapper = shallowMount(BaseButton, {
      props: { title },
    })
    wrapper.trigger('click')
    expect(wrapper.emitted().click).toBeTruthy()
  })
})
