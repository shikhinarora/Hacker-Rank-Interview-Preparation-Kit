import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    static int maximumToys(int[] prices, int k) {
        // Complete this function
        Arrays.sort(prices);
        
        int i = 0;
        int toys = 0;
        while (k > 0){
            int price = prices[i];
            
            if(price > k)
                break;
            else {
                k = k - price;
                toys++;
                i++;
            }
        }
        
        return toys;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();
        int[] prices = new int[n];
        for(int prices_i = 0; prices_i < n; prices_i++){
            prices[prices_i] = in.nextInt();
        }
        int result = maximumToys(prices, k);
        System.out.println(result);
        in.close();
    }
}