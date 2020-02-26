<template>
    <div id="app">
        <h1 class="text-4xl text-center my-8"> container flashcards </h1>
        <div class="w-3/5" style="margin: 0 auto;">
        </div>

        <div class="flex flex-row justify-center">
            <div v-if="!done" >
                <div v-for="(card, index) in cards">
                    <Flashcard v-if="index == current_card" v-bind:front="card.front" v-bind:back="card.back"></Flashcard>
                </div>
                <div class="flex flex-row justify-center mt-8">
                    <button class="bg-green-600 text-xl text-white rounded px-6 py-3 mx-4" @click="knew">I knew that!</button>
                    <button class="bg-purple-600 text-xl text-white rounded px-6 py-3" @click="learned">I learned something!</button>
                </div>
            </div>

            <div v-if="done" style="width: 450px; height: 300px;" class="text-gray-100 bg-gray-700">
                <p class="text-4xl px-8 py-8 text-center">
                that's all!
                </p>
            </div>
        </div>

        <div class="flex flex-row mt-8 flex-wrap">
            <div class="lg:w-1/2 w-full mb-8">
                <h1 class="text-3xl text-center">Things you learned </h1>
                <div class="flex flex-row justify-center flex-wrap">
                    <div v-for="(card, index) in cards">
                        <Flashcard v-if="learned_list[index]" v-bind:front="card.front" v-bind:back="card.back"></Flashcard>
                    </div>
                </div>
            </div>
            <div class="lg:w-1/2 w-full">
                <h1 class="text-3xl text-center">Things you knew </h1>
                <div class="flex flex-row justify-center flex-wrap">
                    <div v-for="(card, index) in cards">
                        <Flashcard v-if="knew_list[index]" v-bind:front="card.front" v-bind:back="card.back"></Flashcard>
                    </div>
                </div>
            </div>
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
    private cards = [];
    private done: boolean = false;
    private current_card: int = 0;
    private knew_list = {};
    private learned_list = {};


    constructor() {
        super()
    }

    knew(): any {
        this.knew_list[this.current_card] = true;

        console.log('knew', this.knew_list);
        this.next();
    }

    learned(): any {
        this.learned_list[this.current_card] = true;
        console.log('learned', this.learned_list);
        this.next();
    }

    next(): any {
        if (this.current_card >= this.cards.length-1) {
            this.done = true;
        } else {
            this.current_card++;
        }
    }

    async created() {
        this.cards = [
            {front: "is a container a virtual machine?", back: "nope!"},
            {front: "can you limit a container's CPU/memory?", back: "yes!"},
            {front: "where do you download container images from?", back: "<p>a container registry!</p><p class='text-2xl'>there are both public and private container registries.</p>"},
        ];
    }
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
