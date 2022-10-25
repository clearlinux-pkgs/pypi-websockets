#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-websockets
Version  : 10.3
Release  : 9
URL      : https://files.pythonhosted.org/packages/f8/a3/622d9acbfb9a71144b5d7609906bc648c62e3ca5fdbb1c8cca222949d82c/websockets-10.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/f8/a3/622d9acbfb9a71144b5d7609906bc648c62e3ca5fdbb1c8cca222949d82c/websockets-10.3.tar.gz
Summary  : An implementation of the WebSocket Protocol (RFC 6455 & 7692)
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-websockets-filemap = %{version}-%{release}
Requires: pypi-websockets-lib = %{version}-%{release}
Requires: pypi-websockets-license = %{version}-%{release}
Requires: pypi-websockets-python = %{version}-%{release}
Requires: pypi-websockets-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
.. image:: logo/horizontal.svg
:width: 480px
:alt: websockets
|licence| |version| |pyversions| |wheel| |tests| |docs|

%package filemap
Summary: filemap components for the pypi-websockets package.
Group: Default

%description filemap
filemap components for the pypi-websockets package.


%package lib
Summary: lib components for the pypi-websockets package.
Group: Libraries
Requires: pypi-websockets-license = %{version}-%{release}
Requires: pypi-websockets-filemap = %{version}-%{release}

%description lib
lib components for the pypi-websockets package.


%package license
Summary: license components for the pypi-websockets package.
Group: Default

%description license
license components for the pypi-websockets package.


%package python
Summary: python components for the pypi-websockets package.
Group: Default
Requires: pypi-websockets-python3 = %{version}-%{release}

%description python
python components for the pypi-websockets package.


%package python3
Summary: python3 components for the pypi-websockets package.
Group: Default
Requires: pypi-websockets-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(websockets)

%description python3
python3 components for the pypi-websockets package.


%prep
%setup -q -n websockets-10.3
cd %{_builddir}/websockets-10.3
pushd ..
cp -a websockets-10.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656361913
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-websockets
cp %{_builddir}/websockets-10.3/LICENSE %{buildroot}/usr/share/package-licenses/pypi-websockets/b61db1cb007caaf9118a9bf274e9a07ed1875d2c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-websockets

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-websockets/b61db1cb007caaf9118a9bf274e9a07ed1875d2c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
