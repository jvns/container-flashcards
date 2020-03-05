<template>
    <div id="app">
        <Game v-bind:cards='[
            "proc",
            "read-file",
            "kill",
            "ctrlc",
            "stop-kill",
            "pipe",
            "use-sockets",
            "unix-differences",
            "inherit",
            "threads-share",
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
