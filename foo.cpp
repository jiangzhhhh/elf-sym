#include "bar.h"

int a() { return 0; }
inline int b() { return 0; }
__attribute__((visibility("default"))) extern "C" int c() { return 0; }
__attribute__((visibility("default"))) extern "C" int foo() {
  bar();
  b();
  c();
  return a();
}