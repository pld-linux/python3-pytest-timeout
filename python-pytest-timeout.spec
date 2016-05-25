#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	pytest-timeout
Summary:	Pytest plugin which will terminate tests after a certain timeout
Summary(pl.UTF-8):	Wtyczka Pytest wymuszająca zakończenie testów po przekroczeniu limitu czasu
Name:		python-%{module}
Version:	1.0.0
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/cf/92/ab29b9baa54d47dfd50e43be35577de9af4e7ebf27d29f546ddeb6c3b6f5/pytest-timeout-%{version}.tar.gz
# Source0-md5:	f9f162bd079689980b5614673ddfdae4
URL:		http://bitbucket.org/pytest-dev/pytest-timeout/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-pytest
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-pytest
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pytest plugin which will terminate tests after a certain timeout When
doing so it will show a stack dump of all threads running at the time.

%description -l pl.UTF-8
Wtyczka Pytest wymuszająca zakończenie testów po przekroczeniu limitu
czasu Przy przekroczeniu pokaże zrzut stosu wszystkich wątków
biegnących w tym czasie

%package -n python3-%{module}
Summary:	Pytest plugin which will terminate tests after a certain timeout
Summary(pl.UTF-8):	Wtyczka Pytest wymuszająca zakończenie testów po przekroczeniu limitu czasu
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
Pytest plugin which will terminate tests after a certain timeout When
doing so it will show a stack dump of all threads running at the time.

%description -n python3-%{module} -l pl.UTF-8
Wtyczka Pytest wymuszająca zakończenie testów po przekroczeniu limitu
czasu Przy przekroczeniu pokaże zrzut stosu wszystkich wątków
biegnących w tym czasie

%package apidocs
Summary:	%{module} API documentation
Summary(pl.UTF-8):	Dokumentacja API %{module}
Group:		Documentation

%description apidocs
API documentation for %{module}.

%description apidocs -l pl.UTF-8
Dokumentacja API %{module}.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
cd docs
%{__make} -j1 html
rm -rf _build/html/_sources
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
%doc README
%{py_sitescriptdir}/pytest_timeout.py[co]
%{py_sitescriptdir}/pytest_timeout-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README
%{py3_sitescriptdir}/pytest_timeout.py
%{py3_sitescriptdir}/__pycache__/pytest_timeout.*.pyc
%{py3_sitescriptdir}/pytest_timeout-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/*
%endif
