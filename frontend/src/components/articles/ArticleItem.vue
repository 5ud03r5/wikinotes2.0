<template>
    <div class="relative px-5 py-3 m-1 bg-gray-100 rounded-md shadow-xl">
        <IconsDots @click="dropHidden = !dropHidden"
            :class="!dropHidden && 'bg-gray-700 fill-slate-100 stroke-slate-100 rounded-md shadow-md '"
            class="absolute transition-all rounded-md fill-slate-800 hover:bg-gray-400 stroke-slate-900 right-5 hover:cursor-pointer " />
        <UniversalDrop v-if="!dropHidden" @showDeleteModal="onDeleteModal(article)" />
        <p class="text-[20px] font-semibold hover:cursor-pointer overflow-clip" @click="$emit('getArticle', article.id)">{{
            article.title
        }}</p>
        <hr>
        <div :class="textClass ? 'overflow-y-scroll h-[650px]' : 'overflow-clip max-h-[70px]'">
            <VueShowdown :markdown="article.text" />
        </div>
        <div :class="textClass ? '' : 'absolute '" class="flex justify-end ml-auto space-x-1 right-2 bottom-2">
            <UniversalTag v-for="tag in article.tags" :key="tag.id">{{ tag.name }}</UniversalTag>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import IconsDots from '../icons/IconsDots.vue'
import UniversalDrop from '../UI/UniversalDrop.vue';
import UniversalTag from '../UI/UniversalTag.vue';
import { Article } from '../../utils/interfaces'

interface Props {
    article: Article;
    textClass: string;
}
const props = defineProps<Props>()
const dropHidden = ref(true)

const emit = defineEmits(['showDeleteModal', 'getArticle'])
const onDeleteModal = (item: Article) => {
    emit('showDeleteModal', item)
    dropHidden.value = true
}

</script>
<script lang="ts">
export default {
    name: "ArticleItem",
    components: { UniversalTag, UniversalDrop }
}
</script>