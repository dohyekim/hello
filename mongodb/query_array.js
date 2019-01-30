
 db.food.insert({ _id: 1, fruit: ['apple', 'banana', 'peach'] })
 db.food.insert({ _id: 2, fruit: ['apple', 'orange', 'melon'] })
 db.food.insert({ _id: 3, fruit: ['cherry', 'peach'] })
 db.food.find({ fruit: 'banana' })
 db.food.find({ fruit: ['apple', 'banana'] })  
 db.food.find({ fruit: { $all: ['apple', 'banana'] } }) 
 db.food.find({ "fruit.2": 'peach' })
 db.food.find({ fruit: {$size: 3} })  