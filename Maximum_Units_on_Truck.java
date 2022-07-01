class Solution {
    public int maximumUnits(int[][] boxTypes, int truckSize) {
        int res = 0;
        Arrays.sort(boxTypes, (a, b) -> b[1] - a[1]);
        for (int[] arr : boxTypes) {
            if (truckSize >= arr[0]) {
                res += arr[0] * arr[1];
                truckSize -= arr[0];
            } else {
                res += truckSize * arr[1];
                break;
            }
        }
        return res;
    }
}
