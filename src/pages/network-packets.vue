<template>
    <div id="app">
        <Game v-bind:cards='[
            "packet-parts",
            "always-packet",
            "ocean",
            "giant-packet",
            "where-is-port",
            "how-many-ips",
            "biggest-port",
            "is-udp-same-port",
            "udp-header",
            "how-packet-routed",
            "ip-ttl",
            "why-network-packets-dropped-2",
            "can-network-packets-lost",
            "spy-network-packet",
            "does-http-always-use-tcp",
        ]'
        basedir='network-packets'
        title="flashcards: network packets!"
        >
        </Game>
    </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
import Game from '../components/Game.vue';

@Component({
    components: {
        Game,
    },
})
export default class NetworkPackets extends Vue {
}
</script>
