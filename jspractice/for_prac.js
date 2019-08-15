// 쉼표 연산자
for (let temp, i=0, j=1; j<30; temp=i, i=j, j = i+temp) console.log(j);

// 초기화 생략
let s = '3333';
for(; s.length<10; s = ' ' + s) console.log(s);

for (let x=0.2; x<3.0; x+=0.2) console.log(x);

// // switch
// switch(totalBet) {
//     case 7:
//         totalBet = funds;
//         break;
//     case 13:
//         funds = funds - 1;
//     case 11:
//         totalBet = 0;
//         break;
//     case 21:
//         totalBet=21;
//         break;
//     default:
//         console.log("No Superstition Here!");
//         break;
// }

// for...in 루프

const player = { name : 'Thomas', rank : 'Diamond', age : 25 };
for (let prop in player) {
    if (!player.hasOwnProperty(prop)) continue;
    console.log(prop + ': ' + player[prop])
} 
// name: Thomas
// rank: Diamond
// age: 25


// for...of 루프
const hand = ['diamond', 'spade', 'heart'];
for (let face of hand) console.log(`You rolled... ${face}!`)
// You rolled... diamond!
// You rolled... spade!
// You rolled... heart!

for (let i=0; i<hand.length; i++) console.log(`Roll ${i + 1} : You rolled ${hand[i]}`)
// Roll 1 : You rolled diamond
// Roll 2 : You rolled spade
// Roll 3 : You rolled heart
