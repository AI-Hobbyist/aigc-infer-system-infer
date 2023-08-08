import { Router, createRouter, createWebHashHistory } from "vue-router";

import login from "./page/login.vue"
import infer from "./page/infer.vue"
import { useUserStore } from "./store";
import { Pinia } from "pinia";

interface Route {
  path: string;
  component: any;
}

const routes: Route[] = [
  // { path: '/accounts', component: Accounts },
  { path: "/infer", component: infer},
  { path: "/login", component: login}
];

let router: Router;

export default (pinia: Pinia) => {
  if (!router) {
    router = createRouter({
      history: createWebHashHistory(),
      routes, // `routes: routes` 的缩写
    });

    console.log("create router");

    const store = useUserStore(pinia);
    
    console.log(store);

    router.beforeEach((to, _from, next) => {
      
      if (!store.isLogin && to.path !== "/login") {
        console.log("go login");

        next({ path: "/login" })
      } else next()
    });
  }
  return router;
};
