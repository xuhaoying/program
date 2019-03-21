
'''
链家格式 house_content.html
XX公寓 house_another.html
'''
from bs4 import BeautifulSoup
import re

html = '''



<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta http-equiv="Cache-Control" content="no-transform" />
  <meta http-equiv="Cache-Control" content="no-siteapp" />
  <meta http-equiv="Content-language" content="zh-CN" />
  <meta name="format-detection" content="telephone=no" />
  <meta name="applicable-device" content="pc">
	<meta name="description" content="贝壳杭州租房网,提供天阳美林湾 2室1厅 4300元出租房源信息,此房源位于杭州拱墅申花的天阳美林湾,2室86㎡4300元.找租房房源,就来杭州贝壳租房!">
	<meta name="keywords" content="天阳美林湾 2室1厅 4300元,天阳美林湾租房信息,杭州拱墅申花房屋出租">
	<meta http-equiv="Cache-Control" content="no-transform " />
	<title>天阳美林湾 2室1厅 4300元-天阳美林湾租房信息-杭州天阳美林湾申花房屋出租【杭州贝壳租房】</title>
	<link href="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/img/favicon.ico?_v=201903142105200c0" type="image/x-icon" rel="icon">
		<link rel="stylesheet" href="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/common/css/common.css?_v=201903142105200c0">
	  <script>
    var g_conf = {};
  </script>
    <link rel="stylesheet" href="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/page/detail/index.css?_v=201903142105200c0">
    <link href='//s1.ljcdn.com/feroot/pc/asset/lianjiaIM/css/lianjiaim.css?v=15212312340214' property='stylesheet' rel="stylesheet">
  <style>
    .browser__low {
      height: 100%;
      overflow: hidden;
    }
    .browser__low--wrapper,
    .browser__low--inner {
      display: none;
    }
    .browser__low .browser__low--wrapper {
      position: absolute;
      left: 0;
      right: 0;
      top: 0;
      bottom: 0;
      z-index: 199999;
      background: #000;
      opacity: 0.5;
      filter: alpha(opacity=50);
      display: block;
    }
    .browser__low .browser__low--inner {
      background: #fff;
      position: absolute;
      left: 50%;
      top: 50%;
      z-index: 19999999;
      width: 360px;
      height: 100px;
      margin-top: -90px;
      margin-left: -200px;
      padding: 40px 20px;
      display: block;
    }
    .browser__low .browser__low--inner p {
      font-size: 20px;
      padding-bottom: 40px;
    }
    .browser__low .browser__low--inner a {
      display: inline-block;
      color: #fff;
      background: #2ab78e;
      padding: 10px 6px;
    }
  </style>
  </head>

<body>
<div class="browser__low--wrapper"></div>
<div class="browser__low--inner">
<p>您的浏览器版本过低，请升级：</p>
<a href="https://www.baidu.com/s?wd=chrome" target="_blank">谷歌 Chrome浏览器</a>
</div>

<script>
;;(function() {
  if(!([].forEach)) {
    document.body.className += ' browser__low';
  }
})();
</script>
<div class="wrapper">
   <!--<link href="--><?//=APP_MODE === 'prod' ? '//s1.ljcdn.com/feroot/pc/asset/lianjiaIM/css/lianjiaim.css?v=15212312340214' : '//s1.pc56.lj-web-56.lianjia.com/feroot/pc/asset/lianjiaIM/css/lianjiaim.css'?><!--" property='stylesheet' rel="stylesheet">-->


<div>

  <!-- 引入公用的头、导航、搜索栏 -->
  <div class="header ">
  <ul class="header__wrapper w1150 clear typeUserInfo" id="top">
                      <li class="header__item fl "><a href="//hz.lianjia.com" target="_blank">首页</a></li>
                        <li class="header__item fl "><a href="//hz.lianjia.com/ershoufang/" target="_blank">二手房</a></li>
                        <li class="header__item fl "><a href="//hz.fang.lianjia.com/loupan/" target="_blank">新房</a></li>
                        <li class="header__item fl cur"><a href="/zufang/" target="_blank">租房</a></li>
                        <li class="header__item fl "><a href="//us.lianjia.com" target="_blank">海外</a></li>
                        <li class="header__item fl "><a href="//hz.lianjia.com/xiaoqu/" target="_blank">小区</a></li>
                        <li class="header__item fl "><a href="//hz.lianjia.com/jingjiren/" target="_blank">经纪人</a></li>
                        <li class="header__item fl "><a href="//hz.lianjia.com/wenda/" target="_blank">指南</a></li>
                        <li class="header__item fl "><a href="//hz.lianjia.com/fangjia/" target="_blank">房价</a></li>
                        <li class="header__item fl "><a href="//hz.lianjia.com/tool.html" target="_blank">工具</a></li>
                        <li class="header__item fl "><a href="//hz.lianjia.com/yezhu/" target="_blank">发布房源</a></li>
                  <li class="header__aside fr pointer typeShowUser" data-el="login" data-event_id="10794" data-event_action="target=login">
      <span data-el="login_box">
        <span data-el="btn_login" data-id="dialog_tel" class="btn-login">登录</span>/<span class="btn-resgiter" data-el="register" data-id="dialog_reg">注册</span>
      </span>
    </li>
    <li class="top__aside fr hide" data-el="user_box">
      <a href="" data-el="userName"></a>
      <a data-el="logout_btn">退出</a>
    </li>

  </ul>

</div>
  <div class="search__area">
  <div class="beike__nav">
  <a class="beike__nav--logo" href="/zufang/"></a>
  
  <ul class="beike__nav--tab">
    <li>
      <a class="cur" href="/zufang/">首页</a>
    </li>

    <li>      
      <a class="" href="/zufang/rt200600000001/">整租</a>
    </li>

    <li><a class="" href="/zufang/rt200600000002/">合租</a></li>
            <li class="beike__nav--code">
      下载APP
      <div class="nav-list beike__nav--qrcode">
        <img src="https://ajax.api.lianjia.com/qr/getDownloadQr?location=nav&amp;ljweb_channel_key=zufang_search" alt="下载贝壳APP" class="QRcode-img">
      </div> 
    </li>
    
  </ul>
</div>  <div class="search w1150" id="search">
  <!-- <a class="search__logo" href="/"></a> -->
  <div class="search__wrap">
    <input class="search__input fl" type="text" data-el="input" placeholder="请输入区域、商圈或小区名开始找房" autocomplete="off" value="" data-value="">
    <span class="search__button fl" data-el="button"></span>
  </div>

</div>  </div>

  <!-- 房源有效时 -->
      <div class="content clear w1150">

      <!-- 房源标题 -->
      <p class="content__title">天阳美林湾 2室1厅 4300元</p>

      <!-- 房源副标题 -->
      <div class="content__subtitle">
          <i class="hide">4人浏览 </i>房源上架时间 2019-03-11          <i class="house_code">房源编号：HZ2207861188309041152</i>
          <!-- 发布人、发布机构入口 -->
                      <ul>
                                     </ul>
                    <span class="content-right" data-el="showReportBox" data-event_id="10804" data-event_action="house_code=HZ2207861188309041152">举报</span>
      </div>

      <!-- 房源左侧内容 -->
      <div class="content__article fl">

        <!-- 房源图片轮播图 -->
        <div class="content__article__slide" id="mySwipe">

          <!-- 房源大图 -->
          <ul class="content__article__slide__wrapper">
                                  <div class="content__article__slide__item" data-el="slideItem">
                              <img alt="天阳美林湾 2室1厅 4300元" src="https://image1.ljcdn.com/330100-inspection/prod-5e6dd45d-c477-4bed-8d43-4d34b0e8d0ad.jpg.780x439.jpg" data-el="lazy-img" data-src="https://image1.ljcdn.com/330100-inspection/prod-5e6dd45d-c477-4bed-8d43-4d34b0e8d0ad.jpg.780x439.jpg" />
                          </div>
                        <div class="content__article__slide__item" data-el="slideItem">
                              <img alt="天阳美林湾 2室1厅 4300元" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/780-439.png?_v=201903142105200c0" data-el="lazy-img" data-src="https://image1.ljcdn.com/330100-inspection/prod-e286f6c6-c9b3-4549-bd9a-1fe30ae3ec38.jpg.780x439.jpg" />
                          </div>
                        <div class="content__article__slide__item" data-el="slideItem">
                              <img alt="天阳美林湾 2室1厅 4300元" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/780-439.png?_v=201903142105200c0" data-el="lazy-img" data-src="https://image1.ljcdn.com/hdic-frame/prod-ba775bd2-81ce-4bf9-9f24-7e170f20b33d.png.780x439.jpg" />
                          </div>
                        <div class="content__article__slide__item" data-el="slideItem">
                              <img alt="天阳美林湾 2室1厅 4300元" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/780-439.png?_v=201903142105200c0" data-el="lazy-img" data-src="https://image1.ljcdn.com/330100-inspection/prod-499a92c6-d432-4dda-8a06-8ac15fd3e4f6.jpg.780x439.jpg" />
                          </div>
                        <div class="content__article__slide__item" data-el="slideItem">
                              <img alt="天阳美林湾 2室1厅 4300元" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/780-439.png?_v=201903142105200c0" data-el="lazy-img" data-src="https://image1.ljcdn.com/330100-inspection/prod-ad296506-f9c9-404d-9cfb-4811a4245b08.jpg.780x439.jpg" />
                          </div>
                        <div class="content__article__slide__item" data-el="slideItem">
                              <img alt="天阳美林湾 2室1厅 4300元" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/780-439.png?_v=201903142105200c0" data-el="lazy-img" data-src="https://image1.ljcdn.com/330100-inspection/prod-02e43dec-f483-4858-b0f1-a6e2cd9dd753.jpg.780x439.jpg" />
                          </div>
                        <div class="content__article__slide__item" data-el="slideItem">
                              <img alt="天阳美林湾 2室1厅 4300元" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/780-439.png?_v=201903142105200c0" data-el="lazy-img" data-src="https://image1.ljcdn.com/330100-inspection/prod-537db92a-29f9-4f6e-8129-1985238a2694.jpg.780x439.jpg" />
                          </div>
                                </ul>

          <!-- 房源缩略图 -->
          <div class="content__thumb--box">
            <ul class="content__article__slide--small content__article__slide_dot" data-el="prefix" id="prefix">
                                                <li class="active" data-index="0">
                    <img src="https://image1.ljcdn.com/330100-inspection/prod-5e6dd45d-c477-4bed-8d43-4d34b0e8d0ad.jpg.126x86.jpg">
                  </li>
                                  <li class="" data-index="1">
                    <img src="https://image1.ljcdn.com/330100-inspection/prod-e286f6c6-c9b3-4549-bd9a-1fe30ae3ec38.jpg.126x86.jpg">
                  </li>
                                  <li class="" data-index="2">
                    <img src="https://image1.ljcdn.com/hdic-frame/prod-ba775bd2-81ce-4bf9-9f24-7e170f20b33d.png.126x86.jpg">
                  </li>
                                  <li class="" data-index="3">
                    <img src="https://image1.ljcdn.com/330100-inspection/prod-499a92c6-d432-4dda-8a06-8ac15fd3e4f6.jpg.126x86.jpg">
                  </li>
                                  <li class="" data-index="4">
                    <img src="https://image1.ljcdn.com/330100-inspection/prod-ad296506-f9c9-404d-9cfb-4811a4245b08.jpg.126x86.jpg">
                  </li>
                                  <li class="" data-index="5">
                    <img src="https://image1.ljcdn.com/330100-inspection/prod-02e43dec-f483-4858-b0f1-a6e2cd9dd753.jpg.126x86.jpg">
                  </li>
                                  <li class="" data-index="6">
                    <img src="https://image1.ljcdn.com/330100-inspection/prod-537db92a-29f9-4f6e-8129-1985238a2694.jpg.126x86.jpg">
                  </li>
                                          </ul>
          </div>

          <!-- 图片切换按钮 -->
          <span class="content__article__slide--prev" data-el="prev"></span>
          <span class="content__article__slide--next" data-el="next"></span>

          <!-- 房源关注入口及hover浮层 -->
          <span class="content__article__slide--tips hide" data-el="getApp">关注的房源请在链家APP中查看</span>
          <span class="content__article__slide--button" data-type="house" data-id="HZ2207861188309041152" data-el="checkWatch"><i class="heart"></i><span>关注房源</span></span>
        </div>

        <!-- 房源基本信息 -->
        <div class="content__article__info">
          <h3 id="info">房屋信息</h3>
          <ul>
            <li class="fl oneline">基本信息</li>
                          <li class="fl oneline">发布：7天前</li>
                                        <li class="fl oneline">入住：随时入住</li>
                              <li class="fl oneline">&nbsp;</li>
                                        <li class="fl oneline">租期：暂无数据</li>
                                        <li class="fl oneline">看房：需提前预约</li>
                              <li class="fl oneline">&nbsp;</li>
                                        <li class="fl oneline">楼层：高楼层/16层</li>
                                        <li class="fl oneline">电梯：有</li>
                              <li class="fl oneline">&nbsp;</li>
                                        <li class="fl oneline">车位：暂无数据</li>
                                        <li class="fl oneline">用水：民水</li>
                              <li class="fl oneline">&nbsp;</li>
                                        <li class="fl oneline">用电：民电</li>
                                        <li class="fl oneline">燃气：有</li>
                              <li class="fl oneline">&nbsp;</li>
                                        <li class="fl oneline">采暖：自采暖</li>
                                    </ul>
        </div>

        <!-- 房源分割标识线，js里用到，勿删 -->
        <div class="info__line line"></div>

        <!-- 配套设施列表 -->
        <ul class="content__article__info2">
          <li class="fl oneline">配套设施</li>
                      <li class="fl oneline television_no "><i style="background-image: url(https://image1.ljcdn.com/rent-front-image/8705ff7fb13cf9fabdc2aed4ca0052c0.1524906061250_49197f72-e296-4eb7-b9c0-78e443675cfa);"></i>电视</li>
                      <li class="fl oneline refrigerator_no "><i style="background-image: url(https://image1.ljcdn.com/rent-front-image/97908a9f37935c43d110762d1ad996f2.1524905937598_92b7500a-1c6c-4569-91b2-9c32cb27c295);"></i>冰箱</li>
                      <li class="fl oneline washing_machine_no "><i style="background-image: url(https://image1.ljcdn.com/rent-front-image/ff28f17d82337aaa2cbdcd44ad1bda4c.1524906571057_0c1a2541-7e92-4557-92d0-7588846918d1);"></i>洗衣机</li>
                      <li class="fl oneline air_conditioner_no "><i style="background-image: url(https://image1.ljcdn.com/rent-front-image/01018daa3c64d5249dc6b5f90b14ecb7.1524906116550_8f0a3e47-0dd1-4888-9f67-31ff52842545);"></i>空调</li>
                      <li class="fl oneline water_heater_no "><i style="background-image: url(https://image1.ljcdn.com/rent-front-image/730ed905f7575d8752520fa858428b06.1524906267640_ef46af19-b1b0-4fe1-8a2d-5d663c000442);"></i>热水器</li>
                      <li class="fl oneline bed_no "><i style="background-image: url(https://image1.ljcdn.com/rent-front-image/ca13bd1b4ecd7104f7df71e40643291a.1524905997899_d5dd7ec6-b9ca-442e-9d3b-c9c85a841076);"></i>床</li>
                      <li class="fl oneline heating_no "><i style="background-image: url(https://image1.ljcdn.com/rent-front-image/ce93a6cec4a601367fbd8f5d8760ecc8.1525926673137_fa39878e-9033-4494-9912-13c176c060ca);"></i>暖气</li>
                      <li class="fl oneline wifi_no "><i style="background-image: url(https://image1.ljcdn.com/rent-front-image/c2e2d43d75f2158cf08fae1c4d2f433f.1524906202377_004ba35e-ce03-480f-bb0c-0acd46ebb1ce);"></i>宽带</li>
                      <li class="fl oneline wardrobe_no "><i style="background-image: url(https://image1.ljcdn.com/rent-front-image/da33d5ca764547cc5ed574d10868f2e5.1524906607735_85ecfcc4-6a05-454d-84a5-63e92bec1e83);"></i>衣柜</li>
                      <li class="fl oneline natural_gas_no "><i style="background-image: url(https://image1.ljcdn.com/rent-front-image/f0e67d57b15b3c47c4ee77847eef5b97.1524906489358_60a401ee-ee85-42eb-aaf3-5caaa5efc0a6);"></i>天然气</li>
                  </ul>

        <!-- 房源描述数据 -->
                
        <!-- 描述展示 -->
        
      </div>

      <!-- 右侧黄金展位 -->
      <div class="content__aside fr" id="aside">

        <!-- 租金及支付方式 -->
        <p class="content__aside--title"><span>4300</span>元/月 </p>
        
        <!-- 房源标签列表 -->
        <p class="content__aside--tags">
                  <i class="content__item__tag--is_subway_house" data-class="is_subway_house">近地铁</i>
                </p>

        <!-- 房源户型、朝向、面积、租赁方式 -->
        <ul class="content__aside__list">
          <p class="content__article__table">
            <span><i class="house"></i>租赁方式未知</span>
            <span><i class="typ"></i>2室1厅1卫</span>
            <span><i class="area"></i>86㎡</span>
            <span><i class="orient"></i>朝南</span>
          </p>
        </ul>
        <!-- 经纪人信息，目前只展示一条信息 -->
                <ul class="content__aside__list">
                    <!-- 判断数据源 是否展示icon等信息-->
                                                        <li>
                  <!--im参数配置2. port 参数中判断 “lianjia / qita” 时，判断条件：1）若UCID为100开头，则传值 “lianjia” 2) 若UCID不为100开头，则传值 “qita”-->
                                    <span data-el="updateAvatar" data-houseCode="HZ2207861188309041152" class="content__aside__list--icon"></span>
                  <div class="content__aside__list--title oneline">

                    <span class="contact_name" data-el="updateName" data-houseCode="HZ2207861188309041152" title="何方颖"></span>
                  
                    <!-- 判断信息卡的房源，是否显示icon-->
                    <div class="duty-pic" data-el="updatePic" data-show_booth="1">
                      <!-- 显示icon-->
                      <span class="duty-icon" data-el="dutyCard"></span>
                      <!-- hover时显示经纪人卡片-->
                      <div class="duty-pop" data-el="picList">
                      </div>
                    </div>

                                          <span class="contact__im" data-el="callIM" data-im_id="1000000026044211" data-info="1000000026044211" data-port="pc_lianjia_zufangplat_detail_house" data-brand="200301001000" data-id="HZ2207861188309041152" data-type="house" data-title="[房源]2室1厅1卫，南，86m²，4300元"></span>
                                      </div>
                  <p class="content__aside__list--subtitle oneline">

                                                            链家                                        经纪人                                    
                  </p> 
                  <p class="content__aside__list--bottom oneline" data-el="updatePhone" data-houseCode="HZ2207861188309041152">10109666</p>
                </li>
                                            </ul>
              </div>
    </div>


    <!-- 地图及推荐房源 -->
    <div class="content--flat w1150" id="mapDetail">

      <!-- 推荐经纪人 -->
            <div class="content__article__info3 brokerList" id="desc">
        <div class="content">
          <div class="agent-header">
            <span class="title">联系经纪人</span>
            <span class="subTitle">您可以通过拨打电话或在线咨询的方式联系经纪人</span>

                      </div>
          <ul id="agentList">
            
              <li style="">
                <a href="https://dianpu.lianjia.com/1000000026044211"><img class="agent-icon" src="https://image1.ljcdn.com/usercenter/images/uc_ehr_avatar/480ac454-83b6-40f9-8dea-f016b6cef673.jpg.120x160.png" alt="" data-event_id="20001" data-bl="agent" data-el="1000000026044211"></a>
                <div class="desc">
                  <div class="title" style="position: relative;">
                    <a href="https://dianpu.lianjia.com/1000000026044211" class="name">何方颖</a>

                    <!-- 判断信息卡的房源，是否显示icon-->
                    
                    <!--im参数配置2. port 参数中判断 “lianjia / qita” 时，判断条件：1）若UCID为100开头，则传值 “lianjia” 2) 若UCID不为100开头，则传值 “qita”-->
                      
                      <a class="agent__im" data-el="callIM"  data-im_id="1000000026044211"  data-info="1000000026044211" data-port="pc_lianjia_zufangplat_detail_house" data-id="HZ2207861188309041152" data-type="house" data-title="[房源]2室1厅1卫，南，86m²，4300元">
                      </a>
                                        <div class="rate">
                      <span class="level">助理经纪人</span>
                      评分:0.0 | 0人评价                    </div>
                  </div>
                  <div class="phone">4008769126转72136</div>
                </div>
              </li>
            
              <li style="">
                <a href="https://dianpu.lianjia.com/1000000026034858"><img class="agent-icon" src="https://image1.ljcdn.com/usercenter/images/uc_ehr_avatar/2e259032-ad42-4a8f-84a8-85f72ea4cf4a.jpg.120x160.png" alt="" data-event_id="20001" data-bl="agent" data-el="1000000026034858"></a>
                <div class="desc">
                  <div class="title" style="position: relative;">
                    <a href="https://dianpu.lianjia.com/1000000026034858" class="name">梁祖林</a>

                    <!-- 判断信息卡的房源，是否显示icon-->
                    
                    <!--im参数配置2. port 参数中判断 “lianjia / qita” 时，判断条件：1）若UCID为100开头，则传值 “lianjia” 2) 若UCID不为100开头，则传值 “qita”-->
                      
                      <a class="agent__im" data-el="callIM"  data-im_id="1000000026034858"  data-info="1000000026034858" data-port="pc_lianjia_zufangplat_detail_house" data-id="HZ2207861188309041152" data-type="house" data-title="[房源]2室1厅1卫，南，86m²，4300元">
                      </a>
                                        <div class="rate">
                      <span class="level">经纪人</span>
                      评分:0.0 | 0人评价                    </div>
                  </div>
                  <div class="phone">4008769126转72140</div>
                </div>
              </li>
            
              <li style="">
                <a href="https://dianpu.lianjia.com/1000000026048136"><img class="agent-icon" src="https://image1.ljcdn.com/.120x160.png" alt="" data-event_id="20001" data-bl="agent" data-el="1000000026048136"></a>
                <div class="desc">
                  <div class="title" style="position: relative;">
                    <a href="https://dianpu.lianjia.com/1000000026048136" class="name">章余舸</a>

                    <!-- 判断信息卡的房源，是否显示icon-->
                    
                    <!--im参数配置2. port 参数中判断 “lianjia / qita” 时，判断条件：1）若UCID为100开头，则传值 “lianjia” 2) 若UCID不为100开头，则传值 “qita”-->
                      
                      <a class="agent__im" data-el="callIM"  data-im_id="1000000026048136"  data-info="1000000026048136" data-port="pc_lianjia_zufangplat_detail_house" data-id="HZ2207861188309041152" data-type="house" data-title="[房源]2室1厅1卫，南，86m²，4300元">
                      </a>
                                        <div class="rate">
                      <span class="level">助理经纪人</span>
                      评分:0.0 | 0人评价                    </div>
                  </div>
                  <div class="phone">4008769126转72144</div>
                </div>
              </li>
                        <li class="fix_align"></li>
            <li class="fix_align"></li>
            <li class="fix_align"></li>
          </ul>
        </div>
      </div>
            <!-- 地址信息 -->
      <div class="content__article__info4" id="around">
        <h3>地址和交通</h3>
        <ul>
                  <li>
            距离
            <span>地铁2号线 - 三墩</span>
            <span>529m</span>
          </li>
                </ul>
      </div>
      <!-- 地图插件显示 -->
      <div class="content__map">
        <div id="map" class="content__map--container">
        </div>
      </div>

      <!-- 小区成交列表，最多显示3条 -->
            <div class="content__table" id="deal">
        <h3>小区最新成交</h3>
        <div class="table">
          <div class="tr">
            <div class="th">成交日期</div>
            <div class="th">居室</div>
            <div class="th">面积</div>
            <div class="th">租赁方式</div>
            <div class="th">出租价格</div>
          </div>
                      <div class="tr">
              <div class="td">2019-02-18</div>
              <div class="td">2室2厅1卫</div>
              <div class="td">89㎡</div>
              <div class="td">整租</div>
              <div class="td">4200元/月</div>
            </div>
                      <div class="tr">
              <div class="td">2019-01-27</div>
              <div class="td">2室2厅1卫</div>
              <div class="td">92㎡</div>
              <div class="td">整租</div>
              <div class="td">4200元/月</div>
            </div>
                      <div class="tr">
              <div class="td">2018-12-17</div>
              <div class="td">2室2厅1卫</div>
              <div class="td">89㎡</div>
              <div class="td">整租</div>
              <div class="td">4200元/月</div>
            </div>
                  </div>
      </div>
      
      <!-- 推荐房源分割线 -->
      <p style="height: 1px;" id="recom"></p>
      
      <!-- 同小区在租房源 -->
              <div class="bottom w1150" style="">
  <div class="bottom__list">

    
        <p class="bottom__list--title">同小区在租房源</p>
    
    <div class="bottom__list--wrapper">
          <div class="bottom__list--item">
        <a href="/zufang/HZ2209171923811188736.html" target="_blank" data-event_id="10805" data-event_action="house_code=HZ2209171923811188736&position=1"><img alt="/zufang/HZ2209171923811188736.html" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/363-274.png?_v=201903142105200c0" data-el="lazy-img" class="lazyload" data-src="https://image1.ljcdn.com/330100-inspection/071b93dc-864d-43ce-81bb-87315d7d1376.jpg.250x182.jpg"></a>
        <p class="bottom__list--item__des">
          <span>
            <a href="/zufang/gongshu" target="_blank">拱墅</a> 
            - 
            <a href="/zufang/shenhua" target="_blank">申花</a>  
            天阳美林湾          </span>
          <span class="bottom__list--item--hl fr">4000元/月</span> 
        </p>
        <p class="bottom__list--item__btm">
          2室1厅1卫 85㎡
        </p>
      </div>
          <div class="bottom__list--item">
        <a href="/zufang/HZ2085350896316981248.html" target="_blank" data-event_id="10805" data-event_action="house_code=HZ2085350896316981248&position=2"><img alt="/zufang/HZ2085350896316981248.html" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/363-274.png?_v=201903142105200c0" data-el="lazy-img" class="lazyload" data-src="https://image1.ljcdn.com/rent-house-1/ad40efae68e06d5607579210fcfcecd2-1551494984760/1afcec5523ebfdcdda723172e648d440.jpg.250x182.jpg"></a>
        <p class="bottom__list--item__des">
          <span>
            <a href="/zufang/gongshu" target="_blank">拱墅</a> 
            - 
            <a href="/zufang/shenhua" target="_blank">申花</a>  
            天阳美林湾          </span>
          <span class="bottom__list--item--hl fr">2330元/月</span> 
        </p>
        <p class="bottom__list--item__btm">
          3室1厅1卫 14㎡
        </p>
      </div>
          <div class="bottom__list--item">
        <a href="/zufang/HZ2118596623826157568.html" target="_blank" data-event_id="10805" data-event_action="house_code=HZ2118596623826157568&position=3"><img alt="/zufang/HZ2118596623826157568.html" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/363-274.png?_v=201903142105200c0" data-el="lazy-img" class="lazyload" data-src="https://image1.ljcdn.com/rent-house-1/ad40efae68e06d5607579210fcfcecd2-1551841625902/5017038e1610e1f01ec225d7fa59c81d.jpg.250x182.jpg"></a>
        <p class="bottom__list--item__des">
          <span>
            <a href="/zufang/gongshu" target="_blank">拱墅</a> 
            - 
            <a href="/zufang/shenhua" target="_blank">申花</a>  
            天阳美林湾          </span>
          <span class="bottom__list--item--hl fr">1690元/月</span> 
        </p>
        <p class="bottom__list--item__btm">
          3室1厅1卫 9㎡
        </p>
      </div>
        </div>
  </div>
</div>
      
      <!-- 商圈在租房源 -->
              <div class="bottom w1150" style="margin-top: -62px">
  <div class="bottom__list">

    
        <p class="bottom__list--title"><a href="/zufang/shenhua" target="_blank" title="申花在租房源">申花在租房源</a></p>
    
    <div class="bottom__list--wrapper">
          <div class="bottom__list--item">
        <a href="/zufang/HZ2203639013745893376.html" target="_blank" data-event_id="10806" data-event_action="house_code=HZ2203639013745893376&position=1"><img alt="/zufang/HZ2203639013745893376.html" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/363-274.png?_v=201903142105200c0" data-el="lazy-img" class="lazyload" data-src="https://image1.ljcdn.com/rent-house-1/ad40efae68e06d5607579210fcfcecd2-1552700446315/dd3d609c112437bc5c826404e795be60.jpg.250x182.jpg"></a>
        <p class="bottom__list--item__des">
          <span>
            <a href="/zufang/gongshu" target="_blank">拱墅</a> 
            - 
            <a href="/zufang/shenhua" target="_blank">申花</a>  
            景瑞申花壹号院          </span>
          <span class="bottom__list--item--hl fr">2760元/月</span> 
        </p>
        <p class="bottom__list--item__btm">
          4室1厅2卫 15㎡
        </p>
      </div>
          <div class="bottom__list--item">
        <a href="/zufang/HZ2164267057024614400.html" target="_blank" data-event_id="10806" data-event_action="house_code=HZ2164267057024614400&position=2"><img alt="/zufang/HZ2164267057024614400.html" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/363-274.png?_v=201903142105200c0" data-el="lazy-img" class="lazyload" data-src="https://image1.ljcdn.com/330100-inspection/6386a7b8-5492-491e-9353-231415f804ac.jpg.250x182.jpg"></a>
        <p class="bottom__list--item__des">
          <span>
            <a href="/zufang/xihu" target="_blank">西湖</a> 
            - 
            <a href="/zufang/shenhua" target="_blank">申花</a>  
            耀江文鼎苑          </span>
          <span class="bottom__list--item--hl fr">5300元/月</span> 
        </p>
        <p class="bottom__list--item__btm">
          2室1厅1卫 89㎡
        </p>
      </div>
          <div class="bottom__list--item">
        <a href="/zufang/HZ2204373778581438464.html" target="_blank" data-event_id="10806" data-event_action="house_code=HZ2204373778581438464&position=3"><img alt="/zufang/HZ2204373778581438464.html" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/363-274.png?_v=201903142105200c0" data-el="lazy-img" class="lazyload" data-src="https://image1.ljcdn.com/rent-house-1/ad40efae68e06d5607579210fcfcecd2-1551616802934/4a0e2d8f4c7264b671ab2e8f16f01d32.jpg.250x182.jpg"></a>
        <p class="bottom__list--item__des">
          <span>
            <a href="/zufang/xihu" target="_blank">西湖</a> 
            - 
            <a href="/zufang/shenhua" target="_blank">申花</a>  
            耀江文鼎苑          </span>
          <span class="bottom__list--item--hl fr">2530元/月</span> 
        </p>
        <p class="bottom__list--item__btm">
          3室1厅1卫 13㎡
        </p>
      </div>
        </div>
  </div>
</div>
          </div>

    <!-- 跟动快捷导航 -->
    <div class="fixednav hide" id="fixed">
      <ul class="w1150">
        <li data-el="fixedNavItem" data-href="info">房源信息</li>
                <li data-el="fixedNavItem" data-href="around">交通周边</li>
                <li data-el="fixedNavItem" data-href="deal">小区成交</li>
                <li data-el="fixedNavItem" data-href="recom">推荐房源</li>
      </ul>
    </div>

    <!-- 全部经纪人信息，目前已被隐藏 -->
    <div class="global__list hide" id="globalList">
      <div class="global__list--bg" data-el="shadow"></div>
      <div class="global__list__container">
        <span class="global__list--close" data-el="close"></span>
        <ul>
                    <li>
            <span class="global__list--icon icon--200301001000"></span>
            <p class="global__list--title"><i data-el="updateName" data-houseCode="HZ2207861188309041152"></i>（链家）<span class="fr" data-el="updatePhone" data-houseCode="HZ2207861188309041152">&nbsp;</span></p>
            <p class="global__list--subtitle oneline"><span>4300</span>/月  </p>
          </li>
                  </ul>
      </div>
    </div>

  <!-- 房源失效时兜底处理 -->
  
  <!-- 底部面包屑链接 -->
  <div class="bread__nav w1150" style="">
  <p class="bread__nav__wrapper oneline">
                  <a href="/zufang/">杭州租房网</a>&nbsp;&gt;&nbsp;
                        <a href="/zufang/gongshu/">拱墅租房</a>&nbsp;&gt;&nbsp;
                        <a href="/zufang/shenhua/">申花租房</a>&nbsp;&gt;&nbsp;
                      <h1>
        <a href="/zufang/c2711051234857/">天阳美林湾租房</a>
      </h1>
            </p>
</div>
</div>

<input type="hidden" data-el="showBooth" value="1">
<!--登录-->
<div class="loninContaner">
    <!--mask-->
    <div class="overlay_bg" style="display: none;"></div>
    <!--账号密码登录-->
    <div id="dialog" class="panel_login animated">
        <div class="panel_info"><i class="close_login">×</i>
            <div class="panel_tab">
                <div class="title">
                    <div class="fl">账号密码登录</div>
                </div>
                <div class="clear"></div>
                <div id="con_login_user">
                    <form action="" method="post">
                        <ul>
                            <li class="item border-t userName">
                                <input type="text" class="the_input topSpecial users" placeholder="请输入手机号" maxlength="11">
                            </li>
                            <li class="item border-b pwd">
                                <input type="password" class="the_input password" maxlength="20" placeholder="请输入登录密码"><em class="password-view"></em>
                            </li>
                            <li class="item checkVerimg" style="display:none;">
                                <input type="text" class="the_input ver-img" maxlength="6" placeholder="请输入验证码">
                                <img class="verImg">
                            </li>
                            <li class="item drag" style="display:none;">
                                <div id="drag"></div>
                            </li>
                            <li class="show-error">
                                <dd>用户名或密码错误</dd>
                            </li>
                            <li class="li_01">
                                <label class="checkbox-btn"><span class="active"><input type="checkbox" name="remember" value="1" class="mind-login" checked=""></span>7天内免登录</label><a href="javascript:;" rel="nofollow" class="toforget">忘记密码</a>
                            </li>
                            <li class="li_btn"><a class="login-user-btn">登录</a>
                            </li>
                            <li class="footer-link"><a href="javascript:;" rel="nofollow" class="totellogin">手机快捷登录</a>
                            </li>
                        </ul>
                    </form>
                </div>
                <div id="con_login_agent" class="undis">
                    <form action="" method="post">
                        <ul>
                            <li class="item">
                                <dd></dd>
                                <input type="text" class="the_input users" placeholder="输入经纪人ID号码">
                            </li>
                            <li class="item">
                                <input type="password" class="the_input password" placeholder="登录密码">
                            </li>
                            <li class="li_01">
                                <label class="checkbox-btn"><span class="active"><input type="checkbox" name="remember" value="1" class="mind-login" checked=""></span>7天内免登录</label><a href="https://passport.lianjDia.com/register/resources/lianjia/forget.html?service=http://bj.lianjia.com/" rel="nofollow">忘记密码</a>
                            </li>
                            <li>
                                <input class="login-agent-btn" value="立即登录">
                            </li>
                        </ul>
                    </form>
                </div>
            </div>
        </div>
        <div class="registered"></div>
    </div>
    <!--手机快捷登录-->
    <div id="dialog_tel" class="panel_login animated btn-login bounceIn actLoginBtn" style="display: none;">
        <div class="panel_info"><i class="close_login">×</i>
            <div class="panel_tab">
                <div class="title">
                    <div class="fl">手机快捷登录</div>
                    <div class="register_text_tel">别担心，无账号自动注册不会导致手机号被泄露</div>
                </div>
                <div class="clear"></div>
                <div id="con_login_user_tel">
                    <form action="" method="post">
                        <ul>
                            <li class="item border-t userName">
                                <input type="text" class="the_input topSpecial users_tel" maxlength="11" placeholder="请输入手机号">
                            </li>
                            <!-- <li class="item pwd"><input type="password" class="the_input password_tel"  placeholder="请输入短信验证码"/></li> -->
                            <li class="item checkVerimg" style="">
                                <input type="text" class="the_input ver-img" maxlength="6" placeholder="请输入验证码">
                                <img class="verImg" src="https://upassport.lianjia.com/freshCaptch?t=1517466208641">
                            </li>
                            <li class="item border-b Verify">
                                <input type="text" class="the_input verifycode" maxlength="6" placeholder="请输入短信验证码"><a class="send_verify_code" id="send_verify_code_tel" href="javascript:;" rel="nofollow"><em>获取验证码</em></a>
                            </li>
                            <li class="send_verify_code_s" id="send_verify_code_tel_s" href="javascript:;" rel="nofollow"><em>没有收到验证码？</em><a class="voice_a">发送语音验证码</a>
                            </li>
                            <li class="show-error">
                                <dd>用户名或密码错误</dd>
                            </li>
                            <li class="li_01">
                                <label class="checkbox-btn"><span class="active"><input type="checkbox" name="remember" value="1" class="mind-login" checked=""></span>7天内免登录</label>
                            </li>
                            <li class="li_btn"><a class="login-user-tel-btn">登录</a>
                            </li>
                            <li class="footer-link"><a href="javascript:;" rel="nofollow" class="tologin">账号密码登录</a>
                            </li>
                        </ul>
                    </form>
                </div>
            </div>
        </div>
        <div class="registered"></div>
    </div>
    <!--手机号码注册-->
    <div id="dialog_reg" class="panel_login animated">
        <div class="panel_info"><i class="close_login">×</i>
            <div class="panel_tab">
                <div class="title">
                    <div class="fl">手机号码注册</div>
                    <label class="fr register_text">已有账号？<a href="javascript:;" rel="nofollow" class="tologin">去登录</a>
                    </label>
                </div>
                <div class="clear"></div>
                <div id="con_login_user_reg">
                    <form action="" method="post">
                        <ul>
                            <li class="item border-t userName">
                                <input type="text" class="the_input topSpecial users_reg" maxlength="11" placeholder="请输入手机号">
                            </li>
                            <li class="item checkVerimg" style="">
                                <input type="text" class="the_input ver-img" maxlength="6" placeholder="请输入验证码">
                                <img class="verImg">
                            </li>
                            <li class="item border-c Verify">
                                <input type="text" class="the_input verifycode" maxlength="6" placeholder="请输入短信验证码"><a class="send_verify_code" id="send_verify_code_reg" href="javascript:;" rel="nofollow"><em>获取验证码</em></a>
                            </li>
                            <li class="item border-b pwd">
                                <input type="password" class="the_input password_reg" maxlength="20" placeholder="请输入密码（最少8位，数字+字母）"><em class="password-view"></em>
                            </li>
                            <li class="send_verify_code_s" id="send_verify_code_reg_s" href="javascript:;" rel="nofollow"><em>没有收到验证码？</em><a class="voice_a">发送语音验证码</a>
                            </li>
                            <li class="show-error">
                                <dd>用户名或密码错误</dd>
                            </li>
                            <li class="li_01">
                                <label class="checkbox-btn"><span class="active"><input type="checkbox" name="read" value="1" class="read-protocol" checked=""></span>我已阅读并同意</label>
                                <a class="toprotocol" href="//www.ke.com/zhuanti/protocol" target="_blank">《贝壳用户使用协议》</a>
                                及
                                <a class="toprotocol" href="//www.ke.com/zhuanti/serviceProtocol" target="_blank">《贝壳用户服务协议》</a>
                            </li>
                            <li class="li_btn"><a class="register-user-btn">注册</a>
                            </li>
                        </ul>
                    </form>
                </div>
            </div>
        </div>
        <div class="registered"></div>
    </div>
    <!--找回密码-->
    <div id="dialog_forget" class="panel_login animated">
        <div class="panel_info"><i class="close_login">×</i>
            <div class="panel_tab">
                <div class="title">
                    <div class="fl">找回密码</div>
                </div>
                <div class="clear"></div>
                <div id="con_forget_user_tel" class="con_forget_user_tel">
                    <form action="" method="post">
                        <ul>
                            <li class="item border-t userName">
                                <input type="text" class="the_input topSpecial user_forget_phone" placeholder="请输入手机号" maxlength="11">
                            </li>
                            <li class="item checkVerimg" style="">
                                <input type="text" class="the_input ver-img" maxlength="6" placeholder="请输入验证码">
                                <img class="verImg">
                            </li>
                            <li class="item border-b Verify">
                                <input type="text" class="the_input verifycode" maxlength="6" placeholder="请输入短信验证码"><a class="send_verify_code" id="send_verify_code_forget" href="javascript:;" rel="nofollow"><em>获取验证码</em></a>
                            </li>
                            <li class="item border-t pwd" style="margin-top:-1px;">
                                <input type="password" class="the_input password_reg" maxlength="20" placeholder="请输入密码（最少8位，数字+字母）"><em class="password-view"></em>
                            </li>
                            <li class="send_verify_code_s" id="send_verify_code_forget_s"><em>没有收到验证码？</em><a class="voice_a">发送语音验证码</a>
                            </li>
                            <li class="show-error">
                                <dd>用户名或密码错误</dd>
                            </li>
                            <li class="li_btn"><a class="user-forget">修改密码</a>
                            </li>
                        </ul>
                    </form>
                </div>
                <div id="con_forget_user_pw" class="con_forget_user_pw">
                    <form action="" method="post">
                        <ul>
                            <li class="item border-t pwd">
                                <input type="password" class="the_input password_reg" maxlength="20" placeholder="请输入密码（最少8位，数字+字母）"><em class="password-view"></em>
                            </li>
                            <li class="show-error">
                                <dd>用户名或密码错误</dd>
                            </li>
                            <li class="li_btn"><a class="modify-user-pswd">修改密码</a>
                            </li>
                        </ul>
                    </form>
                </div>
            </div>
        </div>
        <div class="registered"></div>
    </div>
</div>
<script>
  g_conf.coord = {
    longitude: '120.10495848615',
    latitude: '30.327970851608'
  };
  g_conf.subway = [{"distance":529,"lines":["\u5730\u94c12\u53f7\u7ebf"],"name":"\u4e09\u58a9","point_lat":30.32535,"point_lng":120.099514}];
  g_conf.name = '天阳美林湾';
  g_conf.houseCode = 'HZ2207861188309041152';
  g_conf.offline = '';

  g_conf.pageId = 'rentalDetail';
  var __requireList = ['page/detail/index'];
</script>
</div>

<div class="fix-right-v3" id="back-top" log-mod="sidebar">
  <table>
    <tbody>
      <tr>
        <td>
          <ul>
            <li class="myfav sidebar-item">
              <a title="我关注的房源" data-url="//user.lianjia.com/site/favorHouse/" data-bl="myfav">我关注的房源</a>
              <span class="popup"><i></i>我关注的房源</span>
            </li>
            <li class="sell sidebar-item">
              <a title="在线卖房" href="//hz.lianjia.com/yezhu/" target="_blank" data-bl="sell">在线卖房</a>
              <span class="popup"><i></i>在线卖房</span>
            </li>
            <li class="baodan sidebar-item">
              <a href="//hz.lianjia.com/anxinchengnuo" title="安心保单" target="_blank" data-bl="baodan">安心保单</a>
              <span class="popup">
                <i></i>安心保单
              </span>
            </li>
            <li class="download sidebar-item">
              <a href="//www.lianjia.com/client/" title="" target="_blank" data-bl="client">下载掌上链家</a>
              <span class="popup popup-qr">
                <i></i><img src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/img/wxapp.jpg?_v=201903142105200c0" alt="下载掌上链家" width="94">
                <em class="qr-title">链家微信小程序</em>
              </span>
            </li>
            <li class="phone sidebar-item">
              <a title="官方客服">官方客服</a>
              <span class="popup"><i></i>官方客服</span>
            </li>

                        <li class="feedback sidebar-item">
              <a href="https://helper.lianjia.com/it/index2#/feedbackForC?channel=lj-pc&city=330100" title="反馈/投诉" data-bl="feedback"></a>
              <span class="popup"><i></i>反馈/投诉</span>
            </li>
          </ul>
        </td>
      </tr>
    </tbody>
  </table>
  <ul>
    <li class="gotop sidebar-item" id="gotop" style="display: none;"><a title="返回顶部">返回顶部</a><span class="popup"><i></i>返回顶部</span></li>
  </ul>
</div>
<div class="footer">
  <div class="footer__wrapper w1150">

    <div class="footer__top">
      <ul class="footer__light">
                <li><a href="/zufang/wzdt/">网站地图</a></li>
              </ul>
      <a class="footer__aside" href="tel:10109666">客服电话<span>10109666</span></a>
    </div>

    <div class="footer__middle">
      <ul data-el="parentList">
                  <li><a class="cur" data-index="0">租房城市</a></li>
                  <li><a class="" data-index="1">热门商圈</a></li>
                  <li><a class="" data-index="2">推荐小区</a></li>
                  <li><a class="" data-index="3">城市新房</a></li>
                  <li><a class="" data-index="4">城市二手房</a></li>
                  <li><a class="" data-index="5">友情链接</a></li>
              </ul>
              <ul data-el="childrenList"  style="display:block">
                      <li><a href="https://tj.lianjia.com/zufang/">天津租房</a></li>
                      <li><a href="https://lf.lianjia.com/zufang/">廊坊租房</a></li>
                      <li><a href="https://hk.lianjia.com/zufang/">海口租房</a></li>
                      <li><a href="https://zs.lianjia.com/zufang/">中山租房</a></li>
                      <li><a href="https://ms.lianjia.com/zufang/">眉山租房</a></li>
                      <li><a href="https://hf.lianjia.com/zufang/">合肥租房</a></li>
                      <li><a href="https://jx.lianjia.com/zufang/">嘉兴租房</a></li>
                      <li><a href="https://jn.lianjia.com/zufang/">济南租房</a></li>
                      <li><a href="https://xc.lianjia.com/zufang/">许昌租房</a></li>
                      <li><a href="https://nanchong.lianjia.com/zufang/">南充租房</a></li>
                      <li><a href="https://km.lianjia.com/zufang/">昆明租房</a></li>
                      <li><a href="https://linyi.lianjia.com/zufang/">临沂租房</a></li>
                      <li><a href="https://cc.lianjia.com/zufang/">长春租房</a></li>
                      <li><a href="https://ts.lianjia.com/zufang/">唐山租房</a></li>
                      <li><a href="https://dazhou.lianjia.com/zufang/">达州租房</a></li>
                      <li><a href="https://wuhu.lianjia.com/zufang/">芜湖租房</a></li>
                      <li><a href="https://fs.lianjia.com/zufang/">佛山租房</a></li>
                      <li><a href="https://gy.lianjia.com/zufang/">贵阳租房</a></li>
                      <li><a href="https://nn.lianjia.com/zufang/">南宁租房</a></li>
                      <li><a href="https://nj.lianjia.com/zufang/">南京租房</a></li>
                      <li><a href="https://cs.lianjia.com/zufang/">长沙租房</a></li>
                      <li><a href="https://baoji.lianjia.com/zufang/">宝鸡租房</a></li>
                      <li><a href="https://sy.lianjia.com/zufang/">沈阳租房</a></li>
                      <li><a href="https://zh.lianjia.com/zufang/">珠海租房</a></li>
                      <li><a href="https://yc.lianjia.com/zufang/">盐城租房</a></li>
                      <li><a href="https://bj.lianjia.com/zufang/">北京租房</a></li>
                      <li><a href="https://sjz.lianjia.com/zufang/">石家庄租房</a></li>
                      <li><a href="https://wh.lianjia.com/zufang/">武汉租房</a></li>
                      <li><a href="https://baoding.lianjia.com/zufang/">保定租房</a></li>
                      <li><a href="https://zjk.lianjia.com/zufang/">张家口租房</a></li>
                  </ul>
               <ul data-el="childrenList"  >
                      <li><a href="https://hz.lianjia.com/zufang/sandun/">三墩租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/qiaosi/">乔司租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/qianjiangxincheng/">钱江新城租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/qingtai/">清泰租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/wenjiao/">文教租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/nanxing/">南星租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/gouzhuang/">勾庄租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/cuiyuan/">翠苑租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/feicuicheng1/">翡翠城租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/zhonganqiao/">众安桥租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/nanxiaobu/">南肖埠租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/jianqiao/">笕桥租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/caihongcheng/">彩虹城租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/gulou2/">鼓楼租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/tangqi1/">塘栖租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/qianjiangshijicheng/">钱江世纪城租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/jinshahu/">金沙湖租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/liuxia1/">留下租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/chaoming11/">潮鸣租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/puyan/">浦沿租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/fuyang1/">富阳租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/changhe/">长河租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/gongyeyuanbei/">工业园北租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/hubin1/">湖滨租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/zhijiang/">之江租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/chunan/">淳安租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/gongchenqiao/">拱宸桥租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/dingqiao/">丁桥租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/renhe2/">仁和租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/shenhua/">申花租房</a></li>
                  </ul>
               <ul data-el="childrenList"  >
                      <li><a href="https://hz.lianjia.com/zufang/c1811043640872/">梅苑阁小区租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/c1811043640835/">赞成林风和风苑租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/c1811043640652/">瑞丰格林苑租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/c187623364588178/">恒生科技园租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/c1811043642428/">泰和苑租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/c1811043641078/">梦湖山庄租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/c187574840685010/">赞成赞城租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/c1811043636351/">清合嘉园东区租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/c1811043636476/">长板里租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/c1811043639447/">景芳二区租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/c1811043636704/">宗坛巷租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/c188123089433077/">越秀星汇城租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/c1811043636681/">远东新月公寓租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/c1811043639560/">绿城玉兰公寓租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/c1811043636470/">长新里租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/c187462070530717/">云水山居租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/c187596381319218/">天阳晴朗租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/c1811043636184/">九龙山庄租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/c1811043639582/">丁兰商业中心租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/c1811043638717/">万家花园欣和苑租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/c1811043640685/">东太平巷租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/c1811043635925/">中南公寓租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/c187511744459272/">中新御景湾租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/c1811043635936/">商城东苑租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/c1811043636349/">李家桥小区租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/c1811043640549/">山水佳苑租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/c1811043637477/">大关西四苑租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/c1811043641202/">紫竹苑租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/c1811043640943/">东方金座租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/c1811043635922/">兴耀大厦租房</a></li>
                  </ul>
               <ul data-el="childrenList"  >
                      <li><a href="https://zjk.fang.lianjia.com/">张家口楼盘</a></li>
                      <li><a href="https://wf.fang.lianjia.com/">潍坊楼盘</a></li>
                      <li><a href="https://yc.fang.lianjia.com/">盐城楼盘</a></li>
                      <li><a href="https://zs.fang.lianjia.com/">中山楼盘</a></li>
                      <li><a href="https://dd.fang.lianjia.com/">丹东楼盘</a></li>
                      <li><a href="https://wuhu.fang.lianjia.com/">芜湖楼盘</a></li>
                      <li><a href="https://linyi.fang.lianjia.com/">临沂楼盘</a></li>
                      <li><a href="https://su.fang.lianjia.com/">苏州楼盘</a></li>
                      <li><a href="https://hanzhong.fang.lianjia.com/">汉中楼盘</a></li>
                      <li><a href="https://wh.fang.lianjia.com/">武汉楼盘</a></li>
                      <li><a href="https://tj.fang.lianjia.com/">天津楼盘</a></li>
                      <li><a href="https://zh.fang.lianjia.com/">珠海楼盘</a></li>
                      <li><a href="https://gz.fang.lianjia.com/">广州楼盘</a></li>
                      <li><a href="https://cd.fang.lianjia.com/">成都楼盘</a></li>
                      <li><a href="https://sx.fang.lianjia.com/">绍兴楼盘</a></li>
                      <li><a href="https://huzhou.fang.lianjia.com/">湖州楼盘</a></li>
                      <li><a href="https://san.fang.lianjia.com/">三亚楼盘</a></li>
                      <li><a href="https://jl.fang.lianjia.com/">吉林楼盘</a></li>
                      <li><a href="https://km.fang.lianjia.com/">昆明楼盘</a></li>
                      <li><a href="https://baoji.fang.lianjia.com/">宝鸡楼盘</a></li>
                      <li><a href="https://nb.fang.lianjia.com/">宁波楼盘</a></li>
                      <li><a href="https://baoding.fang.lianjia.com/">保定楼盘</a></li>
                      <li><a href="https://wz.fang.lianjia.com/">温州楼盘</a></li>
                      <li><a href="https://qd.fang.lianjia.com/">青岛楼盘</a></li>
                      <li><a href="https://dl.fang.lianjia.com/">大连楼盘</a></li>
                      <li><a href="https://zj.fang.lianjia.com/">镇江楼盘</a></li>
                      <li><a href="https://xan.fang.lianjia.com/">雄安新区楼盘</a></li>
                      <li><a href="https://liangshan.fang.lianjia.com/">凉山楼盘</a></li>
                      <li><a href="https://sy.fang.lianjia.com/">沈阳楼盘</a></li>
                      <li><a href="https://sz.fang.lianjia.com/">深圳楼盘</a></li>
                  </ul>
               <ul data-el="childrenList"  >
                      <li><a href="https://zz.ke.com/ershoufang/">郑州二手房</a></li>
                      <li><a href="https://zj.ke.com/ershoufang/">镇江二手房</a></li>
                      <li><a href="https://nj.ke.com/ershoufang/">南京二手房</a></li>
                      <li><a href="https://yt.ke.com/ershoufang/">烟台二手房</a></li>
                      <li><a href="https://cs.ke.com/ershoufang/">长沙二手房</a></li>
                      <li><a href="https://dg.ke.com/ershoufang/">东莞二手房</a></li>
                      <li><a href="https://changzhou.ke.com/ershoufang/">常州二手房</a></li>
                      <li><a href="https://wx.ke.com/ershoufang/">无锡二手房</a></li>
                      <li><a href="https://aq.ke.com/ershoufang/">安庆二手房</a></li>
                      <li><a href="https://dd.ke.com/ershoufang/">丹东二手房</a></li>
                      <li><a href="https://hf.ke.com/ershoufang/">合肥二手房</a></li>
                      <li><a href="https://zs.ke.com/ershoufang/">中山二手房</a></li>
                      <li><a href="https://jn.ke.com/ershoufang/">济南二手房</a></li>
                      <li><a href="https://hz.ke.com/ershoufang/">杭州二手房</a></li>
                      <li><a href="https://gz.ke.com/ershoufang/">广州二手房</a></li>
                      <li><a href="https://yy.ke.com/ershoufang/">岳阳二手房</a></li>
                      <li><a href="https://xan.ke.com/ershoufang/">雄安新区二手房</a></li>
                      <li><a href="https://zjk.ke.com/ershoufang/">张家口二手房</a></li>
                      <li><a href="https://xm.ke.com/ershoufang/">厦门二手房</a></li>
                      <li><a href="https://taizhou.ke.com/ershoufang/">台州二手房</a></li>
                      <li><a href="https://yc.ke.com/ershoufang/">盐城二手房</a></li>
                      <li><a href="https://hui.ke.com/ershoufang/">惠州二手房</a></li>
                      <li><a href="https://liangshan.ke.com/ershoufang/">凉山二手房</a></li>
                      <li><a href="https://jiujiang.ke.com/ershoufang/">九江二手房</a></li>
                      <li><a href="https://bj.ke.com/ershoufang/">北京二手房</a></li>
                      <li><a href="https://jh.ke.com/ershoufang/">金华二手房</a></li>
                      <li><a href="https://wh.ke.com/ershoufang/">武汉二手房</a></li>
                      <li><a href="https://nn.ke.com/ershoufang/">南宁二手房</a></li>
                      <li><a href="https://cd.ke.com/ershoufang/">成都二手房</a></li>
                      <li><a href="https://nanchong.ke.com/ershoufang/">南充二手房</a></li>
                  </ul>
               <ul data-el="childrenList"  >
                  </ul>
           </div>

    <div class="footer__bottom">
      <p>链家网（北京）科技有限公司 | 网络经营许可证 京ICP备16057509号-2 | &copy; Copyright&copy;2010-2018 链家网Lianjia.com版权所有</p>
      <a target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010802024019" style="display:inline-block;text-decoration:none;height:20px;line-height:20px;"><img style="margin-right: 5px;" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/img/beian.png?_v=201903142105200c0">京公网安备 11010802024019号</a>
    </div>

  </div>
</div>

<script type="text/javascript">
  var footerList = JSON.parse(JSON.stringify([{"abbr":"zfcs","expire":"2019-03-25 13:04:11","city_id":"330100","children":[{"url":"https:\/\/tj.lianjia.com\/zufang\/","title":"\u5929\u6d25\u79df\u623f"},{"url":"https:\/\/lf.lianjia.com\/zufang\/","title":"\u5eca\u574a\u79df\u623f"},{"url":"https:\/\/hk.lianjia.com\/zufang\/","title":"\u6d77\u53e3\u79df\u623f"},{"url":"https:\/\/zs.lianjia.com\/zufang\/","title":"\u4e2d\u5c71\u79df\u623f"},{"url":"https:\/\/ms.lianjia.com\/zufang\/","title":"\u7709\u5c71\u79df\u623f"},{"url":"https:\/\/hf.lianjia.com\/zufang\/","title":"\u5408\u80a5\u79df\u623f"},{"url":"https:\/\/jx.lianjia.com\/zufang\/","title":"\u5609\u5174\u79df\u623f"},{"url":"https:\/\/jn.lianjia.com\/zufang\/","title":"\u6d4e\u5357\u79df\u623f"},{"url":"https:\/\/xc.lianjia.com\/zufang\/","title":"\u8bb8\u660c\u79df\u623f"},{"url":"https:\/\/nanchong.lianjia.com\/zufang\/","title":"\u5357\u5145\u79df\u623f"},{"url":"https:\/\/km.lianjia.com\/zufang\/","title":"\u6606\u660e\u79df\u623f"},{"url":"https:\/\/linyi.lianjia.com\/zufang\/","title":"\u4e34\u6c82\u79df\u623f"},{"url":"https:\/\/cc.lianjia.com\/zufang\/","title":"\u957f\u6625\u79df\u623f"},{"url":"https:\/\/ts.lianjia.com\/zufang\/","title":"\u5510\u5c71\u79df\u623f"},{"url":"https:\/\/dazhou.lianjia.com\/zufang\/","title":"\u8fbe\u5dde\u79df\u623f"},{"url":"https:\/\/wuhu.lianjia.com\/zufang\/","title":"\u829c\u6e56\u79df\u623f"},{"url":"https:\/\/fs.lianjia.com\/zufang\/","title":"\u4f5b\u5c71\u79df\u623f"},{"url":"https:\/\/gy.lianjia.com\/zufang\/","title":"\u8d35\u9633\u79df\u623f"},{"url":"https:\/\/nn.lianjia.com\/zufang\/","title":"\u5357\u5b81\u79df\u623f"},{"url":"https:\/\/nj.lianjia.com\/zufang\/","title":"\u5357\u4eac\u79df\u623f"},{"url":"https:\/\/cs.lianjia.com\/zufang\/","title":"\u957f\u6c99\u79df\u623f"},{"url":"https:\/\/baoji.lianjia.com\/zufang\/","title":"\u5b9d\u9e21\u79df\u623f"},{"url":"https:\/\/sy.lianjia.com\/zufang\/","title":"\u6c88\u9633\u79df\u623f"},{"url":"https:\/\/zh.lianjia.com\/zufang\/","title":"\u73e0\u6d77\u79df\u623f"},{"url":"https:\/\/yc.lianjia.com\/zufang\/","title":"\u76d0\u57ce\u79df\u623f"},{"url":"https:\/\/bj.lianjia.com\/zufang\/","title":"\u5317\u4eac\u79df\u623f"},{"url":"https:\/\/sjz.lianjia.com\/zufang\/","title":"\u77f3\u5bb6\u5e84\u79df\u623f"},{"url":"https:\/\/wh.lianjia.com\/zufang\/","title":"\u6b66\u6c49\u79df\u623f"},{"url":"https:\/\/baoding.lianjia.com\/zufang\/","title":"\u4fdd\u5b9a\u79df\u623f"},{"url":"https:\/\/zjk.lianjia.com\/zufang\/","title":"\u5f20\u5bb6\u53e3\u79df\u623f"}],"title":"\u79df\u623f\u57ce\u5e02","class":""},{"abbr":"rmsq","expire":"2019-03-25 13:04:11","city_id":"330100","children":[{"url":"https:\/\/hz.lianjia.com\/zufang\/sandun\/","title":"\u4e09\u58a9\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/qiaosi\/","title":"\u4e54\u53f8\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/qianjiangxincheng\/","title":"\u94b1\u6c5f\u65b0\u57ce\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/qingtai\/","title":"\u6e05\u6cf0\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/wenjiao\/","title":"\u6587\u6559\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/nanxing\/","title":"\u5357\u661f\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/gouzhuang\/","title":"\u52fe\u5e84\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/cuiyuan\/","title":"\u7fe0\u82d1\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/feicuicheng1\/","title":"\u7fe1\u7fe0\u57ce\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/zhonganqiao\/","title":"\u4f17\u5b89\u6865\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/nanxiaobu\/","title":"\u5357\u8096\u57e0\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/jianqiao\/","title":"\u7b15\u6865\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/caihongcheng\/","title":"\u5f69\u8679\u57ce\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/gulou2\/","title":"\u9f13\u697c\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/tangqi1\/","title":"\u5858\u6816\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/qianjiangshijicheng\/","title":"\u94b1\u6c5f\u4e16\u7eaa\u57ce\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/jinshahu\/","title":"\u91d1\u6c99\u6e56\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/liuxia1\/","title":"\u7559\u4e0b\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/chaoming11\/","title":"\u6f6e\u9e23\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/puyan\/","title":"\u6d66\u6cbf\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/fuyang1\/","title":"\u5bcc\u9633\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/changhe\/","title":"\u957f\u6cb3\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/gongyeyuanbei\/","title":"\u5de5\u4e1a\u56ed\u5317\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/hubin1\/","title":"\u6e56\u6ee8\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/zhijiang\/","title":"\u4e4b\u6c5f\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/chunan\/","title":"\u6df3\u5b89\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/gongchenqiao\/","title":"\u62f1\u5bb8\u6865\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/dingqiao\/","title":"\u4e01\u6865\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/renhe2\/","title":"\u4ec1\u548c\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/shenhua\/","title":"\u7533\u82b1\u79df\u623f"}],"title":"\u70ed\u95e8\u5546\u5708","class":""},{"abbr":"tjxq","expire":"2019-03-25 13:04:11","city_id":"330100","children":[{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043640872\/","title":"\u6885\u82d1\u9601\u5c0f\u533a\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043640835\/","title":"\u8d5e\u6210\u6797\u98ce\u548c\u98ce\u82d1\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043640652\/","title":"\u745e\u4e30\u683c\u6797\u82d1\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c187623364588178\/","title":"\u6052\u751f\u79d1\u6280\u56ed\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043642428\/","title":"\u6cf0\u548c\u82d1\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043641078\/","title":"\u68a6\u6e56\u5c71\u5e84\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c187574840685010\/","title":"\u8d5e\u6210\u8d5e\u57ce\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043636351\/","title":"\u6e05\u5408\u5609\u56ed\u4e1c\u533a\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043636476\/","title":"\u957f\u677f\u91cc\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043639447\/","title":"\u666f\u82b3\u4e8c\u533a\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043636704\/","title":"\u5b97\u575b\u5df7\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c188123089433077\/","title":"\u8d8a\u79c0\u661f\u6c47\u57ce\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043636681\/","title":"\u8fdc\u4e1c\u65b0\u6708\u516c\u5bd3\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043639560\/","title":"\u7eff\u57ce\u7389\u5170\u516c\u5bd3\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043636470\/","title":"\u957f\u65b0\u91cc\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c187462070530717\/","title":"\u4e91\u6c34\u5c71\u5c45\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c187596381319218\/","title":"\u5929\u9633\u6674\u6717\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043636184\/","title":"\u4e5d\u9f99\u5c71\u5e84\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043639582\/","title":"\u4e01\u5170\u5546\u4e1a\u4e2d\u5fc3\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043638717\/","title":"\u4e07\u5bb6\u82b1\u56ed\u6b23\u548c\u82d1\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043640685\/","title":"\u4e1c\u592a\u5e73\u5df7\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043635925\/","title":"\u4e2d\u5357\u516c\u5bd3\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c187511744459272\/","title":"\u4e2d\u65b0\u5fa1\u666f\u6e7e\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043635936\/","title":"\u5546\u57ce\u4e1c\u82d1\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043636349\/","title":"\u674e\u5bb6\u6865\u5c0f\u533a\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043640549\/","title":"\u5c71\u6c34\u4f73\u82d1\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043637477\/","title":"\u5927\u5173\u897f\u56db\u82d1\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043641202\/","title":"\u7d2b\u7af9\u82d1\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043640943\/","title":"\u4e1c\u65b9\u91d1\u5ea7\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043635922\/","title":"\u5174\u8000\u5927\u53a6\u79df\u623f"}],"title":"\u63a8\u8350\u5c0f\u533a","class":""},{"abbr":"csxf","expire":"2019-03-25 13:04:36","city_id":"330100","children":[{"url":"https:\/\/zjk.fang.lianjia.com\/","title":"\u5f20\u5bb6\u53e3\u697c\u76d8"},{"url":"https:\/\/wf.fang.lianjia.com\/","title":"\u6f4d\u574a\u697c\u76d8"},{"url":"https:\/\/yc.fang.lianjia.com\/","title":"\u76d0\u57ce\u697c\u76d8"},{"url":"https:\/\/zs.fang.lianjia.com\/","title":"\u4e2d\u5c71\u697c\u76d8"},{"url":"https:\/\/dd.fang.lianjia.com\/","title":"\u4e39\u4e1c\u697c\u76d8"},{"url":"https:\/\/wuhu.fang.lianjia.com\/","title":"\u829c\u6e56\u697c\u76d8"},{"url":"https:\/\/linyi.fang.lianjia.com\/","title":"\u4e34\u6c82\u697c\u76d8"},{"url":"https:\/\/su.fang.lianjia.com\/","title":"\u82cf\u5dde\u697c\u76d8"},{"url":"https:\/\/hanzhong.fang.lianjia.com\/","title":"\u6c49\u4e2d\u697c\u76d8"},{"url":"https:\/\/wh.fang.lianjia.com\/","title":"\u6b66\u6c49\u697c\u76d8"},{"url":"https:\/\/tj.fang.lianjia.com\/","title":"\u5929\u6d25\u697c\u76d8"},{"url":"https:\/\/zh.fang.lianjia.com\/","title":"\u73e0\u6d77\u697c\u76d8"},{"url":"https:\/\/gz.fang.lianjia.com\/","title":"\u5e7f\u5dde\u697c\u76d8"},{"url":"https:\/\/cd.fang.lianjia.com\/","title":"\u6210\u90fd\u697c\u76d8"},{"url":"https:\/\/sx.fang.lianjia.com\/","title":"\u7ecd\u5174\u697c\u76d8"},{"url":"https:\/\/huzhou.fang.lianjia.com\/","title":"\u6e56\u5dde\u697c\u76d8"},{"url":"https:\/\/san.fang.lianjia.com\/","title":"\u4e09\u4e9a\u697c\u76d8"},{"url":"https:\/\/jl.fang.lianjia.com\/","title":"\u5409\u6797\u697c\u76d8"},{"url":"https:\/\/km.fang.lianjia.com\/","title":"\u6606\u660e\u697c\u76d8"},{"url":"https:\/\/baoji.fang.lianjia.com\/","title":"\u5b9d\u9e21\u697c\u76d8"},{"url":"https:\/\/nb.fang.lianjia.com\/","title":"\u5b81\u6ce2\u697c\u76d8"},{"url":"https:\/\/baoding.fang.lianjia.com\/","title":"\u4fdd\u5b9a\u697c\u76d8"},{"url":"https:\/\/wz.fang.lianjia.com\/","title":"\u6e29\u5dde\u697c\u76d8"},{"url":"https:\/\/qd.fang.lianjia.com\/","title":"\u9752\u5c9b\u697c\u76d8"},{"url":"https:\/\/dl.fang.lianjia.com\/","title":"\u5927\u8fde\u697c\u76d8"},{"url":"https:\/\/zj.fang.lianjia.com\/","title":"\u9547\u6c5f\u697c\u76d8"},{"url":"https:\/\/xan.fang.lianjia.com\/","title":"\u96c4\u5b89\u65b0\u533a\u697c\u76d8"},{"url":"https:\/\/liangshan.fang.lianjia.com\/","title":"\u51c9\u5c71\u697c\u76d8"},{"url":"https:\/\/sy.fang.lianjia.com\/","title":"\u6c88\u9633\u697c\u76d8"},{"url":"https:\/\/sz.fang.lianjia.com\/","title":"\u6df1\u5733\u697c\u76d8"}],"title":"\u57ce\u5e02\u65b0\u623f","class":""},{"abbr":"csesf","expire":"2019-03-25 13:06:18","city_id":"330100","children":[{"url":"https:\/\/zz.ke.com\/ershoufang\/","title":"\u90d1\u5dde\u4e8c\u624b\u623f"},{"url":"https:\/\/zj.ke.com\/ershoufang\/","title":"\u9547\u6c5f\u4e8c\u624b\u623f"},{"url":"https:\/\/nj.ke.com\/ershoufang\/","title":"\u5357\u4eac\u4e8c\u624b\u623f"},{"url":"https:\/\/yt.ke.com\/ershoufang\/","title":"\u70df\u53f0\u4e8c\u624b\u623f"},{"url":"https:\/\/cs.ke.com\/ershoufang\/","title":"\u957f\u6c99\u4e8c\u624b\u623f"},{"url":"https:\/\/dg.ke.com\/ershoufang\/","title":"\u4e1c\u839e\u4e8c\u624b\u623f"},{"url":"https:\/\/changzhou.ke.com\/ershoufang\/","title":"\u5e38\u5dde\u4e8c\u624b\u623f"},{"url":"https:\/\/wx.ke.com\/ershoufang\/","title":"\u65e0\u9521\u4e8c\u624b\u623f"},{"url":"https:\/\/aq.ke.com\/ershoufang\/","title":"\u5b89\u5e86\u4e8c\u624b\u623f"},{"url":"https:\/\/dd.ke.com\/ershoufang\/","title":"\u4e39\u4e1c\u4e8c\u624b\u623f"},{"url":"https:\/\/hf.ke.com\/ershoufang\/","title":"\u5408\u80a5\u4e8c\u624b\u623f"},{"url":"https:\/\/zs.ke.com\/ershoufang\/","title":"\u4e2d\u5c71\u4e8c\u624b\u623f"},{"url":"https:\/\/jn.ke.com\/ershoufang\/","title":"\u6d4e\u5357\u4e8c\u624b\u623f"},{"url":"https:\/\/hz.ke.com\/ershoufang\/","title":"\u676d\u5dde\u4e8c\u624b\u623f"},{"url":"https:\/\/gz.ke.com\/ershoufang\/","title":"\u5e7f\u5dde\u4e8c\u624b\u623f"},{"url":"https:\/\/yy.ke.com\/ershoufang\/","title":"\u5cb3\u9633\u4e8c\u624b\u623f"},{"url":"https:\/\/xan.ke.com\/ershoufang\/","title":"\u96c4\u5b89\u65b0\u533a\u4e8c\u624b\u623f"},{"url":"https:\/\/zjk.ke.com\/ershoufang\/","title":"\u5f20\u5bb6\u53e3\u4e8c\u624b\u623f"},{"url":"https:\/\/xm.ke.com\/ershoufang\/","title":"\u53a6\u95e8\u4e8c\u624b\u623f"},{"url":"https:\/\/taizhou.ke.com\/ershoufang\/","title":"\u53f0\u5dde\u4e8c\u624b\u623f"},{"url":"https:\/\/yc.ke.com\/ershoufang\/","title":"\u76d0\u57ce\u4e8c\u624b\u623f"},{"url":"https:\/\/hui.ke.com\/ershoufang\/","title":"\u60e0\u5dde\u4e8c\u624b\u623f"},{"url":"https:\/\/liangshan.ke.com\/ershoufang\/","title":"\u51c9\u5c71\u4e8c\u624b\u623f"},{"url":"https:\/\/jiujiang.ke.com\/ershoufang\/","title":"\u4e5d\u6c5f\u4e8c\u624b\u623f"},{"url":"https:\/\/bj.ke.com\/ershoufang\/","title":"\u5317\u4eac\u4e8c\u624b\u623f"},{"url":"https:\/\/jh.ke.com\/ershoufang\/","title":"\u91d1\u534e\u4e8c\u624b\u623f"},{"url":"https:\/\/wh.ke.com\/ershoufang\/","title":"\u6b66\u6c49\u4e8c\u624b\u623f"},{"url":"https:\/\/nn.ke.com\/ershoufang\/","title":"\u5357\u5b81\u4e8c\u624b\u623f"},{"url":"https:\/\/cd.ke.com\/ershoufang\/","title":"\u6210\u90fd\u4e8c\u624b\u623f"},{"url":"https:\/\/nanchong.ke.com\/ershoufang\/","title":"\u5357\u5145\u4e8c\u624b\u623f"}],"title":"\u57ce\u5e02\u4e8c\u624b\u623f","class":""},{"abbr":"yqlj","title":"\u53cb\u60c5\u94fe\u63a5","city_id":"330100","expire":"2019-03-18","children":[]}]))

</script></body>


<!-- 自动推送代码 -->
<script>
  (function(){
  var canonicalURL, curProtocol;
  //Get the <link> tag
  var x=document.getElementsByTagName("link");
  //Find the last canonical URL
  if(x.length > 0){
  for (i=0;i<x.length;i++){
  if(x[i].rel.toLowerCase() == 'canonical' && x[i].href){
  canonicalURL=x[i].href;
  }
  }
  }
  //Get protocol
  if (!canonicalURL){
  curProtocol = window.location.protocol.split(':')[0];
  }
  else{
  curProtocol = canonicalURL.split(':')[0];
  }
  //Get current URL if the canonical URL does not exist
  if (!canonicalURL) canonicalURL = window.location.href;
  //Assign script content. Replace current URL with the canonical URL
  !function(){var e=/([http|https]:\/\/[a-zA-Z0-9\_\.]+\.baidu\.com)/gi,r=canonicalURL,t=document.referrer;if(!e.test(r)){var n=(String(curProtocol).toLowerCase() === 'https')?"https://sp0.baidu.com/9_Q4simg2RQJ8t7jm9iCKT-xh_/s.gif":"//api.share.baidu.com/s.gif";t?(n+="?r="+encodeURIComponent(document.referrer),r&&(n+="&l="+r)):r&&(n+="?l="+r);var i=new Image;i.src=n}}(window);})();
</script>

<script type="text/javascript" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/common/js/common.js?_v=201903142105200c0"></script>

<script type="text/javascript">
  //引入脚本后
  var imConf = {
          "ajaxroot": "\/\/ajax.api.ke.com\/",
          "imAppid": "ZULIN_WEB_20181122",
          "imAppkey": "0a4e8669fc2a50cbbeeb969726a7ab46"
      };
</script>
<script>
var __basePath = 'https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src?_v=201903142105200c0'.split("?");
require.config({
  baseUrl: __basePath[0],
  paths: {
  },
  urlArgs:  __basePath[1]
});
var config = {"fe_root":"https:\/\/s1.ljcdn.com\/matrix_lianjia_pc\/dist\/pc","version":"201903142105200c0","js_ns":"m_pages_zufangDetail","cur_city_id":"330100","cur_city_name":"\u676d\u5dde","cur_city_short":"hz"};
</script>
<script>
;;(function() {
  for(var i = 0, len = __requireList.length; i < len; i++) {
    require([__requireList[i]], function(engine) {
      engine.init();
    });
  }
})();
</script>
<!--动态脚本内容-->
<div style="display: none">
  <script src="https://s19.cnzz.com/z_stat.php?id=1273627291&web_id=1273627291" language="JavaScript"></script>
</div>
<script>
  window.ljConf = {
    city_abbr: 'hz',
    city_id: '330100',
    city_name: '杭州',
  }
window.__UDL_CONFIG = window.__UDL_CONFIG || {};
window.__UDL_CONFIG.pid = window.__UDL_CONFIG.pid || (document.domain.search('ke.com')>-1 ? 'bigc_pc_rent':'matrixpc');
window.__UDL_CONFIG.env = ('prod' === 'prod' ? (document.domain.search('ke.com')>-1 ? 'dac' : 'lianjia') : 'test');
window.__UDL_CONFIG[document.domain.search('ke.com') > -1?'uicode':'ljweb_channel_key'] = g_conf.pageId || '';
with(document)0[(getElementsByTagName('head')[0]||body).appendChild(createElement('script')).src='//s1.ljcdn.com/matrix_pc/dist/pc/third/dig.js?'+__basePath[1]]
</script>

</html>

'''




soup = BeautifulSoup(html, "lxml")

# l = soup.find(attrs={"data-el":"houseComment"})
# print(l.get_text())
 


# data = re.findall("g_conf.name = '(.*?)'", html)

# data = re.search("g_conf.name = '(.*?)'",html).group(1)

# data = re.search("g_conf.coord = {(.*?)};", html)
# data = re.search("g_conf.coord = {.*?longitude:.*?'(.*?)'.*?latitude:.*?'(.*?)'.*?};", html, re.S)
# # data = re.search('''g_conf.coord = {
# #     longitude: '(.*?)',
# #     latitude: '(.*?)'
# #   };''', html)

# print(data)
# print(data.group(1))
# print(data.group(2))

data = soup.select(".content__thumb--box li img")

for img in data:
    print(img['src'])

print(data)

