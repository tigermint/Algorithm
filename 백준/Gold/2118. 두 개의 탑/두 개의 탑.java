import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final int N = Integer.parseInt(br.readLine());

        final int[] distances = new int[N];
        int totalDistance = 0;

        for (int i = 0; i < N; i++) {
            distances[i] = Integer.parseInt(br.readLine());
            totalDistance += distances[i];
        }

        int maxDistance = 0;
        int currentDistance = 0;
        int start = 0;
        int end = 0;

        while (start < N) {
            while (end < start + N && currentDistance < totalDistance / 2) {
                currentDistance += distances[end % N];
                end++;
            }

            maxDistance = Math.max(maxDistance, Math.min(currentDistance, totalDistance - currentDistance));
            currentDistance -= distances[start % N];
            start++;
        }

        System.out.println(maxDistance);
    }
}
