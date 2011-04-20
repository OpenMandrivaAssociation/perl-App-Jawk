%define upstream_name    App-Jawk
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1
Summary:	Awk, but post-modern and perly
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/J/JO/JOSHR/%{upstream_name}-%{upstream_version}.tar.gz
BuildArch: noarch

%description
Jawk can be described as a flexible tool for extracting columns of data from text files. Also, it's a replacement which supports ranges, indexing columns by negative numbers, a perl mode, and more.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc ChangeLog Changes MANIFEST META.yml README
%{_bindir}/jawk
%{_mandir}/man1/*
