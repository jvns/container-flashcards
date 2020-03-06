<template>
    <div>
        <h1 class="text-4xl text-center my-8 w-full"> {{title}} </h1>

        <div class="flex flex-row flex-wrap justify-center">
            <div v-if="!done" class="w-10/12 lg:w-1/3">
                <p class="text-l mb-4 text-center">
                Click the card to see the answer.
                </p>
                <div class="text-center text-xl"> Card {{current_card+1}}  of {{cards.length}} </div>
                <div v-for="(card, index) in cards">
                    <Flashcard v-bind:basedir='basedir' v-bind:card_left="index < current_card" v-bind:card_hidden="index > current_card" v-bind:card_visible="index == current_card" v-bind:name="card"></Flashcard>
                </div>
                <div class="flex flex-row flex-wrap justify-center mt-2">
                    <button class="bg-pink-600 text-white rounded px-3 py-2 mx-4 my-1" @click="knew">I knew that!</button>
                    <button class="bg-blue-600 text-white rounded px-3 py-2 mx-4 my-1" @click="learned">I learned something!</button>
                    <button class="bg-orange-600 text-white rounded px-3 py-2 my-1" @click="confusing">That's confusing</button>
                </div>
            </div>

            <div v-if="done" class="w-10/12 lg:w-1/3">
                <Flashcard basedir='' name="thats-all" v-bind:card_visible="true"></Flashcard>
            </div>
        </div>

        <div class="flex flex-row justify-center mt-8 flex-wrap">
            <div class="lg:w-1/4 w-10/12 mb-8 lg:ml-8">
                <h1 class="text-3xl text-center">Things you learned </h1>
                <div class="flex flex-row justify-center flex-wrap px-8 w-full">
                    <div v-for="(name, index) in cards" class="w-full">
                        <Flashcard v-bind:basedir='basedir' v-bind:card_left="!learned_list[index]" v-bind:card_visible="learned_list[index]" v-bind:name="name"></Flashcard>
                    </div>
                </div>
            </div>
            <div class="lg:w-1/4 w-10/12 mb-8 lg:ml-8">
                <h1 class="text-3xl text-center">Things you knew </h1>
                <div class="flex flex-row justify-center flex-wrap px-8 w-full">
                    <div v-for="(name, index) in cards" class="w-full">
                        <Flashcard v-bind:basedir='basedir' v-bind:card_left="!knew_list[index]" v-bind:card_visible="knew_list[index]" v-bind:name="name"></Flashcard>
                    </div>
                </div>
            </div>
            <div class="lg:w-1/4 w-10/12">
                <h1 class="text-3xl text-center">"That's confusing" </h1>
                <div class="flex flex-row justify-center flex-wrap px-8 w-full">
                    <div v-for="(name, index) in cards" class="w-full">
                        <Flashcard v-bind:basedir='basedir' v-bind:card_left="!confusing_list[index]" v-bind:card_visible="confusing_list[index]" v-bind:name="name"></Flashcard>
                    </div>
                </div>
            </div>

        </div>
    </div>

</template>


<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
import Flashcard from './Flashcard.vue';

import { firebase } from '@firebase/app';
import '@firebase/firestore'

@Component({
    components: {
        Flashcard,
    },
})
export default class Game extends Vue {
    @Prop() private cards!: any;
    @Prop() private basedir!: string;
    @Prop() private title!: string;
    private done: boolean = false;
    //@ts-ignore
    private current_card: int = 0;
    private knew_list = {};
    private learned_list = {};
    private confusing_list = {};


    constructor() {
        super()
    }

    firebase() {
        // Your web app's Firebase configuration
        var firebaseConfig = {
            apiKey: "AIzaSyCEbH_2zf9dDzh6Muq-DdK3byHMUIsHfCA",
            authDomain: "wizard-sql-school.firebaseapp.com",
            databaseURL: "https://wizard-sql-school.firebaseio.com",
            projectId: "wizard-sql-school",
            storageBucket: "",
            messagingSenderId: "779622015462",
            appId: "1:779622015462:web:b0ca93a1d5fbb1ea2d3627"
        };
        firebase.initializeApp(firebaseConfig);
        // @ts-ignore
        Vue.prototype.$firedb = firebase.firestore();
    }

    knew(): any {
        this.metrics('knew');
        //@ts-ignore
        this.knew_list[this.current_card] = true;

        this.next();
    }

    learned(): any {
        this.metrics('learned');
        // @ts-ignore
        this.learned_list[this.current_card] = true;
        this.next();
    }

    confusing(): any {
        this.metrics('confusing');
        // @ts-ignore
        this.confusing_list[this.current_card] = true;
        this.next();
    }

    metrics(label: string): any {
        let update: any = {}
        update[this.cards[this.current_card]] = label;
        update['timestamp'] = Math.floor(Date.now() / 1000);
        // @ts-ignore
-       this.$firedb.collection("container-flashcards").doc(this.$uuid).update(update)
    }

    next(): any {
        if (this.current_card >= this.cards.length-1) {
            this.done = true;
        } else {
            this.current_card++;
        }
    }

    uuidv4() {
        // @ts-ignore
        return ([1e7]+-1e3+-4e3+-8e3+-1e11).replace(/[018]/g, (c: any) =>
            // @ts-ignore
            (c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16)
        );
    }



    async created() {
        this.firebase()
        if (!localStorage.getItem('uuid')) {
            localStorage.setItem('uuid', this.uuidv4());
        }
        // @ts-ignore
        Vue.prototype.$uuid = localStorage.getItem('uuid');
        // @ts-ignore
        this.$firedb.collection("container-flashcards").doc(this.$uuid).set({
            timestamp: Math.floor(Date.now() / 1000),
            game_id: this.basedir,
        });

        //@ts-ignore
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
