import java.util.Arrays;
import java.util.Scanner;

/* Name of the class has to be "Main" only if the class is public. */
public class SmallestNumber
{
	public static void main (String[] args) throws java.lang.Exception
	{
		//Enter the numbers in numbers array
		//int[] numbers = new int[] {8,2,3,11,12,10};
		//int[] numbers = new int[] {10,8,2,3};
		//int[] numbers = new int[] {1,8,11,10};
		//String[] stringNums = new String[numbers.length];
	    
	    Scanner in = new Scanner(System.in);
		String N = in.nextLine();
		int times = Integer.parseInt(N);
		String[] stringNums=new String[times];
		for (int i=0 ; i<times; i++ ) {
			String item = in.nextLine();
			stringNums[i] = item;
		}

	    int i = 0;
	    //while (i < numbers.length) {
	      //  stringNums[i] = String.valueOf(numbers[i++]);
	    //}


		for(i=0; i < stringNums.length ;i++) {
	        for(int j = i; j < stringNums.length ; j++) {
	        	String ab = stringNums[i] + stringNums[j];
	        	String ba = stringNums[j] + stringNums[i];
	        	if(Integer.parseInt(ab) > Integer.parseInt(ba)) {
	        		String temp = stringNums[i];
                    stringNums[i] = stringNums[j];
                    stringNums[j] = temp;
	        	}
	        }
	    }	    
		i = 0;
		String result = "";
	    while (i < stringNums.length) {
	        result +=stringNums[i++];
	    }
	    System.out.println(result);
	}
}