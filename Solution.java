package test;
import java.util.*;

/*
 * Initially on a notepad only one character 'A' is present. 
 * You can perform two operations on this notepad for each step:

	Copy All: You can copy all the characters present on the notepad 
	(partial copy is not allowed).
	Paste: You can paste the characters which are copied last time.

	Given a number n. You have to get exactly n 'A' on the notepad by 
	performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.

	Example 1:

	Input: 3
	Output: 3
	Explanation:
	Intitally, we have one character 'A'.
	In step 1, we use Copy All operation.
	In step 2, we use Paste operation to get 'AA'.
	In step 3, we use Paste operation to get 'AAA'.
 */


class Solution {
	
	//function that foctorizes the given n in minStepps()
	public static List<Integer> factorize(int n) {
		List<Integer> arr = new ArrayList<>();
		int size = n + 1; 
		for (int i = 2; i <= size; i++) {
			while(n % i == 0) {
				arr.add(i);
				n/=i;
			}
		}
		//return arr if n is not a prime number, else return n as a list
		return arr.size() > 0 ? arr : Arrays.asList(n);
	}
	
    public static int minSteps(int n) {
    	if (n == 1) return 0; //checks edge cases
    	else if (n == 2) return 2;
    	//keeps track of turns
    	int turns = 0; 
    	//stores result from factorize function
    	List<Integer> arr = factorize(n);
    	int arrSize = arr.size() - 1; 
    	//loops through list 
    	for (int i = arrSize; i >= 0; i--) {
    		//adds the amount of copies + pastes you have to use
        	//in order to achieve the next factor of the list
    		turns += arr.get(i);
    	}
    	
    	return turns; 
    }
    
    public static void main(String[] args) {
		System.out.println(minSteps(12));
	}
}

