import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import VueCookies from "vue-cookies";
import naive from 'naive-ui'
// @ts-ignore
import piniaPersist from 'pinia-plugin-persist'
import getRouter from './router'
console.log(VueCookies);

createApp(App).use(naive).use(VueCookies.install).use(getRouter()).mount('#app')
