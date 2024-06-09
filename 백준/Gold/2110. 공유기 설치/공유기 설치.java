import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    // 집 N개가 수직선 위 존재
    // 각 집 좌표 X1 ~ XN, 같은 좌표 가지는 일 없음
    // 최대한 많은 곳에 와이파이 사용하려, 인접 공유기 사이 거리 가능한 크게
    // C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로

    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        final int N = Integer.parseInt(st.nextToken());
        final int C = Integer.parseInt(st.nextToken());

        final int[] houses = new int[N];
        for (int i = 0; i < N; i++) {
            houses[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(houses);

        int start = 1;
        int end = houses[houses.length - 1] - houses[0]; // 최대거리
        int maxDistance = 0;

        while (start <= end) {
            int mid = (start + end) / 2;

            if (canPlaceRouters(houses, mid, C)) {
                maxDistance = mid;
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }

        System.out.println(maxDistance);
    }

    private static boolean canPlaceRouters(final int[] houses, final int distance, final int routers) {
        int count = 1; // 첫 번째 공유기를 첫 번째 집에 설치
        int lastLocation = houses[0];

        for (int i = 1; i < houses.length; i++) {
            if (houses[i] - lastLocation >= distance) {
                count++;
                lastLocation = houses[i];
                if (count >= routers) {
                    return true;
                }
            }
        }
        return false;
    }

}
