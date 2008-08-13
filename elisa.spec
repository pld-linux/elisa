Summary:	Media center
Summary(pl.UTF-8):	Centrum multimedialne
Name:		elisa
Version:	0.5.5
Release:	0.1
License:	GPL v3
Group:		Applications/Multimedia
Source0:	http://elisa.fluendo.com/static/download/elisa/%{name}-%{version}.tar.gz
# Source0-md5:	f5b0c69f9aa6348664c0ffc1d177b672
#Patch0:		%{name}-no-source-files.patch
URL:		http://www.fluendo.com/elisa/
BuildRequires:	python-TwistedCore >= 2.2
BuildRequires:	python-gstreamer >= 0.10.9
BuildRequires:	python-setuptools
Requires:	pigment >= 0.1.5
Requires:	pigment-python >= 0.3.5
Requires:	python-TwistedCore >= 2.2
Requires:	python-TwistedWeb
Requires:	python-cssutils
Requires:	python-pygobject
Requires:	python-gstreamer >= 0.10.9
Suggests:	elisa-plugins-good
Suggests:	elisa-plugins-bad
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Elisa is a project to create an open source cross platform media
center solution.

%description -l pl.UTF-8
Elisa jest projektem stworzenia wieloplatformowego centrum
multimedialnego o otwartych źródłach.

%prep
%setup -q
#%patch0 -p1

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}/%{name}/plugins

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# COPYING contains just some notes, LICENSE.GPL includes excemption clause 
%doc AUTHORS COPYING FAQ* LICENSE.* NEWS README FIRST_RUN
%attr(755,root,root) %{_bindir}/elisa*
%{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/%{name}*.egg-info
%{py_sitescriptdir}/%{name}_*.pyc
%{py_sitescriptdir}/%{name}*.pth
%{_desktopdir}/%{name}.desktop
%{_desktopdir}/%{name}-mobile.desktop
%{_pixmapsdir}/%{name}.png
%{_datadir}/dbus-1/services/com.fluendo.elisa.service
%{_mandir}/man1/%{name}*
