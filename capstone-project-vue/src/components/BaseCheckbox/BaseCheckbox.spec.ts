import { shallowMount } from '@vue/test-utils'
import BaseCheckbox from './BaseCheckbox.vue'

describe('BaseCheckbox', () => {
  it('renders title prop', () => {
    const title = 'TestTitle'
    const wrapper = shallowMount(BaseCheckbox, {
      props: { title },
    })
    expect(wrapper.text()).toMatch(title)
  })

  it('starts unselected', () => {
    const title = 'TestTitle'
    const wrapper = shallowMount(BaseCheckbox, {
      props: { title },
    })
    expect(wrapper.props('startSelected')).toBeFalsy()
    const input = wrapper.find('input')
    expect(input.element.checked).toBeFalsy()
  })

  it('is selected on prop startSelected', () => {
    const title = 'TestTitle'
    const startSelected = true
    const wrapper = shallowMount(BaseCheckbox, {
      props: { title, startSelected },
    })
    expect(wrapper.props('startSelected')).toBeTruthy()
    const input = wrapper.find('input')
    expect(input.element.checked).toBeTruthy()
  })

  it('emits update event on click', () => {
    const title = 'TestTitle'
    const wrapper = shallowMount(BaseCheckbox, {
      props: { title },
    })
    const input = wrapper.find('input')
    input.trigger('click')
    expect(wrapper.emitted('update')).toBeTruthy()
  })
})
