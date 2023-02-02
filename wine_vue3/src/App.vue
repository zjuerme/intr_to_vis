<template>
  <div id="App">
    <!-- <img src="./assets/logo.png"> -->
      <div>
        <mapDrag @drag="dragMap" @handleChange="changeName" class="mapbox"></mapDrag>
      </div>
      <div>
        <pGraph class="pcp"></pGraph>
      </div>
      <div>
        <bar class="bar" v-if="chartIsShow"  v-bind:faar="ar"></bar>
      </div>
      <div>
        <pic class="pic" v-if="chartIsShow"  v-bind:faar="ar"></pic>
      </div>
      <!--div>
        <ClickCountButton></ClickCountButton>
      </div-->
       <!--button @click="forceRerender()">reload</button-->
  </div>

</template>

<script>
/* eslint-disable */
import mapDrag from './components/mapDrag'
import pGraph from './components/pGraph'
import bar from './components/bar.vue'
import pic from './components/pic.vue'

//import ClickCountButton from './components/ClickCountButton'
//import eventbus from "@/utils/eventbus";

export default {
  name: 'App',
  components: {
    pGraph,
    mapDrag,
    bar,
    pic,
   // ClickCountButton
},
  data () {
    return {
      //key:0,
      chartIsShow:true,
      ar:1,//初始载入法国数据
      dragData: {
        lng: null,
        lat: null,
        address: null,
        nearestJunction: null,
        nearestRoad: null,
        nearestPOI: null
      }
    }
  },
  methods: {
    //changeappr(){
      //this.appr=r;
   // },

   changeName(r) {  // name形参是子组件中传入的值Jack
      this.ar=r;
      console.log('methods:'+this.ar);
      this.chartIsShow = false;
      this.$nextTick(() => {
          // 在 DOM 中添加 my-component 组件
          this.chartIsShow = true;
      });
    },
    ///////////////////////////如果想以按钮方式刷新，请启用此下方注解
    //forceRerender() {
        // 从 DOM 中删除 my-component 组件
    //        this.chartIsShow = false;
    //        this.$nextTick(() => {
          // 在 DOM 中添加 my-component 组件
     //           this.chartIsShow = true;
    //         });
    //  },


    dragMap (data) {
      this.dragData = {
        lng: data.position.lng,
        lat: data.position.lat,
        address: data.address,
        nearestJunction: data.nearestJunction,
        nearestRoad: data.nearestRoad,
        nearestPOI: data.nearestPOI
      }
    }
  },
    //watch:{
     //   faar(val){    //message即为父组件的值，val参数为值
    //      this.sr = val    //将父组件的值赋给childrenMessage 子组件的值
    //      console.logo("watch"+val)
     //   }
    //  } 
   // mounted(){
      //this.appr=10;
     // this.ar=this.appr;
      //console.logo("have mounted");
    //} 
}


///////////////////////////////////////////////组件间交互eventbus
//const clickChanger = function(r) {
//    this.appr=r;
//    console.log('appr:'+this.appr);
//    //mounted;
//}
//eventbus.$on('clicked', clickChanger);
//eventbus.$off('clicked', clickHandler);
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.mapbox{ width: 1000px; height: 500px; float: left;left:1% }
.pcp{top: 500px;z-index: 13;}
.bar{left:68%;width: 480px;top:30px;z-index: 14;}
.pic{left:68%;width: 480px;bottom:530px;z-index: 1;}
</style>
