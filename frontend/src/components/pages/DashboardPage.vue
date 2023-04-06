<template>
    <div class="mx-auto ">
        <MenuBar class="" />

        <section class="bg-indigo-50 p-4 rounded-md">
            <label class="m-1 text-[40px] font-bold">Articles</label>
            <hr class="my-5" />
            <UniversalSearch :placeholder="'Search in articles...'" class="w-1/3 focus:shadow-md" />
            <ArticleItem v-for="article in articles" :article="article" :key="article.id" />
        </section>

        <section class="bg-indigo-50 p-4 rounded-md mt-2">
            <label class="m-1 text-[40px] font-bold">Notes</label>
            <hr class="my-5" />
            <UniversalSearch :placeholder="'Search in notes...'" class="w-1/3 focus:shadow-md" />
            <NoteItem v-for="note in notes" :note="note" :key="note.id" />
        </section>

    </div>
</template>
<script setup>
import ArticleItem from '../articles/ArticleItem.vue';
import MenuBar from '../MenuBar.vue';
import NoteItem from '../notes/NoteItem.vue';
import UniversalSearch from '../UI/UniversalSearch.vue';
import { watchEffect, ref } from 'vue';
const articles = ref([])
const notes = ref([])
const getArticles = async () => {
    const response = await fetch(import.meta.env.VITE_BACKEND + '/articles')
    if (!response.ok) {
        throw Error('Something went wrong')
    }
    articles.value = await response.json()

}
const getNotes = async () => {
    const response = await fetch(import.meta.env.VITE_BACKEND + '/notes')
    if (!response.ok) {
        throw Error('Something went wrong')
    }
    notes.value = await response.json()

}
watchEffect(getArticles)
watchEffect(getNotes)
</script>
<script>
export default {
    name: "DashboardPage",
    components: { MenuBar }
}
</script>