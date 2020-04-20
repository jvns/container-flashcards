<template>
    <div id="app">
        <Game v-bind:cards='[
            "whats-a-reverse-proxy",
            "what-are-lbs-for",
            "where-are-requests-sent",
            "lb-examples",
            "types-of-lbs",
            "can-tcp-lb-serve-multiple",
            "can-tcp-lb-modify-response",
            "tcp-encrypted",
            "http-paths",
            "http-encrypted",
            "http-modify-response",
            "http2",
            "are-there-limits",
        ]'
        basedir='reverse-proxies'
        title="flashcards: reverse proxies!"
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
export default class ReverseProxies extends Vue {
}
</script>
