import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import { createRouter, createWebHistory } from "vue-router";
import NotesPage from "./components/pages/NotesPage.vue";
import DashboardPage from "./components/pages/DashboardPage.vue";
import ChatPage from "./components/pages/ChatPage.vue";
import ArticlesPage from "./components/pages/ArticlesPage.vue";
import { createPinia } from "pinia";

const routes = [
  { path: "/dashboard", component: DashboardPage },
  { path: "/notes", component: NotesPage },
  { path: "/articles", component: ArticlesPage },
  { path: "/chat", component: ChatPage },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});
const pinia = createPinia();
const app = createApp(App);
app.use(router);
app.use(pinia);
app.mount("#app");
