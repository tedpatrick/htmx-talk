import { defineConfig } from 'vite'

export default defineConfig({
  build: {
    outDir: '../static',
    lib: {
      entry: 'src/index.ts',
      formats: ['es']
    },
    rollupOptions: {
    }
  }
})