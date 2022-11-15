Name:		texlive-clrscode3e
Version:	51137
Release:	1
Summary:	Typesets pseudocode as in Introduction to Algorithms
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/clrscode3e
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/clrscode3e.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/clrscode3e.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows you to typeset pseudocode in the style of
Introduction to Algorithms, Third edition, by Cormen,
Leiserson, Rivest, and Stein. The package was written by the
authors. Use the commands the same way the package's author did
when writing the book, and your output will look just like the
pseudocode in the text.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/clrscode3e
%doc %{_texmfdistdir}/doc/latex/clrscode3e

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
