import { useUserStore } from '../store';
import axios from "./axios";
export default {
    login: async (data: { lang: "zh", email: string, password: string, mac: "" }) => (await axios.post('/user_login', {
        email: data.email,
        pass: data.password
    })).data,
    async check() {
        const store = useUserStore()
        const { data } = await axios.post('/status', { token: store.token.value })
        
        if(data.is_ok !== 1) {
            store.token.value = ""  
            return false
        }
        return true
    },
    async get_access_token(){
        const store = useUserStore()
        const  { data } = await axios.post('/refresh_access_token', { token: store.token.value })
        return data.acc_token
    },
    async logout() {
        const store = useUserStore()
        store.token.value = ""
    }
}