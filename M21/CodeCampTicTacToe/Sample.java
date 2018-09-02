import java.util.*;
import java.io.*;
public class Sample {
	static int a = 2;
	public int efficient_exponentiation(int x, int n) {
		System.out.println(n);
		if(n<0)
			return efficient_exponentiation(1/x, -n);
		else if(n==0)
			return 1;
		else if(n==1)
			return x;
		else if(n%2 == 0)
			return efficient_exponentiation(x*x, n/2);
		else
			return efficient_exponentiation(x*x, (n-1)/2);
	}
	public static void main(String[] args) throws Exception {		
		Scanner scan = new Scanner(System.in);
		int a = 2;
		new Sample().efficient_exponentiation(2, 15);
		System.out.println("Hello world");
	}
}