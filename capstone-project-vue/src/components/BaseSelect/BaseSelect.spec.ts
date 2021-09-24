import { mount } from '@vue/test-utils'
import BaseSelect from './BaseSelect.vue'

// Due to transitions in component, tests dont work fully here

describe('BaseSelect', () => {
  it('renders title prop', () => {
    const title = 'TestTitle'
    const wrapper = mount(BaseSelect, {
      props: { title },
    })
    expect(wrapper.text()).toMatch(title)
  })
})
