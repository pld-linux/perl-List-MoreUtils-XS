#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	List
%define		pnam	MoreUtils-XS
Summary:	List::MoreUtils::XS - Provide compiled List::MoreUtils functions
Summary(pl.UTF-8):	List::MoreUtils::XS - skompilowane funkcje List::MoreUtils
Name:		perl-List-MoreUtils-XS
Version:	0.430
Release:	6
# for code before 0.417: same as perl 5.8.4 or later
License:	Apache v2.0 (code since 0.417), GPL v1+ or Artistic (older code)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/List/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e77113e55b046906aecfb4ddb4f0c662
URL:		https://metacpan.org/dist/List-MoreUtils-XS
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Storable
BuildRequires:	perl-Test-Simple >= 0.96
%endif
Conflicts:	perl-List-MoreUtils < 0.417
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
List::MoreUtils::XS is a backend for List::MoreUtils. Even if it's
possible (because of user wishes) to have it practically independent
from List::MoreUtils, it technically depend on List::MoreUtils. Since
it's only a backend, the API is not public and can change without any
warning.

%description -l pl.UTF-8
List::MoreUtils::XS to backend dla List::MoreUtils. Nawet jeśli jest
możliwe (ze względu na życzenia użytkownika) zainstalowanie tego
modułu niezależnie od List::MoreUtils, technicznie zależy on od
List::MoreUtils. Ponieważ jest to tylko backend, API nie jest
publiczne i może się zmienić bez ostrzeżenia.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.md
%dir %{perl_vendorarch}/List/MoreUtils
%{perl_vendorarch}/List/MoreUtils/XS.pm
%dir %{perl_vendorarch}/auto/List/MoreUtils
%dir %{perl_vendorarch}/auto/List/MoreUtils/XS
%attr(755,root,root) %{perl_vendorarch}/auto/List/MoreUtils/XS/XS.so
%{_mandir}/man3/List::MoreUtils::XS.3pm*
