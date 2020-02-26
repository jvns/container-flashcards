<template>
    <div class="scene py-4">
        <transition name="card-flip" mode="out-in">
        <div v-if="!flipped" v-on:click="flipped = !flipped" key="front">
            <img v-bind:src="'/cards/' + front" class="w-full">
        </div>
        <div v-else v-on:click="flipped = !flipped" key="back" class="bg-pink-200">
            <img v-bind:src="'/cards/' + back" class="w-full">
        </div>
        </transition>
    </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

@Component
export default class Flashcard extends Vue {
    @Prop() private front!: string;
    @Prop() private back!: string;
    @Prop() private width: string;
    private flipped: boolean = false;

    async created() {
        this.flipped = false;
    }
}
</script>



<style scoped>
.scene {
    perspective: 1300px;
}
.card {
    backface-visibility: hidden;
}

.card-flip-enter-active {
  transition: all .15s;
  transform-style: preserve-3d;
}
.card-flip-leave-active {
  transition: all .15s;
  transform-style: preserve-3d;
}
.card-flip-enter 
/* .slide-fade-leave-active below version 2.1.8 */ {
  transform: rotateY(90deg);
}

.card-flip-leave-to  {
  transform: rotateY(-90deg);
}
</style>
