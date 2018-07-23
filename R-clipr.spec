#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-clipr
Version  : 0.4.1
Release  : 1
URL      : https://cran.r-project.org/src/contrib/clipr_0.4.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/clipr_0.4.1.tar.gz
Summary  : Read and Write from the System Clipboard
Group    : Development/Tools
License  : GPL-3.0
BuildRequires : clr-R-helpers

%description
OS X, and X11 clipboards.

%prep
%setup -q -c -n clipr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532310059

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1532310059
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library clipr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library clipr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library clipr
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library clipr|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/clipr/DESCRIPTION
/usr/lib64/R/library/clipr/INDEX
/usr/lib64/R/library/clipr/Meta/Rd.rds
/usr/lib64/R/library/clipr/Meta/features.rds
/usr/lib64/R/library/clipr/Meta/hsearch.rds
/usr/lib64/R/library/clipr/Meta/links.rds
/usr/lib64/R/library/clipr/Meta/nsInfo.rds
/usr/lib64/R/library/clipr/Meta/package.rds
/usr/lib64/R/library/clipr/NAMESPACE
/usr/lib64/R/library/clipr/NEWS.md
/usr/lib64/R/library/clipr/R/clipr
/usr/lib64/R/library/clipr/R/clipr.rdb
/usr/lib64/R/library/clipr/R/clipr.rdx
/usr/lib64/R/library/clipr/help/AnIndex
/usr/lib64/R/library/clipr/help/aliases.rds
/usr/lib64/R/library/clipr/help/clipr.rdb
/usr/lib64/R/library/clipr/help/clipr.rdx
/usr/lib64/R/library/clipr/help/paths.rds
/usr/lib64/R/library/clipr/html/00Index.html
/usr/lib64/R/library/clipr/html/R.css
/usr/lib64/R/library/clipr/rstudio/addins.dcf
