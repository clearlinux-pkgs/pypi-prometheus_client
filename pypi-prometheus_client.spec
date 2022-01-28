#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-prometheus_client
Version  : 0.13.1
Release  : 39
URL      : https://files.pythonhosted.org/packages/a0/e4/af0c31d69c985e83774f5b3ee1b0e28f129a7606e3cfeb3e08b6a1fe8a12/prometheus_client-0.13.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/a0/e4/af0c31d69c985e83774f5b3ee1b0e28f129a7606e3cfeb3e08b6a1fe8a12/prometheus_client-0.13.1.tar.gz
Summary  : Python client for the Prometheus monitoring system.
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-prometheus_client-python = %{version}-%{release}
Requires: pypi-prometheus_client-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
# Prometheus Python Client
The official Python client for [Prometheus](https://prometheus.io).

%package python
Summary: python components for the pypi-prometheus_client package.
Group: Default
Requires: pypi-prometheus_client-python3 = %{version}-%{release}

%description python
python components for the pypi-prometheus_client package.


%package python3
Summary: python3 components for the pypi-prometheus_client package.
Group: Default
Requires: python3-core
Provides: pypi(prometheus_client)

%description python3
python3 components for the pypi-prometheus_client package.


%prep
%setup -q -n prometheus_client-0.13.1
cd %{_builddir}/prometheus_client-0.13.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1643409514
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

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
