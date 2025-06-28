#
# Conditional build:
%bcond_with	tests	# pytest tests [use ptys, so not on builders]

Summary:	pytest plugin to abort hanging tests
Summary(pl.UTF-8):	Wtyczka pytesta do przerywania zawieszonych testów
Name:		python3-pytest-timeout
Version:	2.4.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-timeout/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-timeout/pytest_timeout-%{version}.tar.gz
# Source0-md5:	dbc9a376438aa779cff375236e505792
URL:		https://github.com/pytest-dev/pytest-timeout
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pexpect
BuildRequires:	python3-pytest >= 7.0.0
BuildRequires:	python3-pytest-cov
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a plugin which will terminate tests after a certain timeout.
When doing so it will show a stack dump of all threads running at the
time. This is useful when running tests under a continuous integration
server or simply if you don't know why the test suite hangs.

%description -l pl.UTF-8
Ta wtyczka przerywa testy po upłynięciu określonego limitu czasu. Przy
tym pokazuje zrzut stosu wszystkich wątków działających w tej chwili.
Jest to przydatne przy uruchamianiu testów na serwerze ciągłej
integracji lub jeśli nie wiemy, dlaczego testy się zawieszają.

%prep
%setup -q -n pytest_timeout-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=pytest_cov.plugin,pytest_timeout \
PYTHONPATH=$(pwd) \
%{__python3} -m pytest
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/pytest_timeout.py
%{py3_sitescriptdir}/__pycache__/pytest_timeout.cpython-*.py[co]
%{py3_sitescriptdir}/pytest_timeout-%{version}-py*.egg-info
