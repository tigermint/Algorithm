import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        final int T = Integer.parseInt(bf.readLine());

        for (int i = 0; i < T; i++) {
            final int K = Integer.parseInt(bf.readLine());
            long result = 0;
            PriorityQueue<Long> pq = new PriorityQueue<>();

            StringTokenizer st = new StringTokenizer(bf.readLine());
            for (int j = 0; j < K; j++) {
                pq.offer(Long.parseLong(st.nextToken()));
            }

            while (pq.size() > 1) {
                final long sum = pq.poll() + pq.poll();
                result += sum;
                pq.offer(sum);
            }

            System.out.println(result);
        }
    }
}
