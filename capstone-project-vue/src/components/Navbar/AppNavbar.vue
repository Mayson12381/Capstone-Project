<template>
  <Disclosure as="nav" class="bg-gray-800">
    <div class="px-4 sm:px-6">
      <div class="flex items-center justify-between h-16">
        <div class="flex items-center">
          <div class="hidden sm:block flex-shrink-0">
            <h2 class="text-2xl font-bold leading-7 text-white sm:text-3xl sm:truncate">
              CStrategy.ai
            </h2>
          </div>
          <Tabs :currentRoute="currentRoute" :navigationItems="navigationItems" />
        </div>
        <div class="flex items-center">
          <CompanionStatus :status="companionStatus" />
          <UserMenu v-if="$store.getters.getUser.id" />
        </div>
      </div>
    </div>
  </Disclosure>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { Disclosure } from '@headlessui/vue'
import CompanionStatus from './CompanionStatus'
import { useStore } from 'vuex'
import { key } from '@/store'
import Tabs from './Tabs/Tabs.vue'
import UserMenu from './UserMenu/UserMenu.vue'

export default defineComponent({
  name: 'BaseNavbar',
  components: {
    Disclosure,
    CompanionStatus,
    Tabs,
    UserMenu,
  },
  data() {
    return {
      navigationItems: ['Dashboard', 'Database'],
    }
  },
  cron: {
    time: 5000,
    method: 'fetchCompanionStatus',
    autoStart: true,
  },
  computed: {
    currentRoute() {
      return this.$route.name
    },
    companionStatus() {
      const store = useStore(key)
      return store.getters.companionStatus
    },
  },
  methods: {
    fetchCompanionStatus() {
      this.$store.dispatch('fetchCompanionStatus')
    },
    changeRoute(routeName) {
      this.$router.push({ name: routeName })
    },
  },
})
</script>
