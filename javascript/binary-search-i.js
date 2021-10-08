function binarysearchi(arr,element){
	l = 0
	h = arr.length - 1
	while(l<=h){
		mid = Math.floor((l+h)/2)
		if(arr[mid] == element){
			return mid
		}
		else if(arr[mid] > element){
			h = mid - 1
		}
		else if(arr[mid] < element){
			l = mid + 1
		}
	}
	return null
}

// var arr = [ 73, 98, 238, 923, 2622, 3298 ]
// console.log(binarysearchi(arr,19))