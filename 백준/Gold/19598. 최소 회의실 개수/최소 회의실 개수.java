
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final int N = Integer.parseInt(br.readLine());

        final int[][] times = new int[N][2];
        final PriorityQueue<Integer> pq = new PriorityQueue<>();

        StringTokenizer st;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            times[i][0] = Integer.parseInt(st.nextToken());
            times[i][1] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(times, Comparator.comparingInt(o -> o[0]));

        int maxCount = 0;
        for (int i = 0; i < N; i++) {
            while (!pq.isEmpty()) {
                if (times[i][0] < pq.peek()) {
                    break;
                }
                pq.poll();
            }
            pq.offer(times[i][1]);
            maxCount = Math.max(pq.size(), maxCount);
        }
        System.out.println(maxCount);
    }

}
