#include <iostream>
#include <vector>
#include <algorithm>

#define NUM 20
int data[NUM] = {20,62,17,38,76,92,59,11,93,88,79,50,89,67,75,26,83,22,13,48};

int partition(int a[], int n);
void sort(int a[], int n);
bool compare (int a, int b) { return (a > b) ; }
void output(int i) { std::cerr << i << " " ; }


int main () {
  std::cout << "C++ + std" << std::endl;
  std::for_each(std::begin(data), std::end(data), [](int &i){std::cout << i << " "; });

  std::cout << "\n" << std::endl;  
  
  for(auto i: data) {
    std::cout << i << " ";
  }
  
  std::cout << "\n" << std::endl;
  
  partition(data, NUM);
  std::for_each(std::begin(data), std::end(data), [](int &i){std::cout << i << " "; });

  std::cout << "\n" << std::endl;

  for(auto i: data) {
    std::cout << i << " ";
  }
  
  std::cout << "\n" << std::endl;  
  
  sort(data, NUM);
  std::for_each(std::begin(data), std::end(data), [](int &i){std::cout << i << " "; });
  std::cout << "\n" << std::endl;

  for(auto i: data) {
    std::cout << i << " ";
  }  
  std::cout << "\n" << std::endl;
  return 0;
}

int partition(int a[], int n) {
  int p, i, j, k;
  p = a[0];
  k = 0;
  for(i=0; i<n; i++) {
    if(a[i] < p) {
      a[k] = a[i];
      for(j=i; j>k+1; j--) {
	a[j] = a[j-1];
      }
      a[++k] = p;
    }
  }
  return k;
}

void sort(int a[], int n) {
  int c;
  if(n<=1){
    return;
  }
  c=partition(a,n);
  sort(a,c);
  sort(&a[c+1],n-c-1);
}
