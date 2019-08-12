
// while(funds > 0 && funds < 100) {
// 	// 돈 걸기

// 	// 주사위 던지기

// 	// 돈 가져오기
// }

//m 이상 n 이하의 무작위 정수 반환
function rand(m,n) {
	return m + Math.floor((n - m + 1)* Math.random());
}

// 크라운 앤 앵커 게임의 여섯 그림 중 하나에 해당하는 문자열을 랜덤으로 반환
function randFace() {
	return ["crown", "anchor", "heart", "spade", "club", "diamond"]
	[rand(0,5)];
}

// 시작 조건
let funds = 50;
let round = 0;


while(funds > 1 && funds < 100) {
	round++;
	console.log(`round ${round}! starting funds: ${funds}p`)

	const bets = {
		crown : 0,
		anchor : 0,
		heart : 0,
		spade : 0,
		club : 0,
		diamond : 0
	};

	// 베팅할 금액
	let totalBet = rand(1,funds);
	if (totalBet === 7) {
		totalBet = funds;
		bets['heart'] = totalBet;
	}
	else {
		// 판에 걸린 돈(totalBet)을 분배
		let remaining = totalBet;
		do {
			let bet = rand(1, remaining);
			let face = randFace();
			bets[face] = bets[face] + bet;
			remaining = remaining - bet
		} while(remaining > 0);
	}

	funds = funds - totalBet;
	console.log('\tbets:' + Object.keys(bets).map(face => `${face} : ${bets[face]} pence`).join(', ') + ` (total: ${totalBet} pence)`)

	// 내가 주사위를 굴려서 나온 패
	const hand = [];
	for (let roll = 0;  roll < 3; roll++) {
		hand.push(randFace())
	}
	console.log(`\thand: ${hand.join(', ')}`);

	// 딴 돈을 가져옵니다.
	let winnings = 0;
	for(let die = 0; die < hand.length; die++) {
		let face = hand[die];
		if (bets[face] > 0) winnings = winnings + bets[face];
	}
	// console.log(die) //error, for loop 안의 변수는 for loop 안에서만 <=> while loop 안의 변수는 while loop 밖에서도 사용 가능!
	funds = funds + winnings;
	console.log(`\twinnings:${winnings}`);
}
console.log(`\tending funds : ${funds}`);