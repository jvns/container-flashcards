<template>
    <div id="app">
        <Game v-bind:cards='[
            "kill",
            "ctrlc",
            "stop-kill",
            "pipe-read",
            "use-sockets",
            "unix-differences",
            "read-file",
            "inherit",
            "threads-share",
            "proc",
            "same-address",
            "allocate-more",
            "use-more-memory",
            "shared-library-memory",
            "mmap",
        ]'
        basedir='linux'
        title="linux flashcards"
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
export default class Linux extends Vue {
}
</script>
