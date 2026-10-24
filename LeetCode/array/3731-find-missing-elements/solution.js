/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findMissingElements = function(nums) {
    let nums_sorted=nums.sort((a,b)=>a-b)
    let length=nums_sorted.length
    let final=[]
    if(nums_sorted[length-1] - nums_sorted[0] + 1 === length){
        return final
    }
    else{
        let next=nums_sorted[0]
        let i=0
        while (i<length){
            if(nums_sorted[i]!=next){
                final.push(next)
                next=next+1
                continue
            }
            i++
            next=next+1
        }
        return final
        }
};
