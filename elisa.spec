Summary:	Media center
Summary(pl.UTF-8):	Centrum multimedialne
Name:		elisa
Version:	0.1.4.2
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://www.fluendo.com/elisa/downloads/elisa/%{name}-%{version}.tar.gz
# Source0-md5:	fe9bfb723c8565e62ebf4d2e21588aab
URL:		http://www.fluendo.com/elisa/
BuildRequires:	python-setuptools
BuildRequires:	python-Twisted
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Elisa is a project to create an open source cross platform media
center solution.

%description -l pl.UTF-8
Elisa jest projektem stworzenia wieloplatformowego centrum
multimedialnego o otwartych źródłach.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags}" \
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/%{name}-%{version}*
