<template>
    <div class="shadow-xl bg-slate-100 py-3 px-5 m-1 rounded-md relative">
        <IconsDots class="fill-slate-800 stroke-slate-900 absolute right-5 hover:cursor-pointer" />
        <p class="">{{ note.text }}</p>
        <div class="flex justify-end space-x-1 mt-2">
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