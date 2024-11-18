import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        String input=br.readLine();
        StringBuilder toggled=new StringBuilder();
        for (char c: input.toCharArray()){
            if (Character.isUpperCase(c)){
                toggled.append(Character.toLowerCase(c));
            } else {
                toggled.append(Character.toUpperCase(c));
            }
        }
        System.out.println(toggled.toString());
    }
}
