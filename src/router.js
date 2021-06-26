import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Login from './views/Login.vue'
import Registration from './views/Registration.vue'
import Dashboard from './views/Dashboard.vue'
import NewTemplate from './views/NewTemplate.vue'
import ListTemplates from './views/ListTemplates.vue'
import Template from './views/Template.vue'

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/registration',
      name: 'registration',
      component: Registration
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: Dashboard,
      children: [
        {
          path: '/',
          name: 'list-templates',
          component: ListTemplates
        },
        {
          path: 'new-template',
          name: 'new-template',
          component: NewTemplate
        },
        {
          path: 'template/:id',
          name: 'template',
          component: Template
        }
      ]
    }
  ]
})

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token')
  if ((to.name !== 'home' && to.name !== 'login' && to.name !== 'registration') && !token) {
    next({ name: 'login' })
  } else next()
})

export default router
