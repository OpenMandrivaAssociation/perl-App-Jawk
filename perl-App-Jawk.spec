%define upstream_name    App-Jawk
%define upstream_version 0.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2
Summary:	Awk, but post-modern and perly
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/authors/id/J/JO/JOSHR/App-Jawk-%{upstream_version}.tar.gz
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Jawk can be described as a flexible tool for extracting columns
of data from text files. Also, it's a replacement which supports
ranges, indexing columns by negative numbers, a perl mode, and more.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc ChangeLog Changes MANIFEST META.yml README
%{_bindir}/jawk
%{_mandir}/man1/*
%{perl_vendorlib}/App/Jawk.pm
%{_mandir}/man3/App::Jawk.3pm.xz

%changelog
* Wed Apr 20 2011 Sandro Cazzaniga <kharec@mandriva.org> 0.40.0-1mdv2011.0
+ Revision: 656137
- import perl-App-Jawk


