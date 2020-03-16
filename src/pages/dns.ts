import Vue from 'vue';
import DNS from './dns.vue';

Vue.config.productionTip = false;

new Vue({
    render: (h) => h(DNS),
}).$mount('#app');
