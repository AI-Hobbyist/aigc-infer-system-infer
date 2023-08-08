import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import naive from 'naive-ui'
import { createPinia } from 'pinia'
// import {} from '../node_modules/pinia-plugin-persist/dist/index.d.ts'
// @ts-ignore
import piniaPersist from 'pinia-plugin-persist'
import getRouter from './router'


const pinia = createPinia()

pinia.use(piniaPersist)

createApp(App).use(naive).use(pinia).use(getRouter(pinia)).mount('#app')
