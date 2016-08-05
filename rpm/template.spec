Name:           ros-jade-rosserial
Version:        0.7.3
Release:        0%{?dist}
Summary:        ROS rosserial package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rosserial
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-jade-rosserial-client
Requires:       ros-jade-rosserial-msgs
Requires:       ros-jade-rosserial-python
BuildRequires:  ros-jade-catkin

%description
Metapackage for core of rosserial.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Fri Aug 05 2016 Paul Bouchier <paul.bouchier@gmail.com> - 0.7.3-0
- Autogenerated by Bloom

* Fri Jul 15 2016 Paul Bouchier <paul.bouchier@gmail.com> - 0.7.2-0
- Autogenerated by Bloom

* Mon Jul 06 2015 Paul Bouchier <paul.bouchier@gmail.com> - 0.7.1-0
- Autogenerated by Bloom

* Thu Apr 23 2015 Paul Bouchier <paul.bouchier@gmail.com> - 0.7.0-0
- Autogenerated by Bloom

