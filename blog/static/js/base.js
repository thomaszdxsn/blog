$(document).ready(function() {
    tagcloud({
        selector: ".tagcloud",  //元素选择器
        fontsize: 24,       //基本字体大小
        radius: 60,         //滚动半径
        mspeed: "slow",   //滚动最大速度
        ispeed: "slow",   //滚动初速度
        direction: 135,     //初始滚动方向
        keep: true          //鼠标移出组件后是否继续随鼠标滚动
    });
});