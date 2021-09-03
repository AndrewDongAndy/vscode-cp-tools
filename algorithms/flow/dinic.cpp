template <typename T>
class FlowGraph {
 public:
  static constexpr T EPS = (T) 1e-9;

  struct Edge {
    int from;
    int to;
    T c;
    T f;
  };

  int n;
  vector<vector<int>> g;
  vector<Edge> edges;
  int source, sink;
  T flow;

  vector<int> ptr; // for ensuring the DFS for sending flow is O(n + m) time
  vector<int> dist;
  vector<int> que;

  explicit FlowGraph(int _n, int _source, int _sink)
      : n(_n), g(n), source(_source), sink(_sink), ptr(n), dist(n) {
    assert(0 <= source && source < n);
    assert(0 <= sink && sink < n);
    assert(source != sink);
    flow = 0;
  }

  void clear_flow() {
    for (Edge& e : edges) {
      e.f = 0;
    }
    flow = 0;
  }

  void add(int from, int to, T forward_cap, T backward_cap) {
    assert(0 <= from && from < n && 0 <= to && to < n);
    g[from].push_back((int) edges.size());
    edges.push_back({from, to, forward_cap, 0});
    g[to].push_back((int) edges.size());
    edges.push_back({to, from, backward_cap, 0});
  }

  bool expath() {
    fill(dist.begin(), dist.end(), -1);
    que.assign(1, source);
    dist[source] = 0;
    for (int b = 0; b < (int) que.size(); b++) {
      int v = que[b];
      for (int id : g[v]) {
        const Edge& e = edges[id];
        if (e.c - e.f > EPS && dist[e.to] == -1) {
          dist[e.to] = dist[v] + 1;
          if (e.to == sink) {
            return true;
          }
          que.push_back(e.to);
        }
      }
    }
    return false;
  }

  T dfs(int v, T w) {
    if (v == sink) {
      return w;
    }
    while (ptr[v] < (int) g[v].size()) {
      int id = g[v][ptr[v]];
      Edge& e = edges[id];
      Edge& back = edges[id ^ 1];
      if (e.c - e.f > EPS && dist[e.to] == dist[v] + 1) {
        T t = dfs(e.to, min(e.c - e.f, w));
        if (t > EPS) {
          e.f += t;
          back.f -= t;
          return t;
        }
      }
      // don't increment the pointer if flow could be sent;
      // only rule out this edge if no more flow can be sent along it
      ++ptr[v];
    }
    return 0;
  }

  T max_flow() {
    while (expath()) {
      fill(ptr.begin(), ptr.end(), 0);
      T big_add = 0;
      while (true) {
        T add = dfs(source, numeric_limits<T>::max());
        if (add <= EPS) {
          break;
        }
        big_add += add;
      }
      // blocking flow found
      if (big_add <= EPS) {
        break;
      }
      flow += big_add;
    }
    return flow;
    // final blocking flow found
  }

  vector<bool> min_cut() {
    max_flow();
    vector<bool> ret(n);
    for (int i = 0; i < n; i++) {
      ret[i] = (dist[i] == -1);
    }
    return ret;
    // returns the partition of each node:
    // 0 - source side; 1 - sink side
  }
};
