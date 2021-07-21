/*
数组中占比超过一半的元素称之为主要元素。给你一个 整数 数组，找出其中的主要元素。若没有，返回 -1 。请设计时间复杂度为 O(N) 、空间复杂度为 O(1) 的解决方案。

 

示例 1：

输入：[1,2,5,9,5,9,5,5,5]
输出：5
示例 2：

输入：[3,2]
输出：-1
示例 3：

输入：[2,2,1,1,1,2,2]
输出：2


*/

class Solution {
    public int majorityElement(int[] nums) {
        if(nums.length == 0){
            return 0;
        }
        
        int register = nums[0];
        int cnt = 1;
        for(int i=1;i<nums.length;i++){
            if(register == nums[i]){
                cnt += 1;
            }
            else{
                cnt -= 1; 
                if(cnt==0){
                   register=nums[i] ;
                   cnt = 1;
                }

            }

        }
        return register;
    }
}