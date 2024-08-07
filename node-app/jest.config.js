/** @type {import('ts-jest').JestConfigWithTsJest} **/
module.exports = {
  clearMocks:true,
  coverageProvider: "v8",
  moduleFileExtensions : ["js", "jsx", "ts", "tsx", "json", "node"],
  testEnvironment: "node",
  roots: ["<rootDir>/"],
  testMatch: ["**/__tests__/**/*.[jt]s?(x)", "**/?(*.)+(spec|test).[tj]s?(x)"],
  transform: {
    "^.+.tsx?$": ["ts-jest",{}],
  },
};