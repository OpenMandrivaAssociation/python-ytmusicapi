Name:		python-ytmusicapi
Version:	0.20.0
Release:	1
Summary:	Unofficial API for YouTube Music
Group:		Development/Python
License:	MIT
URL:		https://github.com/sigma67/ytmusicapi
Source0:	https://github.com/sigma67/ytmusicapi/archive/refs/tags/%{version}.tar.gz
BuildRequires:	python-devel
BuildRequires:	python-pip
BuildArch:	noarch

%description
ytmusicapi is a Python 3 library to send requests to the YouTube Music API.
It emulates YouTube Music web client requests using the user's cookie data for
authentication.

%prep
%autosetup -p1 -n ytmusicapi-%{version}

%build
python setup.py build

%install
python setup.py install --skip-build --root %{buildroot}

%files
%{python_sitelib}/ytmusicapi
%{python_sitelib}/ytmusicapi*.egg-info
