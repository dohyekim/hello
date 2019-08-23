const cart = [
    {name: "Widget", price: 9.95},
    {name: "Gadget", price: 22.95},
]

const names = cart.map(x => x.name);
console.log(names) //[ 'Widget', 'Gadget' ]
const prices = cart.map( x => x.price);
console.log(prices) //[ 9.95, 22.95 ]
const discountPrices = prices.map(x => x*0.8);
console.log(discountPrices); //[ 7.96, 18.36 ]
const newCart = names.map((x,i) => ({ name: x, prices: prices[i]}) );
console.log(newCart)
//[ { name: 'Widget', prices: 9.95 },
// { name: 'Gadget', prices: 22.95 } ]
