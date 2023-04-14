<template>
    <div class="mx-auto ">
        <!--/components/MenuBar.vue-->
        <MenuBar />
        <section class="flex m-2 space-x-2 " v-if="articlesShow">
            <!--/components/UI/DashboardItemWrapper.vue-->
            <DashboardItemWrapper>
                <!--/components/articles/ArticleDisplay.vue-->
                <ArticleDisplay :tagsProp="tags" />
            </DashboardItemWrapper>
            <!--/components/UI/DashboardItemWrapper.vue-->
            <DashboardItemWrapper>
                <!--/components/articles/ArticleForm.vue-->
                <ArticleForm :tags="tags" />
            </DashboardItemWrapper>
        </section>
        <section class="flex m-2 space-x-2" v-if="notesShow">
            <!--/components/UI/DashboardItemWrapper.vue-->
            <DashboardItemWrapper>
                <!--/components/notes/NoteDisplay.vue-->
                <NoteDisplay />
            </DashboardItemWrapper>
            <!--/components/UI/DashboardItemWrapper.vue-->
            <DashboardItemWrapper>
                <!--/components/notes/NoteForm.vue-->
                <NoteForm />
            </DashboardItemWrapper>
        </section>
    </div>
</template>

<script setup>
import MenuBar from '../MenuBar.vue';
import { watchEffect, ref, } from 'vue';
import { getTags } from '../../utils/apiFetchers'
import { useUiStore } from '../../store/ui';
import { storeToRefs } from 'pinia';
import ArticleForm from '../articles/ArticleForm.vue';
import ArticleDisplay from '../articles/ArticleDisplay.vue';
import NoteDisplay from '../notes/NoteDisplay.vue';
import NoteForm from '../notes/NoteForm.vue';
import DashboardItemWrapper from '../UI/DashboardItemWrapper.vue';

const store = useUiStore()
const { articlesShow, notesShow } = storeToRefs(store)
const tags = ref([])
watchEffect(async () => tags.value = await getTags())
</script>
<script>
export default {
    name: "DashboardPage",
    components: { DashboardItemWrapper }
}
</script>