/* eslint-disable */
import Vue from 'vue';
/**
 * 事件总线
 * @usage:
 * eventbus.$emit('event',payload);
 * eventbus.$on('on',(payload)=>{});
 */
const eventbus = new Vue();
export default eventbus
