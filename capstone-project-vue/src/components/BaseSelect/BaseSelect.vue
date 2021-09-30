<template>
  <Listbox as="div" value="options[selectedIndex]">
    <ListboxLabel v-if="title" class="block text-sm font-medium text-gray-700">
      {{ title }}
    </ListboxLabel>
    <div class="mt-1 relative">
      <ListboxButton
        class="
          bg-white
          relative
          w-full
          border border-gray-300
          rounded-md
          shadow-sm
          pl-3
          pr-10
          py-2
          text-left
          cursor-default
          focus:outline-none focus:ring-1 focus:ring-indigo-500 focus:border-indigo-500
          sm:text-sm
        "
      >
        <span class="block truncate">{{ options[selectedIndex].name }}</span>
        <span
          class="absolute inset-y-0 right-0 flex items-center pr-2 pointer-events-none"
        >
          <SelectorIcon class="h-5 w-5 text-gray-400" aria-hidden="true" />
        </span>
      </ListboxButton>

      <transition
        leave-active-class="transition ease-in duration-100"
        leave-from-class="opacity-100"
        leave-to-class="opacity-0"
      >
        <ListboxOptions
          class="
            absolute
            z-10
            mt-1
            w-full
            bg-white
            shadow-lg
            max-h-60
            rounded-md
            py-1
            text-base
            ring-1 ring-black ring-opacity-5
            overflow-auto
            focus:outline-none
            sm:text-sm
          "
        >
          <ListboxOption
            as="template"
            v-for="option in options"
            :key="option.id"
            :value="option"
            v-slot="{ active }"
          >
            <li
              :class="[
                active ? 'text-white bg-indigo-600' : 'text-gray-900',
                'cursor-default select-none relative py-2 pl-3 pr-9',
              ]"
            >
              <span
                :class="[
                  options[selectedIndex] === option ? 'font-semibold' : 'font-normal',
                  'block truncate',
                ]"
              >
                {{ option.name }}
              </span>

              <span
                v-if="options[selectedIndex] === option"
                :class="[
                  active ? 'text-white' : 'text-indigo-600',
                  'absolute inset-y-0 right-0 flex items-center pr-4',
                ]"
              >
                <CheckIcon class="h-5 w-5" aria-hidden="true" />
              </span>
            </li>
          </ListboxOption>
        </ListboxOptions>
      </transition>
    </div>
  </Listbox>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

import {
  Listbox,
  ListboxButton,
  ListboxLabel,
  ListboxOption,
  ListboxOptions,
} from '@headlessui/vue'
import { CheckIcon, SelectorIcon } from '@heroicons/vue/solid'

interface OptionsObject {
  id: number
  name: string
}

export default defineComponent({
  components: {
    Listbox,
    ListboxButton,
    ListboxLabel,
    ListboxOption,
    ListboxOptions,
    CheckIcon,
    SelectorIcon,
  },
  props: {
    title: {
      required: false,
      default: '',
    },
    options: {
      required: false,
      default: (): Array<OptionsObject> => [
        { id: 0, name: 'Inferno' },
        { id: 1, name: 'Overpass' },
      ],
    },
    selectedIndex: {
      required: false,
      default: 0,
    },
  },
})
</script>
