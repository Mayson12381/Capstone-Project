module.exports = {
  preset: '@vue/cli-plugin-unit-jest/presets/typescript-and-babel',
  transform: {
    '^.+\\.vue$': 'vue-jest',
  },
  testMatch: ['**/src/**/*.spec.[jt]s?(x)'],
  collectCoverageFrom: [
    'src/**/*.{js,vue,ts}',
    '!src/main.ts',
    '!src/components/**/index.ts',
    '!src/components/**/App*.vue',
  ],
}
