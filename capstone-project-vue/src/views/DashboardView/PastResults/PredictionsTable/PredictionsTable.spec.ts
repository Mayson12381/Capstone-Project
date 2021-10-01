import { shallowMount } from '@vue/test-utils'
import PredictionsTable from './PredictionsTable.vue'

describe('PredictionsTable', () => {
  it('renders correct table titles', () => {
    const predictions = []
    const wrapper = shallowMount(PredictionsTable, {
      props: { predictions },
    })
    expect(wrapper.text()).toContain('Map')
    expect(wrapper.text()).toContain('Predictions')
    expect(wrapper.text()).toContain('Buy Type')
    expect(wrapper.text()).toContain('Predicted On')
  })

  it('renders predictions', () => {
    const predictions = [
      {
        map: 'Inferno',
        buyType: 'full',
        predicted_on: '2020-01-01',
        id: 1,
        prediction: {
          A: 50,
          B: 58,
        },
      },
    ]
    const wrapper = shallowMount(PredictionsTable, {
      props: { predictions },
    })
    expect(wrapper.text()).toContain(predictions[0].map)
    expect(wrapper.text()).toContain(predictions[0].predicted_on)
    expect(wrapper.text()).toContain(predictions[0].prediction.A)
    expect(wrapper.text()).toContain(predictions[0].prediction.B)
  })
})
