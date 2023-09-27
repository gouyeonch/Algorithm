
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static ArrayList<Integer>[] A;
    static boolean visited[];

    public static void main(String[] args) throws IOException {
        //입력 잘 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken()); //노드 개수
        int e = Integer.parseInt(st.nextToken()); //에지 개수
        int s = Integer.parseInt(st.nextToken());

        //만들꺼 2가지 1. 방문 리스트, 2. 인접 리스트, 3. 호출 스택
        A = new ArrayList[n + 1];
        for (int i = 1; i < n + 1; i++) {
            A[i] = new ArrayList<Integer>();
        }

        visited = new boolean[n + 1];

        for (int i = 0; i < e; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            A[u].add(v);
            A[v].add(u);
        }
        for (int i = 1; i < n + 1; i++) {
            Collections.sort(A[i]);
        }

        int count = 0;
        visited = new boolean[n + 1];
        dfs(s);
        System.out.println();

        visited = new boolean[n + 1];
        bfs(s);
        System.out.println();

        //호출 스택에 첫번째꺼 넣기

        //노드 개수 만큼 방문한 적 없으면 노드 다 돌기
        //노드 돌때는 dfs 함수를 통해 재귀호출 진행

    }

    static void dfs(int e) {
        System.out.print(e + " ");
        visited[e] = true;
        for (int i : A[e]) {
            if (!visited[i]) {
                dfs(i);
            }
        }
    }

    static void bfs(int e) {
        Queue<Integer> queue = new LinkedList<Integer>();
        queue.add(e);
        visited[e] = true;

        while (!queue.isEmpty()) {
            int now = queue.poll();
            System.out.print(now + " ");
            for(int i : A[now]){
                if(!visited[i]) {
                    visited[i] = true;
                    queue.add(i);
                }
            }
        }
    }
}
