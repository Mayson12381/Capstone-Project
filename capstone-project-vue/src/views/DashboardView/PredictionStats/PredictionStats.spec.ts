import { shallowMount } from '@vue/test-utils'
import PredictionStats from './PredictionStats.vue'

describe('PredictionStats', () => {
  it('renders both bombsites as title', () => {
    const prediction = {
      A: 30,
      B: 30,
    }
    const wrapper = shallowMount(PredictionStats, {
      props: { prediction },
    })
    expect(wrapper.text()).toContain('A Site')
    expect(wrapper.text()).toContain('B Site')
  })

  it('renders predictions results', () => {
    const prediction = {
      A: 30,
      B: 30,
    }
    const wrapper = shallowMount(PredictionStats, {
      props: { prediction },
    })
    expect(wrapper.text()).toContain(prediction.A)
    expect(wrapper.text()).toContain(prediction.B)
  })
})
