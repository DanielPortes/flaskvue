import { createRouter, createWebHistory } from "vue-router";
import Whiskies from "../views/WhiskiesView.vue";
import About from "../views/AboutView.vue";
import Favorites from "../views/FavoritesView.vue";
import Contact from "../views/ContactView.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      name: "home",
      component: Whiskies,
    },
    {
      path: "/about",
      name: "about",
      component: About,
    },
    {
      path: "/favorites",
      name: "favorites",
      component: Favorites,
    },
    {
      path: "/contact",
      name: "contact",
      component: Contact,
    },
    {
      path: "/:catchAll(.*)",
      name: "not-found",
      redirect: "/",
    },
  ],
});

export default router;