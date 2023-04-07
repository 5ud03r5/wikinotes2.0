<template>
    <div class="fixed z-[1000]  top-5 right-0  h-max bg-slate-900 shadow-xl py-2 justify-center w-max mx-auto  rounded-md">
        <div v-if="!barHidden" class="flex space-x-2 px-2">
            <IconsArrowRight @click="barHidden = true"
                class="w-10 h-10 hover:fill-gray-300 fill-gray-100 hover:cursor-pointer transition-all" />
            <IconsArticles @click="articlesShow = !articlesShow"
                :class="articlesShow ? 'hover:stroke-pink-600 stroke-pink-800' : 'hover:stroke-gray-300 stroke-gray-100'"
                class="w-10 h-10 hover:cursor-pointer transition-all" />
            <IconsNotes @click="notesShow = !notesShow"
                :class="notesShow ? 'hover:stroke-pink-600 stroke-pink-800' : 'hover:stroke-gray-300 stroke-gray-100'"
                class="w-10 h-10 hover:cursor-pointer transition-all" />
            <IconsChat @click="chatShow = !chatShow"
                :class="chatShow ? 'hover:stroke-pink-600 stroke-pink-800' : 'hover:stroke-gray-300 stroke-gray-100'"
                class="w-10 h-10 hover:fill-gray-300 fill-gray-100 hover:cursor-pointer transition-all" />
        </div>
        <div v-else class="px-2" @click="barHidden = false">
            <IconsArrowLeft class="w-10 h-10 hover:fill-gray-300 fill-gray-100 hover:cursor-pointer transition-all" />
        </div>


    </div>
</template>

<script setup>
import IconsArrowLeft from './icons/IconsArrowLeft.vue';
import IconsArrowRight from './icons/IconsArrowRight.vue';
import IconsArticles from './icons/IconsArticles.vue';
import IconsChat from './icons/IconsChat.vue';
import IconsNotes from './icons/IconsNotes.vue';
import { ref } from 'vue';
import { useUiStore } from '../store/ui';
import { storeToRefs } from 'pinia';

const store = useUiStore()
const { articlesShow, notesShow, chatShow } = storeToRefs(store)
const barHidden = ref(false)



</script>