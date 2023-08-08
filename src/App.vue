<script setup lang="ts">
import { useRouter } from 'vue-router';
import user from './api/user';
const router = useRouter()
const checkToken = async () => {
  const result = await user.check()
  if(!result) {
    router.push("/login")
  }
}
checkToken()
</script>

<template>
<n-notification-provider>
  <div style="height: 100%;background: #f0ffff00;">
    <!-- <n-page-header subtitle="让你的听觉更懂视觉"></n-page-header> -->
    <n-layout style="height: 100%;">
      <n-layout-header class="header" bordered style="width: 100vw;position: fixed;top: 0;z-index: 999;padding-left: 20px;height: 40px;flex-direction: column;justify-content: center;font-size: 22px;">
        <div>
          原神语音合成
        </div>
  
        <!-- <router-link to="/login">登录</router-link>
        <router-link to="/infer">推理</router-link> -->
      </n-layout-header>
      <n-layout-content bordered class="layout-content" style="padding: 800px;padding-top: 50px;background: rgba(240, 255, 255, 0);">
        <router-view></router-view>
      </n-layout-content>
      <n-layout-footer bordered class="footer" style="width: 100vw;position: fixed;bottom: 0;">
        <div class="footer-m">
          <div>模型训练: <n-a href="https://space.bilibili.com/163056936">Stardust_减</n-a></div>
          <div>前端: <n-a href="https://space.bilibili.com/503423945">多玩幻灵qwq</n-a></div>
          <div>备案: <n-a href="https://beian.miit.gov.cn/">赣ICP备2022008365号-1</n-a></div>
        </div>
        <div class="footer-d">
          <n-grid :cols="3">
            <n-gi class="footer-d-t">
              <div>模型训练: <n-a href="https://space.bilibili.com/163056936">Stardust_减</n-a></div>
              <div>前端: <n-a href="https://space.bilibili.com/503423945">多玩幻灵qwq</n-a></div> 
            </n-gi>
            <n-gi class="footer-d-t">
              <div>备案: <n-a href="https://beian.miit.gov.cn/">赣ICP备2022008365号-1</n-a></div>
            </n-gi>
            <n-gi class="footer-d-t">
              <div>友链</div>
              <n-a href="https://ai-lab.top/">AI 二创资源中心</n-a>
            </n-gi>
          </n-grid>
        </div>
      </n-layout-footer>
    </n-layout>
  </div>
</n-notification-provider>
</template>

<style scoped>
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

/* 给layout-content上响应式布局，如果是移动端，padding设为200px，桌面端设为800px */
@media screen and (max-width: 768px) {
  .layout-content {
    padding: 50px !important ;
  }
  .footer-m {
    display: flex;
    flex-direction: column;
    text-align: center;
  }
  .footer-d {
    display: none;
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
    background-color: rgba(255, 255, 255, 0.166);
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

</style>
