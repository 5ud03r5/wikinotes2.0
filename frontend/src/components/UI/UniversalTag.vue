<template>
    <div class="bg-slate-800 px-2 py-1 rounded-md text-white">
        <slot></slot>
    </div>
</template>
<script setup>
const props = defineProps({
    tag: String
})
</script>

<script>
export default {
    name: 'UniversalTag'
}
</script>