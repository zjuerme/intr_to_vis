
<template>
  <div class="m-map">
    <div id="js-container" class="map">正在加载数据 ...</div>
  </div>

</template>
<script>
/* eslint-disable */
import remoteLoad from '@/utils/remoteLoad.js'
import eventbus from "@/utils/eventbus";

// 高德地图 key
export const MapKey = 'cfd8da5cf010c5f7441834ff5e764f5b'
// 地图限定城市
export const MapCityName = 'New York'

// import { MapKey, MapCityName } from '@/config/config'
export default {
  props: ['lat', 'lng'],
  data () {
    return {
      searchKey: '',
      placeSearch: null,
      dragStatus: false,
      AMapUI: null,
      AMap: null,
      r: 0
    }
  },
  methods: {
    // 实例化地图
    initMap () {
      // 加载PositionPicker，loadUI的路径参数为模块名中 'ui/' 之后的部分
      let AMapUI = this.AMapUI = window.AMapUI
      let AMap = this.AMap = window.AMap
      AMapUI.loadUI(['misc/PositionPicker'], PositionPicker => {
        let mapConfig = {
          zoom: 4,
          center: [15, 45],
          cityName: MapCityName,
          //mapStyle: 'amap://styles/whitesmoke'
          mapStyle: 'amap://styles/fresh'    //控制地图样式，不加为默认

        }


        let map = new AMap.Map('js-container', mapConfig)
        
        // 启用工具条
        AMap.plugin(['AMap.ToolBar'], function () {
          map.addControl(new AMap.ToolBar({
            position: 'RB'
          }))
        })
        
        ////////////////////////////////////////////////////////////////////酒瓶标记
        var markerChile = new AMap.Marker({
          position: new AMap.LngLat(-71,-33.463867),
          offset: new AMap.Pixel(-10, -10),
          icon: 'static/Chile.png',
          anchor: 'center-left',
          title:'Chile',
          //label: {content: 'Chile',direction: 'top',offset: [20, 20]}
        });
        var markerFrance = new AMap.Marker({
          position: new AMap.LngLat(2.21,48.5124),
          icon: 'static/France.png',
          anchor: 'center-center',
          title:'France',
          //label: {content: 'France',direction: 'top',offset: [20, 20]}
        });
        var markerItaly = new AMap.Marker({
          position: new AMap.LngLat(12.2858,41.5335),
          offset: new AMap.Pixel(-10, -10),
          icon: 'static/Italy.png',
          anchor: 'center-left',
          title:'Italy',
          //label: {content: 'Chile',direction: 'top',offset: [20, 20]}
        });
        var markerUSA = new AMap.Marker({
          position: new AMap.LngLat(-111.53,40.45),
          offset: new AMap.Pixel(-10, -10),
          icon: 'static/USA.png',
          anchor: 'center-left',
          title:'USA',
          //label: {content: 'Chile',direction: 'top',offset: [20, 20]}
        });
        var markerSpain = new AMap.Marker({
          position: new AMap.LngLat(-5.43,40.23),
          offset: new AMap.Pixel(0, -10),
          icon: 'static/Spain.png',
          anchor: 'center-left',
          title:'Spain',
          //label: {content: 'Chile',direction: 'top',offset: [20, 20]}
        });
        var markerAustralia = new AMap.Marker({
          position: new AMap.LngLat(147.12,-33.51),
          offset: new AMap.Pixel(-10, -10),
          icon: 'static/Australia.png',
          anchor: 'center-left',
          title:'Australia',
          //label: {content: 'Chile',direction: 'top',offset: [20, 20]}
        });
        var markerArgentina = new AMap.Marker({
          position: new AMap.LngLat(-63,-34.33),
          offset: new AMap.Pixel(-10, -10),
          icon: 'static/Argentina.png',
          anchor: 'center-left',
          title:'Argentina',
          //label: {content: 'Chile',direction: 'top',offset: [20, 20]}
        });
        var markerNewZealand = new AMap.Marker({
          position: new AMap.LngLat(170,-41.3),
      
          icon: 'static/NewZealand.png',
          anchor: 'center-left',
          title:'NewZealand',
          //label: {content: 'Chile',direction: 'top',offset: [20, 20]}
        });
        var markerGermany = new AMap.Marker({
          position: new AMap.LngLat(13.33,52.51),
          offset: new AMap.Pixel(-10, -10),
          icon: 'static/Germany.png',
          anchor: 'center-left',
          title:'Germany',
          //label: {content: 'Chile',direction: 'top',offset: [20, 20]}
        });
        var markerSouthAfrica = new AMap.Marker({
          position: new AMap.LngLat(28.29,-25.67),
          offset: new AMap.Pixel(-8, -11),
          icon: 'static/SouthAfrica.png',
          anchor: 'center-left',
          title:'SouthAfrica',
          //label: {content: 'Chile',direction: 'top',offset: [20, 20]}
        });
        var markerPortugal = new AMap.Marker({
          position: new AMap.LngLat(-9.06,38.71),
          offset: new AMap.Pixel(-10, -10),
          icon: 'static/Portugal.png',
          anchor: 'center-left',
          title:'Portugal',
          //label: {content: 'Chile',direction: 'top',offset: [20, 20]}
        });
        var markerGreece = new AMap.Marker({
          position: new AMap.LngLat(23.72,37.95),
          offset: new AMap.Pixel(-10, -10),
          icon: 'static/Greece.png',
          anchor: 'center-left',
          title:'Greece',
          //label: {content: 'Chile',direction: 'top',offset: [20, 20]}
        });
        var markerAustria = new AMap.Marker({
          position: new AMap.LngLat(16.38,48.15),
          offset: new AMap.Pixel(-10, -10),
          icon: 'static/Austria.png',
          anchor: 'center-left',
          title:'Austria',
          //label: {content: 'Chile',direction: 'top',offset: [20, 20]}
        });
        var markerCanada = new AMap.Marker({
          position: new AMap.LngLat(-75.66,45.45),
          offset: new AMap.Pixel(-10, -10),
          icon: 'static/Canada.png',
          anchor: 'center-left',
          title:'Canada',
          //label: {content: 'Chile',direction: 'top',offset: [20, 20]}
        });
        var markerSlovenia = new AMap.Marker({
          position: new AMap.LngLat(14.50,46.05),
          offset: new AMap.Pixel(-10, -10),
          icon: 'static/Slovenia.png',
          anchor: 'center-left',
          title:'Slovenia',
          //label: {content: 'Chile',direction: 'top',offset: [20, 20]}
        });
        var markerHungary = new AMap.Marker({
          position: new AMap.LngLat(19.05,47.499),
          offset: new AMap.Pixel(-10,0 ),
          icon: 'static/Hungary.png',
          anchor: 'center-left',
          title:'Hungary',
          //label: {content: 'Chile',direction: 'top',offset: [20, 20]}
        });
        var markerGeorgia = new AMap.Marker({
          position: new AMap.LngLat(44.75,41.7),
          offset: new AMap.Pixel(-10, -10),
          icon: 'static/Georgia.png',
          anchor: 'center-left',
          title:'Georgia',
          //label: {content: 'Chile',direction: 'top',offset: [20, 20]}
        });
        var markerKorea = new AMap.Marker({
          position: new AMap.LngLat(126.97,37.57),
          offset: new AMap.Pixel(-10, -10),
          icon: 'static/Korea.png',
          anchor: 'center-left',
          title:'Korea',
          //label: {content: 'Chile',direction: 'top',offset: [20, 20]}
        });
        var markerRomania = new AMap.Marker({
          position: new AMap.LngLat(26.11,44.56),
          offset: new AMap.Pixel(-10, -10),
          icon: 'static/Romania.png',
          anchor: 'center-left',
          title:'Romania',
          //label: {content: 'Chile',direction: 'top',offset: [20, 20]}
        });
        var markerCroatia = new AMap.Marker({
          position: new AMap.LngLat(16,45.77),
          offset: new AMap.Pixel(-10, -10),
          icon: 'static/Croatia.png',
          anchor: 'center-left',
          title:'Croatia',
          //label: {content: 'Chile',direction: 'top',offset: [20, 20]}
        });
        var markerUruguay = new AMap.Marker({
          position: new AMap.LngLat(-56.167,-32.82),
          offset: new AMap.Pixel(-10, -10),
          icon: 'static/Uruguay.png',
          anchor: 'center-left',
          title:'Uruguay',
          //label: {content: 'Chile',direction: 'top',offset: [20, 20]}
        });
        var markerBulgaria = new AMap.Marker({
          position: new AMap.LngLat(23.34,42.67),
          offset: new AMap.Pixel(-10, -10),
          icon: 'static/Bulgaria.png',
          anchor: 'center-left',
          title:'Bulgaria',
          //label: {content: 'Chile',direction: 'top',offset: [20, 20]}
        });
        var markerJapan = new AMap.Marker({
          position: new AMap.LngLat(139.7,35.66),
          offset: new AMap.Pixel(-10, -10),
          icon: 'static/Japan.png',
          anchor: 'center-left',
          title:'Japan',
          //label: {content: 'Chile',direction: 'top',offset: [20, 20]}
        });
        var markerMoldova = new AMap.Marker({
          position: new AMap.LngLat(28.5,47),
          offset: new AMap.Pixel(-10, -10),
          icon: 'static/Moldova.png',
          anchor: 'center-left',
          title:'Moldova',
          //label: {content: 'Chile',direction: 'top',offset: [20, 20]}
        });
        var markerIsrael = new AMap.Marker({
          position: new AMap.LngLat(35.13,31.47),
          offset: new AMap.Pixel(-10, -10),
          icon: 'static/Israel.png',
          anchor: 'center-left',
          title:'Israel',
          //label: {content: 'Chile',direction: 'top',offset: [20, 20]}
        });
        var markerUK = new AMap.Marker({
          position: new AMap.LngLat(-3,53),
          offset: new AMap.Pixel(-10, -10),
          icon: 'static/UK.png',
          anchor: 'center-left',
          title:'UK',
          //label: {content: 'Chile',direction: 'top',offset: [20, 20]}
        });
        map.add(markerChile);
        map.add(markerFrance);
        map.add(markerItaly);
        map.add(markerUSA);
        map.add(markerSpain);
        map.add(markerAustralia);
        map.add(markerArgentina);
        map.add(markerNewZealand);
        map.add(markerGermany);
        map.add(markerSouthAfrica);
        map.add(markerPortugal);
        map.add(markerGreece);
        map.add(markerAustria);
        map.add(markerCanada);
        map.add(markerSlovenia);
        map.add(markerHungary);
        map.add(markerGeorgia);
        map.add(markerKorea);
        map.add(markerRomania);
        map.add(markerCroatia);
        map.add(markerUruguay);
        map.add(markerBulgaria);
        map.add(markerJapan);
        map.add(markerMoldova);
        map.add(markerIsrael);
        map.add(markerUK);

        /////////鼠标点击事件
        ///////eventbus,传参
        //AMap.event.addListener(markerFrance, 'click', function(){
        //  r=2;
        //  eventbus.$emit('clicked',r);
        //});
        markerFrance.on("click", this.changeFrance);
        markerUSA.on("click", this.changeUSA);
        markerArgentina.on("click", this.changeArgentina);
        markerAustralia.on("click", this.changeAustralia);
        markerAustria.on("click", this.changeAustria);
        markerBulgaria.on("click", this.changeBulgaria);
        markerCanada.on("click", this.changeCanada);
        markerChile.on("click", this.changeChile);
        markerCroatia.on("click", this.changeCroatia);
        markerGeorgia.on("click", this.changeGeorgia);
        markerGermany.on("click", this.changeGermany);
        markerGreece.on("click", this.changeGreece);
        markerHungary.on("click", this.changeHungary);
        markerIsrael.on("click", this.changeIsrael);
        markerItaly.on("click", this.changeItaly);
        markerJapan.on("click", this.changeJapan);
        markerKorea.on("click", this.changeKorea);
        markerMoldova.on("click", this.changeMoldova);
        markerNewZealand.on("click", this.changeNewZealand);
        markerPortugal.on("click", this.changePortugal);
        markerRomania.on("click", this.changeRomania);
        markerSlovenia.on("click", this.changeSlovenia);
        markerSouthAfrica.on("click", this.changeSouthAfrica);
        markerSpain.on("click", this.changeSpain);
        markerUK.on("click", this.changeUK);
        markerUruguay.on("click", this.changeUruguay);
      })
    },
    changeFrance() {
          this.$emit('handleChange', 1) 
        },
    changeUSA() {
          this.$emit('handleChange', 2) 
        },
    changeArgentina() {
          this.$emit('handleChange', 3) 
        },
    changeAustralia() {
          this.$emit('handleChange', 4) 
        },
    changeAustria() {
          this.$emit('handleChange', 5) 
        },
    changeBulgaria() {
          this.$emit('handleChange', 6) 
        },
    changeCanada() {
          this.$emit('handleChange', 7) 
        },
    changeChile() {
          this.$emit('handleChange', 8) 
        },
    changeCroatia() {
          this.$emit('handleChange', 9) 
        },
    changeGeorgia() {
          this.$emit('handleChange', 10) 
        },
    changeGermany() {
          this.$emit('handleChange', 11) 
        },
    changeGreece() {
          this.$emit('handleChange', 12) 
        },
    changeHungary() {
          this.$emit('handleChange', 13) 
        },
    changeIsrael() {
          this.$emit('handleChange', 14) 
        },
    changeItaly() {
          this.$emit('handleChange', 15) 
        },
    changeJapan() {
          this.$emit('handleChange', 16) 
        },
    changeKorea() {
          this.$emit('handleChange', 17) 
        },
    changeMoldova() {
          this.$emit('handleChange', 18) 
        },
    changeNewZealand() {
          this.$emit('handleChange', 19) 
        },
    changePortugal() {
          this.$emit('handleChange', 20) 
        },
    changeRomania() {
          this.$emit('handleChange', 21) 
        },
    changeSlovenia() {
          this.$emit('handleChange', 22) 
        },
    changeSpain() {
          this.$emit('handleChange', 23) 
        },
    changeSouthAfrica() {
          this.$emit('handleChange', 24) 
        },
    changeUK() {
          this.$emit('handleChange', 25) 
        },
    changeUruguay() {
          this.$emit('handleChange', 26) 
        }
    },
  async created () {
    // 已载入高德地图API，则直接初始化地图
    if (window.AMap && window.AMapUI) {
      this.initMap()
    // 未载入高德地图API，则先载入API再初始化
    } else {
      await remoteLoad(`http://webapi.amap.com/maps?v=1.3&key=${MapKey}`)
      await remoteLoad('http://webapi.amap.com/ui/1.0/main.js')
      this.initMap()
    }
  }

}
</script>

<style lang="css">
.m-map{ min-width: 500px; min-height: 300px; position: relative; }
.m-map .map{ height: 100%; }
</style>
