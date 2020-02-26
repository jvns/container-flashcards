<template>
    <div class="scene mb-3">
        <transition name="card-flip" mode="out-in">
        <div v-if="!flipped" v-on:click="flipped = !flipped" key="front">
            <img v-bind:src="'/cards/' + name + '.svg'" class="px-2 w-full rounded-lg border border-gray-200">
        </div>
        <div v-else v-on:click="flipped = !flipped" key="back">
            <img v-bind:src="'/cards/' + name + '-back.svg'" class="px-2 bg-yellow-300 w-full rounded-lg border border-gray-200" style="filter: invert()">
        </div>
        </transition>
    </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

@Component
export default class Flashcard extends Vue {
    @Prop() private name!: string;
    private flipped: boolean = false;
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
