<template>
    <input autocomplete="off" autocorrect="off" @input="$emit('update:value', $event.target.value)" :value="value"
        class="placeholder:italic  bg-slate-100 outline-1 outline outline-slate-300 px-3 py-2 rounded-xl m-1"
        :placeholder="placeholder" />
</template>

<script setup>
const props = defineProps({
    placeholder: String,
    value: String
})
const emit = defineEmits(['update:value'])
</script>