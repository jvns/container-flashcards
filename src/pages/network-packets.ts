import Vue from 'vue';
import NetworkPackets from './network-packets.vue';

Vue.config.productionTip = false;

new Vue({
    render: (h) => h(NetworkPackets),
}).$mount('#app');
