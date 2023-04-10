<template>
    <div class="shadow-xl bg-slate-100 py-3 px-5 m-1 rounded-md relative">
        <IconsDots @click="dropHidden = !dropHidden"
            :class="!dropHidden && 'bg-gray-700 fill-slate-100 stroke-slate-100 rounded-md shadow-md '"
            class="fill-slate-800 transition-all hover:bg-gray-400 rounded-md stroke-slate-900 absolute right-5 hover:cursor-pointer " />
        <UniversalDrop v-if="!dropHidden" @showDeleteModal="onDeleteModal({ id: article.id, title: article.title })" />
        <p class="text-[20px] font-semibold">{{ article.title }}</p>
        <p class="">{{ article.text }}</p>
        <div class="flex justify-end space-x-1 mt-2">
            <UniversalTag v-for="tag in article.tags" :key="tag.id">{{ tag.name }}</UniversalTag>
        </div>

    </div>
</template>

<script setup>
import { ref } from 'vue';
import IconsDots from '../icons/IconsDots.vue'
import UniversalDrop from '../UI/UniversalDrop.vue';
import UniversalTag from '../UI/UniversalTag.vue';
const dropHidden = ref(true)
const props = defineProps({
    article: Object
})

const emit = defineEmits(['showDeleteModal'])
const onDeleteModal = (item) => {
    emit('showDeleteModal', item)
    dropHidden.value = true
}

</script>
<script>
export default {
    name: "ArticleItem",
    components: { UniversalTag, UniversalDrop }
}
</script>