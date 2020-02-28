<template>
    <div id="app">
        <h1 class="text-4xl text-center my-8 w-full"> container flashcards </h1>

        <div class="flex flex-row flex-wrap justify-center">
            <div v-if="!done" class="w-10/12 lg:w-1/3">
                <p class="text-l mb-4 text-center">
                Click the card to see the answer.
                </p>
                <div v-for="(card, index) in cards">
                    <Flashcard v-bind:card_left="index < current_card" v-bind:card_hidden="index > current_card" v-bind:card_visible="index == current_card" v-bind:name="card"></Flashcard>
                </div>
                <div class="flex flex-row flex-wrap justify-center mt-2">
                    <button class="bg-pink-600 text-white rounded px-3 py-2 mx-4 my-1" @click="knew">I knew that!</button>
                    <button class="bg-blue-600 text-white rounded px-3 py-2 mx-4 my-1" @click="learned">I learned something!</button>
                    <button class="bg-orange-600 text-white rounded px-3 py-2 my-1" @click="confusing">That's confusing</button>
                </div>
            </div>

            <div v-if="done" class="w-10/12 lg:w-1/3t">
                <Flashcard name="thats-all" v-bind:card_visible="true"></Flashcard>
            </div>
        </div>

        <div class="flex flex-row justify-center mt-8 flex-wrap">
            <div class="lg:w-1/4 w-10/12 mb-8 lg:ml-8">
                <h1 class="text-3xl text-center">Things you learned </h1>
                <div class="flex flex-row justify-center flex-wrap px-8 w-full">
                    <div v-for="(name, index) in cards" class="w-full">
                        <Flashcard v-bind:card_left="!learned_list[index]" v-bind:card_visible="learned_list[index]" v-bind:name="name"></Flashcard>
                    </div>
                </div>
            </div>
            <div class="lg:w-1/4 w-10/12">
                <h1 class="text-3xl text-center">Things you knew </h1>
                <div class="flex flex-row justify-center flex-wrap px-8 w-full">
                    <div v-for="(name, index) in cards" class="w-full">
                        <Flashcard v-bind:card_left="!knew_list[index]" v-bind:card_visible="knew_list[index]" v-bind:name="name"></Flashcard>
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
    //@ts-ignore
    private current_card: int = 0;
    private knew_list = {};
    private learned_list = {};
    private confusing_list = {};


    constructor() {
        super()
    }

    knew(): any {
        //@ts-ignore
        this.knew_list[this.current_card] = true;

        console.log('knew', this.knew_list);
        this.next();
    }

    learned(): any {
        // @ts-ignore
        this.learned_list[this.current_card] = true;
        console.log('learned', this.learned_list);
        this.next();
    }

    confusing(): any {
        // @ts-ignore
        this.confusing_list[this.current_card] = true;
        console.log('confusing', this.confusing_list);
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
        //@ts-ignore
        this.cards = [
        //@ts-ignore
            "storage",
        //@ts-ignore
            "vm",
        //@ts-ignore
            "memory",
        //@ts-ignore
            "what-is-image",
        //@ts-ignore
            "image-files",
        //@ts-ignore
            "access-files",
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
