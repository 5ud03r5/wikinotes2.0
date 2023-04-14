<template>
    <div class="relative px-5 py-3 m-1 rounded-md shadow-xl bg-slate-100">
        <IconsDots @click="dropHidden = !dropHidden"
            :class="!dropHidden && 'bg-gray-700 fill-slate-100 stroke-slate-100 rounded-md shadow-md '"
            class="absolute transition-all rounded-md fill-slate-800 hover:bg-gray-400 stroke-slate-900 right-5 hover:cursor-pointer " />
        <UniversalDrop v-if="!dropHidden" @showDeleteModal="onDeleteModal({ id: article.id, title: article.title })" />
        <p class="text-[20px] font-semibold">{{ article.title }}</p>
        <div class="truncate overflow-clip max-h-[70px]">
            <VueShowdown :markdown="article.text" />
        </div>

        <div class="absolute flex justify-end mt-2 space-x-1 bottom-2 right-2">
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