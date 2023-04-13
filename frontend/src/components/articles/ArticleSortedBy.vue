<template>
    <div class="flex items-center w-full px-5 my-4 space-x-2 ">
        <p class="text-[18px] font-semibold">Filtered by:</p>
        <div class="flex mt-2 space-x-1">
            <UniversalTag v-for="tag in tags" :key="tag.id">{{ tag.name }}</UniversalTag>
        </div>
    </div>
</template>
<script setup>
import UniversalTag from '../UI/UniversalTag.vue';
const props = defineProps({
    tags: Array
})
</script>

<script>
export default {
    name: 'ArticleSortedBy'
}
</script>