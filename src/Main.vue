<template>
    <div id="app" class="px-16 py-8">
        <h1 class="text-3xl text-center">flashcards!</h1>
        <p class="py-4">
        Here are the 2 sets of flashcards so far:
        <br><br>
        </p>
        <p class="underline text-blue-800">
        <a class="hover:text-blue-400" href="/container-basics">Container basics</a><br>
        <a class="hover:text-blue-400" href="/linux">Linux</a>
        </p>
    </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

export default class Main extends Vue {
}
</script>
