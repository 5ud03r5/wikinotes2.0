<template>
    <div class="">
        <UniversalInput :placeholder="'Search in notes...'" class="flex w-1/2 mx-auto mb-5 focus:shadow-xl" />
        <NoteItem class="w-full " v-for="note in notes" :note="note" :key="note.id" />
        <UniversalPagination class="mx-auto" :currentPage="notesPage" :totalPages="notesTotalPages!"
            @update:page="newValue => notesPage = newValue" />
    </div>
</template>

<script setup lang="ts">
import { watchEffect, ref, Ref } from 'vue';
import { getItems } from '../../utils/apiFetchers';
import NoteItem from '../notes/NoteItem.vue';
import UniversalPagination from '../UI/UniversalPagination.vue';
import UniversalInput from '../UI/UniversalInput.vue';
import { Note } from '../../utils/interfaces';

const notes: Ref<Note[]> = ref([])
const notesPage = ref(1)
const notesTotalPages = ref(null)


watchEffect(async () => [notes.value, notesTotalPages.value] = await getItems(notesPage.value, 'notes', 7))
</script>