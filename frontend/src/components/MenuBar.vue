<template>
    <div class="fixed z-[1000]  top-5 right-0   bg-slate-900 shadow-xl py-2 justify-center rounded-md">

        <div v-if="!barHidden" class="flex px-2 space-x-2 w-[200px] show" key="first">
            <IconsArrowRight @click="barHidden = true"
                class="w-10 h-10 transition-all hover:fill-gray-300 fill-gray-100 hover:cursor-pointer" />
            <IconsArticles @click="articlesShow = !articlesShow"
                :class="articlesShow ? 'hover:stroke-pink-600 stroke-pink-800' : 'hover:stroke-gray-300 stroke-gray-100'"
                class="w-10 h-10 transition-all hover:cursor-pointer" />
            <IconsNotes @click="notesShow = !notesShow"
                :class="notesShow ? 'hover:stroke-pink-600 stroke-pink-800' : 'hover:stroke-gray-300 stroke-gray-100'"
                class="w-10 h-10 transition-all hover:cursor-pointer" />
            <IconsChat @click="chatShow = !chatShow"
                :class="chatShow ? 'hover:stroke-pink-600 stroke-pink-800' : 'hover:stroke-gray-300 stroke-gray-100'"
                class="w-10 h-10 transition-all hover:fill-gray-300 fill-gray-100 hover:cursor-pointer" />

        </div>
        <div v-else="barHidden" class="w-[40px] " @click="barHidden = false" key="second">
            <IconsArrowLeft class="w-10 h-10 transition-all hover:fill-gray-300 fill-gray-100 hover:cursor-pointer" />
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
const barHidden = ref(true)
</script>

<style scoped>
.show {
    animation: show 0.3s forwards
}


@keyframes show {
    from {
        width: 40px
    }

    to {
        width: 200px
    }
}
</style>