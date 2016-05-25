object Euler_68{
    def isValid(nums:List[Int]) = {
        val t = nums.take(5).sum
        if(t%5 == 0){
            val s = t/5+11
            val a1 = nums(0)+nums(1)+nums(5)
            val a2 = nums(1)+nums(2)+nums(6)
            val a3 = nums(2)+nums(3)+nums(7)
            val a4 = nums(3)+nums(4)+nums(8)
            val a5 = nums(0)+nums(4)+nums(9)
            if(a1==s && a2==s && a3==s && a4==s && a5==s){
                true
            }
            else{
                false
            }
        }
        else{
            false
        }
    }
    def clockString(nums:List[Int]) = {
        val m = List(nums(5),nums(6),nums(7),nums(8),nums(9)).min
        val s1 = (nums(5)*100+nums(0)*10+nums(1)).toString
        val s2 = (nums(6)*100+nums(1)*10+nums(2)).toString
        val s3 = (nums(7)*100+nums(2)*10+nums(3)).toString
        val s4 = (nums(8)*100+nums(3)*10+nums(4)).toString
        val s5 = (nums(9)*100+nums(4)*10+nums(0)).toString
        if(nums(5)==m){
            s1+s2+s3+s4+s5
        }else if(nums(6)==m){
            s2+s3+s4+s5+s1
        }else if(nums(7)==m){
            s3+s4+s5+s1+s2
        }else if(nums(8)==m){
            s4+s5+s1+s2+s3
        }else{
            s5+s1+s2+s3+s4
        }
    }
    def main(args:Array[String]):Unit = {
        val nums = List(1,2,3,4,5,6,7,8,9,10)
        val it = nums.permutations
        var maxString = "0"
        while(it.hasNext){
            val l = it.next()
            if(isValid(l)){
                val s = clockString(l)
                if(s.length == 16 && s>maxString){
                    maxString = s
                }
            }
        }
        println(maxString)        
    }
}
