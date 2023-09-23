import { ref, Ref, computed, watch } from 'vue'
// import { VueCookies as cookies } from "vue-cookies";
import VueCookies from "vue-cookies";
import { VueCookies as vc } from "vue-cookies";

// @ts-ignore
const cookies = VueCookies as vc

export interface Store {
    isLogin: Ref<boolean>
    token: Ref<string>
}

let store: Store;

export const useUserStore = (): Store => {
    if (store) {
        return store
    }
    let token = ref(cookies.get("token") || "")
    // 监听 token 变更，同步到 cookie
    watch(token, (value) => {
        console.log("token", value);
        cookies.set("token", value)
    })
    const isLogin = computed(() => token.value !== undefined)
    
    return store = { token, isLogin }
}