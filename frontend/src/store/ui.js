import { defineStore } from "pinia";
import { ref } from "vue";

export const useUiStore = defineStore("ui", () => {
  const articlesShow = ref(true);
  const notesShow = ref(true);
  const chatShow = ref(true);
  return { articlesShow, notesShow, chatShow };
});
