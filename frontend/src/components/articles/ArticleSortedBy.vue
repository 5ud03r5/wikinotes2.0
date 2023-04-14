<template>
    <div class="flex flex-col w-full px-2 my-4 i ">
        <p class="text-[20px] font-semibold text-slate-700 font-mono">
            <slot></slot>
        </p>
        <div class="flex mt-2 space-x-1">
            <UniversalTag v-for="tag in tags" :key="tag.id" class="flex items-center text-[16px]  pr-1">{{ tag.name }}
                <IconsX @click="$emit('update:value', tag)"
                    class="w-8 h-8 transition-all hover:cursor-pointer hover:fill-pink-500" />
            </UniversalTag>
        </div>
    </div>
</template>
<script setup>
import UniversalTag from '../UI/UniversalTag.vue';
import IconsX from '../icons/IconsX.vue'
const emit = defineEmits(['update:value'])
const props = defineProps({
    tags: Array
})
</script>

<script>
export default {
    name: 'ArticleSortedBy'
}
</script>