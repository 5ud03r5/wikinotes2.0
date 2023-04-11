<template>
    <div
        class="fixed top-10 left-0 opacity-1 text-center p-10 right-0 ml-auto mr-auto bg-indigo-100 outline outline-1 outline-indigo-200 w-[400px] h-[100px] shadow-xl rounded-md">
        {{ toastText }}
    </div>
</template>

<script setup>
import { useUiStore } from '../../store/ui';
import { storeToRefs } from 'pinia';

const store = useUiStore()
const { toastShow, toastText } = storeToRefs(store)

setTimeout(() => {
    toastShow.value = false
}, 3500)
</script>

<script>
export default {
    name: 'UniversalToast'
}
</script>

