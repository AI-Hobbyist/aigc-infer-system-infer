<template>
    <n-layout-content bordered class="layout-content" style="padding: 800px;padding-top: 50px;background: rgba(240, 255, 255, 0);">
    <div class="box">
        <!-- <div"> -->
        <n-space vertical class="input">
            <div class="title">登录</div>
            <n-input v-model:value="email" round  type="email" placeholder="邮箱" />
            <n-input v-model:value="pwd" round  type="password" placeholder="密码" />
            <n-button type="primary" round style="width: 100%;" @click="login">登录</n-button>
        </n-space>
        <n-a href="https://reg.ai-hobbyist.org">点击注册账号</n-a>
    </div>
</n-layout-content>
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
    if(data.token) {
        store.token = data.token
        notification.success({
            content: "登录成功！\n友情提示：\n如果不喜欢在线推理，喜欢本地推理的话，可以点击右上角的 “整合包下载” 来下载本地推理整合包哦！",
            duration: 5000
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
@media screen and (max-width: 768px) {
  .layout-content {
    padding: 50px !important ;
  }
}
@media screen and (min-width: 768px) {
  .layout-content {
    padding: 0 40vw !important ;
  }
}
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