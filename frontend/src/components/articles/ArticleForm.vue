<template>
    <div>
        <div class="mb-4">
            <UniversalLabel>Create article</UniversalLabel>
        </div>
        <form @submit.prevent="articleValidation" class="relative flex flex-col space-y-2 ">
            <div class="flex flex-wrap items-center">
                <div class="flex flex-wrap items-center">
                    <UniversalInput :placeholder="'Article title...'" class="focus:shadow-md"
                        @update:value="newValue => articleTitle = newValue" :value="articleTitle" />
                    <div class="relative ">
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
                <div class="flex justify-end ml-auto space-x-2">
                    <div class="px-2 py-1 text-gray-200 rounded-md w-max hover:text-gray-100"
                        :class="articleText.length == 0 ? 'bg-gray-400 hover:cursor-not-allowed hover:bg-gray-400' : 'hover:bg-gray-800 hover:cursor-pointer bg-gray-900'"
                        @click="changeFormat">{{ markdown ? 'Plain text' : 'Markdown'
                        }}
                    </div>
                    <UniversalButton class="">Create article</UniversalButton>

                </div>
            </div>
            <ArticleSortedBy :tags="filterBy" @update:value="deleteTags">{{ filterBy.length > 0 ? null : 'No tags added'
            }}
            </ArticleSortedBy>
            <UniversalTextarea v-if="!markdown" :placeholder="'Article text...'" class="focus:shadow-md"
                @update:value="newValue => articleText = newValue" :value="articleText" />
            <div v-if="markdown" class="px-3 py-2 m-1 bg-slate-100 outline-1 outline outline-slate-300 rounded-xl">
                <VueShowdown :markdown="articleText" />
            </div>
        </form>
    </div>
</template>

<script setup lang="ts">

import UniversalTextarea from '../UI/UniversalTextarea.vue';
import UniversalButton from '../UI/UniversalButton.vue';
import UniversalInput from '../UI/UniversalInput.vue';
import ArticleSortedBy from './ArticleSortedBy.vue';
import { Ref, ref, watch } from 'vue';
import { storeToRefs } from 'pinia';
import { useUiStore } from '../../store/ui';
import { createItem } from '../../utils/apiFetchers'
import UniversalLabel from '../UI/UniversalLabel.vue';
import { Tag } from '../../utils/interfaces'

interface Props {
    tags: Tag[]
}

const props = defineProps<Props>()
const store = useUiStore()
const markdown = ref(false)
const { toastShow, toastText } = storeToRefs(store)
const articleTitle = ref('')
const articleText = ref('')
const tags = ref(props.tags)
const filter = ref('')
const filteredTags: Ref<Tag[]> = ref([])
const filterBy: Ref<Tag[]> = ref([])
const showTags = ref(false)

const articleValidation = () => {
    if (articleText.value.trim().length > 0 && articleTitle.value.trim().length > 0) {
        createItem('articles', { title: articleTitle.value, text: articleText.value, tags: filterBy.value })
        articleText.value = ''
        articleTitle.value = ''
        toastShow.value = true
        toastText.value = 'Article created!'
        filterBy.value.map(tag => tags.value.push(tag))
        filterBy.value = []
    }
}

const changeFormat = () => {
    if (articleText.value.length > 0) {
        markdown.value = !markdown.value
    }
}
const addToList = (tag: { name: string, id: string }) => {
    filterBy.value.push(tag)
    tags.value = tags.value.filter(item => item.name !== tag.name)
    filteredTags.value = filteredTags.value.filter(item => item.name !== tag.name)
    filter.value = ''
}
const deleteTags = (tag: { name: string, id: string }) => {
    filterBy.value = filterBy.value.filter(item => item.name !== tag.name)
    tags.value.push(tag)

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
watch(props, () => {
    tags.value = props.tags
})

</script>