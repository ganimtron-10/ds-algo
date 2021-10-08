function selctionsort(arr){
	h = arr.length - 1
	for(let i = 0;i<h;i++){
		for(let l = i+1;l <= h;l++){
			if(arr[i] > arr[l]){
				var temp = arr[l]
				arr[l] = arr[i]
				arr[i] = temp
			}
		}
	}
	return arr
}

// var arr = [3298,238,73,98,2622,923]
// console.log(selctionsort(arr))