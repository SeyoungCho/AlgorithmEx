import java.io.*;

class ImageCompression {
    static void printArr(int[][] arr){
        for (int i = 0; i < arr.length; i++){
            for (int j = 0; j < arr.length; j++){
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
    }
    static void dfs(int[][] arr){
        if (checkSame(arr)) {
            System.out.print(arr[0][0]);
            return ;
        }else{
            System.out.print("(");
            dfs(extractArr(arr, 1));
            dfs(extractArr(arr, 2));
            dfs(extractArr(arr, 3));
            dfs(extractArr(arr, 4));
            System.out.print(")");
        }
    }
    static boolean checkSame(int[][] arr){
        int first = arr[0][0];
        for (int i = 0; i < arr.length; i++){
            for (int j = 0; j < arr.length; j++){
                if (arr[i][j] != first)
                    return false;
            }
        }
        return true;
    }
    static int[][] extractArr(int[][] arr, int n){
        int len = arr.length;
        int[][] ret = new int[len/2][len/2];
        int i, j;
        int row = 0, col = 0;
        switch(n){
            case 1:
                row = 0;
                col = 0;
                break;
            case 2:
                row = 0;
                col = len / 2;
                break;
            case 3:
                row = len / 2;
                col = 0;
                break;
            case 4:
                row = len / 2;
                col = len / 2;
                break;
            default:
                break;
        }
        for (i = 0; i < len / 2; i++){
            for (j = 0; j < len / 2; j++){
                ret[i][j] = arr[i+row][j+col];
            }
        }
        return ret;
    }
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[][] arr = new int[n][n];
        String[] st;
        for (int i = 0; i < n; i++){
            st = br.readLine().split("");
            for (int j = 0; j < n; j++){
                int num = Integer.parseInt(st[j]);
                arr[i][j] = num;
            }
        }
        dfs(arr);
    }
}