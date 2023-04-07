<template>
    <div class="flex space-x-2 m-1 flex-wrap w-1/2 justify-center">
        <div :class="currentPage === item ? 'bg-pink-700 hover:bg-pink-500' : 'bg-gray-900 hover:bg-gray-700'"
            class="px-2 m-1 py-1 text-gray-100 rounded-sm hover:shadow-md hover:cursor-pointer transition-all"
            @click="$emit('update:page', item)" v-for="item in totalPages" :key="item">
            {{ item }}
        </div>
    </div>
</template>
<script setup>
const props = defineProps({
    totalPages: Number,
    currentPage: Number
})
const emit = defineEmits(['update:page'])

</script>