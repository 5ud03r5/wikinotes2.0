<template>
    <div class="relative px-5 py-3 m-1 bg-gray-100 rounded-md shadow-xl">
        <IconsDots class="absolute fill-slate-800 stroke-slate-900 right-5 hover:cursor-pointer" />
        <p class="">{{ note.text }}</p>


    </div>
</template>

<script setup lang="ts">
import IconsDots from '../icons/IconsDots.vue'
import UniversalTag from '../UI/UniversalTag.vue';
import { Note } from '../../utils/interfaces';

interface Props {
    note: Note
}
const props = defineProps<Props>()

</script>
<script lang="ts">
export default {
    name: "NoteItem",
    components: { UniversalTag }
}
</script>