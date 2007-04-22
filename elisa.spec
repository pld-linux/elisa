Summary:	Media center
Summary(pl.UTF-8):	Centrum multimedialne
Name:		elisa
Version:	0.1.5
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://elisa.fluendo.com/static/download/elisa/%{name}-%{version}.tar.gz
# Source0-md5:	988807e75a27c756f92b29d8c10daeb5
URL:		http://www.fluendo.com/elisa/
BuildRequires:	python-setuptools
BuildRequires:	python-TwistedCore
Requires:	pigment >= 0.1.5
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
