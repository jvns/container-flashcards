<template>
    <div id="app">
        <Game v-bind:cards='[
            "dns-basics",
            "command-line",
            "opposite",
            "many-ips",
            "dns-information",
            "email",
            "update-instant",
            "ttl",
            "cname",
            "google-dns",
            "where-dns-responses-come-from",
            "where-nameserver",
            "types-of-dns-servers",
            "own-dns-server",
            "dns-protocol",
        ]'
        basedir='dns'
        title="DNS flashcards"
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
export default class DNS extends Vue {
}
</script>
