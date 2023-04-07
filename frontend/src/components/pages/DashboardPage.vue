<template>
    <div class="mx-auto ">
        <MenuBar class="" />

        <section class="bg-indigo-50 p-4 rounded-md" v-if="articlesShow">
            <label class="m-1 text-[40px] font-bold">Articles</label>
            <div @click="createItem('articles', { title: 'article', text: 'test art', tags: [{ name: 'one' }, { name: 'two' }] })"
                class="bg-gray-900 px-2 py-1 hover:cursor-pointer w-max text-gray-100">Test create
            </div>
            <hr class="my-5" />
            <UniversalSearch :placeholder="'Search in articles...'" class="w-1/3 focus:shadow-md" />
            <ArticleItem class="w-1/2 " v-for="article in articles" :article="article" :key="article.id" />
            <UniversalPagination :currentPage="articlesPage" :totalPages="articlesTotalPages"
                @update:page="newValue => articlesPage = newValue" />

        </section>

        <section class="bg-indigo-50 p-4 rounded-md mt-2" v-if="notesShow">
            <label class="m-1 text-[40px] font-bold">Notes</label>
            <div @click="createItem('notes', { text: 'test note' })"
                class="bg-gray-900 px-2 py-1 hover:cursor-pointer w-max text-gray-100">Test create
            </div>

            <hr class="my-5" />
            <UniversalSearch :placeholder="'Search in notes...'" class="w-1/3 focus:shadow-md" />
            <NoteItem v-for="note in notes" :note="note" :key="note.id" />
            <UniversalPagination :currentPage="notesPage" :totalPages="notesTotalPages"
                @update:page="newValue => notesPage = newValue" />
        </section>

    </div>
</template>
<script setup>
import ArticleItem from '../articles/ArticleItem.vue';
import MenuBar from '../MenuBar.vue';
import NoteItem from '../notes/NoteItem.vue';
import UniversalSearch from '../UI/UniversalSearch.vue';
import { watchEffect, ref } from 'vue';
import { getItems, createItem } from '../../utils/apiFetchers'
import UniversalPagination from '../UI/UniversalPagination.vue';
import { useUiStore } from '../../store/ui';
import { storeToRefs } from 'pinia';

const store = useUiStore()
const { articlesShow, notesShow, chatShow } = storeToRefs(store)
const articles = ref([])
const articlesPage = ref(1)
const articlesTotalPages = ref(null)
const notes = ref([])
const notesPage = ref(1)
const notesTotalPages = ref(null)


watchEffect(async () => [articles.value, articlesTotalPages.value] = await getItems(articlesPage, 'articles', 3))
watchEffect(async () => [notes.value, notesTotalPages.value] = await getItems(notesPage, 'notes', 3))
</script>
<script>
export default {
    name: "DashboardPage",
    components: { MenuBar, UniversalPagination }
}
</script>