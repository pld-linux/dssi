Summary:	Disposable Soft Synth Interface specification
Name:		dssi
Version:	0.9.1
Release:	0.1
License:	LGPL v2.1
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/dssi/%{name}-%{version}.tar.gz
# Source0-md5:	1a353c3ae80328cded838853ddf52164
URL:		http://dssi.sourceforge.net/
BuildRequires:	alsa-lib-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	ladspa-devel
# lib{lo,sndfile,samplerate} are req. to build examples
#BuildRequires:	liblo-devel
#BuildRequires:	libsndfile-devel
#BuildRequires:	libsamplerate-devel
Requires:	alsa-lib-devel
Requires:	ladspa-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DSSI (pronounced "dizzy") is an API for audio plugins, with particular
application for software synthesis plugins with native user
interfaces. DSSI is an open specification developed for use in Linux
audio applications, although portable to other platforms. It may be
thought of as LADSPA-for-instruments, or something comparable to VSTi.

DSSI consists of a C language API for use by plugins and hosts, based
on the LADSPA API, and an OSC (Open Sound Control) API for use in user
interface to host communications. The DSSI specification consists of
an RFC which describes the background for the proposal and defines the
OSC part of the specification, and a documented header file which
defines the C API.

%prep
%setup -q

%build
#%{__libtoolize}
#%{__aclocal}
#%{__autoconf}
#%{__autoheader}
#%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README doc/TODO doc/*.txt
%attr(755,root,root) %{_bindir}/jack-dssi-host
%{_includedir}/dssi.h
%{_pkgconfigdir}/dssi.pc
