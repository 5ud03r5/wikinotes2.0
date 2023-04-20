<template>
    <div>
        <div class="px-5 py-3 rounded-md shadow-md bg-slate-300">
            <div class="flex items-center w-1/2 mx-auto mb-5">
                <UniversalInput :placeholder="'Search in articles...'" class="w-5/6 focus:shadow-md" />
                <UniversalButton v-if="singleArticle" @click="singleArticle = null" class="ml-auto">Show form
                </UniversalButton>
            </div>
            <div class="flex justify-center space-x-10 ">
                <div class="flex flex-col w-1/2 h-[750px] relative">
                    <ArticleItem textClass="" class="h-[150px] bg-slate-200" v-for="article in articles" :article="article"
                        :key="article.id" @getArticle="getArticle" @showDeleteModal="onDelete" />
                    <div class="absolute bottom-0 left-0 right-0 flex items-center justify-center">
                        <UniversalPagination class="mx-auto " :currentPage="articlesPage" :totalPages="articlesTotalPages!"
                            @update:page="newValue => articlesPage = newValue" />
                    </div>
                </div>
                <div v-if="!singleArticle" class="flex w-1/2 px-2 py-5 rounded-md shadow-md bg-slate-200 h-max">
                    <ArticleForm class="w-full" :tags="tags" />
                </div>
                <div v-else class="w-1/2 h-max">
                    <ArticleItem :article="singleArticle" :textClass="'h-max'" class=" bg-slate-200" />
                </div>
            </div>
        </div>
        <teleport to="body" v-if="showDeleteModal">
            <UniversalDisplayModal :item="(article as Article)" @showDeleteModal="showDeleteModal = false"
                @deleteItem="deleteItem" />
        </teleport>
    </div>
</template>

<script setup lang="ts">
import { watchEffect, ref, Ref } from 'vue';
import { getItems, getTags, getItem, removeItem } from '../../utils/apiFetchers';
import ArticleItem from '../articles/ArticleItem.vue';
import UniversalPagination from '../UI/UniversalPagination.vue';
import UniversalInput from '../UI/UniversalInput.vue';
import ArticleForm from '../articles/ArticleForm.vue';
import UniversalButton from '../UI/UniversalButton.vue';
import { Article, Tag } from '../../utils/interfaces';
import UniversalDisplayModal from '../UI/UniversalDisplayModal.vue';

const article: Ref<Article | undefined> = ref()
const articles: Ref<Article[]> = ref([])
const articlesPage = ref(1)
const articlesTotalPages = ref(null)
const tags = ref([])
const singleArticle = ref(null)
const filterBy: Ref<Tag[]> = ref([])
const showDeleteModal = ref(false)

const getArticle = async (id: string) => {
    singleArticle.value = await getItem(id)
}

const deleteItem = (id: string) => {
    if (articles.value.length === 1) {
        articlesPage.value = articlesPage.value - 1
    }
    removeItem('articles', id).then(async () => [articles.value, articlesTotalPages.value] =
        await getItems(articlesPage.value, 'articles', 4, filterBy.value))
    showDeleteModal.value = false
}

const onDelete = (value: Article) => {
    article.value = value
    showDeleteModal.value = true
}

watchEffect(async () => [articles.value, articlesTotalPages.value] = await getItems(articlesPage.value, 'articles', 4, []))
watchEffect(async () => tags.value = await getTags())
</script>