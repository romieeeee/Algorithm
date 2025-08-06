import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int[][] map;
	static boolean [][] visited;
	static int n;
	static boolean canwin = false;
	
	static void dfs(int r, int c) {
		// 1.종료 조건
		if(canwin == true) return;
		
		if(r < 0 || c < 0 || r >= n || c >= n) return;
		
		if(visited[r][c] == true) return;
		
		visited[r][c] = true;
		
		int jump = map[r][c];
		
		if(map[r][c] == -1) {
			canwin = true;
		}
		
		dfs(r + jump, c);
		dfs(r, c + jump);
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		n = Integer.parseInt(br.readLine());
		map = new int[n][n];
		visited = new boolean[n][n];
		
		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
			
		}
		
		dfs(0,0);
		
		System.out.println(canwin ? "HaruHaru" : "Hing");
		
	}

}
