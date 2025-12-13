%define oname ytmusicapi

Name:		python-ytmusicapi
Version:	1.11.3
Release:	1
Summary:	Unofficial API for YouTube Music
Group:		Development/Python
License:	MIT
URL:		https://github.com/sigma67/ytmusicapi
Source0:	https://files.pythonhosted.org/packages/source/y/%{oname}/%{oname}-%{version}.tar.gz
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(requests)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildArch:	noarch

%description
ytmusicapi is a Python 3 library to send requests to the YouTube Music API.
It emulates YouTube Music web client requests using the user's cookie data for
authentication.

%prep
%autosetup -p1 -n %{oname}-%{version}
# Remove bundled egg-info
rm -rf %{oname}.egg-info

%build
%py_build

%install
%py_install

%files
%{_bindir}/%{oname}
%{python_sitelib}/%{oname}
%{python_sitelib}/%{oname}-%{version}.dist-info
