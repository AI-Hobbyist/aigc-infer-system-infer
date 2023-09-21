import { useUserStore } from '../store';
import axios from "./axios";
export default {
    login: async (data: { email: string, password: string }) => (await axios.post('/user_login', {
        email: data.email,
        pass: data.password
    })).data,
    async check() {
        const store = useUserStore()
        const { data } = await axios.post('/login/status', { token: store.token })
        
        if(data.status !== 1) {
            store.token = undefined
            return false
        }
        return true
    }
}