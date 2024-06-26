
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {

    static int[] parent;
    static int[][] graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            final int m = Integer.parseInt(st.nextToken()); // 노드
            final int n = Integer.parseInt(st.nextToken()); // 간선

            if (m == 0 && n == 0) break;

            // 간선 초기화
            graph = new int[n][3];
            int totalPrice = 0;

            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                graph[i][0] = Integer.parseInt(st.nextToken());
                graph[i][1] = Integer.parseInt(st.nextToken());
                graph[i][2] = Integer.parseInt(st.nextToken());
                totalPrice += graph[i][2];
            }

            // 간선 정렬
            Arrays.sort(graph, Comparator.comparingInt(node -> node[2]));

            // Union-Find 용 parent 초기화
            parent = new int[m];
            for (int i = 0; i < m; i++) {
                parent[i] = i;
            }

            int minPrice = 0;
            for (int i = 0; i < n; i++) {
                // 간선 선택
                if (find(graph[i][0]) != find(graph[i][1])) {
                    union(graph[i][0], graph[i][1]);
                    minPrice += graph[i][2];
                }
            }
            System.out.println(totalPrice - minPrice);
        }
    }

    private static void union(final int nodeA, final int nodeB) {
        final int rootA = find(nodeA);
        final int rootB = find(nodeB);
        if (rootA != rootB) {
            if (rootA < rootB) {
                parent[rootB] = rootA;
            } else {
                parent[rootA] = rootB;
            }
        }
    }

    private static int find(final int node) {
        if (parent[node] != node) {
            parent[node] = find(parent[node]); // 경로 압축
        }
        return parent[node];
    }
}
