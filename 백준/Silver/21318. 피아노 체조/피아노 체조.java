
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        final int N = Integer.parseInt(bf.readLine());
        final int[] difficulties = new int[N];

        final int[] dp = new int[N];
        Arrays.fill(dp, 0);

        StringTokenizer st = new StringTokenizer(bf.readLine());
        for (int i = 0; i < N; i++) {
            difficulties[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 1; i < N; i++) {
            dp[i] += dp[i - 1];
            if (difficulties[i - 1] > difficulties[i]) {
                dp[i]++;
            }
        }

        StringBuffer sb = new StringBuffer();
        final int Q = Integer.parseInt(bf.readLine());
        for (int i = 0; i < Q; i++) {
            st = new StringTokenizer(bf.readLine());
            final int x = Integer.parseInt(st.nextToken());
            final int y = Integer.parseInt(st.nextToken());
            sb.append(dp[y - 1] - dp[x - 1]);
            sb.append("\n");
        }
        System.out.println(sb);
    }
}