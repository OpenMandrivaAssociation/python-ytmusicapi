Name:		python-ytmusicapi
Version:	1.2.1
Release:	2
Summary:	Unofficial API for YouTube Music
Group:		Development/Python
License:	MIT
URL:		https://github.com/sigma67/ytmusicapi
Source0:	https://files.pythonhosted.org/packages/source/y/ytmusicapi/ytmusicapi-%{version}.tar.gz
BuildRequires:	python-devel
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildArch:	noarch

%description
ytmusicapi is a Python 3 library to send requests to the YouTube Music API.
It emulates YouTube Music web client requests using the user's cookie data for
authentication.

%prep
%autosetup -p1 -n ytmusicapi-%{version}

%build
%py_build

%install
%py_install

%files
%{_bindir}/ytmusicapi
%{python_sitelib}/ytmusicapi
%{python_sitelib}/ytmusicapi*.*-info
