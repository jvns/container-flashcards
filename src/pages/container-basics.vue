<template>
    <div id="app">
        <Game v-bind:cards='[
            "container-do",
            "database",
            "vm-2",
            "redhat-2",
            "storage",
            "memory",
            "mac",
            "what-is-image",
            "host",
            "image-files",
            "access-files",
        ]'
        basedir='container-basics'>
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
export default class ContainerBasics extends Vue {
}
</script>
