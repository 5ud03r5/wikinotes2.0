import { defineStore } from "pinia";
import { ref } from "vue";

export const useUiStore = defineStore("ui", () => {
  const articlesShow = ref(true);
  const notesShow = ref(true);
  const chatShow = ref(true);
  const toastShow = ref(false);
  const toastText = ref("");
  return { articlesShow, notesShow, chatShow, toastShow, toastText };
});
