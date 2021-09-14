module.exports = {
  preset: '@vue/cli-plugin-unit-jest/presets/typescript-and-babel',
  transform: {
    '^.+\\.vue$': 'vue-jest',
  },
  testMatch: ['**/src/**/*.spec.[jt]s?(x)'],
  collectCoverage: true,
  collectCoverageFrom: [
    'src/**/*.{js,vue,ts}',
    '!src/main.ts',
    '!src/components/**/index.ts',
  ],
}
