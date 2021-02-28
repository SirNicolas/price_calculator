import '@babel/polyfill';
// Import Component hooks before component definitions
import './component-hooks';
import Vue from 'vue';
import './plugins/vuetify';
import './plugins/vee-validate';
import App from './Calculation.vue';
import router from './router';
import './registerServiceWorker';
import 'vuetify/dist/vuetify.min.css';

Vue.config.productionTip = false;

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
