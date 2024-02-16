# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-zope.interface
Epoch: 100
Version: 6.4.post1
Release: 1%{?dist}
Summary: Interfaces for Python
License: ZPL-2.1
URL: https://github.com/zopefoundation/zope.interface/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-Cython3
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
This package provides an implementation of “object interfaces” for
Python. Interfaces are a mechanism for labeling objects as conforming to
a given API or contract. So, this package can be considered as
implementation of the Design By Contract methodology support in Python.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-zope.interface
Summary: Interfaces for Python
Requires: python3
Provides: python3-zope.interface = %{epoch}:%{version}-%{release}
Provides: python3dist(zope.interface) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-zope.interface = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(zope.interface) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-zope.interface = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(zope.interface) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-zope.interface
This package provides an implementation of “object interfaces” for
Python. Interfaces are a mechanism for labeling objects as conforming to
a given API or contract. So, this package can be considered as
implementation of the Design By Contract methodology support in Python.

%files -n python%{python3_version_nodots}-zope.interface
%license LICENSE.txt
%{python3_sitearch}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-zope.interface
Summary: Interfaces for Python
Requires: python3
Provides: python3-zope.interface = %{epoch}:%{version}-%{release}
Provides: python3dist(zope.interface) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-zope.interface = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(zope.interface) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-zope.interface = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(zope.interface) = %{epoch}:%{version}-%{release}

%description -n python3-zope.interface
This package provides an implementation of “object interfaces” for
Python. Interfaces are a mechanism for labeling objects as conforming to
a given API or contract. So, this package can be considered as
implementation of the Design By Contract methodology support in Python.

%files -n python3-zope.interface
%license LICENSE.txt
%{python3_sitearch}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-zope.interface
Summary: Interfaces for Python
Requires: python3
Provides: python3-zope.interface = %{epoch}:%{version}-%{release}
Provides: python3dist(zope.interface) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-zope.interface = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(zope.interface) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-zope.interface = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(zope.interface) = %{epoch}:%{version}-%{release}

%description -n python3-zope.interface
This package provides an implementation of “object interfaces” for
Python. Interfaces are a mechanism for labeling objects as conforming to
a given API or contract. So, this package can be considered as
implementation of the Design By Contract methodology support in Python.

%files -n python3-zope.interface
%license LICENSE.txt
%{python3_sitearch}/*
%endif

%changelog
