import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String str = br.readLine();
		
		int[] num = new int[26];
		
		int cnt = 0;
		int put = 2;
		for (int i = 0; i < 26 ; i++) {
			num[i] = put;
			cnt++;
			
			if (put == 7 || put == 9) {
				if(cnt == 4) {
					put++;
					cnt -= 4;
				}
			}else {
				if(cnt == 3) {
					put++;
					cnt -= 3;
				}
			}
		}
        
		int[] time = new int[9];
		int a = 2;
		for (int i = 0; i < time.length; i++) {
			time[i] = a++;
		}
		
		int sum = 0;
		
		for (int i = 0; i < str.length(); i++) {
			int temp = num[str.charAt(i)-'A'];
			sum += time[temp - 1];
		}
		
		System.out.println(sum);
	}

}

