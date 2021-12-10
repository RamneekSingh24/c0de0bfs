#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

// @End Preprocessor //

using namespace  std;



int  main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t; cin >> t;
    while(t--) {
        int n; cin >> n;
        long long sum = 0;
        for (int i = 0; i < n; i++) {
            int x; cin >> x;
            sum += x;
        }
        if (sum > n) {
            cout << sum - n << endl;
        } else if (sum < n) {
            cout << 1 << endl;
        } else {
            cout << 0 << endl;
        }

    }
    return 0;
}