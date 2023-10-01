<template>
    <n-layout-content bordered class="layout-content" style="padding: 800px;padding-top: 50px;background: rgba(240, 255, 255, 0);">
    <div class="box">
        <!-- <div"> -->
        <n-space vertical class="input">
            <div class="title">API Token</div>
            <n-input v-model:value="acc_token" round  type="text" placeholder="Token" readonly="readonly"/>
            <n-button type="primary" round style="width: 100%;" @click="open_link">返回</n-button>
        </n-space>
    </div>
</n-layout-content>
</template>
<script lang="ts" setup>
import { ref } from 'vue';
import user from '../api/user'
import { useRouter } from 'vue-router';
const router = useRouter()

//const acc = await user.get_access_key()

const acc_token = ref("123")
const open_link = () => {
  router.push("/infer")
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