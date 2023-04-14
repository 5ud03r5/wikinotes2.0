<template>
    <div class="relative w-1/3">
        <input autocomplete="off" autocorrect="off" @input="$emit('update:filter', $event.target.value)" :value="filter"
            class="px-3 py-2 m-1 placeholder:italic bg-slate-100 outline-1 outline outline-slate-300 rounded-xl"
            placeholder="Enter tags..." />
        <div v-if="filteredTags.length > 0 && showTags"
            class="bg-gray-100 outline outline-1  outline-gray-200 p-1 top-12 rounded-md shadow-md w-[200px] mx-1 z-[200]">
            <div v-for="tag in filteredTags" :key="tag.id" @click="addToList(tag)"
                class="px-2 m-1 hover:cursor-pointer hover:bg-gray-700 hover:text-gray-100 ">
                {{ tag.name }}
            </div>
        </div>
    </div>
</template>

<script setup>
import { watch } from 'vue';


const showTags = (false)
const props = defineProps({
    filteredTags: Array,
    showTags: Boolean,
    filter: String,
})
const emit = defineEmits(['addToList', 'update:filter'])

watch(props, () => {
    console.log(props.showTags, props.filteredTags.length)
})

const addToList = (tag) => {
    emit('addToList', tag)
    emit('update:filter', '')
}

</script>

