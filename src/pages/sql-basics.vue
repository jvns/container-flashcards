<template>
    <div id="app">
        <Game v-bind:cards='[
            "count",
            "case",
            "query-order",
            "null-equals",
            "coalesce",
            "null-integer",
            "no-nulls",
            "where-aggregation",
            "sql-conditionals",
            "strings",
            "inner-join-every-row",
            "left-join-every-row",
            "index-effectiveness",
            "explain",
        ]'
        basedir='sql-basics'
        title="SQL flashcards"
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
export default class SQLBasics extends Vue {
}
</script>
