<template>
    <div class="py-4" style="width: 400px">
        <div class="front">
            Front
        </div>
        <div class="back">
            Back!
        </div>
    </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

@Component
export default class Flashcard extends Vue {
}
</script>


