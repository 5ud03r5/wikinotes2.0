<template>
    <div>
        <UniversalInput :placeholder="'Enter tags...'" :class="class" />

    </div>
</template>

<script setup>
import { ref } from 'vue';
import UniversalInput from './UniversalInput.vue';
const props = defineProps({
    tags: Array,
    class: String
})

</script>

<script>

export default {
    name: "UniversalTagInput",
    components: { UniversalInput }
}
</script>