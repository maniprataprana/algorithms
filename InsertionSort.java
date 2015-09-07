import java.io.*;
public class InsertionSort {
	public static void main(String[] args) {
		int[] input = { 4, 2, 9, 6, 23, 12, 34, 0, 1 };
		for (int i = 1; i < input.length; i++) {
			int temp = input[i],j;
			for (j = i-1; j >= 0 && temp < input[j]; j--) {
				input[j+1] = input[j];
			}
			input[j+1] = temp;
		}

		// Print all the array elements
      for (int i = 0; i < input.length; i++) {
         System.out.println(input[i] + " ");
      }
	}
}