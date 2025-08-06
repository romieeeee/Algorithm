import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int[][] map;
	static boolean [][] visited;
	static int[] dr = {1, 0};
	static int[] dc = {0, 1};
	static int w;
	static int h;
	
	static void dfs(int r, int c) {
		if(r < 0 || c < 0 || r >= h || c >= w) return;
		
		if(visited[r][c]) return;
		
		visited[r][c] = true;
		
		for (int i = 0; i < 2; i++) {
			
			int nr = r + dr[i];
			int nc = c + dc[i];
			
			if(nr < 0 || nc < 0 || nr >= h || nc >= w) continue;
			if (map[nr][nc] == 0) continue;
			if (visited[nr][nc]) continue;

			
			dfs(nr,nc);
			
		}
		
	}
			
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		w = Integer.parseInt(st.nextToken());
		h = Integer.parseInt(st.nextToken());
		map = new int[h][w];
		visited = new boolean[h][w];
		
		for (int i = 0; i < h; i++) {
			StringTokenizer s = new StringTokenizer(br.readLine());
			for (int j = 0; j < w; j++) {
				map[i][j] = Integer.parseInt(s.nextToken());
			}
		}
		
		dfs(0,0);
		
		System.out.println(visited[h-1][w-1] == true ? "Yes" : "No");

	}

}
