<template>
    <div class="">
        <div class="mb-4 ">
            <UniversalLabel>Articles</UniversalLabel>
        </div>
        <div class="flex flex-wrap">
            <form @submit.prevent="searchFinal = search" class="">
                <UniversalInput :placeholder="'Search in articles...'" class="focus:shadow-md" :value="search"
                    @update:value="(newValue: string) => search = newValue" />
            </form>
            <div class="relative ">
                <UniversalInput :placeholder="'Enter tags...'" class=" focus:shadow-md" :value="filter"
                    @update:value="(newValue: string) => filter = newValue" />
                <div v-if="filteredTags.length > 0 && showTags"
                    class="bg-gray-100 outline outline-1  outline-gray-200 p-1 absolute top-12 rounded-md shadow-md w-[200px] mx-1 z-[200]">
                    <div v-for="tag in filteredTags" :key="tag.id" @click="addToList(tag)"
                        class="px-2 m-1 hover:cursor-pointer hover:bg-gray-700 hover:text-gray-100 ">
                        {{ tag.name }}
                    </div>
                </div>
            </div>
        </div>
        <ArticleSortedBy :tags="filterBy" @update:value="deleteTags">{{ filterBy.length > 0 ?
            '' : 'No filters applied' }}
        </ArticleSortedBy>
        <ArticleItem textClass="" v-for="article in articles" :article="article" :key="article.id"
            @showDeleteModal="onDelete" class="h-[180px]" />
        <div class="mt-10"></div>
        <div class="absolute bottom-0 left-0 right-0 flex items-center justify-center">
            <UniversalPagination :currentPage="articlesPage" :totalPages="articlesTotalPages!"
                @update:page="(newValue: number) => articlesPage = newValue" />
        </div>
    </div>
    <teleport to="body" v-if="showDeleteModal">
        <UniversalDisplayModal :item="(article as Article)" @showDeleteModal="showDeleteModal = false"
            @deleteItem="deleteItem" />
    </teleport>
</template>
<script setup lang="ts">
import UniversalLabel from '../UI/UniversalLabel.vue';
import UniversalInput from '../UI/UniversalInput.vue';
import ArticleSortedBy from './ArticleSortedBy.vue';
import ArticleItem from './ArticleItem.vue';
import UniversalPagination from '../UI/UniversalPagination.vue';
import { getItems, removeItem } from '../../utils/apiFetchers';
import UniversalDisplayModal from '../UI/UniversalDisplayModal.vue';
import { Ref, ref, watch, watchEffect } from 'vue';
import { Article, Tag } from '../../utils/interfaces'



interface Props {
    tags: Tag[]
}

const props = defineProps<Props>()

const searchFinal = ref('')
const search = ref('')
const filter = ref('')
const filteredTags: Ref<Tag[]> = ref([])
const filterBy: Ref<Tag[]> = ref([])
const tags = ref(props.tags)
const showTags = ref(false)
const articles: Ref<Article[]> = ref([])
const articlesPage = ref(1)
const articlesTotalPages = ref(null)
const showDeleteModal = ref(false)
const article: Ref<Article | undefined> = ref(undefined)

const deleteItem = (id: string) => {
    if (articles.value.length === 1) {
        articlesPage.value = articlesPage.value - 1
    }
    removeItem('articles', id).then(async () => [articles.value, articlesTotalPages.value] =
        await getItems(articlesPage.value, 'articles', 3, filterBy.value))
    showDeleteModal.value = false
}

const addToList = (tag: Tag) => {
    filterBy.value.push(tag)
    tags.value = tags.value.filter(item => item.name !== tag.name)
    filteredTags.value = filteredTags.value.filter(item => item.name !== tag.name)
    filter.value = ''
}

const deleteTags = (tag: Tag) => {
    filterBy.value = filterBy.value.filter(item => item.name !== tag.name)
    tags.value.push(tag)

}

const onDelete = (value: Article) => {
    article.value = value
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

    if (articlesPage.value > articlesTotalPages.value!) {
        articlesPage.value = articlesTotalPages.value!
    }
    if (articlesPage.value === 0 && articlesTotalPages.value! > 0) {
        articlesPage.value = 1
    }

})

watch(props, () => {
    tags.value = props.tags
})

watchEffect(async () => [articles.value, articlesTotalPages.value] = await getItems(articlesPage.value, 'articles', 3, filterBy.value, searchFinal.value))
</script>
