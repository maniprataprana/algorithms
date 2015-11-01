import java.util.Arrays;
import java.util.List;
import java.util.TreeSet;
import java.util.Scanner;

public class SortingStrings
{
	public static void main (String[] args)
	{	
		Scanner in = new Scanner(System.in);
		String N = in.nextLine();
		int times = Integer.parseInt(N);
		String[] strArr=new String[times];
		for (int i=0 ; i<times; i++ ) {
			String item = in.nextLine();
			strArr[i] = item;
		}

        List<String> nameList = Arrays.asList(strArr);
        //create a treeset with the list and remove the duplicates
        TreeSet<String> unique = new TreeSet<String>(nameList);
        //System.out.println("=============");
        for (String name : unique) {
			System.out.println(name);
		}	

	}
}