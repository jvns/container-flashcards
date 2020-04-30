<template>
    <div id="app" class="px-16 py-8">
        <h1 class="text-3xl text-center">flashcards!</h1>
        <div class="lg:w-1/3 w-full m-auto">
        <p class="py-4">
        Here are all the sets of flashcards so far:
        </p>
        <p class="underline text-blue-800">
        <ul>
            <li><a class="hover:text-blue-400" href="/container-basics">Container basics</a></li>
            <!-- <li><a class="hover:text-blue-400" href="/advanced-containers">More containers</a></li> -->
            <li><a class="hover:text-blue-400" href="/linux">Linux</a></li>
            <li><a class="hover:text-blue-400" href="/dns">DNS</a></li>
            <li><a class="hover:text-blue-400" href="/tls">TLS</a></li>
            <li><a class="hover:text-blue-400" href="/network-packets">Network packets</a></li>
            <!-- <li><a class="hover:text-blue-400" href="/HTTP">HTTP</a></li> -->
            <li><a class="hover:text-blue-400" href="/sql-basics">SQL basics</a></li>
        </ul>
        </p>
        </div>
    </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

export default class Main extends Vue {
}
</script>
