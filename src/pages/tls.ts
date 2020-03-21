import Vue from 'vue';
import TLS from './tls.vue';

Vue.config.productionTip = false;

new Vue({
    render: (h) => h(TLS),
}).$mount('#app');
