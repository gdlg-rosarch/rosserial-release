# Script generated with Bloom
pkgdesc="ROS - A specialized harness which allows end-to-end integration testing of the rosserial client and server components."


pkgname='ros-lunar-rosserial-test'
pkgver='0.7.7_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('gtest'
'ros-lunar-catkin'
'ros-lunar-roscpp'
'ros-lunar-rosserial-client'
'ros-lunar-rosserial-msgs'
'ros-lunar-rosserial-python'
'ros-lunar-rosserial-server'
'ros-lunar-rostest'
'ros-lunar-std-msgs'
)

depends=('gtest'
'ros-lunar-roscpp'
'ros-lunar-rosserial-client'
'ros-lunar-rosserial-msgs'
'ros-lunar-rosserial-python'
'ros-lunar-rosserial-server'
'ros-lunar-rostest'
'ros-lunar-std-msgs'
)

conflicts=()
replaces=()

_dir=rosserial_test
source=()
md5sums=()

prepare() {
    cp -R $startdir/rosserial_test $srcdir/rosserial_test
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

