#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void solve() {
    int n;
    cin >> n;
    
    // 1-based indexing for easier mapping with the problem description
    vector<long long> a(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }
    
    vector<long long> dp(n + 1, -1e18);
    dp[1] = 0; // Starting at index 1 with balance 0
    
    long long max_balance = 0; // Minimum possible maximum balance is 0 (0 jumps)
    
    for (int j = 2; j <= n; ++j) {
        for (int i = 1; i < j; ++i) {
            long long gain = a[j] - j + i;
            dp[j] = max(dp[j], dp[i] + gain);
        }
        max_balance = max(max_balance, dp[j]);
    }
    
    cout << max_balance << "\n";
}

int main() {
    // Fast I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    
    return 0;
}
