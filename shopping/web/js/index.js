$(function(){
	// 轮播图
	var imgIndex = 0;
	function autoPlay(){
		//当前图片隐藏
		//eq(index)指定下标获取jquery对象
		$("#banner img").eq(imgIndex).css("display","none");
		$("#banner li").eq(imgIndex).css("background","#fff");
		
		//下标后移取图片
		imgIndex++;
		if(imgIndex == $("#banner img").length){
			imgIndex = 0;
		}
		//设置图片显示
		$("#banner li").eq(imgIndex).css("background","gray");
		$("#banner img").eq(imgIndex).css("display","block");
	}
	var timer = setInterval(autoPlay,2000);	
	$("#banner").mouseover(function (){
		//鼠标移入，停止定时器
		clearInterval(timer);
	});
	//鼠标移出，重启定时器
	$("#banner").mouseout(function (){
		timer = setInterval(autoPlay,2000);
	});
	// 手动调整轮播图
	$('#banner .next').click(autoPlay)
	$('#banner .prev').click(function(){
		$("#banner img").eq(imgIndex).css("display","none");
		$("#banner li").eq(imgIndex).css("background","#fff");
		
		//下标后移取图片
// 		imgIndex--;
// 		if(imgIndex == -1){
// 			imgIndex = $("#banner img").length - 1;
// 		}
		imgIndex =  (--imgIndex == -1) ? ($("#banner img").length - 1) : imgIndex
		//设置图片显示
		$("#banner li").eq(imgIndex).css("background","gray");
		$("#banner img").eq(imgIndex).css("display","block");
	})
})


