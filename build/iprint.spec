Name:           iprint
Version:        1.3
Release:        1%{?dist}
Summary:        Print values in decimal, hex and octal

Group:          Applications/Engineering
License:        GPL
URL:            https://www.samba.org/~tridge/
Source0:        https://raw.githubusercontent.com/tridge/junkcode/master/i.c

%description
Use i to print values in decimal, hex and octal.
Perform maths and have the result translated.


%prep


%build
gcc %{optflags} %{SOURCE0} -o i


%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -m 755 i $RPM_BUILD_ROOT/%{_bindir}/i

%files
%defattr(-,root,root,-)
%{_bindir}/i

%changelog
* Thu Aug 27 2015 Chris Smart<csmart@kororaproject.org> - 1.3-1
- Initial build of iprint for Fedora.

