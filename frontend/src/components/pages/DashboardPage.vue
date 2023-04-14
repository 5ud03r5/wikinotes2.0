<template>
    <div class="mx-auto ">
        <MenuBar class="" />

        <section class="flex m-1 space-x-2 " v-if="articlesShow">
            <div class="relative w-1/2 p-4 rounded-md bg-indigo-50">
                <label class="m-1 text-[40px] font-bold">Articles</label>
                <div @click="createItem('articles', { title: 'article', text: 'test art', tags: [{ name: 'two' }] })"
                    class="px-2 py-1 text-gray-100 bg-gray-900 hover:cursor-pointer w-max">Test create
                </div>
                <hr class="my-5" />
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
                <ArticleSortedBy v-if="filterBy.length > 0" :tags="filterBy" @update:value="deleteTags" />
                <ArticleItem v-for="article in articles" :article="article" :key="article.id" @showDeleteModal="onDelete"
                    class="h-[150px]" />
                <div class="mt-10"></div>
                <div class="absolute bottom-0 left-0 right-0 flex items-center justify-center">
                    <UniversalPagination :currentPage="articlesPage" :totalPages="articlesTotalPages"
                        @update:page="newValue => articlesPage = newValue" />
                </div>




            </div>
            <div class="w-1/2 p-4 rounded-md bg-indigo-50">
                <label class="m-1 text-[40px] font-bold">Create article</label>
                <div @click="createItem('articles', { title: 'article', text: 'test art', tags: [{ name: 'one' }, { name: 'two' }] })"
                    class="px-2 py-1 text-gray-100 bg-gray-900 hover:cursor-pointer w-max">Test create
                </div>
                <hr class="my-5" />
                <form @submit.prevent="articleValidation" class="flex flex-col space-y-2">
                    <div class="flex space-x-2">
                        <UniversalInput :placeholder="'Article title...'" class="focus:shadow-md"
                            @update:value="newValue => articleTitle = newValue" :value="articleTitle" />
                        <UniversalTagInput class="ml-auto" />
                    </div>

                    <UniversalTextarea :placeholder="'Article text...'" class="focus:shadow-md"
                        @update:value="newValue => articleText = newValue" :value="articleText" />
                    <UniversalButton class="ml-auto ">Create article</UniversalButton>
                </form>
            </div>

        </section>

        <section class="flex m-1 space-x-2" v-if="notesShow">
            <div class="relative w-1/2 p-4 rounded-md bg-indigo-50 ">
                <label class="m-1 text-[40px] font-bold">Notes</label>
                <hr class="my-5" />
                <UniversalInput :placeholder="'Search in notes...'" class="focus:shadow-md" />
                <NoteItem v-for="note in notes" :note="note" :key="note.id" />
                <div class="absolute bottom-0 left-0 right-0 flex items-center justify-center w-1/2 ml-auto mr-auto">
                    <UniversalPagination :currentPage="notesPage" :totalPages="notesTotalPages"
                        @update:page="newValue => notesPage = newValue" />
                </div>
            </div>
            <div class="w-1/2 p-4 rounded-md bg-indigo-50">
                <label class="m-1 text-[40px] font-bold">Create Note</label>
                <hr class="my-5" />
                <form @submit.prevent="noteValidation" class="flex flex-col space-y-2">

                    <UniversalTextarea :placeholder="'Note text...'" class="focus:shadow-md"
                        @update:value="newValue => noteText = newValue" :value="noteText" />
                    <UniversalButton class="ml-auto">Create note</UniversalButton>
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
import { watchEffect, ref, watch } from 'vue';
import { getItems, createItem, removeItem, getTags } from '../../utils/apiFetchers'
import UniversalPagination from '../UI/UniversalPagination.vue';
import { useUiStore } from '../../store/ui';
import { storeToRefs } from 'pinia';
import UniversalTextarea from '../UI/UniversalTextarea.vue';
import UniversalDisplayModal from '../UI/UniversalDisplayModal.vue';
import UniversalTagInput from '../UI/UniversalTagInput.vue';
import UniversalTag from '../UI/UniversalTag.vue';
import ArticleSortedBy from '../articles/ArticleSortedBy.vue';


const store = useUiStore()
const { articlesShow, notesShow, chatShow, toastShow, toastText } = storeToRefs(store)
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
const tags = ref([])
const filter = ref('')
const filteredTags = ref([])
const filterBy = ref([])
const showTags = ref(false)

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

const deleteItem = (id) => {
    if (articles.value.length === 1) {
        articlesPage.value = articlesPage.value - 1
    }
    removeItem('articles', id).then(showDeleteModal.value = false).finally(async () => [articles.value, articlesTotalPages.value] =
        await getItems(articlesPage.value, 'articles', 3))
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
        toastShow.value = true
        toastText.value = 'Article created!'
    }
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

watchEffect(async () => [articles.value, articlesTotalPages.value] = await getItems(articlesPage.value, 'articles', 3, filterBy.value))
watchEffect(async () => [notes.value, notesTotalPages.value] = await getItems(notesPage.value, 'notes', 3))
watchEffect(async () => tags.value = await getTags())
watch(articlesTotalPages, () => {
    if (articlesPage.value > articlesTotalPages.value) {
        articlesPage.value = articlesTotalPages.value
    }
})
</script>
<script>
export default {
    name: "DashboardPage",
    components: { MenuBar, UniversalPagination, UniversalTextarea, UniversalDisplayModal, UniversalTagInput, UniversalTag, ArticleSortedBy }
}
</script>