<template>
    <div>
        <div class="mb-4">
            <UniversalLabel>Create note</UniversalLabel>
        </div>
        <form @submit.prevent="noteValidation" class="flex flex-col space-y-2">

            <UniversalTextarea :placeholder="'Note text...'" class="focus:shadow-md"
                @update:value="newValue => noteText = newValue" :value="noteText" />
            <UniversalButton class="ml-auto">Create note</UniversalButton>
        </form>
    </div>
</template>

<script setup lang="ts">
import UniversalLabel from '../UI/UniversalLabel.vue';
import UniversalTextarea from '../UI/UniversalTextarea.vue';
import UniversalButton from '../UI/UniversalButton.vue';
import { ref } from 'vue';
import { createItem } from '../../utils/apiFetchers';

const noteText = ref('')
const noteValidation = () => {
    if (noteText.value.trim().length > 0) {
        createItem('notes', { text: noteText.value })
        noteText.value = ''
    }
}

</script>