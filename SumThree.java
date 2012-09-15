//given n distinct integer how many sum to zero
// brute force
public class SumThree {

	public static int count(int [] a) {
		int n = a.length;
		int c = 0;

		for(int i = 0;i < n-2; i++) {
			for (int j = i+1; j < n ; j++ ) {
				for (int k = j+1; k < n ; k++ ) {
					if ((a[i] + a[j] + a[k]) == 0) {
						c++;
						System.out.print(a[i]+"	"+a[j]+"	"+a[k] +"\n");

					}
				}
			}
		}
		return c;
	}


	public static void main(String [] args) {
		int [] num = {1,23,4,-2,3,42,-1,-2};
		System.out.println(count(num));
	}
}
