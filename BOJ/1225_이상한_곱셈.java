import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String aStr = in.next();
        String bStr = in.next();
        
        long answer=0;
        for (int i=0;i<aStr.length();i++){
            for (int j=0;j<bStr.length();j++){
                int aa = aStr.charAt(i)-'0';
                int bb = bStr.charAt(j)-'0';
                answer+=aa*bb;
            }
        }
        System.out.println(answer);
    }
}
