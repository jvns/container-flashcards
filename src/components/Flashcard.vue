<template>
    <div class="scene scene--card w-full" v-bind:class="{card_visible: card_visible, card_hidden: card_hidden, card_left: card_left}">
    <div v-on:click="flip" class="card mb-4 w-full rounded-lg border-gray-300 border-2" v-bind:class="{ flipped: flipped}">
        <div v-if="ribbon" class="ribbon">click card to flip!</div>
        <div class="card__face card__face--front">
            <img v-bind:src="'/cards/' + basedir + '/' + name + '.png'">
        </div>
        <div class="card__face card__face--back">
            <img v-bind:src="'/cards/' + basedir + '/' + name + '-back.png'">
        </div>
    </div>
</div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

@Component
export default class Flashcard extends Vue {
    @Prop() private name!: string;
    @Prop() private basedir!: string;
    @Prop() private card_left!: boolean;
    @Prop() private ribbon!: boolean;
    @Prop() private card_visible!: boolean;
    @Prop() private card_hidden!: boolean;
    private flipped: boolean = false;
    flip () {
        this.flipped = !this.flipped;
        this.ribbon = false;
    }
}
</script>



<style scoped>
body { font-family: sans-serif; }

.scene {
  perspective: 1200px;
  transition: all 1s ease-in-out;
}

.card_hidden {
    visibility: hidden;
    opacity: 0;
    height: 0px;
}

.card_visible {
    visibility: visible;
}

.card_left {
    visibility: hidden;
    opacity: 0;
    transform: translateX(100%); 
    height: 0px;
}

.ribbon {
    opacity: 30%;
    margin-top: 1rem;
    position: absolute;
    z-index: 1;
    background-color: #000;
    color: white;
    font-size: 1rem;
    padding: 0.25rem 0.5rem;
	-webkit-box-shadow: 0px 2px 2px #888;
	-moz-box-shadow: 0px 2px 2px #888;
	box-shadow: 0px 2px 2px #888;
}

.card {
  position: relative;
  cursor: pointer;
  transform-style: preserve-3d;
  transition: transform 0.3s;
  padding-bottom: 62.4%;
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
