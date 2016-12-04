Summary:	APNG Disassembler - deconstruct APNG files into individual frames
Summary(pl.UTF-8):	APNG Disassembler - rozkładanie plików APNG na poszczególne ramki
Name:		apngdis
Version:	2.8
Release:	1
License:	Zlib (BSD-like)
Group:		Applications/Graphics
Source0:	http://downloads.sourceforge.net/apngdis/%{name}-%{version}-src-only.zip
# Source0-md5:	9131ab35fc5f96606b7c94c4cab618df
URL:		http://apngdis.sourceforge.net/
BuildRequires:	libpng-devel >= 2:1.6.17
BuildRequires:	libstdc++-devel
BuildRequires:	zlib-devel >= 1.2.8
Requires:	libpng >= 2:1.6.17
Requires:	zlib >= 1.2.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
APNG Disassembler deconstructs APNG files into individual frames.

%description -l pl.UTF-8
APNG Disassembler rozkłada pliki APNG na poszczególne ramki.

%prep
%setup -q -c

%build
%{__cxx} %{rpmldflags} %{rpmcxxflags} %{rpmcppflags} -Wall -o apngdis apngdis.cpp -lpng -lz -lm

%install
rm -rf $RPM_BUILD_ROOT

install -D apngdis $RPM_BUILD_ROOT%{_bindir}/apngdis

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%attr(755,root,root) %{_bindir}/apngdis
