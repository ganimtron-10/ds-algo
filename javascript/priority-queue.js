class PriorityQueue{
	constructor(){
		this.array = []
	}
	enqueue(ele,priority){
		if(this.array.length == 0){
			this.array.push([priority,ele])
		}
		else{
			let isadded = false
			for(let i = 0;i<this.array.length;i++){
				if(this.array[i][0] == priority){
					this.array[i].push(ele)
					isadded = true
				}
			}
			if(!isadded){
				this.array.push([priority,ele])
			}
		}
	}
	dequeue(){
		for(let i = 0;i<this.array.length;i++){
			if(this.array[i].length != 1){
				return this.array[i].splice(1,1)
				break
			}
		}
	}
	print(){
		console.log(this.array)
	}
}

// var pq = new PriorityQueue()
// pq.enqueue('10',1)
// pq.print()
// pq.enqueue('198',3)
// pq.print()
// pq.enqueue('2',5)
// pq.enqueue('53',10)
// pq.print()
// pq.dequeue()
// pq.print()
// pq.dequeue()
// pq.print()