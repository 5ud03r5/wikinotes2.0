<template>
    <div>
        <div class="mb-4">
            <UniversalLabel>Notes</UniversalLabel>
        </div>
        <UniversalInput :placeholder="'Search in notes...'" class="focus:shadow-md" />
        <NoteItem v-for="note in notes" :note="note" :key="note.id" />
        <div class="absolute bottom-0 left-0 right-0 flex items-center justify-center w-1/2 ml-auto mr-auto">
            <UniversalPagination :currentPage="notesPage" :totalPages="notesTotalPages!"
                @update:page="newValue => notesPage = newValue" />
        </div>
    </div>
</template>
<script setup lang="ts">
import UniversalInput from '../UI/UniversalInput.vue';
import NoteItem from './NoteItem.vue';
import UniversalPagination from '../UI/UniversalPagination.vue';
import { ref, watchEffect, Ref } from 'vue';
import { getItems } from '../../utils/apiFetchers';
import UniversalLabel from '../UI/UniversalLabel.vue';
import { Note } from '../../utils/interfaces';

const notes: Ref<Note[]> = ref([])
const notesPage = ref(1)
const notesTotalPages = ref(null)
watchEffect(async () => [notes.value, notesTotalPages.value] = await getItems(notesPage.value, 'notes', 3))
</script>