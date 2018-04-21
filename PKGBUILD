# Script generated with Bloom
pkgdesc="ROS - A more performance- and stability-oriented server alternative implemented in C++ to rosserial_python."


pkgname='ros-kinetic-rosserial-server'
pkgver='0.7.7_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-roscpp'
'ros-kinetic-rosserial-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-topic-tools'
)

depends=('ros-kinetic-roscpp'
'ros-kinetic-rosserial-msgs'
'ros-kinetic-rosserial-python'
'ros-kinetic-std-msgs'
'ros-kinetic-topic-tools'
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
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
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

