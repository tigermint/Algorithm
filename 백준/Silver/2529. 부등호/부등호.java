import java.util.*;

public class Main {
    private static int k;
    private static String[] inequalitySigns;
    private static boolean[] nums = new boolean[10];
    private static String minNum = "9999999999";
    private static String maxNum = "0";

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        k = scanner.nextInt();
        scanner.nextLine(); // 개행 문자 제거
        inequalitySigns = scanner.nextLine().split(" ");

        for (int i = 0; i < 10; i++) {
            nums[i] = true;
        }

        dfs(new ArrayList<>(), 0);
        System.out.println(maxNum);
        System.out.println(minNum);
    }

    static void dfs(List<Integer> num, int index) {
        // 종료 조건
        if (num.size() == k + 1) {
            String numStr = num.stream().map(String::valueOf).reduce("", String::concat);
            minNum = minNum.compareTo(numStr) < 0 ? minNum : numStr;
            maxNum = maxNum.compareTo(numStr) > 0 ? maxNum : numStr;
            return;
        }

        // 실행 조건
        for (int i = 0; i < 10; i++) {
            if (nums[i] && promising(index - 1, num.isEmpty() ? null : num.get(num.size() - 1), i)) {
                nums[i] = false;
                num.add(i);
                dfs(num, index + 1);
                num.remove(num.size() - 1);
                nums[i] = true;
            }
        }
    }

    static boolean promising(int index, Integer x, int y) {
        if (x == null || index < 0) {
            return true;
        }
        if (inequalitySigns[index].equals("<")) {
            return x < y;
        } else if (inequalitySigns[index].equals(">")) {
            return x > y;
        }
        return false;
    }
}