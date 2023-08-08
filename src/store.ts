import { defineStore } from 'pinia'

import { ref, computed } from 'vue'

export const useUserStore = defineStore('user', () => {
    const token = ref<string>() // 这边之前都是 var

    const isLogin = computed(()=>Boolean(token.value))

    return { isLogin, token }
}, {
    // @ts-ignore
    persist: {
        enabled: true,
        strategies: [{
            key: "user",
            storage: localStorage
        }]
    }   
})
