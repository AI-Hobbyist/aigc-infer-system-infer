<script setup lang="ts">
import { useRouter } from 'vue-router';
import user from './api/user';
const router = useRouter()
const checkToken = async () => {
  const result = await user.check()
  if (!result) {
    router.push("/login")
  }
}
checkToken()

const open_link = () => {
  window.location.href='https://pan.ai-hobbyist.org/Models/Vits/Packs';
}

const logout = () => {
  user.logout()
  router.push("/login?logout=true")
}

const get_token = () => {
  checkToken()
  router.push("/apikey")
}
const reload = () => window.location.reload()

</script>

<template>
  <n-notification-provider>
    <div style="height: 100%;background: #f0ffff00;">
      <!-- <n-page-header subtitle="让你的听觉更懂视觉"></n-page-header> -->
      <n-layout style="height: 100%;">
        <n-layout-header class="header" bordered
          style="width: 100vw;position: fixed;top: 0;z-index: 999;padding-left: 20px;height: 40px;flex-direction: column;justify-content: center;font-size: 22px;">
            <span @click="reload" style="cursor: pointer;">
              <p class="text">原/星语音合成</p>
              <p class="logo"><img src="/logo.png"></p>
            </span>
            <p class="nav">
              <n-button type="primary" @click="get_token">获取API Token</n-button>&nbsp;
              <n-button type="primary" @click="open_link">整合包下载</n-button>&nbsp;
              <n-button circle type="primary" @click="logout">
                <template #icon>
                  <n-icon>
                    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 24 24"><path d="M6 2h9a2 2 0 0 1 2 2v1a1 1 0 0 1-2 0V4H6v16h9v-1a1 1 0 0 1 2 0v1a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2z" fill="currentColor"></path><path d="M16.795 16.295c.39.39 1.02.39 1.41 0l3.588-3.588a1 1 0 0 0 0-1.414l-3.588-3.588a.999.999 0 0 0-1.411 1.411L18.67 11H10a1 1 0 0 0 0 2h8.67l-1.876 1.884a.999.999 0 0 0 .001 1.411z" fill="currentColor"></path></svg>
                  </n-icon>
                </template>
              </n-button>
            </p>
          <!--<router-link to="/login">登录</router-link>
        <router-link to="/infer">推理</router-link> -->
        </n-layout-header>

        <router-view></router-view>

        <n-layout-footer bordered class="footer" style="width: 100vw;position: fixed;bottom: 0;">
          <div class="footer-m">
            <div>模型训练: <n-a href="https://space.bilibili.com/6589795">@红血球AE3803</n-a></div>
            <div>前端: <n-a href="https://space.bilibili.com/503423945">@多玩幻灵qwq</n-a>、<n-a href="https://space.bilibili.com/6589795">@红血球AE3803</n-a></div>
            <div>相关组织: <n-a href="https://github.com/AI-Hobbyist">AI-Hobbyist</n-a></div>
          </div>
          <div class="footer-d">
            <n-grid :cols="3">
              <n-gi class="footer-d-t">
                <div>模型训练: <n-a href="https://space.bilibili.com/6589795">@红血球AE3803</n-a></div>
                <div>前端: <n-a href="https://space.bilibili.com/503423945">@多玩幻灵qwq</n-a>、<n-a href="https://space.bilibili.com/6589795">@红血球AE3803</n-a></div>
              </n-gi>
              <n-gi class="footer-d-t">
                <div>数据集: <n-a href="https://www.bilibili.com/read/cv24180458">@红血球AE3803</n-a>、<n-a href="https://github.com/w4123/GenshinVoice">@溯洄</n-a></div>
                <div>后端: <n-a href="https://space.bilibili.com/6589795">@红血球AE3803</n-a></div>
              </n-gi>
              <n-gi class="footer-d-t">
                <div>相关组织</div>
                <n-a href="https://www.ai-hobbyist.org/">AI-Hobbyist</n-a>
              </n-gi>
            </n-grid>
          </div>
        </n-layout-footer>
      </n-layout>
    </div>
  </n-notification-provider>
</template>

<style scoped lang="less">
.backdrop {
  backdrop-filter: blur(10px);
  /* background: rgba(240, 255, 255, 0); */
  background: rgb(255 255 255 / 31%);
  padding: 20px;
  border-radius: 20px;
}

.layout-content {
  display: flex;
}

.nav{
  display: flex;
  align-items: center;
  flex-direction: row;
  padding: 4px;
  justify-content: flex-end;
}
/* 给layout-content上响应式布局，如果是移动端，padding设为200px，桌面端设为800px */
@media screen and (max-width: 768px) {
  .layout-content {
    padding: 50px !important;
  }

  .footer-m {
    display: flex;
    flex-direction: column;
    text-align: center;
  }

  .footer-d {
    display: none;
  }

  .footer {
    --n-border-color: rgba(255, 255, 255, 0) !important;
    background-color: rgba(255, 255, 255, 0.44);
    backdrop-filter: blur(20px); 
  }
  
  a {
    --n-text-color: #28d130 !important;
  }


  .header {
    --n-border-color: rgba(255, 255, 255, 0) !important;
    background-color: rgba(255, 255, 255, 0.44);
    backdrop-filter: blur(20px);
  }
}

@media screen and (min-width: 768px) {
  .layout-content {
    padding: 0 40vw !important;
  }

  .footer-m {
    display: none;
    /* padding-left: 50px; */
  }

  .footer-d {
    /* 让 footer-d 的宽度只有 50% 的父元素宽度，并且居中于父元素 */
    padding-top: 10px;
    padding-bottom: 10px;
    width: 50%;
    margin: 0 auto;
    display: flex;
  }

  .footer {
    --n-border-color: rgba(255, 255, 255, 0) !important;
    background-color: rgba(255, 255, 255, 0.678);
    backdrop-filter: blur(20px);
  }

  .header {
    --n-border-color: rgba(255, 255, 255, 0) !important;
    background-color: rgba(255, 255, 255, 0.166);
    backdrop-filter: blur(20px);
  }
}

.footer-d-t {
  text-align: center;
}

.text{
  margin-top: 3px ;
  margin-left: 40px;
  font-weight: bold;
}
.logo{
  margin-top: -56px;
}
.nav{
  margin-top: -68px;
  margin-right: 20px;
}
</style>
