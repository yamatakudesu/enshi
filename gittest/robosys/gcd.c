/*gcd.c*/
#include <stdio.h>

int g_c_d(int x, int y) {
  if (x > y) {
    x = x - y;  //x>yならxにx-yを代入し,gcd関数を再び行う
    g_c_d(x, y);
  } else if (x < y) { 
    y = y - x;  //x<yならyにy-xを代入し,gcd関数を再び行う
    g_c_d(x, y);
  } else {
    return x;  //x=yなら値xを返す
  }
}


int main(void) {
  int x, y;
  scanf("%d %d", &x, &y); //"整数 整数"で入力しx,yそれぞれに代入

  int gcd = g_c_d(x, y); //最大公約数をgcdに代入
  printf("g_c_d(x,y) = %d\n", gcd); //結果を表示
  
  return 0;
}
