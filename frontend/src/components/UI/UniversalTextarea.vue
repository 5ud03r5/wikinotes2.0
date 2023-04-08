<template>
    <textarea :value="value" autocomplete="off" autocorrect="off" rows="14"
        @input="$emit('update:value', $event.target.value)"
        class="placeholder:italic  bg-slate-100 outline-1 outline outline-slate-300 px-3 py-2 rounded-xl m-1 resize-none"
        :placeholder="placeholder"></textarea>
</template>

<script setup>
const props = defineProps({
    placeholder: String,
    value: String,

})
const emit = defineEmits(['update:value'])

</script>