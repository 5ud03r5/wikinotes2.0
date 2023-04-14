<template>
    <div class="">
        <UniversalInput :placeholder="'Search in articles...'" class="flex w-1/2 mx-auto mb-5 focus:shadow-xl" />
        <ArticleItem class="w-1/2 h-[150px]" v-for="article in articles" :article="article" :key="article.id" />
        <UniversalPagination class="mx-auto" :currentPage="articlesPage" :totalPages="articlesTotalPages"
            @update:page="newValue => articlesPage = newValue" />
    </div>
</template>

<script setup>
import { watchEffect, ref } from 'vue';
import { getItems } from '../../utils/apiFetchers';
import ArticleItem from '../articles/ArticleItem.vue';
import UniversalPagination from '../UI/UniversalPagination.vue';
import UniversalInput from '../UI/UniversalInput.vue';
const articles = ref([])
const articlesPage = ref(1)
const articlesTotalPages = ref(null)


watchEffect(async () => [articles.value, articlesTotalPages.value] = await getItems(articlesPage.value, 'articles', 7))
</script>