<template>
    <n-layout-content bordered class="layout-content" style="padding: 800px;padding-top: 50px;background: rgba(240, 255, 255, 0);">
    <div class="box">
        <!-- <div"> -->
        <n-space vertical class="input">
          <div class="title">API Token</div>
          <!-- 显示的替换掉中间三位数 -->
          <n-input v-model:value="acc_token" round  type="text" placeholder="Token" readonly="readonly"/>
          <n-button type="warning" round style="width: 100%;" :loading="loading" @click="getAccessToken">获取</n-button>
          <n-button type="primary" round style="width: 100%;" :loading="loading" v-if="!acc_token.includes('AccessToken')" @click="copy">复制</n-button>
          <n-button type="primary" round style="width: 100%;" :loading="loading" @click="openLink">返回</n-button>
        </n-space>
    </div>
</n-layout-content>
</template>
<script lang="ts" setup>
import { ref } from 'vue';
import user from '../api/user'
import { useRouter } from 'vue-router';
const router = useRouter()

const acc_token = ref("点击下方按钮重新获取 AccessToken")

const loading = ref(false)

const getAccessToken = async () => {
  loading.value = true
  await user.get_access_token().then((token) => acc_token.value = token)
  loading.value = false
}

const openLink = () => {
  router.push("/infer")
}

const copy = () => {
  const input = document.createElement('input');
  input.setAttribute('readonly', 'readonly');
  input.setAttribute('value', acc_token.value);
  document.body.appendChild(input);
  input.select();
  input.setSelectionRange(0, 9999);
  if (document.execCommand('copy')) {
    document.execCommand('copy');
    console.log('复制成功');
  }
  document.body.removeChild(input);
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