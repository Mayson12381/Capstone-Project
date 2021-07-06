<template>
  <Disclosure as="nav" class="bg-gray-800">
    <div class="px-4 sm:px-6">
      <div class="flex items-center justify-between h-16">
        <div class="flex items-center">
          <div class="flex-shrink-0">
            <h2 class="text-2xl font-bold leading-7 text-white sm:text-3xl sm:truncate">
              CStrategy.ai
            </h2>
          </div>
          <div class="hidden md:block">
            <div class="ml-10 flex items-baseline space-x-4">
              <template v-for="item in navigation" :key="item">
                <template v-if="currentRoute === item">
                  <div
                    class="
                      bg-gray-900
                      text-white
                      px-3
                      py-2
                      rounded-md
                      text-sm
                      font-medium
                      cursor-pointer
                    "
                    @click="changeRoute(item)"
                  >
                    {{ item }}
                  </div>
                </template>
                <div
                  v-else
                  class="
                    text-gray-300
                    hover:bg-gray-700 hover:text-white
                    px-3
                    py-2
                    rounded-md
                    text-sm
                    font-medium
                    cursor-pointer
                  "
                  @click="changeRoute(item)"
                >
                  {{ item }}
                </div>
              </template>
            </div>
          </div>
        </div>
        <div class="hidden md:block">
          <div class="ml-4 flex items-center md:ml-6">
            <Menu as="div" class="ml-3 relative">
              <div>
                <MenuButton
                  class="
                    max-w-xs
                    bg-gray-800
                    rounded-full
                    flex
                    items-center
                    text-sm
                    focus:outline-none
                    focus:ring-2
                    focus:ring-offset-2
                    focus:ring-offset-gray-800
                    focus:ring-white
                  "
                >
                  <span class="sr-only">Open user menu</span>
                  <img
                    class="h-8 w-8 rounded-full"
                    src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
                    alt=""
                  />
                </MenuButton>
              </div>
              <transition
                enter-active-class="transition ease-out duration-100"
                enter-from-class="transform opacity-0 scale-95"
                enter-to-class="transform opacity-100 scale-100"
                leave-active-class="transition ease-in duration-75"
                leave-from-class="transform opacity-100 scale-100"
                leave-to-class="transform opacity-0 scale-95"
              >
                <MenuItems
                  class="
                    origin-top-right
                    absolute
                    right-0
                    mt-2
                    w-48
                    rounded-md
                    shadow-lg
                    py-1
                    bg-white
                    ring-1 ring-black ring-opacity-5
                    focus:outline-none
                  "
                >
                  <MenuItem v-for="item in profile" :key="item" v-slot="{ active }">
                    <a
                      href="#"
                      :class="[
                        active ? 'bg-gray-100' : '',
                        'block px-4 py-2 text-sm text-gray-700',
                      ]"
                      >{{ item }}</a
                    >
                  </MenuItem>
                </MenuItems>
              </transition>
            </Menu>
          </div>
        </div>
      </div>
    </div>
  </Disclosure>
</template>

<script lang="ts">
import { defineComponent, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { Disclosure, Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue'

const profile = ['Your Profile', 'Settings', 'Sign out']
const navigation = ['Dashboard', 'Database']

export default defineComponent({
  components: {
    Disclosure,
    Menu,
    MenuButton,
    MenuItem,
    MenuItems,
  },
  setup() {
    const router = useRouter()
    const route = useRoute()

    const currentRoute = computed(() => route.name)
    const changeRoute = (name: string): void => {
      router.push({ name: name })
    }
    return {
      currentRoute,
      changeRoute,
      navigation,
      profile,
    }
  },
})
</script>
