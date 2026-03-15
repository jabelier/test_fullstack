import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      redirect: '/feed',
    },
    {
      path: '/feed',
      component: () => import('./components/FeedPage.vue'),
    },
    {
      path: '/videos',
      component: () => import('./components/SearchResults.vue'),
    },
  ],
})

export default router
