<template>
<div class="scene scene--card">
    <div v-on:click="flipped = !flipped" class="card" v-bind:class="{ flipped: flipped }">
    <div class="card__face card__face--front">
        <img v-bind:src="'/cards/' + name + '.png'">
    </div>
    <div class="card__face card__face--back">
      <img v-bind:src="'/cards/' + name + '-back.png'">
    </div>
  </div>
</div>
            <!--
    <div class="scene mb-3">
            <div v-bind:src="'/cards/' + name + '.png'" class="card__face--front card__face px-2 w-full rounded-lg border border-gray-200" >
            <div class="card__face--back card__face px-2 bg-yellow-300 w-full rounded-lg border border-gray-200" style="">
                hi
                <!--             </div>
            <img v-bind:src="'/cards/' + name + '-back.png'" class="fake px-2">
        </div>
        </transition>
    </div>
            -->
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
body { font-family: sans-serif; }

.scene {
  border: 1px solid #CCC;
  margin: 40px 0;
  perspective: 600px;
}

.card {
  position: relative;
  width: 500px;
  height: 312px;
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
