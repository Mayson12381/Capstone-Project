import { shallowMount } from '@vue/test-utils'
import PlayerTable from './PlayerTable.vue'

describe('PlayerTable', () => {
  it('renders correct table titles', () => {
    const players = []
    const wrapper = shallowMount(PlayerTable, {
      props: { players },
    })
    expect(wrapper.text()).toContain('Player')
    expect(wrapper.text()).toContain('Weapon')
    expect(wrapper.text()).toContain('Armor')
    expect(wrapper.text()).toContain('Utility')
    expect(wrapper.text()).toContain('Status')
  })

  it('renders players', () => {
    const players = [
      {
        health_status: 1,
        weapon: 'AK47',
        kevlar: 'Helmet',
        nades: ['Flashbang', 'Smoke'],
      },
    ]
    const wrapper = shallowMount(PlayerTable, {
      props: { players },
    })
    expect(wrapper.text()).toContain(players[0].weapon)
    expect(wrapper.text()).toContain(players[0].health_status)
    expect(wrapper.text()).toContain(players[0].kevlar)
    expect(wrapper.text()).toContain(players[0].nades[0])
    expect(wrapper.text()).toContain(players[0].nades[1])
  })
})
