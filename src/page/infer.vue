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


const spk = ref("")
const text = ref("")
const sdp_dp = ref(0.2)
const noise = ref(0.5)
const noisew = ref(0.9)
const length = ref(1.0)
const audio_url = ref("")
const msg = ref("")
// setInterval(() => console.log(options.value),500)

const autocomplete_options = computed(() => spks.value.filter((item: string) => item.includes(spk.value)).map((spk: any) => {
  return {
    label: spk,
    value: spk
  }
}))
const infer_fn = async () => {
  const data = await infer({
    text: text.value,
    speaker: spk.value as unknown as string,
    sdp_ratio: sdp_dp.value,
    noise: noise.value,
    noisew: noisew.value,
    length: length.value,
    token: store.token.value as string,
  })
  audio_url.value = data.audio
  msg.value = data.message
  notification.info({content: msg.value,duration: 10000})  
}

// 1 选择
// 2 auto complete
var spk_mode = ref(1)

</script>

<template>
  <n-layout-content bordered class="layout-content" style="padding: 800px;padding-top: 50px;background: rgba(240, 255, 255, 0);">
  <n-form class="backdrop">
    <n-form-item label="文本">
      <n-input
        v-model:value="text"
        type="textarea"
        placeholder="原神4.0版本模型测试中，本地推理整合包将在模型最终版发布时候发布 。反馈邮箱：aihobbyistorg@gmail.com"
        class = "text"
        rows="17"
      />
    </n-form-item>
    <n-form-item label="角色">
      <n-select v-model:value="spk" size="medium" :options="options" v-if="spk_mode == 1"/>
      <n-auto-complete
        v-else
        v-model:value="spk"
        :input-props="{
          autocomplete: 'disabled'
        }"
        :options="autocomplete_options"
        placeholder="角色"
      />
      <n-button type="primary" @click="spk_mode = spk_mode == 1? 2: 1">切换到{{ spk_mode == 1? "查找模式": "选择模式" }}</n-button>
    </n-form-item>
    <!-- SDP/DP混合比 -->
    <n-grid :cols="24" item-responsive>https://tts.ai-lab.top/audio/92ae2682b38dfec16575428c3622e31d.wav
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
          <div><n-button type="primary" @click="infer_fn">合成！</n-button></div>
        <!-- </div> -->
      </n-gi>
    </n-grid>
  </n-form>
</n-layout-content>
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
}
@media screen and (min-width: 768px) {
  .layout-content {
    padding: 0 20vw !important;
  }
}

.footer-d-t {
  text-align: center;
}

.text{
  width: 1500px;
}

</style>
