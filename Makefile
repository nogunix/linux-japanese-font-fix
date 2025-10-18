srpm:
	$(MAKE) -C .copr srpm

srpm_path:
	$(MAKE) -C .copr srpm_path

.PHONY: srpm srpm_path
