<template>
    <div id="app">
        <h1 class="text-3xl my-8"> container flashcards </h1>
        <div class="w-3/5" style="margin: 0 auto;">
        </div>

        <Flashcard front="is a container a kind of virtual machine?" back="no."> </Flashcard>
        <div class="mx-8">
            hi
        </div>
    </div>

</template>


<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
import Flashcard from './components/Flashcard.vue';

@Component({
    components: {
        Flashcard,
    },
})
export default class Main extends Vue {
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
    margin: 40px 0 0;
}
ul {
    list-style-type: none;
    padding: 0;
}
li {
    display: inline-block;
    margin: 0 10px;
}
</style>
