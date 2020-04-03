<template>
    <div class="scene w-full" v-on:click="flip">
        <div class="card relative border-gray-300 border-2 rounded-lg no_highlights mb-4 w-full" v-bind:class="{ flipped: flipped }">
            <div v-if="ribbon" class="ribbon">click card to flip!</div>
            <!-- use object instead of img so that we don't have to embed the font in every svg -->
            <img class="absolute inset-0 w-full card__face" v-bind:src="'/cards/' + basedir + '/' + name + '.png'"></object>
            <img class="absolute inset-0 w-full card__face card__face--back"  v-bind:src="'/cards/' + basedir + '/' + name + '-back.png'"></object>
        </div>
    </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

@Component
export default class Flashcard extends Vue {
    @Prop() private name!: string;
    @Prop() private basedir!: string;
    @Prop() private ribbon!: boolean;
    private flipped: boolean = false;
    flip () {
        this.flipped = !this.flipped;
    }
}
</script>

<style scoped>
.scene {
    perspective: 1200px;
}

object {
    pointer-events: none;
    width: 100%;
}

.no_highlights {
  -webkit-tap-highlight-color: transparent;
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.ribbon {
    opacity: 50%;
    margin-top: 1rem;
    position: absolute;
    z-index: 1;
    background-color: #444;
    color: white;
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
  padding-bottom: 62.5%;
}

.card.flipped {
  transform: rotateY(-180deg);
}

.card__face {
  backface-visibility: hidden;
  background: white;
}

.card__face--back {
  transform: rotateY(180deg);
}
</style>
