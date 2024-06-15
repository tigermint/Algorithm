import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        final int N = Integer.parseInt(st.nextToken());
        final int M = Integer.parseInt(st.nextToken());

        // 인접 리스트 초기화
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(bf.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            graph.get(u).add(v);
            graph.get(v).add(u);
        }

        boolean[] visited = new boolean[N + 1];
        int components = 0;
        int extraEdges = 0;

        // DFS를 통해 컴포넌트 수를 계산
        for (int i = 1; i <= N; i++) {
            if (!visited[i]) {
                extraEdges += dfs(graph, visited, i, -1);
                components++;
            }
        }

        // 필요한 최소 연산 횟수는 (컴포넌트 수 - 1) + 초과 간선 수
        int neededEdges = (components - 1) + (extraEdges / 2);
        System.out.println(neededEdges);
    }

    // DFS 구현
    public static int dfs(List<List<Integer>> graph, boolean[] visited, int node, int parent) {
        visited[node] = true;
        int edges = 0;

        for (int neighbor : graph.get(node)) {
            if (neighbor != parent) {
                if (!visited[neighbor]) {
                    edges += dfs(graph, visited, neighbor, node);
                } else {
                    edges++; // 발견된 간선이 이미 방문된 노드로 연결되어 있으면 초과 간선
                }
            }
        }

        return edges;
    }
}
