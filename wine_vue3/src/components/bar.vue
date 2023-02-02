<template>
    <div id="barchart" class="bar" ref="chartone"></div>
</template>

<script>
/* eslint-disable */
  let echarts = require('echarts/lib/echarts');
  // 引入柱状图
  require('echarts/lib/chart/bar');
  require('echarts/lib/component/tooltip');
  require('echarts/lib/component/title');
  require('echarts/lib/component/grid');
  require('echarts/lib/component/toolbox');
  require('echarts/lib/component/legend');
  require('echarts/lib/chart/line');
  require('echarts/lib/component/brush');

  //import eventbus from "@/utils/eventbus";

    export default {
      name: "bar",
      props: {
        id: {
          type: String,
          default: 'barchart'
        },
        faar:{
          type:Number,
          required: true,
        },
      },
      mounted(){
        //console.log("start mounted");
                 
        this.initData();
      },
      data() {
        return {chartone: null,
                sr:this.faar
        };
      },
      methods:{
        initData() {
           var sr=this.faar;  
                  //let xAxisData=['France','Italy','USA','Chile','Spain'];    
           switch (this.sr) {
                    //France
                    case 1:
                        this.data1 = [0, 0, 3, 1, 17];
                        this.data2 = [5, 4, 0, 0, 11];
                        this.data3 = [16, 26, 1, 0, 1];
                        this.data4 = [1296, 1108, 887, 669, 497];
                        this.data5 = [31, 25, 26, 4, 18];
                        this.data6 = [286, 186, 24, 9, 93];
                        this.data7 = [468, 377, 318, 185, 126];
                        this.xAxisData =['France','Italy','USA','Chile','Spain'];
                        console.log('barsuccess:'+sr);
                        break;
                    //USA
                    case 2:
                        this.data1 = [0, 0, 3, 1, 17];
                        this.data2 = [5, 4, 0, 0, 11];
                        this.data3 = [16, 26, 1, 0, 1];
                        this.data4 = [1296, 1108, 887, 669, 497];
                        this.data5 = [31, 25, 26, 4, 18];
                        this.data6 = [286, 186, 24, 9, 93];
                        this.data7 = [468, 377, 318, 185, 126];
                        this.xAxisData =['France','Italy','USA','Chile','Spain'];
                        break;
                    //Argentina
                    case 3:
                        this.data1 = [17, 0, 0, 0, 3];
                        this.data2 = [11, 6, 0, 0, 0];
                        this.data3 = [1, 0, 0, 0, 0];
                        this.data4 = [497, 397, 210, 55, 7];
                        this.data5 =  [18, 4, 1, 0, 2];
                        this.data6 = [93, 24, 6, 4, 9];
                        this.data7 = [126, 132, 43, 95, 116];
                        this.xAxisData =['Spain','Australia','Argentina','NZL','Germany'];
                        break;
                    //Australia
                    case 4:
                        this.data1 = [1, 17, 0, 0, 0];
                        this.data2 = [0, 11, 6, 0, 0];
                        this.data3 = [0, 1, 0, 0, 0];
                        this.data4 = [669, 497, 397, 210, 55];
                        this.data5 = [4, 18, 4, 1, 0];
                        this.data6 = [9, 93, 24, 6, 4];
                        this.data7 =  [185, 126, 132, 43, 95];
                        this.xAxisData =['Chile','Spain','Australia','Argentina','NZL'];
                        break;
                    //Austria
                    case 5:
                        this.data1 = [1, 0, 0, 0, 0];
                        this.data2 = [61, 0, 0, 0, 0];
                        this.data3 = [0, 0, 0, 0, 0];
                        this.data4 = [33, 31, 17, 3, 5];
                        this.data5 = [1, 3, 2, 0, 0];
                        this.data6 = [2, 2, 2, 1, 1];
                        this.data7 = [15, 22, 23, 17, 13];
                        this.xAxisData =['Portugal','Greec','Austria','Canada','Slovenia'];
                        break;
                    //Bulgaria
                    case 6:
                        this.data1 = [0, 0, 0, 0, 0];
                        this.data2 = [0, 0, 0, 0, 0];
                        this.data3 = [0, 0, 0, 0, 0];
                        this.data4 = [4, 3, 2, 1, 0];
                        this.data5 = [0, 0, 0, 0, 1];
                        this.data6 = [0, 1, 0, 0, 1];
                        this.data7 = [2, 0, 1, 2, 0];
                        this.xAxisData =['Croatia','Uruguay','Bulgaria','Japan','Moldova'];
                        break;
                    //Canada
                    case 7:
                        this.data1 = [0, 0, 0, 0, 0];
                        this.data2 = [0, 0, 0, 0, 0];
                        this.data3 = [0, 0, 0, 0, 0];
                        this.data4 = [31, 17, 3, 5, 4];
                        this.data5 = [3, 2, 0, 0, 0];
                        this.data6 = [2, 2, 1, 1, 0];
                        this.data7 = [22, 23, 17, 13, 10];
                        this.xAxisData =['Greece','Austria','Canada','Slovenia','Hungary'];
                        break;
                    //Chile
                    case 8:
                        this.data1 = [0, 3, 1, 17, 0];
                        this.data2 = [4, 0, 0, 11, 6];
                        this.data3 = [26, 1, 0, 1, 0];
                        this.data4 = [1108, 887, 669, 497, 397];
                        this.data5 = [25, 26, 4, 18, 4];
                        this.data6 = [186, 24, 9, 93, 24];
                        this.data7 =  [377, 318, 185, 126, 132];
                        this.xAxisData =['Italy','USA','Chile','Spain','Australia'];
                        break;
                    //Croatia
                    case 9:
                        this.data1 = [0, 0, 0, 0, 0];
                        this.data2 = [2, 0, 0, 0, 0];
                        this.data3 = [0, 0, 0, 0, 0];
                        this.data4 = [2, 4, 4, 3, 2];
                        this.data5 = [0, 0, 0, 0, 0];
                        this.data6 = [3, 0, 0, 1, 0];
                        this.data7 = [3, 2, 2, 0, 1];
                        this.xAxisData =['Korea','Romania','Croatia','Uruguay','Bulgaria'];
                        break;
                    //Georgia
                    case 10:
                        this.data1 = [0, 0, 0, 0, 0];
                        this.data2 = [0, 0, 0, 2, 0];
                        this.data3 = [0, 0, 0, 0, 0];
                        this.data4 = [5, 4, 7, 2, 4];
                        this.data5 = [0, 0, 0, 0, 0];
                        this.data6 = [1, 0, 0, 3, 0];
                        this.data7 = [13, 10, 6, 3, 2];
                        this.xAxisData =['Slovenia','Hungary','Georgia','Korea','Romania'];
                        break;
                    //Germany
                    case 11:
                        this.data1 = [0, 0, 3, 0, 1];
                        this.data2 = [0, 0, 0, 0, 61];
                        this.data3 = [0, 0, 0, 0, 0];
                        this.data4 = [210, 55, 7, 84, 33];
                        this.data5 = [1, 0, 2, 5, 1];
                        this.data6 = [6, 4, 9, 7, 2];
                        this.data7 = [43, 95, 116, 34, 15];
                        this.xAxisData =['Argentina','NZL','Germany','ZA','Portugal'];
                        break;
                    //Greece
                    case 12:
                        this.data1 = [0, 1, 0, 0, 0];
                        this.data2 = [0, 61, 0, 0, 0];
                        this.data3 = [0, 0, 0, 0, 0];
                        this.data4 = [84, 33, 31, 17, 3];
                        this.data5 = [5, 1, 3, 2, 0];
                        this.data6 = [7, 2, 2, 2, 1];
                        this.data7 = [34, 15, 22, 23, 17];
                        this.xAxisData =['ZA','Portugal','Greece','Austria','Canada'];
                        break;
                    //Hungary
                    case 13:
                        this.data1 = [0, 0, 0, 0, 0];
                        this.data2 = [0, 0, 0, 0, 2];
                        this.data3 = [0, 0, 0, 0, 0];
                        this.data4 = [3, 5, 4, 7, 2];
                        this.data5 = [0, 0, 0, 0, 0];
                        this.data6 = [1, 1, 0, 0, 3];
                        this.data7 = [17, 13, 10, 6, 3];
                        this.xAxisData =['Canada','Slovenia','Hungary','Georgia','Korea'];
                        break;
                    //Israel
                    case 14:
                        this.data1 = [0, 0, 0, 0, 0];
                        this.data2 = [0, 0, 0, 0, 0];
                        this.data3 = [0, 0, 0, 0, 0];
                        this.data4 = [2, 1, 0, 1, 0];
                        this.data5 = [0, 0, 1, 0, 0];
                        this.data6 = [0, 0, 1, 0, 1];
                        this.data7 = [1, 2, 0, 0, 0];
                        this.xAxisData =['Bulgaria','Japan','Moldova','Israel','UK'];
                        break;
                    //Italy
                    case 15:
                        this.data1 = [0, 0, 3, 1, 17];
                        this.data2 = [5, 4, 0, 0, 11];
                        this.data3 = [16, 26, 1, 0, 1];
                        this.data4 = [1296, 1108, 887, 669, 497];
                        this.data5 = [31, 25, 26, 4, 18];
                        this.data6 = [286, 186, 24, 9, 93];
                        this.data7 = [468, 377, 318, 185, 126];
                        this.xAxisData =['France','Italy','USA','Chile','Spain'];
                        break;
                    //Japan
                    case 16:
                        this.data1 = [0, 0, 0, 0, 0];
                        this.data2 = [0, 0, 0, 0, 0];
                        this.data3 = [0, 0, 0, 0, 0];
                        this.data4 = [3, 2, 1, 0, 1];
                        this.data5 = [0, 0, 0, 1, 0];
                        this.data6 = [1, 0, 0, 1, 0];
                        this.data7 = [0, 1, 2, 0, 0];
                        this.xAxisData =['Uruguay','Bulgaria','Japan','Moldova','Israel'];
                        break;
                    //Korea
                    case 17:
                        this.data1 = [0, 0, 0, 0, 0];
                        this.data2 = [0, 0, 2, 0, 0];
                        this.data3 = [0, 0, 0, 0, 0];
                        this.data4 = [4, 7, 2, 4, 4];
                        this.data5 = [0, 0, 0, 0, 0];
                        this.data6 = [0, 0, 3, 0, 0];
                        this.data7 = [10, 6, 3, 2, 2];
                        this.xAxisData =['Hungary','Georgia','Korea','Romania','Croatia'];
                        break;
                    //Moldova
                    case 18:
                        this.data1 = [0, 0, 0, 0, 0];
                        this.data2 = [0, 0, 0, 0, 0];
                        this.data3 = [0, 0, 0, 0, 0];
                        this.data4 = [2, 1, 0, 1, 0];
                        this.data5 = [0, 0, 1, 0, 0];
                        this.data6 = [0, 0, 1, 0, 1];
                        this.data7 = [1, 2, 0, 0, 0];
                        this.xAxisData =['Bulgaria','Japan','Moldova','Israel','UK'];
                        break;
                    //NZL
                    case 19:
                        this.data1 = [0, 0, 0, 3, 0];
                        this.data2 = [6, 0, 0, 0, 0];
                        this.data3 = [0, 0, 0, 0, 0];
                        this.data4 = [397, 210, 55, 7, 84];
                        this.data5 = [4, 1, 0, 2, 5];
                        this.data6 = [24, 6, 4, 9, 7];
                        this.data7 = [132, 43, 95, 116, 34];
                        this.xAxisData =['Australia','Argentina','NZL','Germany','ZA'];
                        break;
                    //Portugal
                    case 20:
                        this.data1 = [3, 0, 1, 0, 0];
                        this.data2 = [0, 0, 61, 0, 0];
                        this.data3 = [0, 0, 0, 0, 0];
                        this.data4 = [7, 84, 33, 31, 17];
                        this.data5 = [2, 5, 1, 3, 2];
                        this.data6 = [9, 7, 2, 2, 2];
                        this.data7 = [116, 34, 15, 22, 23];
                        this.xAxisData =['Germany','ZA','Portugal','Greece','Austria'];
                        break;
                    //Romania
                    case 21:
                        this.data1 = [0, 0, 0, 0, 0];
                        this.data2 = [0, 2, 0, 0, 0];
                        this.data3 = [0, 0, 0, 0, 0];
                        this.data4 = [7, 2, 4, 4, 3];
                        this.data5 = [0, 0, 0, 0, 0];
                        this.data6 = [0, 3, 0, 0, 1];
                        this.data7 = [6, 3, 2, 2, 0];
                        this.xAxisData =['Georgia','Korea','Romania','Croatia','Uruguay'];
                        break;
                    //Slovenia
                    case 22:
                        this.data1 = [0, 0, 0, 0, 0];
                        this.data2 = [0, 0, 0, 0, 0];
                        this.data3 = [0, 0, 0, 0, 0];
                        this.data4 = [17, 3, 5, 4, 7];
                        this.data5 = [2, 0, 0, 0, 0];
                        this.data6 = [2, 1, 1, 0, 0];
                        this.data7 = [23, 17, 13, 10, 6];
                        this.xAxisData =['Austria','Canada','Slovenia','Hungary','Georgia'];
                        break;
                    //Spain
                    case 23:
                        this.data1 = [3, 1, 17, 0, 0];
                        this.data2 = [0, 0, 11, 6, 0];
                        this.data3 = [1, 0, 1, 0, 0];
                        this.data4 = [887, 669, 497, 397, 210];
                        this.data5 = [26, 4, 18, 4, 1];
                        this.data6 = [24, 9, 93, 24, 6];
                        this.data7 = [318, 185, 126, 132, 43];
                        this.xAxisData =['USA','Chile','Spain','Australia','Argentina'];
                        break;
                    //ZA
                    case 24:
                        this.data1 = [0, 3, 0, 1, 0];
                        this.data2 = [0, 0, 0, 61, 0];
                        this.data3 = [0, 0, 0, 0, 0];
                        this.data4 = [55, 7, 84, 33, 31];
                        this.data5 = [0, 2, 5, 1, 3];
                        this.data6 = [4, 9, 7, 2, 2];
                        this.data7 = [95, 116, 34, 15, 22];
                        this.xAxisData =['NZL','Germany','ZA','Portugal','Greece'];
                        break;
                    //UK
                    case 25:
                        this.data1 = [0, 0, 0, 0, 0];
                        this.data2 = [0, 0, 0, 0, 0];
                        this.data3 = [0, 0, 0, 0, 0];
                        this.data4 = [2, 1, 0, 1, 0];
                        this.data5 = [0, 0, 1, 0, 0];
                        this.data6 = [0, 0, 1, 0, 1];
                        this.data7 = [1, 2, 0, 0, 0];
                        this.xAxisData =['Bulgaria','Japan','Moldova','Israel','UK'];
                        break;
                    //Uruguay
                    case 26:
                        this.data1 = [0, 0, 0, 0, 0];
                        this.data2 = [0, 0, 0, 0, 0];
                        this.data3 = [0, 0, 0, 0, 0];
                        this.data4 = [4, 4, 3, 2, 1];
                        this.data5 = [0, 0, 0, 0, 0];
                        this.data6 = [0, 0, 1, 0, 0];
                        this.data7 = [2, 2, 0, 1, 2];
                        this.xAxisData =['Romania','Croatia','Uruguay','Bulgaria','Japan'];
                        break;
                    //展示法国
                    default:
                        this.data1 = [0, 0, 3, 1, 17];
                        this.data2 = [5, 4, 0, 0, 11];
                        this.data3 = [16, 26, 1, 0, 1];
                        this.data4 = [1296, 1108, 887, 669, 497];
                        this.data5 = [31, 25, 26, 4, 18];
                        this.data6 = [286, 186, 24, 9, 93];
                        this.data7 = [468, 377, 318, 185, 126];
                        this.xAxisData =['France','Italy','USA','Chile','Spain'];
                        break;
           }
         for (let i = 0; i < 5; i++) {
          this.data1.push();
          this.data2.push();
          this.data3.push();
          this.data4.push();
          this.data5.push();
          this.data6.push();
          this.data7.push();
          }
           this.chartone= echarts.init(this.$refs.chartone);

var emphasisStyle = {
  itemStyle: {
    shadowBlur: 10,
    shadowColor: 'rgba(0,0,0,0.3)'
  }
};
          let option = {
  brush: {
    toolbox: ['rect', 'clear'],
    xAxisIndex: 0
  },
  toolbox: {
    feature: {
      magicType: {
        type: ['stack']
      },
      dataView: {}
    }
  },
  tooltip: {},
  xAxis: {
    data: this.xAxisData,
    name: '',
    //nameTextStyle:{
      //fontWeight:'lighter',
      //fontSize:2,
      //color:"red"},
    axisLine: { onZero: true },
    splitLine: { show: false },
    splitArea: { show: false }
  },
  yAxis: {},
  grid: {
    bottom: 100
  },
  series: [
    {
      name: 'Red',
      color:"#de1c31",
      type: 'bar',
      stack: 'one',
      emphasis: emphasisStyle,
      data: this.data4
    },
    {
      name: 'White',
      color:'#fbf2e3',
      type: 'bar',
      stack: 'two',
      emphasis: emphasisStyle,
      data: this.data7
    },
    {
      name: 'Rose',
      color:'#f17666',
      type: 'bar',
      stack: 'three',
      emphasis: emphasisStyle,
      data: this.data5
    },
    {
      name: 'Fortified',
      color:'#2e317c',
      type: 'bar',
      stack: 'four',
      emphasis: emphasisStyle,
      data: this.data2
    },
    {
      name: 'Sparkling',
      color:'#83cbac',
      type: 'bar',
      stack: 'five',
      emphasis: emphasisStyle,
      data: this.data6
    },
    {
      name: 'Etc',
      color:'#2177b8',
      type: 'bar',
      stack: 'six',
      emphasis: emphasisStyle,
      data: this.data1
    },
    {
      name: 'Hard',
      color:'#bce936',
      type: 'bar',
      stack: 'seven',
      emphasis: emphasisStyle,
      data: this.data3
    }
  ]
};
         this.chartone.on('brushSelected', function (params) {
          var brushed = [];
          var brushComponent = params.batch[0];
          for (var sIdx = 0; sIdx < brushComponent.selected.length; sIdx++) {
          var rawIndices = brushComponent.selected[sIdx].dataIndex;
          brushed.push('[Series ' + sIdx + '] ' + rawIndices.join(', '));
          }
        });

    if (option && typeof option === 'object') {
      this.chartone.setOption(option);
    }
        }
      }
    }
</script>

<style lang="css">
  .bar {min-height: 300px; min-width: 480px;position: relative;height: 100%; }
</style>