
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        final int r = Integer.parseInt(st.nextToken()) - 1;
        final int c = Integer.parseInt(st.nextToken()) - 1;
        final int k = Integer.parseInt(st.nextToken());

        List<List<Integer>> list = new ArrayList<>();
        for (int i = 0; i < 3; i++) {
            list.add(new ArrayList<>());
        }

        for (int i = 0; i < 3; i++) {
            st = new StringTokenizer(bf.readLine());
            for (int j = 0; j < 3; j++) {
                list.get(i).add(Integer.parseInt(st.nextToken()));
            }
        }

        int time = 0;
        while (time <= 100) {
            final int row = list.size();
            final int col = list.get(0).size();

            if (r < row && c < col && list.get(r).get(c) == k) {
                System.out.println(time);
                return;
            }

            if (row >= col) { // R 연산
                list = calculate(list);
            } else { // C 연산
                list = trans(list);
                list = calculate(list);
                list = trans(list);
            }
            time++;
        }

        System.out.println(-1);
    }

    private static List<List<Integer>> trans(final List<List<Integer>> list) {
        int row = list.size();
        int col = list.get(0).size();
        List<List<Integer>> transMatrix = new ArrayList<>();
        for (int i = 0; i < col; i++) {
            transMatrix.add(new ArrayList<>());
        }
        for (int i = 0; i < col; i++) {
            for (int j = 0; j < row; j++) {
                transMatrix.get(i).add(list.get(j).get(i));
            }
        }
        return transMatrix;
    }

    private static List<List<Integer>> calculate(final List<List<Integer>> list) {
        int maxSize = 0;
        List<List<Integer>> newList = new ArrayList<>();

        for (int i = 0; i < list.size(); i++) {
            final Map<Integer, Integer> map = new HashMap<>();
            for (int j = 0; j < list.get(i).size(); j++) {
                int value = list.get(i).get(j);
                if (value != 0) { // 0은 무시합니다.
                    map.put(value, map.getOrDefault(value, 0) + 1);
                }
            }

            final List<Map.Entry<Integer, Integer>> entries = new ArrayList<>(map.entrySet());
            entries.sort(
                    Comparator.comparing(Map.Entry<Integer, Integer>::getValue)
                            .thenComparing(Map.Entry::getKey)
            );

            final List<Integer> sortedList = new ArrayList<>();
            for (Map.Entry<Integer, Integer> entry : entries) {
                sortedList.add(entry.getKey());
                sortedList.add(entry.getValue());
            }
            maxSize = Math.max(maxSize, sortedList.size());
            newList.add(sortedList);
        }

        for (List<Integer> row : newList) {
            while (row.size() < maxSize) {
                row.add(0);
            }
        }

        // 최대 크기 100 제한
        if (newList.size() > 100) {
            newList = newList.subList(0, 100);
        }
        for (List<Integer> row : newList) {
            if (row.size() > 100) {
                row.subList(100, row.size()).clear();
            }
        }

        return newList;
    }
}
