%define module	parso

Name:		python-%{module}
Version:	0.8.2
Release:	%mkrel 3
Summary:	A Python Parser
Group:		Development/Python
License:	MIT
URL:		https://github.com/davidhalter/parso
Source0:	%{pypi_source %{module}}
BuildArch:	noarch

%description
Parso is a Python parser that supports error recovery and round-trip
parsing for different Python versions (in multiple Python versions).
Parso is also able to list multiple syntax errors in your python file.

Parso has been battle-tested by jedi. It was pulled out of jedi to be
useful for other projects as well.

Parso consists of a small API to parse Python and analyse the syntax
tree.

%package -n	python3-%{module}
Summary:	A Python 3 Parser
Group:		Development/Python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(setuptools)
%{?python_provide:%python_provide python3-%{module}}

%description -n	python3-%{module}
Parso is a Python 3 parser that supports error recovery and round-trip
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
%py3_build

%install
%py3_install

%files -n python3-%{module}
%doc CHANGELOG.rst README.rst
%license LICENSE.txt
%{python3_sitelib}/%{module}
%{python3_sitelib}/%{module}-%{version}-py%{python3_version}.egg-info
