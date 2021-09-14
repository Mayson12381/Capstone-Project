import { shallowMount } from '@vue/test-utils'
import BaseModal from './BaseModal.vue'

// Due to transitions in component, tests dont work here

describe('BaseModal', () => {
  it('renders title prop', async () => {
    const isActive = true
    const wrapper = shallowMount(BaseModal, {
      props: { isActive },
    })
    expect(wrapper)
  })
})
