Summary:	Media center
Summary(pl.UTF-8):	Centrum multimedialne
Name:		elisa
Version:	0.5.31
Release:	1
License:	GPL v3
Group:		Applications/Multimedia
Source0:	http://elisa.fluendo.com/static/download/elisa/%{name}-%{version}.tar.gz
# Source0-md5:	5b4853a015310381cce2998bfc151642
URL:		http://www.fluendo.com/elisa/
BuildRequires:	python-TwistedCore >= 8.0.0
BuildRequires:	python-gstreamer >= 0.10.9
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
Requires:	gstreamer-plugins-good >= 0.10.10-1
Requires:	python-PIL
Requires:	python-TwistedCore >= 8.0.0
Requires:	python-TwistedCore-ssl >= 8.0.0
Requires:	python-TwistedWeb >= 8.0.0
Requires:	python-TwistedWeb2 >= 8.0.0
Requires:	python-coherence
Requires:	python-cssutils >= 0.9.5.1
Requires:	python-encutils
Requires:	python-gstreamer >= 0.10.9
Requires:	python-pigment >= 0.3.9-2
Requires:	python-pygobject
Requires:	python-pymetar
Requires:	python-setuptools
Requires:	python-sqlite
Suggests:	elisa-plugins-good
Suggests:	elisa-plugins-bad
Suggests:	elisa-plugins-ugly
Suggests:	python-gpod
Suggests:	python-dbus
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

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}/%{name}/plugins

python setup.py install \
	--root=$RPM_BUILD_ROOT

#py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# COPYING contains just some notes, LICENSE.GPL includes excemption clause 
%doc AUTHORS COPYING FAQ* LICENSE.* NEWS README FIRST_RUN
%attr(755,root,root) %{_bindir}/elisa*
%{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/%{name}*.egg-info
#%{py_sitescriptdir}/%{name}_*.py*
%{py_sitescriptdir}/%{name}*.pth
%{_desktopdir}/%{name}.desktop
%{_desktopdir}/%{name}-mobile.desktop
%{_pixmapsdir}/%{name}.png
%{_datadir}/dbus-1/services/com.fluendo.elisa.service
%{_mandir}/man1/%{name}*
