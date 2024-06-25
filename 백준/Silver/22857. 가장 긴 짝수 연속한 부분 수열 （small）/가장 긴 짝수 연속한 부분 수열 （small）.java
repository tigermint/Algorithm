
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    // K번

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        final int N = Integer.parseInt(st.nextToken());
        final int K = Integer.parseInt(st.nextToken());

        final int[] S = new int[N];
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            S[i] = Integer.parseInt(st.nextToken());
        }

        int maxLength = 0;
        int left = 0;
        int oddCount = 0;

        for (int right = 0; right < N; right++) {
            if (S[right] % 2 != 0) {
                oddCount++;
            }

            while (oddCount > K) {
                if (S[left] % 2 != 0) {
                    oddCount--;
                }
                left++;
            }

            int evenLength = right - left + 1 - oddCount;
            maxLength = Math.max(maxLength, evenLength);
        }
        System.out.println(maxLength);
    }
}

