<template>
    <div class="">
        <UniversalInput :placeholder="'Search in notes...'" class="w-1/2 mx-auto flex focus:shadow-xl mb-5" />
        <NoteItem class="w-full " v-for="note in notes" :note="note" :key="note.id" />
        <UniversalPagination class="mx-auto" :currentPage="notesPage" :totalPages="notesTotalPages"
            @update:page="newValue => notesPage = newValue" />
    </div>
</template>

<script setup>
import { watchEffect, ref } from 'vue';
import { getItems } from '../../utils/apiFetchers';
import NoteItem from '../notes/NoteItem.vue';
import UniversalPagination from '../UI/UniversalPagination.vue';
import UniversalInput from '../UI/UniversalInput.vue';
const notes = ref([])
const notesPage = ref(1)
const notesTotalPages = ref(null)


watchEffect(async () => [notes.value, notesTotalPages.value] = await getItems(notesPage, 'notes', 7))
</script>