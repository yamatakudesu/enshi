#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <boost/assign/std/vector.hpp>
#include <boost/assign/list_of.hpp>
#include <boost/foreach.hpp>
#include <boost/lambda/bind.hpp>
#include <boost/lambda/lambda.hpp>
#include <boost/range/algorithm.hpp>

#define NUM 20

int main {
  int data[NUM] = {20,62,17,38,76,92,59,11,93,88,79,50,89,67,75,26,83,22,13,48};
  int i;
  std::vector<int> b(data, data+20);
  for(i=0;i<NUM;i++) {
    std::cerr << data[i] << " ";
  }
  return 0;
}
