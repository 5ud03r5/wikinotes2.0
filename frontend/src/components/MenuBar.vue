<template>
    <div class="z-[1000] container fixed top-0 flex justify-end py-2 rounded-bl-md shadow-xl w-max right-0 bg-slate-900">

        <div class="flex flex-col px-2 space-y-2 " key="first">
            <!-- <IconsArrowRight class="w-10 h-10 transition-all hover:fill-gray-300 fill-gray-100 hover:cursor-pointer" /> -->
            <IconsArticles @click="articlesShow = !articlesShow"
                :class="articlesShow ? 'hover:stroke-gray-300 stroke-gray-100' : 'hover:stroke-gray-500 stroke-gray-600'"
                class="w-10 h-10 transition-all hover:cursor-pointer" />
            <IconsNotes @click="notesShow = !notesShow"
                :class="notesShow ? 'hover:stroke-gray-300 stroke-gray-100' : 'hover:stroke-gray-500 stroke-gray-600'"
                class="w-10 h-10 transition-all hover:cursor-pointer" />
            <IconsChat @click="chatShow = !chatShow"
                :class="chatShow ? 'hover:stroke-gray-300 stroke-gray-100' : 'hover:stroke-gray-500 stroke-gray-600'"
                class="w-10 h-10 transition-all hover:fill-gray-300 fill-gray-100 hover:cursor-pointer" />

        </div>
        <!--  <div v-else="barHidden" class="w-[40px] " @click="barHidden = false" key="second">
            <IconsArrowLeft class="w-10 h-10 transition-all hover:fill-gray-300 fill-gray-100 hover:cursor-pointer" />
        </div> -->

    </div>
</template>

<script setup lang="ts">
import IconsArticles from './icons/IconsArticles.vue';
import IconsChat from './icons/IconsChat.vue';
import IconsNotes from './icons/IconsNotes.vue';
import { ref } from 'vue';
import { useUiStore } from '../store/ui';
import { storeToRefs } from 'pinia';
const store = useUiStore()
const { articlesShow, notesShow, chatShow } = storeToRefs(store)

</script>

<script lang="ts">
export default {
    name: 'MenuBar'
}
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