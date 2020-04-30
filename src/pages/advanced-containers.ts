import Vue from 'vue';
import AdvancedContainers from './advanced-containers.vue';

Vue.config.productionTip = false;

new Vue({
    render: (h) => h(AdvancedContainers),
}).$mount('#app');
