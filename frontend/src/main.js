import './assets/main.css'

import {createApp} from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.css'
import vuetify from "vite-plugin-vuetify";

createApp(App).use(router).use(vuetify).mount('#app')
