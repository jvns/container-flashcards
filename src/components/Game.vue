<template>
    <div>
        <h1 class="text-4xl text-center my-8 w-full"> {{title}} </h1>

        <div class="flex flex-row flex-wrap justify-center">
            <!-- put the perspective up here instead of in the flashcard because a perspective creates a new stacking context and we want everything to be in the same stacking-context -->
            <div v-if="!done" class="w-10/12 lg:w-1/3">
                <p class="text-l mb-4 text-center">
                The point of this game is to learn something, not to get them
                all "right"! The more you learn, the better. <br>(knowing the answers is ok too though)
                </p>
                <p class="text-l mb-4 text-center">
                Click the card to see the answer.
                </p>
                <div class="text-center text-xl"> Card {{current_card+1}}  of {{cards.length}} </div>
                <div class="w-full relative" style="padding-bottom: 62.5%;">
                    <div v-on:click="start" v-for="card in indexed_cards().reverse()" v-bind:class='{
                    "next": card.index == next_card,
                    }'>
                        <transition name="slide-out">
                        <Flashcard
                            class="inset-0 absolute"
                            v-if="should_display(card.index)" 
                            v-bind:ribbon='ribbon'
                            v-bind:basedir='basedir'
                            v-bind:name="card.name"
                            >
                        </Flashcard>
                        </transition>
                    </div>
                </div>
                <div class="flex flex-row flex-wrap justify-center mt-2">
                    <button class="bg-pink-600 text-white rounded px-3 py-2 mx-4 my-1" @click="button('knew')">I knew that!</button>
                    <button class="bg-blue-600 text-white rounded px-3 py-2 mx-4 my-1" @click="button('learned')">I learned something!</button>
                    <button class="bg-orange-600 text-white rounded px-3 py-2 my-1" @click="button('confusing')">That's confusing</button>
                </div>
            </div>

            <div v-if="done" class="w-10/12 lg:w-1/3">
                <Flashcard basedir='' name="thats-all" v-bind:card_visible="true"></Flashcard>
            </div>
        </div>

        <div class="flex flex-row justify-center mt-8 flex-wrap">
            <div v-for="column in columns()" class="lg:w-1/4 w-10/12 " v-bind:class='{
                    "mb-8" : !column.last,
                    "lg:ml-8" : !column.last,
                }'>
                <h1 class="text-3xl text-center">{{column.title}}</h1>
                <div class="flex flex-row justify-center flex-wrap px-8 w-full">
                    <div v-for="card in indexed_cards()" class="w-full">
                        <transition name="slide-in">
                            <Flashcard v-if="card_status[card.index] == column.id" v-bind:basedir='basedir' v-bind:name="card.name"></Flashcard>
                        </transition>
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
    private ribbon: boolean = true;
    //@ts-ignore
    private card_status = {};

    private current_card: number = 0;
    private next_card: number = 1;

    columns(): any {
        return [
            {
                title: 'Things you learned',
                id: 'learned',
            },
            {
                title: 'Things you knew',
                id: 'knew',
            },
            {
                title: '"That\'s confusing"',
                id: 'confusing',
            },
        ]
    }

    indexed_cards() { 
        var all_cards = [];
        for (let [index, card] of this.cards.entries()) {
            all_cards.push({
                name: card,
                index: index,
            });
        }
        return all_cards;
    }
    
    start() {
        this.ribbon = false;
    }

    button(result: string): any {
        this.metrics(result);
        //@ts-ignore
        this.card_status[this.current_card] = result;
        this.next();
    }

    should_display(index: number): boolean {
        return (index == this.current_card) || index == this.next_card;
    }

    next(): any {
        if (this.current_card >= this.cards.length-1) {
            this.done = true;
        } else {
            this.current_card++;
        }
        if (this.current_card < this.cards.length - 1) {
            this.next_card = this.current_card + 1;
        } else {
            this.next_card = -1;
        }
    }

    async created() {
        this.firebase()
        if (!localStorage.getItem('uuid')) {
            localStorage.setItem('uuid', this.uuidv4());
        }
        // @ts-ignore
        Vue.prototype.$uuid = localStorage.getItem('uuid');
        // @ts-ignore
        this.$firedb.collection("container-flashcards").doc(this.doc()).set({
            start_timestamp: Math.floor(Date.now() / 1000),
            game_id: this.basedir,
        });

        //@ts-ignore
    }

    // metrics stuff after this
    uuidv4() {
        // @ts-ignore
        return ([1e7]+-1e3+-4e3+-8e3+-1e11).replace(/[018]/g, (c: any) =>
            // @ts-ignore
            (c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16)
        );
    }

    doc(): any {
        // @ts-ignore
        return this.$uuid + '--' + this.basedir
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

    metrics(label: string): any {
        let update: any = {}
        update[this.cards[this.current_card]] = label;
        update['timestamp'] = Math.floor((new Date()).getTime() / 1000);
        // @ts-ignore
        this.$firedb.collection("container-flashcards").doc(this.doc()).update(update)
    }


}
</script>

<style scoped>
.slide-in-enter-active {
    transition: all 1s ease;
}

.slide-in-enter {
    transform: translateX(100%); 
    opacity: 0;
}

.slide-out-leave-active {
    transition: all 1s ease-in-out;
}

.slide-out-leave-to {
    transform: translateX(100%); 
    opacity: 0;
}

.next {
    opacity: 0;
}
</style>
