<template>
  <div class="">
    <SideBar />
    <Transition>
      <Teleport v-if="toastShow" to="body">

        <UniversalToast />

      </Teleport>
    </Transition>



    <RouterView class="ml-72 mr-16 mt-5" />
  </div>
</template>


<script setup>
import SideBar from './components/UI/SideBar.vue';
import UniversalToast from './components/UI/UniversalToast.vue';

import { useUiStore } from './store/ui';
import { storeToRefs } from 'pinia';

const store = useUiStore()
const { toastShow } = storeToRefs(store)

</script>
<style scoped>
.v-enter-active,
.v-leave-active {
  transition: opacity 2s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}
</style>