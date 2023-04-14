<template>
    <div>
        <label class="m-1 text-[40px] font-bold text-slate-700">Create article</label>
        <hr class="my-5" />
        <form @submit.prevent="articleValidation" class="relative flex flex-col space-y-2 ">
            <div class="flex space-x-2">
                <UniversalInput :placeholder="'Article title...'" class="focus:shadow-md"
                    @update:value="newValue => articleTitle = newValue" :value="articleTitle" />

            </div>

            <UniversalTextarea :placeholder="'Article text...'" class="focus:shadow-md"
                @update:value="newValue => articleText = newValue" :value="articleText" />
            <UniversalButton class="absolute right-4 ">Create article</UniversalButton>
        </form>
    </div>
</template>

<script setup>
import UniversalTextarea from '../UI/UniversalTextarea.vue';
import UniversalButton from '../UI/UniversalButton.vue';
import UniversalInput from '../UI/UniversalInput.vue';
import { ref } from 'vue';
import { storeToRefs } from 'pinia';
import { useUiStore } from '../../store/ui';
import { createItem } from '../../utils/apiFetchers'
const props = defineProps({
    tags: Array
})
const store = useUiStore()
const { toastShow, toastText } = storeToRefs(store)
const articleTitle = ref('')
const articleText = ref('')
const tags = ref(props.tags)

const articleValidation = () => {
    if (articleText.value.trim().length > 0 && articleTitle.value.trim().length > 0) {
        createItem('articles', { title: articleTitle.value, text: articleText.value, tags: [] })
        articleText.value = ''
        articleTitle.value = ''
        toastShow.value = true
        toastText.value = 'Article created!'
    }
}

</script>