import { Router, createRouter, createWebHashHistory } from "vue-router";

import login from "./page/login.vue"
import infer from "./page/infer.vue"
import acc from "./page/access.vue"
import { useUserStore } from "./store";

interface Route {
  path: string;
  component: any;
}

const routes: Route[] = [
  // { path: '/accounts', component: Accounts },
  { path: "/infer", component: infer},
  { path: "/login", component: login},
  { path: "/apikey", component: acc}
];

let router: Router;
export default () => {
  if (!router) {
    router = createRouter({
      history: createWebHashHistory(),
      routes, // `routes: routes` 的缩写
    });

    const store = useUserStore();
    
    console.log(store);
    // 检测 DEV
    if (import.meta.env.DEV) {
      // @ts-ignore
      window.store = store;
    }

    router.beforeEach((to, _from, next) => {
      if(to.query.logout) next()
      if (!store.isLogin.value && to.path !== "/login") {
        console.log("go login");
        next({ path: "/login" })

      } else if(to.path !== "/infer" && to.path !== "/apikey" && to.path !== "/login") {
        next({ path: "/infer" })
        console.log("go infer");
      } else next();
    });
  }
  return router;
};
