<!--本组件用于测试通讯-->
<template>
  <button @click="emitGlobalClickEvent()">{{ clickCount }}</button>
</template>

<script>
/* eslint-disable */
import eventbus from "@/utils/eventbus";

export default {
  data() {
    return {
      clickCount: 0
    }
  },

  methods: {
    emitGlobalClickEvent() {
      this.clickCount++;
      eventbus.$emit('clicked', this.clickCount);
    }
  }
}
</script>