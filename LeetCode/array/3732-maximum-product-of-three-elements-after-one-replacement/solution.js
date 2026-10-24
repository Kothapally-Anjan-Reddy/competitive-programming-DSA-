/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    let sorted=nums.sort((a,b)=>Math.abs(b)-Math.abs(a))
    let x=sorted[0]
    let y=sorted[1]
    if(x*y>0){
        return x*y*100000
    }
    else if(x*y===0){
        return 0
    }
    else{
        return x*y*100000*-1
    }
};
