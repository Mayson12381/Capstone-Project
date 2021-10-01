module.exports = {
  preset: '@vue/cli-plugin-unit-jest/presets/typescript-and-babel',
  transform: {
    '^.+\\.vue$': 'vue-jest',
  },
  testMatch: ['**/src/**/*.spec.[jt]s?(x)'],
  collectCoverageFrom: [
    'src/**/*.{js,vue,ts}',
    '!src/main.ts',
    '!src/**/index.ts',
    '!src/**/App*.vue',
    '!src/firebaseConfig.ts',
    '!src/services/FirestoreService.ts',
  ],
}
