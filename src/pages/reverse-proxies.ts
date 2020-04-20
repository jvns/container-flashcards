import Vue from 'vue';
import ReverseProxies from './reverse-proxies.vue';

Vue.config.productionTip = false;

new Vue({
    render: (h) => h(ReverseProxies),
}).$mount('#app');
