# Script generated with Bloom
pkgdesc="ROS - A more performance- and stability-oriented server alternative implemented in C++ to rosserial_python."


pkgname='ros-lunar-rosserial-server'
pkgver='0.7.7_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-lunar-catkin'
'ros-lunar-roscpp'
'ros-lunar-rosserial-msgs'
'ros-lunar-std-msgs'
'ros-lunar-topic-tools'
)

depends=('ros-lunar-roscpp'
'ros-lunar-rosserial-msgs'
'ros-lunar-rosserial-python'
'ros-lunar-std-msgs'
'ros-lunar-topic-tools'
)

conflicts=()
replaces=()

_dir=rosserial_server
source=()
md5sums=()

prepare() {
    cp -R $startdir/rosserial_server $srcdir/rosserial_server
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

