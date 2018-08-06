import java.util.*;

class MyList {
	public static void main(String[] args) {
		ArrayList<String> al = new ArrayList<String>();
		al.add("One");
		al.add("Two");
		al.add("Three");
		al.add(0, "Zero");

		for(int i=0; i<al.size(); i++)
			System.out.println("Element at Index " + i + " is : " + al.get(i));

		for(String s : al)
			System.out.println(s);


		int index = al.indexOf("zero");
		System.out.println(index);
		al.clear();
		System.out.println(al.isEmpty());

		ArrayList<Integer> alInt = new ArrayList<Integer>();
		alInt.add(1);
		alInt.add(2);
		for(int value : alInt)
			System.out.println(value);
	}
}