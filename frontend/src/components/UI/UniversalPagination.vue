<template>
    <div class="flex justify-center flex-auto w-1/2 m-1 space-x-2 ">
        <div :class="currentPage === item ? 'bg-slate-400 hover:bg-slate-500 text-gray-900' : 'bg-gray-900 hover:bg-gray-700 text-gray-100'"
            class="px-2 py-1 m-1 transition-all rounded-sm hover:shadow-md hover:cursor-pointer"
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