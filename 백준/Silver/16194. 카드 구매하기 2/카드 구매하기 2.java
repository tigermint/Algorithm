import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(bf.readLine());
        int[] P = new int[N + 1];

        StringTokenizer st = new StringTokenizer(bf.readLine());
        for (int i = 1; i <= N; i++) {
            P[i] = Integer.parseInt(st.nextToken());
        }

        int[] dp = new int[N + 1];

        for (int i = 1; i <= N; i++) {
            dp[i] = P[i]; // 기본값: i개의 카드가 든 팩을 사는 비용
            for (int j = 1; j < i; j++) {
                dp[i] = Math.min(dp[i], dp[i - j] + P[j]);
            }
        }

        System.out.println(dp[N]);
    }
}
