<template>
    <div class="bg-gray-700/20 inset-0 w-full h-full absolute z-[1500] transition-all" @click="$emit('showDeleteModal')">
    </div>
    <div
        class="bg-gray-200 z-[1600] rounded-md absolute shadow-xl top-52 ml-auto mr-auto left-0 right-0 items-center w-[400px] min-h-[150px] max-h-max">
        <div class="bg-gray-900 w-full h-50px text-gray-100 text-[20px] text-center py-2 rounded-t-md">
            Deleting {{ item.title }}
        </div>
        <p class="text-center py-2 text-[18px]">
            Are you sure you want to delete {{ item.title }}?
        </p>
        <div class="absolute flex space-x-2 bottom-2 right-2">
            <UniversalButton @click="$emit('deleteItem', item.id)">Yes</UniversalButton>
            <UniversalButton @click="$emit('showDeleteModal')">No</UniversalButton>
        </div>

    </div>
</template>
<script setup lang="ts">
import UniversalButton from './UniversalButton.vue';
import { Article } from '../../utils/interfaces';

interface Props {
    item: Article
}

const props = defineProps<Props>()
const emit = defineEmits(['showDeleteModal', 'deleteItem'])


</script>

<script lang="ts">

export default {
    name: "UniversalDisplayModal",
    components: { UniversalButton }
}

</script>