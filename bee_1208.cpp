#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> graph;
vector<bool> visited;

void dfs(int v, vector<int>& current_chain) {
    visited[v] = true;
    current_chain.push_back(v);

    for (int u : graph[v]) {
        if (!visited[u]) {
            dfs(u, current_chain);
        }
    }
}

int find_min_chains(int n) {
    int result = 0;
    visited.assign(n + 1, false);

    for (int i = 1; i <= n; ++i) {
        if (!visited[i]) {
            vector<int> current_chain;
            dfs(i, current_chain);
            ++result;
        }
    }

    return result;
}

int main() {
    int n, m;

    while (cin >> n >> m) {
        graph.assign(n + 1, vector<int>());
        
        for (int i = 0; i < m; ++i) {
            int pi, fi;
            cin >> pi >> fi;
            graph[fi].push_back(pi);
        }

        int result = find_min_chains(n);
        cout << result << endl;
    }

    return 0;
}