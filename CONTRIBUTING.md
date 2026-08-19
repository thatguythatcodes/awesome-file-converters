# Contributing

Thanks for helping make Awesome File Converters more useful and trustworthy.

## Before submitting

An entry must perform a genuine file conversion and link to its official product or project page. Search the existing dataset first to avoid duplicates.

We accept commercial and open-source converters. Inclusion depends on usefulness and accurate disclosure, not payment, backlinks, or reciprocal promotion.

We do not accept:

- Affiliate or referral links
- URL shorteners
- Keyword-stuffed descriptions
- Tools without a working official page
- Misleading “free” claims
- Products that merely rename file extensions
- Bulk submissions of unverified tools

## Add or update an entry

1. Edit `data/converters.json`.
2. Keep array values lowercase, unique, and alphabetically sorted.
3. Use `unknown` rather than guessing.
4. Set `last_verified` to the date you personally checked the entry.
5. Include an official documentation URL supporting the format claims.
6. Run `python3 scripts/validate.py` and `python3 scripts/generate_catalog.py`.
7. Open a pull request explaining what you verified.

If you are affiliated with a submitted product, disclose that relationship in the pull request.

## Meaning of fields

- `free`: `yes`, `limited`, `no`, or `unknown`.
- `account_required`: whether an account is required for normal use.
- `local_processing`: whether the conversion occurs on the user's device.
- `open_source`: whether the converter's relevant source code is publicly available under an open-source license.
- `batch`: whether multiple files or jobs can be converted together.
- `watermark`: whether normal output includes a watermark.
- `last_verified`: the most recent manual verification date in `YYYY-MM-DD` format.

For local-processing claims, verify the product documentation or inspect network behavior during a representative conversion. Do not infer privacy from marketing language alone.

## Pull-request checklist

- [ ] I used the official canonical HTTPS URL.
- [ ] I personally checked the stated capabilities.
- [ ] I disclosed free limits, account requirements, and watermarks.
- [ ] I disclosed any affiliation.
- [ ] The validation script passes.
