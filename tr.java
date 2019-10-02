import java.util.*;
import java.lang.String;

class tr{
    public static void main(String[] args) {
        String X;
        Scanner sc = new Scanner(System.in);
        X = sc.nextLine();
        String Y = new String();
        int count = 0;
        int start = -1, end = -1;
        int i=1;
        for(int x=X.length()-1;x>=0;x--)
            Y += X.charAt(x);
        if(X.equalsIgnoreCase(Y)){
            System.out.println(X);
        }
        else{
            Y = new String();
            while(i < X.length()){
                int curr = 0;
                while(curr < X.length()){
                    int j = 0;
                    while(j<=i && curr < X.length()){
                        Y += X.charAt(curr);
                        curr++;
                        j++;
                    }
                    String rev = new String();
                    for(j=0;j<Y.length();j++)
                        rev+=Y.charAt(Y.length()-j-1);
                    if(Y.equalsIgnoreCase(rev)){
                        count = i+1;
                        start = curr - j - 1;
                        end = curr -1;
                        break;
                    }
                    curr--;
                }
                i++;
            }
            if(start != -1 && end != -1)
                System.out.println(X.substring(start, end));
            else
                System.out.print("No palindrome exist");
        }
    }
}
