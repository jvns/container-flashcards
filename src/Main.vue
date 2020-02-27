<template>
    <div id="app">
        <h1 class="text-4xl text-center my-8"> container flashcards </h1>
        <div class="w-3/5" style="margin: 0 auto;">
        </div>

        <div class="flex flex-row justify-center">
            <div v-if="!done" >
                <div v-for="(card, index) in cards">
                    <Flashcard v-if="index == current_card" v-bind:name="card"></Flashcard>
                </div>
                <div class="flex flex-row justify-center mt-8">
                    <button class="bg-pink-600 text-xl text-white rounded px-6 py-3 mx-4" @click="knew">I knew that!</button>
                    <button class="bg-blue-600 text-xl text-white rounded px-6 py-3" @click="learned">I learned something!</button>
                </div>
            </div>

            <div v-if="done" style="width: 600px; height: 300px;" class="text-gray-100 bg-gray-700 border-gray-200 border rounded-lg">
                <p class="text-4xl px-8 py-8 text-center">
                that's all!
                </p>
            </div>
        </div>

        <div class="flex flex-row mt-8 flex-wrap">
            <div class="lg:w-1/4 w-full mb-8">
            </div>
            <div class="lg:w-1/4 w-full mb-8">
                <h1 class="text-3xl text-center">Things you learned </h1>
                <div class="flex flex-row justify-center flex-wrap px-8">
                    <div v-for="(name, index) in cards">
                        <Flashcard v-if="learned_list[index]" v-bind:name="name"></Flashcard>
                    </div>
                </div>
            </div>
            <div class="lg:w-1/4 w-full">
                <h1 class="text-3xl text-center">Things you knew </h1>
                <div class="flex flex-row justify-center flex-wrap px-8">
                    <div v-for="(name, index) in cards">
                        <Flashcard v-if="knew_list[index]" v-bind:name="name"></Flashcard>
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
            "memoy",
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
