<template>
    <div class="scene scene--card w-full" v-bind:class="{card_visible: visible, card_hidden: !visible}">
    <div v-on:click="flipped = !flipped" class="card mb-4 w-full rounded-lg border-gray-300 border-2" v-bind:class="{ flipped: flipped, normal: !small, small: small}">
        <div class="card__face card__face--front">
            <img v-bind:src="'/cards/png/' + name + '.png'">
        </div>
        <div class="card__face card__face--back">
            <img v-bind:src="'/cards/png/' + name + '-back.png'" class="bg-yellow-300" style="filter: invert();">
        </div>
    </div>
</div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

@Component
export default class Flashcard extends Vue {
    @Prop() private name!: string;
    @Prop() private small!: boolean;
    @Prop() private visible!: boolean;
    private flipped: boolean = false;
}
</script>



<style scoped>
body { font-family: sans-serif; }

.scene {
  perspective: 1200px;
  transition: all 1s ease-in-out;
}

.card.small {
  padding-bottom: 62.4%;
}

.card.normal {
  width: 500px;
  padding-bottom: 62.4%;
}

.card_visible {
    opacity: 1;
    visibility: visible;
}

.card_hidden {
    opacity: 0;
    visibility: hidden;
    height: 0px;
}

.card {
  position: relative;
  cursor: pointer;
  transform-style: preserve-3d;
  transition: transform 0.3s;
}

.card.flipped {
  transform: rotateY(-180deg);
}

.card__face {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
}

.card__face--front {
  background: white;
}

.card__face--back {
  background: white;
  transform: rotateY(180deg);
}
</style>
