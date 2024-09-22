import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int q = in.nextInt();
        int[] bi= new int[n];

        int max_len =0;
        for (int i=0; i<n;i++){
            bi[i]=in.nextInt();
            max_len+=bi[i];
        }
        int[] cum_bi=new int[max_len];
        int idx=0;
        for (int i=0; i<n;i++){
            int now_len = bi[i];
            for (int j=0;j<now_len;j++){
                cum_bi[idx]=i+1;
                idx+=1;
            }
        }

        for (int i=0; i<q;i++){
            int now_q=in.nextInt();
            System.out.println(cum_bi[now_q]);
        }
    }
}
