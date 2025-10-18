# .copr/Makefile
SPEC     := ../linux-japanese-font-fix.spec
TOPDIR   := $(CURDIR)/_build
SOURCES  := $(TOPDIR)/SOURCES
SRPMS    := $(TOPDIR)/SRPMS
TARBALLS := 50-user-jp-fonts.conf README.md README.ja.md LICENSE

srpm:
	@rm -rf $(TOPDIR)
	@mkdir -p $(SOURCES)
	@cp $(addprefix ../,$(TARBALLS)) $(SOURCES)/
	@rpmbuild -D "_topdir $(TOPDIR)" -bs $(SPEC)
	@cp $(SRPMS)/*.src.rpm $(CURDIR)/
	@ls linux-japanese-font-fix-*.src.rpm > srpm.list

srpm_path:
	@cat srpm.list

.PHONY: srpm srpm_path
