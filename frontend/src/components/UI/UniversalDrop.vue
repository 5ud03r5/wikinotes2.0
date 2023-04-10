<template>
    <div
        class="bg-slate-200  outline outline-1 outline-slate-400 flex flex-col tansition-all space-y-2 shadow-md absolute right-10 h-max w-max rounded-sm p-[2px]">
        <div @click="$emit('showDeleteModal')"
            class="hover:bg-slate-800 hover:text-slate-300 hover:cursor-pointer w-full px-3 py-1 transition-all rounded-sm">
            Delete</div>

        <div
            class="hover:bg-slate-800 hover:text-slate-300 hover:cursor-pointer w-full px-3 py-1 transition-all rounded-sm">
            Edit</div>
    </div>
</template>


<script setup>
const emit = defineEmits(['showDeleteModal'])

</script>

<script>

export default {
    name: 'UniversalDrop'
}
</script>