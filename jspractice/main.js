$(document).ready(function() {
	'use strict';

	// paper.js를 전역 스코프에 설치
	paper.install(window);
	
	// paper.js를 mainCanvas에 연결, paper.js가 그림을 그릴 수 잇도록 준비
	paper.setup(document.getElementById('mainCanvas'));
	
	//TODO (실제 그림을 그리는 코드가 들어갈 자리)
	// var c = new Shape.Circle(new Point(200,200),50);
	// c.fillColor='green';


	// var c;
	// for(var x=25; x<400; x+=50) {
	// 	for(var y=25; y<400; y+=50) {
	// 		c = new Shape.Circle(x,y,20);
	// 		c.fillColor='green';
	// 	} 
	// }


	var c = new Shape.Circle(200, 200, 80);
	c.fillColor='black';
	var text = new PointText(200,200);
	text.justification = 'center';
	text.fillColor='white';
	text.fontsize=20;
	text.content = 'hello world';

	var tool = new Tool();
	tool.onMouseDown = function(evt) {
		console.log("evt>>>>>>", evt)
		// var c = new Shape.Circle(evt.point.x, evt.point.y, 20);
		var d = new Shape.Circle(evt.point, 20);
		d.fillColor='green';
	};
	
	// paper.js가 화면에 그림을 그리라는 명령
	paper.view.draw();
	
	console.log("main.js loaded")
});