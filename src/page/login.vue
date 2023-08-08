<template>
    <div class="box">
        <!-- <div"> -->
        <n-space vertical class="input">
            <div class="title">登录</div>
            <n-input v-model:value="email" round  type="text" placeholder="邮箱" />
            <n-input v-model:value="pwd" round  type="text" placeholder="密码" />
            <n-button type="primary" round style="width: 100%;" @click="login">登录</n-button>
        </n-space>
        <n-a href="https://reg.ai-hobbyist.org">点击注册账号</n-a>
    </div>
</template>
<script lang="ts" setup>
import { ref } from 'vue';
import user from '../api/user'
import { useUserStore } from '../store';
import { useNotification } from 'naive-ui'
import { useRouter } from 'vue-router';
const notification = useNotification()
const pwd = ref("")
const email = ref("")
const router = useRouter()
const store = useUserStore()
const login = async () => {
    const data = await user.login({email: email.value,password: pwd.value})
    console.log(data);
    if(data.token) {
        store.token = data.token
        notification.success({
            content: "登陆成功",
            duration: 3000
        })
        router.push("/infer")
    } else {
        notification.error({
            content: data.message,
            duration: 3000
        })
    }
}

</script>
<style scoped>
.box {
    width: 100%;
    background-color: rgba(240, 248, 255, 0.329);
    backdrop-filter: blur(5px);
    display: flex;
    margin-top: 50px;
    /* align-content: center; */
    align-items: center;
    flex-direction: column; 
    border-radius: 17px; 
    padding: 20px 0px
}
.title {
    font-size: 24px;
    font-weight: 600;
    text-align: center;
}
.input {
    width: 80%;
}
</style>