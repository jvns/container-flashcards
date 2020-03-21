<template>
    <div id="app">
        <Game v-bind:cards='[
            "ssl-vs-tls",
            "whats-tls-for",
            "can-tls-decrypt-2",
            "https-vs-tls",
            "tls-wire",
            "every-cert-domain",
            "multiple-domains",
            "how-get-certificate",
            "how-browser-check",
            "are-free-certificates-secure",
            "do-tls-certificates-expire",
            "do-i-need-a-ca",
            "is-ssl-dangerous",
            "certificate-secret",
        ]'
        basedir='tls'
        title="TLS flashcards"
        >
        </Game>
    </div>
</template>

<script lang="ts">
// note: "domain name" should really be "hostname" bc a subdomain can have any ip
// note: they're not actually returned in random order
import { Component, Prop, Vue } from 'vue-property-decorator';
import Game from '../components/Game.vue';

@Component({
    components: {
        Game,
    },
})
export default class TLS extends Vue {
}
</script>
