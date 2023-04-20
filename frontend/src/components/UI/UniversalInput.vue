<template>
    <input autocomplete="off" autocorrect="off" @input="$emit('update:value', ($event.target as HTMLInputElement).value)"
        :value="value" class="px-3 py-2 m-1 placeholder:italic bg-slate-100 outline-1 outline outline-slate-300 rounded-xl"
        :placeholder="placeholder" />
</template>

<script setup lang="ts">
const props = defineProps({
    placeholder: String,
    value: String
})
const emit = defineEmits<{
    (e: 'update:value', value: string): void;
}>()


</script>
<script lang="ts">
export default {
    name: 'UniversalInput'
}
</script>