%define module	parso

Name:		python-%{module}
Version:	0.8.3
Release:	1
Summary:	A Python Parser
Group:		Development/Python
License:	MIT
URL:		https://github.com/davidhalter/parso
Source0:	https://pypi.python.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(setuptools)
%{?python_provide:%python_provide python3-%{module}}

%description
Parso is a Python parser that supports error recovery and round-trip
parsing for different Python versions (in multiple Python versions).
Parso is also able to list multiple syntax errors in your python file.

Parso has been battle-tested by jedi. It was pulled out of jedi to be
useful for other projects as well.

Parso consists of a small API to parse Python and analyse the syntax
tree.

%prep
%setup -q -n %{module}-%{version}

# Remove bundled egg-info
rm -rf %{module}.egg-info

%build
%py_build

%install
%py_install

%files
%doc CHANGELOG.rst README.rst
%license LICENSE.txt
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}-py%{python_version}.egg-info
