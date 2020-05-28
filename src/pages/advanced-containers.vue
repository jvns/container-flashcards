<template>
    <div id="app">
        <Game v-bind:cards='[
        "kernel-features",
        "kernel-feature-memory",
        "ps-processes",
        "own-pid",
        "layer-implementation",
        "docker-required",
        "just-use-cgroups",
        "whats-inside",
        "namespace-command",
        "prevent",
        "exceed-memory",
        "ip-address",
        "memory-tracking",
        ]'
        basedir='advanced-containers'
        title="more container flashcards"
        >
        </Game>
    </div>
</template>

<script lang="ts">
// note: for `kill`, "what happens?" is a bit vague
import { Component, Prop, Vue } from 'vue-property-decorator';
import Game from '../components/Game.vue';

@Component({
    components: {
        Game,
    },
})
export default class AdvancedContainers extends Vue {
}
</script>
