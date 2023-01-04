import java.util.*;
public class Week1_1 {

	public static void main(String[] args) {
		int n1;
		Scanner sc = new Scanner(System.in);
		n1 = sc.nextInt();
		int []arr = new int[n1];
		for(int i = 0; i < n1; i++) {
			arr[i] = sc.nextInt();
		}
		for(int i = 0; i < n1 - 1; i++) {
			for(int j = i + 1; j < n1; j++) {
				if(arr[i] > arr[j]) {
					int temp = arr[i];
					arr[i] = arr[j];
					arr[j] = temp;
				}
			}
		}
		
		for(int i = 0; i < n1; i++) {
			System.out.println(arr[i]);
		}
	}
}
