#include<iostream>
#include<vector>
using namespace std;

int main(int argc, char** argv)
{
  int N;
  cin >> N;
  vector<int> X(N);
  
  for (int i = 0; i < N; ++i) {
    cin >> X[i];
  }

  int orig = 0;
  for (int i = 1; i < N; ++i) {
    orig += abs(X[i] - X[i - 1]);
  }

  int min_total = 1e9;
  for (int skip = 1; skip < N - 1; ++skip) {
    int temp = 0;
    for (int i = 1; i < N; ++i) {
      if (i == skip) continue;
      if (i - 1 == skip) {
        temp += abs(X[i] - X[i - 2]);
      } else {
        temp += abs(X[i] - X[i - 1]);
      }
    }
    min_total = min(min_total, temp);
  }

  if (N <= 2) {
    cout << orig << endl;
  } else {
    cout << min_total << endl;
  }

  return 0;
}
