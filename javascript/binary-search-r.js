function binarysearchr(arr,l,h,element){
	if(l>h){
		return null
	}
	mid = Math.floor((l+h)/2)
	if(arr[mid] == element){
		return mid
	}
	else if(arr[mid] < element){
		return binarysearchr(arr,mid+1,h,element)
	}
	else if(arr[mid] > element){
		return binarysearchr(arr,l,mid-1,element)
	}
}

// var arr = [ 73, 98, 238, 923, 2622, 3298 ]
// console.log(binarysearchr(arr,0,arr.length-1,2622))
