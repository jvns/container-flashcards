import Vue from 'vue';
import Linux from './linux.vue';

Vue.config.productionTip = false;

new Vue({
    render: (h) => h(Linux),
}).$mount('#app');
