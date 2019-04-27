#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-clipr
Version  : 0.6.0
Release  : 9
URL      : https://cran.r-project.org/src/contrib/clipr_0.6.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/clipr_0.6.0.tar.gz
Summary  : Read and Write from the System Clipboard
Group    : Development/Tools
License  : GPL-3.0
BuildRequires : buildreq-R

%description
# clipr
[![CRAN
status.](http://www.r-pkg.org/badges/version/clipr)](http://www.r-pkg.org/pkg/clipr)
total](http://cranlogs.r-pkg.org/badges/grand-total/clipr) [![Travis-CI
Build
Status](https://travis-ci.org/mdlincoln/clipr.svg?branch=master)](https://travis-ci.org/mdlincoln/clipr)
[![AppVeyor Build
Status](https://ci.appveyor.com/api/projects/status/github/mdlincoln/clipr?branch=master&svg=true)](https://ci.appveyor.com/project/mdlincoln/clipr)
[![Coverage
Status](https://img.shields.io/codecov/c/github/mdlincoln/clipr/master.svg)](https://codecov.io/github/mdlincoln/clipr?branch=master)

%prep
%setup -q -c -n clipr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1555410285

%install
export SOURCE_DATE_EPOCH=1555410285
rm -rf %{buildroot}
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
R CMD check --no-manual --no-examples --no-codoc clipr || :


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
/usr/lib64/R/library/clipr/Meta/vignette.rds
/usr/lib64/R/library/clipr/NAMESPACE
/usr/lib64/R/library/clipr/NEWS.md
/usr/lib64/R/library/clipr/R/clipr
/usr/lib64/R/library/clipr/R/clipr.rdb
/usr/lib64/R/library/clipr/R/clipr.rdx
/usr/lib64/R/library/clipr/doc/developing-with-clipr.R
/usr/lib64/R/library/clipr/doc/developing-with-clipr.Rmd
/usr/lib64/R/library/clipr/doc/developing-with-clipr.html
/usr/lib64/R/library/clipr/doc/index.html
/usr/lib64/R/library/clipr/help/AnIndex
/usr/lib64/R/library/clipr/help/aliases.rds
/usr/lib64/R/library/clipr/help/clipr.rdb
/usr/lib64/R/library/clipr/help/clipr.rdx
/usr/lib64/R/library/clipr/help/paths.rds
/usr/lib64/R/library/clipr/html/00Index.html
/usr/lib64/R/library/clipr/html/R.css
/usr/lib64/R/library/clipr/rstudio/addins.dcf
/usr/lib64/R/library/clipr/tests/testthat.R
/usr/lib64/R/library/clipr/tests/testthat/setup.R
/usr/lib64/R/library/clipr/tests/testthat/test-diagnostics.R
/usr/lib64/R/library/clipr/tests/testthat/test-systems.R
/usr/lib64/R/library/clipr/tests/testthat/test_render.R
