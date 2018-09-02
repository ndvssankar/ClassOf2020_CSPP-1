import java.util.*;
class Sample {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String str = scan.nextLine();
		
		StringBuffer sb = new StringBuffer(str);
		String reverseStr = sb.reverse().toString();
		System.out.println(str);
		

		for(int i=str.length()-1; i>=0; i--)
			System.out.println(str.charAt(i));

		System.out.println(str);


	}

	public static boolean isEven(int number) {
		// if(number%2==0)
		// 	return true;
		// else
		// 	return false;

		return number%2==0;
	}


	public static boolean isPrime(int number) {
		int count = 0;
		for(int i=1; i<=number; i++) {
			if(number%i == 0)
				count++;
		}
		if(count==2)
			return true;
		else
			return false;
	}

	public static int power(int a, int b) {
		if(a==0 || b==0)
			return -1;
		else {
			int product = 1;
			for(int i=0; i<b; i++)
				product = product * a;
			return product;	
		}
	}

	public static int countDigits(int number) {
		int count = 0;
		if(number<0) 
			number = -number;

		if(number == 0)
			return 1;
		else {
			while(number > 0) {
				count = count + 1;
				number = number / 10;
			}
			return count;
		}
	}

	public static double mean() {
		Scanner scan = new Scanner(System.in);
		int[] list = new int(10);
		int sum = 0;
		double mean = 0.0;
		for(int i=0; i<10; i++)
			list[i] = scan.nextInt();
		for(int i=0; i<10; i++)
			sum = sum + list[i];
		mean = sum / list.length;
		return mean;
	}

	public static void swap(int a, int b) {
		int temp = a;
		a = b;
		b = temp;
	}
}


