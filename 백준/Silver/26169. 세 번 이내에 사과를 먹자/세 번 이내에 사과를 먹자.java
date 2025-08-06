import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int[][] map;
	static boolean [][] visit;
	static boolean isposs = false;
	static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};
	
	static void dfs(int r, int c, int movecount, int applecount) {
		
		if (movecount >3) return;
		if (applecount >= 2) {
			isposs = true;
			return;
		}
		
		visit[r][c] = true;
		
		for(int dir = 0; dir < 4; dir++) {
			int nr = r + dr[dir];
			int nc = c + dc[dir];
			
			if(nr < 0 || nc < 0 || nr >= 5 || nc >= 5) continue;
			if(visit[nr][nc]) continue;
			if(map[nr][nc] == -1) continue;
			
			int original = map[nr][nc];
			dfs(nr, nc, movecount + 1, applecount + (original == 1 ? 1 : 0));
		}
		
		visit[r][c] = false;
		
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		map = new int[5][5];
		visit = new boolean[5][5];
		
		for (int i = 0; i < 5; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 5; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		StringTokenizer position = new StringTokenizer(br.readLine());
		
		int sr = Integer.parseInt(position.nextToken());
		int sc = Integer.parseInt(position.nextToken());
		
		dfs(sr, sc, 0, map[sr][sc] == 1 ? 1 :0);
		
		 System.out.println(isposs? 1 : 0);
		
	}

}
