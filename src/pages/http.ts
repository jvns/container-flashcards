import Vue from 'vue';
import HTTP from './http.vue';

Vue.config.productionTip = false;

new Vue({
    render: (h) => h(HTTP),
}).$mount('#app');
