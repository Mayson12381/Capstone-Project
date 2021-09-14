import { createApp } from 'vue'
import './firebaseConfig.ts'
import App from './App.vue'
import router from './router'
import './styles/main.css'
import store, { key } from './store'
import crono from 'vue-crono';

createApp(App)
.use(store, key)
.use(router)
.use(crono)
.mount('#app')
