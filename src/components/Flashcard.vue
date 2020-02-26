<template>
    <div class="scene py-4">
        <transition name="card-flip" mode="out-in">
        <div v-if="!flipped" v-on:click="flipped = !flipped" class="card text-center text-blue-800 bg-white border rounded-lg p-8" key="front">
            <p v-html="front" class="text-3xl">
            </p>
        </div>
        <div v-else v-on:click="flipped = !flipped" class="card text-center bg-blue-800 text-blue-100 border rounded-lg p-8" key="back">
            <p v-html="back" class="text-3xl">
            </p>
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
    width: 450px;
    height: 300px;
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
