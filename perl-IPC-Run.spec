Name:           perl-IPC-Run
Version:        0.84
Release:        2%{?dist}
Summary:        Perl module for interacting with child processes
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/IPC-Run/
Source0:        http://www.cpan.org/authors/id/A/AD/ADAMK/IPC-Run-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Pty) >= 1.00
BuildRequires:  perl(Test::More) >= 0.47
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
IPC::Run allows you run and interact with child processes using files,
pipes, and pseudo-ttys. Both system()-style and scripted usages are
supported and may be mixed. Likewise, functional and OO API styles are
both supported and may be mixed.
Various redirection operators reminiscent of those seen on common Unix
and DOS command lines are provided.

%prep
%setup -q -n IPC-Run-%{version}
chmod 644 lib/IPC/*.pm lib/IPC/Run/*.pm Changes eg/*
for file in eg/run_daemon abuse/timers abuse/blocking_debug_with_sub_coprocess ; do
    %{__perl} -pi -e 's,^#!.*/perl,%{__perl}, if ($. == 1)' "$file"
done

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/IPC/Run/Win32*.pm
rm -f $RPM_BUILD_ROOT%{_mandir}/man3/IPC::Run::Win32*.3*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes LICENSE README TODO
%doc abuse/ eg/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jan 28 2011 Petr Pisar <ppisar@redhat.com> - 0.84-2
- Import into RHEL-6 (bug #669403)

* Wed Sep 02 2009 Steven Pritchard <steve@kspei.com> 0.84-1
- Update to 0.84.
- Drop IPCRUNDEBUG from "make test" (bug fixed long ago).

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.82-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.82-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 16 2009 Steven Pritchard <steve@kspei.com> 0.82-1
- Update to 0.82.
- Use fixperms macro instead of our own chmod incantation.
- Fix Source0 URL.
- BR Test::More.
- Include LICENSE, README, and abuse/ in docs.
- Cleanup to more closely resemble cpanspec output.

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.80-5
- Rebuild for perl 5.10 (again)

* Mon Jan 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.80-4
- rebuild for new perl

* Tue Apr 17 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.80-3
- BuildRequire perl(ExtUtils::MakeMaker).

* Wed Aug 30 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.80-2
- Fix order of arguments to find(1).

* Thu May 11 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.80-1
- 0.80, fine tune build dependencies.

* Tue Jan 17 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.79-3
- Rebuild, cosmetic cleanups.

* Sun Apr 10 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.79-2
- Exclude Win32 specific modules.
- Include more docs.
- Skip tests if /dev/pts doesn't exist.

* Sat Apr  2 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.79-1
- 0.79.

* Sat Apr  2 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.78-2
- Sync with fedora-rpmdevtools' Perl spec template.
- Improve dependency filtering script.

* Sun Mar 14 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.78-0.fdr.1
- Update to 0.78.

* Sun Feb  1 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.77-0.fdr.4
- Reduce directory ownership bloat.

* Fri Nov 21 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.77-0.fdr.3
- BuildRequire perl-IO-Tty for better test coverage.

* Sat Oct 11 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.77-0.fdr.2
- Fix typo in dependency filtering scriptlet.

* Sat Sep 27 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.77-0.fdr.1
- Update to 0.77.

* Fri Sep  5 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.75-0.fdr.3
- Avoid Win32-specific dependencies.
- Use PERL_INSTALL_ROOT.

* Sun Aug 31 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.75-0.fdr.2
- Install into vendor dirs.

* Thu Jun 19 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.75-0.fdr.1
- First build.
