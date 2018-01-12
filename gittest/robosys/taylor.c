#include <stdio.h>

// テイラー級数の計算を用いて自然対数eを求める
int main() {
  int k, n;
  double sk, ak;

  printf("何項まで計算するか");
  scanf("%d", &n);

  ak = 1.0;
  sk = ak;

  for (k = 1; k <= n; k++) {
    ak = ak / k;
    sk = sk + ak;
    printf("k=%3d, Ak=%e, sk=%20.15e\n", k, ak, sk);
  }
  return 0;  
}
