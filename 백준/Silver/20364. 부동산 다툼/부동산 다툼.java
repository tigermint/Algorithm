
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    private static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        final int N = Integer.parseInt(st.nextToken());
        final int Q = Integer.parseInt(st.nextToken());

        visited = new boolean[N + 1];
        Arrays.fill(visited, false);

        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < Q; i++) {
            final int landNum = Integer.parseInt(bf.readLine());
            sb.append(binarySearch(landNum)).append("\n");
        }
        System.out.println(sb);
    }

    private static int binarySearch(final int landNum) {
       int current = landNum;
       int firstOccupied = 0;

        while (current > 0) {
            if (visited[current]) {
                firstOccupied = current;
            }
            current /= 2;
        }

        if (firstOccupied == 0) {
            visited[landNum] = true;
        }
        return firstOccupied;
    }
}