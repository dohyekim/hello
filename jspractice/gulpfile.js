const gulp = require('gulp');
// 걸프 의존성을 여기 씁니다.

// gulp.task('default', function(done) {
// 	// 걸프 작업을 여기 씁니다.
// 	done();
// });

// //Since your task might contain asynchronous code you have to signal gulp 
// // when your task has finished executing (= "async completion").

// // 3. Call the callback function
// // This is probably the easiest way for your use case: gulp automatically passes a callback function to your task as its first argument. Just call that function when you're done:

// // gulp.task('message', function(done) {
// //   console.log("HTTP Server Started");
// //   done();
// // });
const babel = require('gulp-babel');

gulp.task('default', function(done) {
	// 노드 소스
	gulp.src("es6/**/*.js") // 서브디렉토리 깊이에 상관없이 es6 아래의 모든 .js파일 선택
		.pipe(babel()) // 위 소스를 babel에 파이프로 연결
		.pipe(gulp.dest("dist")); // 바벨이 ES6를 ES5로 변형해서 컴파일된 ES5코드를 dist 디렉토리에 저장
		//ES6/a.js -> dist/a,js파일이 됨.

	// 브라우저 소스
	gulp.src("public/es6/**/*.js")
		.pipe(babel())
		.pipe(gulp.dest("public/dist"));
	done();
});