<template>
    <div class="relative px-5 py-3 m-1 bg-gray-100 rounded-md shadow-xl">
        <IconsDots class="absolute fill-slate-800 stroke-slate-900 right-5 hover:cursor-pointer" />
        <p class="">{{ note.text }}</p>
        <div class="flex justify-end mt-2 space-x-1">
            <UniversalTag v-for="tag in note.tags" :key="tag.id">{{ tag.name }}</UniversalTag>
        </div>

    </div>
</template>

<script setup>
import IconsDots from '../icons/IconsDots.vue'
import UniversalTag from '../UI/UniversalTag.vue';
const props = defineProps({
    note: Object
})

</script>
<script>
export default {
    name: "NoteItem",
    components: { UniversalTag }
}
</script>