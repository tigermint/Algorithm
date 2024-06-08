
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    // 단어는 적어도 2글자
    // 1초
    // String Tokenizer로 자르면 됨

    static final List<String> words = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        final int R = Integer.parseInt(st.nextToken());
        final int C = Integer.parseInt(st.nextToken());

        final String[][] puzzle = new String[R][C];

        for (int i = 0; i < R; i++) {
            st = new StringTokenizer(br.readLine());
            puzzle[i] = st.nextToken().split("");
        }


        // 가로
        extractWord(puzzle);

        //회전
        final String[][] rotatedPuzzle = rotate(puzzle);

        // 세로
        extractWord(rotatedPuzzle);

        words.sort(String::compareTo);
        System.out.println(words.get(0));

    }

    private static void extractWord(final String[][] puzzle) {
        for (final String[] strings : puzzle) {
            final String[] splitWords = String.join("", strings).split("#");
            for (String word : splitWords) {
                if (word.length() >= 2) {
                    words.add(word);
                }
            }
        }
    }

    private static String[][] rotate(final String[][] matrix) {

        int n = matrix.length;
        int m = matrix[0].length;
        String[][] rotate = new String[m][n];

        for (int i = 0; i < rotate.length; i++) {
            for (int j = 0; j < rotate[i].length; j++) {
                rotate[i][j] = matrix[j][i];
            }
        }
        return rotate;
    }
}
