class Solution {
public:
    int reverse(int x) {
        int num = abs(x);
        int new_num = 0;
        int cur = 0;
        while(num > 0){
            cur = num % 10;
            num/=10;
            new_num = new_num*10 + cur;
        }
        new_num = new_num%10 == cur ? new_num:0;
        if(x < 0){
            return new_num * -1;
        }
        return new_num;
    }
};