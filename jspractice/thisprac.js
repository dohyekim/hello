// const o = {
// 	name : 'Julie',
// 	greetBackwards : function () {
// 		function getReverseName() {
// 			let nanmeBackwards = '';
// 			for (let i=this.name.length-1; i>= 0; i--) {
// 				nanmeBackwards += this.name[i];
// 			}
// 		return nanmeBackwards;
// 		}
// 	return `${getReverseName()} si eman ym, olleH`;
// 	}
// };
// o.greetBackwards();

const p = {
	name : 'Julie',
	greetBackwards : function () {
		const getReverseName = () => {
			let nanmeBackwards = '';
			for (let i=this.name.length-1; i>= 0; i--) {
				nanmeBackwards += this.name[i];
			}
		return nanmeBackwards;
		}
	console.log(`${getReverseName()} si eman ym, olleH`)
	return `${getReverseName()} si eman ym, olleH`;
	}
};

p.greetBackwards();