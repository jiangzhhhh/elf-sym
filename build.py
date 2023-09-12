import subprocess as sp
import os

NDK = '/Users/jiangzh/android/ndk/android-ndk-r21e'
toolchain = NDK + '/toolchains/llvm/prebuilt/darwin-x86_64/bin/aarch64-linux-android21-clang++'
make = NDK + '/prebuilt/darwin-x86_64/bin/make'
cmd = f'''cmake .. -DCMAKE_TOOLCHAIN_FILE="{NDK}/build/cmake/android.toolchain.cmake" \
-DANDROID_ABI="arm64-v8a" \
-DANDROID_PLATFORM=android-21 \
-DANDROID_STL=c++_static \
-DCMAKE_ANDROID_NDK_TOOLCHAIN_VERSION=clang \
-DCMAKE_MAKE_PROGRAM="{make}" \
&& cmake --build . --target all\
'''
os.chdir('build')
sp.call(cmd, shell=True)

print(sp.call('nm -C libfoo.so | grep " [TtwW] "', shell=True))