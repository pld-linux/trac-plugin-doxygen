%define		trac_ver	0.11
%define		plugin		doxygen
Summary:	Integrates doxygen documentation into Trac
Name:		trac-plugin-%{plugin}
Version:	0.11.0.2
Release:	1
License:	BSD-like
Group:		Applications/WWW
Source0:	http://trac-hacks.org/changeset/latest/doxygenplugin/0.11?old_path=/&filename=doxygenplugin/0.11&format=zip&/%{plugin}.zip
# Source0-md5:	2e009d081920b2ec80e43cbdd2d7b138
URL:		http://trac-hacks.org/wiki/DoxygenPlugin
BuildRequires:	python-devel
BuildRequires:	python-distribute
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	unzip
Requires:	trac >= %{trac_ver}.7-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The aim is to embed one or multiple doxygen-generated documentation(s)
within Trac, in order to have consistent look and feel, and easy
referencing to doxygen pages using the usual TracLinks and the
doxygen: prefix.

%prep
%setup -q -n %{plugin}plugin

%build
cd %{trac_ver}
%{__python} setup.py build
%{__python} setup.py egg_info

%install
rm -rf $RPM_BUILD_ROOT
cd %{trac_ver}
%{__python} setup.py install \
	--single-version-externally-managed \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post
trac-enableplugin doxygentrac.doxygentrac.doxygenplugin

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/doxygentrac
%{py_sitescriptdir}/TracDoxygen-*.egg-info
