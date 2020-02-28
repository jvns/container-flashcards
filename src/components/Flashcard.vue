<template>
<div class="scene scene--card w-full">
    <div v-on:click="flipped = !flipped" class="card w-full rounded-lg border-gray-300 border-2" v-bind:class="{ flipped: flipped, normal: !small, small: small}">
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
    private flipped: boolean = false;
}
</script>



<style scoped>
body { font-family: sans-serif; }

.scene {
  margin: 40px 0;
  perspective: 1200px;
}

.card.small {
  padding-bottom: 62.4%
}

.card.normal {
  width: 500px;
  padding-bottom: 62.4%
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
