<template>
    <div class="px-2 py-1 text-white rounded-md bg-slate-800">
        <slot></slot>
    </div>
</template>
<script setup lang="ts">
const props = defineProps({
    tag: String
})
</script>

<script lang="ts">
export default {
    name: 'UniversalTag'
}
</script>