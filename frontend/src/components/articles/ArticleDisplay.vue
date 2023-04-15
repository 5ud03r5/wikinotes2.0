<template>
    <div class="">
        <div class="mb-4">
            <UniversalLabel>Articles</UniversalLabel>
        </div>


        <div class="flex space-x-2">
            <UniversalInput :placeholder="'Search in articles...'" class="w-1/3 focus:shadow-md" />
            <div class="relative w-1/3">
                <UniversalInput :placeholder="'Enter tags...'" class=" focus:shadow-md" :value="filter"
                    @update:value="newValue => filter = newValue" />
                <div v-if="filteredTags.length > 0 && showTags"
                    class="bg-gray-100 outline outline-1  outline-gray-200 p-1 absolute top-12 rounded-md shadow-md w-[200px] mx-1 z-[200]">
                    <div v-for="tag in filteredTags" :key="tag.id" @click="addToList(tag)"
                        class="px-2 m-1 hover:cursor-pointer hover:bg-gray-700 hover:text-gray-100 ">
                        {{ tag.name }}
                    </div>
                </div>
            </div>
        </div>
        <ArticleSortedBy v-if="filterBy.length > 0" :tags="filterBy" @update:value="deleteTags">Filtered by:
        </ArticleSortedBy>
        <ArticleItem v-for="article in articles" :article="article" :key="article.id" @showDeleteModal="onDelete"
            class="h-[150px]" />
        <div class="mt-10"></div>
        <div class="absolute bottom-0 left-0 right-0 flex items-center justify-center">
            <UniversalPagination :currentPage="articlesPage" :totalPages="articlesTotalPages"
                @update:page="newValue => articlesPage = newValue" />
        </div>
    </div>
    <teleport to="body" v-if="showDeleteModal">
        <UniversalDisplayModal :item="title" @showDeleteModal="showDeleteModal = false" @deleteItem="deleteItem" />
    </teleport>
</template>
<script setup>
import UniversalLabel from '../UI/UniversalLabel.vue'
import UniversalInput from '../UI/UniversalInput.vue';
import ArticleSortedBy from './ArticleSortedBy.vue';
import ArticleItem from './ArticleItem.vue';
import UniversalPagination from '../UI/UniversalPagination.vue';
import { getItems, removeItem } from '../../utils/apiFetchers';
import UniversalDisplayModal from '../UI/UniversalDisplayModal.vue';
import { ref, watch, watchEffect } from 'vue';
const props = defineProps({
    tagsProp: Array
})


const filter = ref('')
const filteredTags = ref([])
const filterBy = ref([])
const tags = ref(props.tagsProp)
const showTags = ref(false)
const articles = ref([])
const articlesPage = ref(1)
const articlesTotalPages = ref(null)
const showDeleteModal = ref(false)
const title = ref('')

const deleteItem = (id) => {
    if (articles.value.length === 1) {
        articlesPage.value = articlesPage.value - 1
    }
    removeItem('articles', id).then(showDeleteModal.value = false).finally(async () => [articles.value, articlesTotalPages.value] =
        await getItems(articlesPage.value, 'articles', 3, filterBy.value))
}

const addToList = (tag) => {
    filterBy.value.push(tag)
    tags.value = tags.value.filter(item => item.name !== tag.name)
    filteredTags.value = filteredTags.value.filter(item => item.name !== tag.name)
    filter.value = ''
}

const deleteTags = (tag) => {
    filterBy.value = filterBy.value.filter(item => item.name !== tag.name)
    tags.value.push(tag)

}

const onDelete = (value) => {
    title.value = value
    showDeleteModal.value = true
}

watch(filter, () => {
    if (tags.value.length > 0 && filter.value.length > 0) {
        filteredTags.value = tags.value.filter(tag => tag.name.includes(filter.value))
        showTags.value = true
    } else {
        filteredTags.value = []
        showTags.value = false
    }
})

watch(articlesTotalPages, () => {
    if (articlesPage.value > articlesTotalPages.value) {
        articlesPage.value = articlesTotalPages.value
    }
})

watch(props, () => {
    tags.value = props.tagsProp
})

watchEffect(async () => [articles.value, articlesTotalPages.value] = await getItems(articlesPage.value, 'articles', 3, filterBy.value))
</script>
