#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-websockets
Version  : 11.0.2
Release  : 14
URL      : https://files.pythonhosted.org/packages/9d/67/68e568bb4a0617529db2723c75958223b70b95921cd114b5fd13567db4d8/websockets-11.0.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/9d/67/68e568bb4a0617529db2723c75958223b70b95921cd114b5fd13567db4d8/websockets-11.0.2.tar.gz
Summary  : An implementation of the WebSocket Protocol (RFC 6455 & 7692)
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-websockets-filemap = %{version}-%{release}
Requires: pypi-websockets-lib = %{version}-%{release}
Requires: pypi-websockets-license = %{version}-%{release}
Requires: pypi-websockets-python = %{version}-%{release}
Requires: pypi-websockets-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
.. image:: logo/horizontal.svg
:width: 480px
:alt: websockets
|licence| |version| |pyversions| |tests| |docs| |openssf|

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
%setup -q -n websockets-11.0.2
cd %{_builddir}/websockets-11.0.2
pushd ..
cp -a websockets-11.0.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1681833316
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-websockets
cp %{_builddir}/websockets-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-websockets/170ef1f638721e2626a4c067bb1841f3001b9651 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
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
/usr/share/package-licenses/pypi-websockets/170ef1f638721e2626a4c067bb1841f3001b9651

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
