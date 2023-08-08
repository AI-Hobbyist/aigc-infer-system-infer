<script setup lang="ts">
import infer from '../api/infer';
import getSpks from '../api/spks'
import { computed, ref } from "vue"
import { useUserStore } from '../store';
import { useNotification } from 'naive-ui'
const notification = useNotification()

const spks = ref([])
const store = useUserStore()

getSpks().then(data => {
  spks.value = data
  console.log(spks.value);
  
})

const options = computed(() => spks.value.map((spk: any) => {
  return {
    label: spk,
    value: spk
  }
}))

const spk = ref(null)
const text = ref("")
const sdp_dp = ref(0.2)
const noise = ref(0.5)
const noisew = ref(0.9)
const length = ref(0.8)
const format = ref("wav")
const audio_url = ref("")
// setInterval(() => console.log(options.value),500)

const infer_fn = async () => {
  const data = await infer({
    text: text.value,
    speaker: spk.value as unknown as string,
    sdp_ratio: sdp_dp.value,
    noise: noise.value,
    noisew: noisew.value,
    length: length.value,
    token: store.token as string,
  })
  console.log(data);
  audio_url.value = data.audio
  notification.success({content: "推理成功",duration: 3000})  
}

</script>

<template>
  <n-form class="backdrop">
    <n-form-item label="文本">
      <n-input
        v-model:value="text"
        type="textarea"
        placeholder="就在这理发店"
      />
    </n-form-item>
    <n-form-item label="角色">
      <n-select v-model:value="spk" size="medium" :options="options" />
    </n-form-item>
    <!-- SDP/DP混合比 -->
    <n-grid :cols="24" item-responsive>
      <n-gi span="0:24 768:12">
        <n-form-item-gi style="padding-left: 3px;padding-right: 3px;" label="SDP/DP 混合比">
          <!-- <n-select v-model:value="spk" size="medium" :options="options" /> -->
          <n-slider v-model:value="sdp_dp" :step="0.1" :min="0.1" :max="0.8" />
        </n-form-item-gi>
      </n-gi>
      <n-gi span="0:24 768:12">
        <n-form-item-gi style="padding-left: 3px;padding-right: 3px;" label="感情">
          <!-- <n-select v-model:value="spk" size="medium" :options="options" /> -->
          <n-slider v-model:value="noise" :min="0" :max="1.5" :step="0.1" />
        </n-form-item-gi>
      </n-gi>
      <n-gi span="0:24 768:12">
        <n-form-item-gi style="padding-left: 3px;padding-right: 3px;" label="音素长度">
          <!-- <n-select v-model:value="spk" size="medium" :options="options" /> -->
          <n-slider v-model:value="noisew" :min="0.5" :max="1.5" :step="0.1" />
        </n-form-item-gi>
      </n-gi>
      <n-gi span="0:24 768:12">
        <n-form-item-gi style="padding-left: 3px;padding-right: 3px;" label="语速">
          <!-- <n-select v-model:value="spk" size="medium" :options="options" /> -->
          <n-slider v-model:value="length" :min="0.5" :max="2" :step="0.1" />
        </n-form-item-gi>
      </n-gi>
    </n-grid>
    <!-- Audio -->
    <n-grid cols="24" item-responsive>
      <n-gi span="0:24 768:12" style="display: flex;">
        <div style="display: flex;flex-direction: column;justify-content: center;">
          <audio controls :src="audio_url"></audio>
        </div>
      </n-gi>
      <n-gi span="0:24 768:12" style="display: flex;justify-content: flex-end;">
        <!-- <div> -->
          <!-- <div style="display: flex;margin-left: 10px;margin-right: 10px;flex-direction: column;justify-content: center;">格式</div> -->
          <div><n-button type="primary" @click="infer_fn">即刻生成</n-button></div>
          <div><n-select v-model:value="format" style="min-width: 100px;" size="medium" :options="[{label: 'wav', value: 'wav'},{label: 'mp3', value: 'mp3'}]" /></div>
        <!-- </div> -->
      </n-gi>
    </n-grid>
  </n-form>
</template>

<style scoped>
.backdrop {
  backdrop-filter: blur(10px);
  /* background: rgba(240, 255, 255, 0); */
  background: rgb(255 255 255 / 31%);
  padding: 20px;
  border-radius: 20px;
  margin-top: 50px;
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
    padding: 800px;
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
