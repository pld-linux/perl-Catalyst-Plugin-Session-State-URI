#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Catalyst
%define	pnam	Plugin-Session-State-URI
Summary:	Catalyst::Plugin::Session::State::URI - Saves session IDs by rewriting URIs
Summary(pl.UTF-8):   Catalyst::Plugin::Session::State::URL - przechowywanie ID sesji w URI
Name:		perl-Catalyst-Plugin-Session-State-URI
Version:	0.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	340ec60b008f8abe5fde8661a393b960
URL:		http://search.cpan.org/dist/Catalyst-Plugin-Session-State-URI/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Catalyst-Plugin-Session >= 0.01
BuildRequires:	perl-HTML-TokeParser-Simple
BuildRequires:	perl-MIME-Types
BuildRequires:	perl-Test-MockObject >= 1.01
BuildRequires:	perl-URI
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
In order for Catalyst::Plugin::Session to work the session ID needs to
be stored on the client, and the session data needs to be stored on
the server.

This plugin cheats and instead of storing the session ID on the
client, it simply embeds the session ID into every URI sent to the
user.

%description -l pl.UTF-8
Aby wtyczka Catalyst::Plugin::Session działała, identyfikator sesji
musi być przechowywany po stronie klienta, a dane sesji - po stronie
serwera.

Ta wtyczka oszukuje i zamiast przechowywać ID sesji po stronie
klienta, po prostu osadza ID sesji w każdym URI wysyłanym do
użytkownika.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Catalyst/Plugin/Session/State/URI.pm
%{_mandir}/man3/*
