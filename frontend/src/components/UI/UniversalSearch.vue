<template>
    <input autocomplete="off" autocorrect="off"
        class="placeholder:italic  bg-slate-100 outline-1 outline outline-slate-300 px-3 py-2 rounded-xl m-1"
        :placeholder="placeholder" />
</template>

<script setup>
const props = defineProps({
    placeholder: String
})

</script>