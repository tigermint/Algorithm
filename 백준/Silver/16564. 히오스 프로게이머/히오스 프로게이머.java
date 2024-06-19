
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        final int N = Integer.parseInt(st.nextToken());
        final int K = Integer.parseInt(st.nextToken());

        final int[] levels = new int[N];

        for (int i = 0; i < N; i++) {
            levels[i] = Integer.parseInt(bf.readLine());
        }

        Arrays.sort(levels);
        System.out.println(binarySearch(levels, N, K));
    }

    private static int binarySearch(final int[] levels, final int N, final int K) {
        int start = levels[0];
        int end = levels[N - 1] + K;
        int result = start;

        while (start <= end) {
            int mid = (start + end) / 2;

            if (canAchieveLevel(levels, N, K, mid)) {
                result = mid;  // mid가 가능하면 결과로 저장하고 더 높은 값을 시도
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }

        return result;
    }

    private static boolean canAchieveLevel(final int[] levels, final int N, final int K, int targetLevel) {
        long neededValue = 0;  // 필요 레벨의 총합을 담을 변수 (long 타입 사용)

        for (int i = 0; i < N; i++) {
            if (levels[i] < targetLevel) {
                neededValue += targetLevel - levels[i];
                if (neededValue > K) {  // 중간에 K를 초과하면 false 반환
                    return false;
                }
            }
        }

        return neededValue <= K;
    }
}