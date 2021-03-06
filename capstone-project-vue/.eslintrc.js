module.exports = {
  root: true,
  env: {
    node: true,
  },
  extends: [
    "plugin:vue/vue3-essential",
    "eslint:recommended",
    "@vue/typescript/recommended",
    "@vue/prettier",
    "@vue/prettier/@typescript-eslint",
  ],
  parserOptions: {
    ecmaVersion: 2020,
  },
  rules: {
    "no-console": process.env.NODE_ENV === "production" ? "warn" : "off",
    "no-debugger": process.env.NODE_ENV === "production" ? "warn" : "off",
    camelcase: 'off',
    'prettier/prettier': [
      'warn',
      {
        semi: false,
        singleQuote: true,
        trailingComma: 'es5',
        printWidth: 90,
      },
    ],
  },
  overrides: [
    {
      files: [
        "**/__tests__/*.{j,t}s?n(x)",
        "**/tests/unit/**/*.spec.{j,t}s?(x)",
        "**spec.ts",
      ],
      env: {
        jest: true,
      },
    },
  ],
};
