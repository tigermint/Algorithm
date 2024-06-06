import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static int maxCount = 0;
    static boolean[] visited;
    static List<Integer>[] graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        final int N = Integer.parseInt(st.nextToken());
        final int M = Integer.parseInt(st.nextToken());

        graph = new ArrayList[N + 1];
        for (int i = 1; i <= N; i++) {
            graph[i] = new ArrayList<>();
        }

        // 인접 리스트 구성
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            graph[u].add(v);
            graph[v].add(u);
        }

        visited = new boolean[N + 1];
        backtracking(1, 0, N);

        // 한 명이라도 세우는 경우를 처리
        if (maxCount < N) maxCount++;

        System.out.println(maxCount);
    }

    private static void backtracking(int current, int count, int n) {
        maxCount = Math.max(maxCount, count);
        if (current > n) return;

        if (visited[current]) {
            backtracking(current + 1, count, n);
        } else {
            visited[current] = true;
            for (int friend : graph[current]) {
                if (!visited[friend]) {
                    visited[friend] = true;
                    backtracking(current + 1, count + 2, n);
                    visited[friend] = false;
                }
            }
            visited[current] = false;
            backtracking(current + 1, count, n);
        }
    }
}
