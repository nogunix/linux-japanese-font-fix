srpm:
	$(MAKE) -C .copr srpm $(if $(outdir),outdir="$(outdir)") $(if $(spec),spec="$(spec)")

srpm_path:
	$(MAKE) -C .copr srpm_path $(if $(outdir),outdir="$(outdir)") $(if $(spec),spec="$(spec)")

.PHONY: srpm srpm_path
