<template>
    <div class="mx-auto ">
        <!--/components/MenuBar.vue-->
        <MenuBar />
        <section class="flex m-2 space-x-2 " v-if="articlesShow">
            <!--/components/UI/DashboardItemWrapper.vue-->
            <DashboardItemWrapper>
                <!--/components/articles/ArticleDisplay.vue-->
                <ArticleDisplay :tags="tags" />
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

<script setup lang="ts">

import MenuBar from '../MenuBar.vue';
import { watchEffect, ref, Ref } from 'vue';
import { getTags } from '../../utils/apiFetchers'
import { useUiStore } from '../../store/ui';
import { storeToRefs } from 'pinia';
import ArticleForm from '../articles/ArticleForm.vue';
import ArticleDisplay from '../articles/ArticleDisplay.vue';
import NoteDisplay from '../notes/NoteDisplay.vue';
import NoteForm from '../notes/NoteForm.vue';
import DashboardItemWrapper from '../UI/DashboardItemWrapper.vue';
import { Tag } from '../../utils/interfaces';

const store = useUiStore()
const { articlesShow, notesShow } = storeToRefs(store)
const tags: Ref<Tag[]> = ref([])
watchEffect(async () => tags.value = await getTags())
</script>
<script lang="ts">
export default {
    name: "DashboardPage",
    components: { DashboardItemWrapper }
}
</script>