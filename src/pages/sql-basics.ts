import Vue from 'vue';
import SQLBasics from './sql-basics.vue';

Vue.config.productionTip = false;

new Vue({
    render: (h) => h(SQLBasics),
}).$mount('#app');
