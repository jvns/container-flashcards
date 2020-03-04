import Vue from 'vue';
import ContainerBasics from './container-basics.vue';

Vue.config.productionTip = false;

new Vue({
    render: (h) => h(ContainerBasics),
}).$mount('#app');
