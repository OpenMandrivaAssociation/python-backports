%global srcname backports
%global srcversion 1.0

Name:           python2-%srcname
Version:        1.1
Release:        1
Summary:        A lightweight derivative of Enthought Traits for configuring Python objects
Group:          Development/Python
License:        BSD
URL:            https://pypi.python.org/pypi/backports
Source0:	backports.py

BuildRequires:	python2-setuptools
BuildRequires:	python2-devel

%description
A lightweight pure-Python derivative of Enthought Traits, used for
configuring Python objects.

This package powers the config system of IPython and Jupyter.

%prep

%build

%install
mkdir -pm 755 %{buildroot}%{python2_sitelib}/backports
install -pm 644 %{SOURCE0} %{buildroot}%{python2_sitelib}/backports/__init__.py
%if "%{python2_sitelib}" != "%{python2_sitearch}"
mkdir -pm 755 %{buildroot}%{python2_sitearch}/backports
install -pm 644 %{SOURCE0} %{buildroot}%{python2_sitearch}/backports/__init__.py
%endif

%files
%{python2_sitelib}/backports
%if "%{python2_sitelib}" != "%{python2_sitearch}"
%{python2_sitearch}/backports
%endif
