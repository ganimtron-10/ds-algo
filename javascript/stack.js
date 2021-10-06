class Stack{
	constructor(){
		this.array = []
	}
	push(ele){
		this.array.push(ele)
	}
	pop(){
		return this.array.pop()
	}
	print(){
		console.log(this.array)
	}
}

// var s = new Stack()
// s.push(10)
// s.print()
// s.push(198)
// s.print()
// s.push(2)
// s.push(53)
// s.print()
// s.pop()
// s.print()