<template>
    <div class="mx-auto ">
        <MenuBar class="" />

        <section class="flex space-x-2 m-1 " v-if="articlesShow">
            <div class="w-1/2 bg-indigo-50 p-4 rounded-md relative">
                <label class="m-1 text-[40px] font-bold">Articles</label>
                <div @click="createItem('articles', { title: 'article', text: 'test art', tags: [{ name: 'one' }, { name: 'two' }] })"
                    class="bg-gray-900 px-2 py-1 hover:cursor-pointer w-max text-gray-100">Test create
                </div>
                <hr class="my-5" />
                <UniversalInput :placeholder="'Search in articles...'" class="w-1/3 focus:shadow-md" />
                <ArticleItem v-for="article in articles" :article="article" :key="article.id" @showDeleteModal="onDelete" />
                <div class="flex justify-center absolute bottom-0 ml-auto mr-auto right-0 left-0 items-center">
                    <UniversalPagination :currentPage="articlesPage" :totalPages="articlesTotalPages"
                        @update:page="newValue => articlesPage = newValue" />
                </div>

            </div>
            <div class="w-1/2 bg-indigo-50 p-4 rounded-md">
                <label class="m-1 text-[40px] font-bold">Create article</label>
                <div @click="createItem('articles', { title: 'article', text: 'test art', tags: [{ name: 'one' }, { name: 'two' }] })"
                    class="bg-gray-900 px-2 py-1 hover:cursor-pointer w-max text-gray-100">Test create
                </div>
                <hr class="my-5" />
                <form @submit.prevent="articleValidation" class="flex flex-col space-y-2">
                    <UniversalInput :placeholder="'Article title...'" class="focus:shadow-md"
                        @update:value="newValue => articleTitle = newValue" :value="articleTitle" />
                    <UniversalTextarea :placeholder="'Article text...'" class="focus:shadow-md"
                        @update:value="newValue => articleText = newValue" :value="articleText" />
                    <UniversalButton class="ml-auto text-[25px]">Create article</UniversalButton>
                </form>
            </div>

        </section>

        <section class="flex space-x-2 m-1" v-if="notesShow">
            <div class="w-1/2 bg-indigo-50 p-4 rounded-md relative ">
                <label class="m-1 text-[40px] font-bold">Notes</label>
                <hr class="my-5" />
                <UniversalInput :placeholder="'Search in notes...'" class="focus:shadow-md" />
                <NoteItem v-for="note in notes" :note="note" :key="note.id" />
                <div class="flex justify-center absolute bottom-0 ml-auto mr-auto right-0 left-0 items-center">
                    <UniversalPagination :currentPage="notesPage" :totalPages="notesTotalPages"
                        @update:page="newValue => notesPage = newValue" />
                </div>

            </div>


            <div class="w-1/2 bg-indigo-50 p-4 rounded-md">
                <label class="m-1 text-[40px] font-bold">Create Note</label>
                <hr class="my-5" />
                <form @submit.prevent="noteValidation" class="flex flex-col space-y-2">

                    <UniversalTextarea :placeholder="'Note text...'" class="focus:shadow-md"
                        @update:value="newValue => noteText = newValue" :value="noteText" />
                    <UniversalButton class="ml-auto text-[25px]">Create note</UniversalButton>
                </form>
            </div>

        </section>
        <teleport to="body" v-if="showDeleteModal">
            <UniversalDisplayModal :item="title" @showDeleteModal="showDeleteModal = false" @deleteItem="deleteItem" />
        </teleport>

    </div>
</template>
<script setup>
import ArticleItem from '../articles/ArticleItem.vue';
import MenuBar from '../MenuBar.vue';
import NoteItem from '../notes/NoteItem.vue';
import UniversalButton from '../UI/UniversalButton.vue'
import UniversalInput from '../UI/UniversalInput.vue';
import { watchEffect, ref } from 'vue';
import { getItems, createItem, removeItem } from '../../utils/apiFetchers'
import UniversalPagination from '../UI/UniversalPagination.vue';
import { useUiStore } from '../../store/ui';
import { storeToRefs } from 'pinia';
import UniversalTextarea from '../UI/UniversalTextarea.vue';
import UniversalDisplayModal from '../UI/UniversalDisplayModal.vue';


const store = useUiStore()
const { articlesShow, notesShow, chatShow } = storeToRefs(store)
const articles = ref([])
const articlesPage = ref(1)
const articlesTotalPages = ref(null)
const notes = ref([])
const notesPage = ref(1)
const notesTotalPages = ref(null)
const noteText = ref('')
const articleText = ref('')
const articleTitle = ref('')
const showDeleteModal = ref(false)
const title = ref('')

const deleteItem = (id) => {
    removeItem('articles', id).then(showDeleteModal.value = false)

}

const onDelete = (value) => {
    title.value = value
    showDeleteModal.value = true
}

const noteValidation = () => {
    if (noteText.value.trim().length > 0) {
        createItem('notes', { text: noteText.value })
        noteText.value = ''
    }
}

const articleValidation = () => {
    if (articleText.value.trim().length > 0 && articleTitle.value.trim().length > 0) {
        createItem('articles', { title: articleTitle.value, text: articleText.value, tags: [] })
        articleText.value = ''
        articleTitle.value = ''
    }
}

watchEffect(async () => [articles.value, articlesTotalPages.value] = await getItems(articlesPage, 'articles', 3))
watchEffect(async () => [notes.value, notesTotalPages.value] = await getItems(notesPage, 'notes', 3))
</script>
<script>
export default {
    name: "DashboardPage",
    components: { MenuBar, UniversalPagination, UniversalTextarea, UniversalDisplayModal }
}
</script>