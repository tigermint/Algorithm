import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        final Map<String, Integer> treeMap = new HashMap<>();

        int total = 0;
        String tree;
        while (true) {
            tree = bf.readLine();
            if(tree == null || tree.isEmpty()) break;
            total += 1;
            treeMap.put(tree, treeMap.getOrDefault(tree, 0) + 1);
        }

        final String[] keys = treeMap.keySet().toArray(new String[0]);
        Arrays.sort(keys);

        for (String key : keys) {
            System.out.println(key + " " +String.format("%.4f", (double) treeMap.get(key) * 100 / total));
        }

    }
}