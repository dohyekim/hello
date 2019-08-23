const cards = [];
for (let suit of ['H','C','D','S'])
	for(let value=1; value<=13; value++)
		cards.push({suit, value});
		// cards.push({suit: suit, value: value});
	console.log(cards)

// [ { suit: 'H', value: 1 },
//   { suit: 'H', value: 2 },
//   { suit: 'H', value: 3 },
//   { suit: 'H', value: 4 },
//   { suit: 'H', value: 5 },
//   { suit: 'H', value: 6 },
//   { suit: 'H', value: 7 },
//   { suit: 'H', value: 8 },
//   { suit: 'H', value: 9 },
//   { suit: 'H', value: 10 },
//   { suit: 'H', value: 11 },
//   { suit: 'H', value: 12 },
//   { suit: 'H', value: 13 },
//   { suit: 'C', value: 1 },
//   { suit: 'C', value: 2 },
//   { suit: 'C', value: 3 },
//   { suit: 'C', value: 4 },
//   { suit: 'C', value: 5 },
//   { suit: 'C', value: 6 },
//   { suit: 'C', value: 7 },
//   { suit: 'C', value: 8 },
//   { suit: 'C', value: 9 },
//   { suit: 'C', value: 10 },
//   { suit: 'C', value: 11 },
//   { suit: 'C', value: 12 },
//   { suit: 'C', value: 13 },
//   { suit: 'D', value: 1 },
//   { suit: 'D', value: 2 },
//   { suit: 'D', value: 3 },
//   { suit: 'D', value: 4 },
//   { suit: 'D', value: 5 },
//   { suit: 'D', value: 6 },
//   { suit: 'D', value: 7 },
//   { suit: 'D', value: 8 },
//   { suit: 'D', value: 9 },
//   { suit: 'D', value: 10 },
//   { suit: 'D', value: 11 },
//   { suit: 'D', value: 12 },
//   { suit: 'D', value: 13 },
//   { suit: 'S', value: 1 },
//   { suit: 'S', value: 2 },
//   { suit: 'S', value: 3 },
//   { suit: 'S', value: 4 },
//   { suit: 'S', value: 5 },
//   { suit: 'S', value: 6 },
//   { suit: 'S', value: 7 },
//   { suit: 'S', value: 8 },
//   { suit: 'S', value: 9 },
//   { suit: 'S', value: 10 },
//   { suit: 'S', value: 11 },
//   { suit: 'S', value: 12 },
//   { suit: 'S', value: 13 } ]


const suits = { 'H': '\u2665', 'C':'\u2663', 'D':'\u2666', 'S':'\u2660' }
const values = { 1:'A', 11:'J', 12:'Q', 13:'K'};

function cardToString(c) {
	for (let i = 2; i < 11; i++) {
		values[i]=i};

	return values[c.value] + suits[c.suit];
	
}
let valtwo = cards.filter(c => c.value === 2).map(cardToString);
console.log(valtwo); //[ '2♥', '2♣', '2♦', '2♠' ]
let suitheart = cards.filter(c => c.suit === 'H' && c.value >= 11).map(cardToString); 
console.log(suitheart); //[ 'J♥', 'Q♥', 'K♥' ]

//reduce
const arr = [5,7,2,4];
const sum = arr.reduce((a,x) => a += x, 0)
const sum2 = arr.reduce((a,x) => a +=x);

console.log(sum) //18
console.log(arr) //[5,7,2,4];
console.log(sum2) //18

const words = ["Beachball", "Rodeo", "Angel", "Aardvark", "Xylophone", "November", "Chocolate", "Papaya",
				"Uniform", "Joker", "Clover", "Bali"];
const alphabetical = words.reduce( (a,x) => {
	if (!a[x[0]]) {
		a[x[0]] = [];
	}
	a[x[0]].push(x);
	return a
}, {});
console.log(alphabetical);
// { B: [ 'Beachball', 'Bali' ],
//   R: [ 'Rodeo' ],
//   A: [ 'Angel', 'Aardvark' ],
//   X: [ 'Xylophone' ],
//   N: [ 'November' ],
//   C: [ 'Chocolate', 'Clover' ],
//   P: [ 'Papaya' ],
//   U: [ 'Uniform' ],
//   J: [ 'Joker' ] }

const longWords = words.reduce( (a, x) => x.length>6 ? a+" "+x : a, "").trim();
console.log(longWords); //Beachball Aardvark Xylophone November Chocolate Uniform





























