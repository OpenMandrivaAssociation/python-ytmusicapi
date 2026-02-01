%define oname ytmusicapi

Name:		python-ytmusicapi
Version:	1.11.5
Release:	1
Summary:	Unofficial API for YouTube Music
Group:		Development/Python
License:	MIT
URL:		https://github.com/sigma67/ytmusicapi
Source0:	https://files.pythonhosted.org/packages/source/y/%{oname}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(requests)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)

%description
ytmusicapi is a Python 3 library to send requests to the YouTube Music API.
It emulates YouTube Music web client requests using the user's cookie data for
authentication.

%prep -a
# Remove bundled egg-info
rm -rf %{oname}.egg-info

%files
%{_bindir}/%{oname}
%{python_sitelib}/%{oname}
%{python_sitelib}/%{oname}-%{version}.dist-info
