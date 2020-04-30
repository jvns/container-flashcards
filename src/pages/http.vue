<template>
    <div id="app">
        <Game v-bind:cards='[
            "fragment",
            "every-website-http",
            "request-parts",
            "response-parts",
            "what-part-html",
            "what-part-caching",
            "what-part-redirect",
            "what-header-login",
            "request-method-get",
            "request-method-post",
            "content-type",
            "browser-view-http-request",
            "500-error",
            "js-request-limits",
        ]'
        basedir='http'
        title="HTTP flashcards"
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
export default class HTTP extends Vue {
}
</script>
