# Script generated with Bloom
pkgdesc="ROS - Allows multipoint communication between rosserial nodes connected to an xbee. All nodes communicate back to a master xbee connected to a computer running ROS. This software currently only works with Series 1 Xbees. This pkg includes python code from the python-xbee project: http://code.google.com/p/python-xbee/"
url='http://ros.org/wiki/rosserial_xbee'

pkgname='ros-kinetic-rosserial-xbee'
pkgver='0.7.7_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('python2-pyserial'
'ros-kinetic-diagnostic-msgs'
'ros-kinetic-rospy'
'ros-kinetic-rosserial-msgs'
'ros-kinetic-rosserial-python'
)

conflicts=()
replaces=()

_dir=rosserial_xbee
source=()
md5sums=()

prepare() {
    cp -R $startdir/rosserial_xbee $srcdir/rosserial_xbee
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

