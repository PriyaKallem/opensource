import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());
        List<Integer>result=createArray(n);
        System.out.println(result);
    }
    public static List<Integer>createArray(int n){
        List<Integer>array=new ArrayList<>();
        for (int i=0;i<n;i++){
            array.add(i);
        }
        return array;
    }
}
