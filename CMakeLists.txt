cmake_minimum_required(VERSION 3.13)
project(reloc C CXX)

add_library(bar STATIC bar.cpp)

add_library(foo SHARED foo.cpp)
target_link_libraries(foo bar)
target_compile_options(foo PRIVATE -fvisibility=hidden) # 设置符号默认可见性是隐藏
target_link_options(foo PRIVATE -Wl,--exclude-libs,ALL) # 链接.a时，不引入.a里的导出符号
target_link_options(foo PRIVATE -Wl,-Bsymbolic) # so内部使用内部导出符号时，不通过plt跳转，直接使用相对偏移