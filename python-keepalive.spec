#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Python 2 HTTP handler for urllib2 that supports HTTP 1.1 and keepalive
Summary(pl.UTF-8):	Klasa Pythona 2 obsługująca HTTP dla urllib2 z obsługą HTTP 1.1 i keepalive
Name:		python-keepalive
Version:	0.5
Release:	2
License:	LGPL v2.1+
Group:		Libraries/Python
#Source0Download: https://github.com/wikier/keepalive/releases
Source0:	https://github.com/wikier/keepalive/archive/%{version}/keepalive-%{version}.tar.gz
# Source0-md5:	493d1c161cec22df7e90cb5d57b98187
URL:		https://github.com/wikier/keepalive
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-2to3 >= 1:3.3
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An HTTP handler for urllib2 that supports HTTP 1.1 and keepalive.

%description -l pl.UTF-8
Klasa obsługująca HTTP dla modułu urllib2 z obsługą HTTP 1.1 oraz
keepalive.

%package -n python3-keepalive
Summary:	Python 3 HTTP handler for urllib2 that supports HTTP 1.1 and keepalive
Summary(pl.UTF-8):	Klasa Pythona 3 obsługująca HTTP dla urllib2 z obsługą HTTP 1.1 i keepalive
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-keepalive
An HTTP handler for urllib2 that supports HTTP 1.1 and keepalive.

%description -n python3-keepalive -l pl.UTF-8
Klasa obsługująca HTTP dla modułu urllib2 z obsługą HTTP 1.1 oraz
keepalive.

%prep
%setup -q -n keepalive-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.md
%{py_sitescriptdir}/keepalive
%{py_sitescriptdir}/keepalive-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-keepalive
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/keepalive
%{py3_sitescriptdir}/keepalive-%{version}-py*.egg-info
%endif
