import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Iterator;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		
		int count = 0;
		
		for (int k = 0; k < n; k++) {
			boolean [] isin = new boolean[26];
			
			String a = br.readLine();
			char prev = 0;
			boolean istrue = false;
			for (int i = 0; i < a.length(); i++) {
				if(a.charAt(i) != prev) {
					if(isin[a.charAt(i)-'a'] == false) {
						isin[a.charAt(i)-'a'] = true;
						prev = a.charAt(i);
						istrue = true;
					} else {
						istrue = false;
						break;
					}
				}
			}	
			if(istrue == true) {
				count += 1;
			}
			
		}
		
		System.out.println(count);
	}

}
