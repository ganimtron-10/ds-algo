class Queue{
	constructor(){
		this.array = []
	}
	enqueue(ele){
		this.array.push(ele)
	}
	dequeue(){
		return this.array.shift()
	}
	print(){
		console.log(this.array)
	}
}

// var q = new Queue()
// q.enqueue(10)
// q.print()
// q.enqueue(198)
// q.print()
// q.enqueue(2)
// q.enqueue(53)
// q.print()
// q.dequeue()
// q.print()